#!/usr/bin/env python3
__author__ = 'GQ'

import urllib.request
import re
import os
import ssl
import time

#导入ssl模块，要用全局的。否则报错<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed>
ssl._create_default_https_context = ssl._create_unverified_context
#创建图片的文件夹
#targetDir = r"C:\Users\pic"
def destFile(path):
    targetDir = os.getcwd()
    targetDir = os.path.join(targetDir, 'pic')
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    #截取url,获取带有图片名称的字符串
    url_path, url_name = os.path.split(path)
    #截取？之前的字符串，获取图片名称
    img_name, img_nm = url_name.split('?')
    img = img_name + '.jpg'
    if not os.path.exists(img):
        t = os.path.join(targetDir, img)
        return t

if __name__ == "__main__":
    while True:
        #抓取图片的url
        hostname = "https://unsplash.com/"
        #模拟浏览器访问
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        # req = urllib.request.Request(hostname, headers=headers)
        req = urllib.request.Request(hostname)
        req.add_header("User-Agent", "fake-client")
        web_page = urllib.request.urlopen(req)
        data = web_page.read().decode('utf-8')

        #for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(data))):
        for link, t in set(re.findall(r'(https:[^\s]*?(jpg))', str(data))):
             print(link)
             urllib.request.urlretrieve(link, destFile(link))
             time.sleep(1)
