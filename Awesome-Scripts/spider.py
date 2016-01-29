#!/url/bin/env python
# -*- coding: utf-8 -*-


import os,codecs
import re, urllib
from bs4 import BeautifulSoup
from urllib import request


# 伪装成浏览器访问，通过修改http包中的header来实现
headers = ('User-Agent',
           'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')


class Spider(object):

    def getUrl(self, url, coding='utf-8'):
        req = request.Request(url)
        # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 ')
        req.add_header = headers
        with request.urlopen(req) as respone:
            return BeautifulSoup(respone.read().decode(coding))

    # 创建目录
    def checkPath(self, path):
        dirname = os.path.dirname(path.strip())
        if not os.path.exists(dirname):
            os.makedirs(dirname)

    # 保存文件文本至本地
    def saveText(self, filename, content, mode='w'):
        self.checkPath(filename)
        with codecs.open(filename, encoding='utf-8', mode=mode) as f:
            f.write(content)

    # 保存图片至本地
    def saveImg(self,imgUrl,imgName):
        self.checkPath(imgName)
        data = request.urlopen(imgUrl).read()
        with open(imgName, 'wb') as f:
            f.write(data)

    #处理文本内容
    def filter_tags(self, htmlstr):
        re_script = re.compile('<noscript>[\s\S]*</noscript>', re.I)   # Script
        re_div = re.compile('<div class="zm-editable-content clearfix">|</div>', re.I)   # div
        # re_img = re.compile('<img\s*>', re.I)
        re_p = re.compile('</?p>|</?b>|</?strong>', re.I)
        re_i = re.compile('<i\s*/?>|</i>')
        re_br = re.compile('<br\s*/?>')

        s = re.sub(re_script, '', htmlstr)   # 去掉SCRIPT
        s = re.sub(re_div, '', s)  # 去掉div
        s = re.sub(re_p, '', s)   #
        s = re.sub(re_i, '', s)
        s = re.sub(re_br, '\n', s)  # 将br转换为换行
        return s






