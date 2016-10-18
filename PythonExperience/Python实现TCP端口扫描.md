在渗透测试的初步阶段通常我们都需要对攻击目标进行信息搜集，而端口扫描就是信息搜集中至关重要的一个步骤。通过端口扫描我们可以了解到目标主机都开放了哪些服务，甚至能根据服务猜测可能存在某些漏洞。 TCP端口扫描一般分为以下几种类型：

- TCP connect扫描：也称为全连接扫描，这种方式直接连接到目标端口，完成了TCP三次握手的过程，这种方式扫描结果比较准确，但速度比较慢而且可轻易被目标系统检测到。
- TCP SYN扫描：也称为半开放扫描，这种方式将发送一个SYN包，启动一个TCP会话，并等待目标响应数据包。如果收到的是一个RST包，则表明端口是关闭的，而如果收到的是一个SYN/ACK包，则表示相应的端口是打开的。
- Tcp FIN扫描：这种方式发送一个表示拆除一个活动的TCP连接的FIN包，让对方关闭连接。如果收到了一个RST包，则表明相应的端口是关闭的。
- TCP XMAS扫描：这种方式通过发送PSH、FIN、URG、和TCP标志位被设为1的数据包。如果收到了一个RST包，则表明相应的端口是关闭的。


### 最简单的端口扫描实现
全连接扫描方式的核心就是针对不同端口进行TCP连接,根据是否连接成功来判断端口是否打开，现在我们来实现一个最简单的端口扫描器：

```python
# -*- coding: utf-8 -*-
from socket import *

def portScanner(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        print('[+] %d open' % port)
        s.close()
    except:
        print('[-] %d close' % port)

def main():
    setdefaulttimeout(1)
    for p in range(1,1024):
        portScanner('192.168.0.100',p)

if __name__ == '__main__':
    main()
```    
这段代码的核心就是 `portScanner` 函数，从其中的内容可以看出，只是进行了简单的TCP连接，如果连接成功则判断为端口打开，否则视为关闭。 我们来看一下运行结果：
```
[-] 1 close
[-] 2 close
[-] 3 close
[-] 4 close
[-] 5 close
[-] 6 close
[-] 7 close
[-] 8 close
[-] 9 close
[-] 10 close
...
```

这样的扫描看起来效率太低了，实际也确实很慢，因为我们设置了默认的超时时间为1秒，这要是扫描10000个端口，岂不是要等到花都谢了？


### 多线程实现端口扫描
最简单的办法就是用多线程来提高效率，虽然python的多线程有点太弱了，不过至少可以利用我们等待的时间去干点别的。另外之前扫描的端口比较多， 显示的信息我们看起来不方便，这次我们只显示我们关心的打开的端口 ，并将打开端口的数量在扫描结束的时候显示出来。

```python
# -*- coding: utf-8 -*-
from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    for p in range(1,1024):
        t = threading.Thread(target=portScanner,args=('192.168.0.100',p))
        threads.append(t)
        t.start()     

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()
``    
运行看一下效果：
```python
[*] The scan is complete!
[*] A total of 0 open port
```


这下看起来是不是方便多了？至此效率上的问题解决了，现在我们还需要为扫描器增加一个 参数解析的功能，这样才能看起来像个样子，总不能每次都改代码来修改扫描目标和端口吧！

### 参数解析扫描端口
参数解析我们将用python3自带的标准模块 argparse ,这样我们就省去了自己解析字符串的麻烦！ 下面来看代码：

```python
# -*- coding: utf-8 -*-
from socket import *
import threading
import argparse

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    p = argparse.ArgumentParser(description='Port scanner!.')
    p.add_argument('-H', dest='hosts', type=str)
    args = p.parse_args()
    hostList = args.hosts.split(',')
    setdefaulttimeout(1)
    for host in hostList:
        print('Scanning the host:%s......' % (host))
        for p in range(1,1024):
            t = threading.Thread(target=portScanner,args=(host,p))
            threads.append(t)
            t.start()     

        for t in threads:
            t.join()

        print('[*] The host:%s scan is complete!' % (host))
        print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()
```    
看一下运行效果：
```python
F:\VENV\test>python 1.py -H 192.168.43.50,192.168.43.10
Scanning the host:192.168.43.50......
[*] The host:192.168.43.50 scan is complete!
[*] A total of 0 open port
Scanning the host:192.168.43.10......
[*] The host:192.168.43.10 scan is complete!
[*] A total of 0 open port
```

至此我们的端口扫描器就基本完成了，虽然功能比较简单，旨在表达端口扫描器的基本实现思路！ 
