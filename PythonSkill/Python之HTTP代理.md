# Python之HTTP代理

### HTTP代理

HTTP代理本质上是一个Web应用，它和其他普通Web应用没有根本区别。HTTP代理收到请求后，根据Header中Host字段的主机名和Get/POST请求地址综合判断目标主机，建立新的HTTP请求并转发请求数据，并将收到的响应数据转发给客户端。

如果请求地址是绝对地址，HTTP代理采用该地址中的Host，否则使用Header中的HOST字段。做一个简单测试，假设网络环境如下：

192.168.1.2 Web服务器
192.168.1.3 HTTP代理服务器

使用telnet进行测试

$ telnet 192.168.1.3
GET / HTTP/1.0
HOST: 192.168.1.2

注意最后需要连续两个回车，这是HTTP协议要求。完成后，可以收到 http://192.168.1.2/ 的页面内容。下面做一下调整，GET请求时带上绝对地址

$ telnet 192.168.1.3
GET http://httpbin.org/ip HTTP/1.0
HOST: 192.168.1.2

注意这里同样设置了HOST为192.168.1.2，但运行结果却返回了 http://httpbin.org/ip 页面的内容，也就是公网IP地址信息。

从上面的测试过程可以看出，HTTP代理并不是什么很复杂的东西，只要将原始请求发送到代理服务器即可。在无法设置HTTP代理的情况下，对于少量Host需要走HTTP代理的场景来说，最简单的方式就是将目标Host域名的IP指向代理服务器，可以采取修改hosts文件的方式来实现。


### Python中设置HTTP代理

#### urllib代理设置
Python3使用urllib模块中通过ProxyHandler来设置使用代理服务器。
```python
proxy_handler = urllib.request.ProxyHandler({'http': 'http://121.193.143.249:80/'})
opener = urllib.request.build_opener(proxy_handler)
r = opener.open('http://httpbin.org/ip')
print(r.read())
```
#### requests 代理设置
requests是目前最优秀的HTTP库之一，也是我平时构造http请求时使用最多的库。它的API设计非常人性化，使用起来很容易上手。给requests设置代理很简单，只需要给proxies设置一个形如 `{'http': 'x.x.x.x:8080', 'https': 'x.x.x.x:8080'}` 的参数即可。其中http和https相互独立。
```python
In [5]: requests.get('http://httpbin.org/ip', proxies={'http': '121.193.143.249:80'}).json()
Out[5]: {'origin': '121.193.143.249'}
```
可以直接设置session的proxies属性，省去每次请求都要带上proxies参数的麻烦。
```python
s = requests.session()
s.proxies = {'http': '121.193.143.249:80'}
print(s.get('http://httpbin.org/ip').json())
```
#### HTTP_PROXY / HTTPS_PROXY 环境变量
urllib 和 Requests 库都能识别 HTTP_PROXY 和 HTTPS_PROXY 环境变量，一旦检测到这些环境变量就会自动设置使用代理。这在用HTTP代理进行调试的时候非常有用，因为不用修改代码，可以随意根据环境变量来调整代理服务器的ip地址和端口。linix中的大部分软件也都支持HTTP_PROXY环境变量识别，比如curl、wget、axel、aria2c等。
```python
$ http_proxy=121.193.143.249:80 python -c 'import requests; print(requests.get("http://httpbin.org/ip").json())'
{u'origin': u'121.193.143.249'}

$ http_proxy=121.193.143.249:80 curl httpbin.org/ip
{
  "origin": "121.193.143.249"
}
```
在IPython交互环境中，可能经常需要临时性地调试HTTP请求，可以简单通过设置 os.environ['http_proxy'] 增加/取消HTTP代理来实现。
```python
In [245]: os.environ['http_proxy'] = '121.193.143.249:80'
In [246]: requests.get("http://httpbin.org/ip").json()
Out[246]: {u'origin': u'121.193.143.249'}
In [249]: os.environ['http_proxy'] = ''
In [250]: requests.get("http://httpbin.org/ip").json()
Out[250]: {u'origin': u'x.x.x.x'}
```

#### MITM-Proxy

MITM 源于 Man-in-the-Middle Attack，指中间人攻击，一般在客户端和服务器之间的网络中拦截、监听和篡改数据。

mitmproxy是一款Python语言开发的开源中间人代理神器，支持SSL，支持透明代理、反向代理，支持流量录制回放，支持自定义脚本等。功能上同Windows中的Fiddler有些类似，但mitmproxy是一款console程序，没有GUI界面，不过用起来还算方便。使用mitmproxy可以很方便的过滤、拦截、修改任意经过代理的HTTP请求/响应数据包，甚至可以利用它的scripting API，编写脚本达到自动拦截修改HTTP数据的目的。
```python
# test.py
def response(flow):
    flow.response.headers["BOOM"] = "boom!boom!boom!"
```
上面的脚本会在所有经过代理的Http响应包头里面加上一个名为BOOM的header。用mitmproxy -s 'test.py'命令启动mitmproxy，curl验证结果发现的确多了一个BOOM头。
```python
$ http_proxy=localhost:8080 curl -I 'httpbin.org/get'
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 03 Nov 2016 09:02:04 GMT
Content-Type: application/json
Content-Length: 186
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
BOOM: boom!boom!boom!
...
```
显然mitmproxy脚本能做的事情远不止这些，结合Python强大的功能，可以衍生出很多应用途径。除此之外，mitmproxy还提供了强大的API，在这些API的基础上，完全可以自己定制一个实现了特殊功能的专属代理服务器。
