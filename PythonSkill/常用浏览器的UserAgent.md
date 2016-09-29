# 常用浏览器的UserAgent

## 为什么需要修改UserAgent

写python网络爬虫程序的时候，经常需要修改UserAgent，有很多原因，罗列几个如下：
- 不同Agent下看到的内容不一样，比如，购物网站的手机版网页和pc版网页上的商品优惠不一样
- 为避免被屏蔽，爬取不同的网站经常要定义和修改useragent值。


## 列出常用浏览器的UserAgent

### PC端的UserAgent

**safari 5.1 – MAC**  
`User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50`

**safari 5.1 – Windows**  
`User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50`

**Firefox 4.0.1 – Windows**  
`User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1`

**Chrome 17.0 – MAC**  
`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11`

### 移动端的UserAgent

**safari iOS 4.33 – iPhone**  
`User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5`

**Android QQ浏览器**  
`User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1`
