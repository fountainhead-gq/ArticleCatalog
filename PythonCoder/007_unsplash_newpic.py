#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
from urllib.request import HTTPError
import threading
import os,sys
import json
import time
import random
import http

__author__ = 'GQ'


PageCount = 42  # 截取总页数
sleep_time = random.randint(1, 3)

# headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
imgPath = os.getcwd()
imgPath = os.path.join(imgPath, r'pic\unsplash')
if not os.path.exists(imgPath):
    os.mkdir(imgPath)  # 是否创建图片文件夹

def getUnsplashPic(PageUrl):
    try:
        ###############################################################
        # PageUrl = PageUrl+str(PageNum)
        # request = urllib.request.Request(PageUrl)
        # request.add_header("User-Agent", "fake-client")
        # web_page = urllib.request.urlopen(request)
        # content_data = web_page.read().decode('utf-8')
        #===========================================================#
        # handler = urllib.request.ProxyHandler({'http': 'https://unsplash.com/'})
        # opener = urllib.request.build_opener(handler)
        # urllib.request.install_opener(opener)
        # opener.add_handler = headers
        # content_data = opener.open(PageUrl).read()
        ###############################################################
        handler = urllib.request.ProxyHandler({'http': 'https://unsplash.com/'})
        opener = urllib.request.build_opener(handler, urllib.request.HTTPHandler(debuglevel=1))
        urllib.request.install_opener(opener)
        opener.add_handler = headers
        req = urllib.request.Request(PageUrl, None, headers)
        content_data = opener.open(req).read()
        soup = BeautifulSoup(content_data, "html5lib")
        print(PageUrl)
        downloding_pic = soup.find('div', {"class": "photo-grid photo-grid--single js-pagination-container js-grid"})
        list_class_item = downloding_pic.find_all('div', {"class": "sheet photo-container js-grid-image-container"})
        time.sleep(3)
        for list_content in list_class_item:
            if list_content.find('div', {"class": "photo"}):
                img_src = list_content.find('div', {"class": "photo"}).a.img['src']
                # img_name = list_content.find('div', {"class": "photo"}).a['title']
                # 获取图片名称
                img_url, split_name = img_src.split('?')
                img_sec_url = img_url.split('/')
                img_sec_name = img_sec_url[-1]
                if '.'in img_sec_name:
                    img_pic = img_sec_name.split('.')
                    img_sec_name = img_pic[0]
                img_name = img_sec_name  # 截取图片名称
                pic_name = imgPath + os.sep + img_name + '.jpg'
                print(pic_name)
                if os.path.isfile(pic_name):
                    continue
                # urllib.request.urlretrieve(img_src, pic_name)
                # f = open(pic_name, "wb")
                # f.write(urllib.request.urlopen(img_src).read())
                # f.close()
                #################################################################################
                # http.client.IncompleteRead: IncompleteRead(48832 bytes read, 63925 more expected)
                ###################################################################################
            while True:
                try:
                     responseJSONpart = urllib.request.urlopen(img_src).read()
                     f = open(pic_name, "wb")
                     f.write(urllib.request.urlopen(img_src).read())
                     f.close()
                except http.client.IncompleteRead as icread:
                    responseJSON = icread.partial.decode('utf-8')
                    continue
                else:
                    responseJSON = responseJSON + responseJSONpart.decode('utf-8')
                    break
            return json.loads(responseJSON)
    except Exception as RESTex:
        print("Exception occurred : " + RESTex.__str__())

threads = []
def startDownload():
    for PageNum in range(40, PageCount):
        PageUrl ="https://unsplash.com/?_=1440470076360&page=%d" % PageNum
        thr = threading.Thread(target=getUnsplashPic, args=(PageUrl,))
        threads.append(thr)
    for t in threads:
        t.start()
        time.sleep(5)
    for t in threads:
        t.join()
        time.sleep(5)

def Download(PageNum):
    PageUrl ="https://unsplash.com/?_=1440470076360&page=%d" % PageNum
    thr = threading.Thread(target=getUnsplashPic, args=(PageUrl,))
    threads.append(thr)
    for t in threads:
        t.start()

    for t in threads:
        t.join()

#dw_url = "https://unsplash.com/?_=1440470076360&page="

if __name__ == "__main__":
    choosePage = int(input('请输入要下载第几页的图片 : '))
    Download(choosePage)
    #startDownload()





