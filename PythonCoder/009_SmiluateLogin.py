#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
模拟登录获取豆瓣的想读书籍列表
使用requests
'''

import requests
from bs4 import BeautifulSoup
import urllib.request
import re

__author__ = 'GQ'

username = input('please input loginname:')
password = input('please input password:')

loginUrl = 'http://accounts.douban.com/login'
formData={
    "redir":"http://book.douban.com/mine?status=wish",
    "form_email":username,
    "form_password":password,
    "login":u'登录'
}
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
r = requests.post(loginUrl, data=formData, headers=headers)
page = r.text

# 获取验证码图片
# 利用bs4获取captcha地址
soup = BeautifulSoup(page,"html.parser")
captchaAddr = soup.find('img',id='captcha_image')['src']
# 利用正则表达式获取captcha的ID
reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
captchaID = re.findall(reCaptchaID,page)

print('验证码链接:%s'% captchaAddr)
# 验证图片下载到本地
urllib.request.urlretrieve(captchaAddr,"captcha.jpg")
captcha = input('please input the captcha:')

formData['captcha-solution'] = captcha
formData['captcha-id'] = captchaID

r = requests.post(loginUrl, data=formData, headers=headers)
page = r.text

if r.url=='http://book.douban.com/mine?status=wish':
    print('已登录成功!想读的书籍:\n', '='*60)

    soup = BeautifulSoup(page,"html.parser")
    result = soup.findAll('li',attrs={"class":"subject-item"})

    for item in result:
        print(item.find('div',attrs={"class":"info"}).a.get_text("|", strip=True)) #获取文本内容,除去前后空白
else:
    print("failed!")

