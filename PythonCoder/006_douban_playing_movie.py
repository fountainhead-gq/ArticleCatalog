#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re
import os
import json
import time

__author__ = 'GQ'

# 伪装成浏览器访问，通过修改http包中的header来实现
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')

path = os.getcwd()
path = os.path.join(path, 'pic')
# 将图片保存至pic文件夹
if not os.path.exists(path):
    os.mkdir(path)

def get_playing_films(url):
    # 使用代理访问网页
    handler = urllib.request.ProxyHandler({'http': 'http://www.douban.com'})
    # Return an OpenerDirector instance
    opener = urllib.request.build_opener(handler)
    # opener = urllib.request.build_opener(handler)
    # 使用全局 ulr opener：结合ProxyHandler，避免urlerror链接报错
    urllib.request.install_opener(opener)
    # add header
    opener.add_handler = headers
    # content = opener.open(url).read().decode('gbk', 'ignore').encode('utf-8')
    content = opener.open(url).read()
    # 解析器解析格式：Python标准库中的HTML解析器；第三方的解析器,是lxml、html5lib
    # soup = BeautifulSoup(content, "html5lib")
    soup = BeautifulSoup(content, "html.parser")
    # 获取正在上映电影
    now_playing_film = soup.find('div', {"id": "nowplaying"})
    # now_playing_film = soup.find('div', {"id": "upcoming"})

    # 获取所有的电影列表:findAll->find_all
    list_content = now_playing_film.find_all('li', {"class": "list-item"})
    i = 0
    all_film_content = []
    for list_film in list_content:
        film_content = {}
        if (list_film.ul.li['class'] == ['poster']):
            # tag的属性操作方法与字典一样
            film_content['film_name'] = list_film.ul.li.img['alt']
            film_content['film_release'] = list_film['data-release']+'年'
            film_content['film_actors'] = list_film['data-actors']
            film_content['film_director'] = list_film['data-director']
            film_content['film_href'] = list_film.ul.li.a['href']
            film_content['film_src'] = list_film.ul.li.a.img['src']
            pic_name = path + os.sep + film_content['film_name']+'.jpg'
            # 下载图片
            urllib.request.urlretrieve(film_content['film_src'], pic_name)
            film_content['film_pic'] = film_content['film_name']+'.gif'
            if list_film.find('span', {'class', 'subject-rate'}):
                film_content['points'] = list_film.find('span', {'class', 'subject-rate'}).string.strip()
                film_content['film_points'] = film_content['points']+'分'
            else:
                film_content['points'] = '0'
                film_content['film_points'] = '暂无评分'

            stars = list_film.find('li', {'class': 'srating'}).span['class']

            if stars[0] != 'rating-star':
                film_content['film_stars'] = '评价人数不足'
            else:
                original_film_stars = stars[1]
                # 用正则获取整数
                re_film_stars = re.compile(r'^\D*(\d{2})$')
                film_content['film_stars'] = str(int(re_film_stars.search(original_film_stars).groups()[0])/10)+'颗星'
        all_film_content.append(film_content)
        i = i + 1

    # sort_all_film = sorted(all_film_content, key=lambda x:x['points'], reverse = True)    # 将列表中字典元素按从大到小排列
    # 起始处插入上映的总数
    total = {'正上映电影总数': str(i)+'部'}
    all_film_content.insert(0, total)
    opener.close()
    return all_film_content
# url
film_url = "http://movie.douban.com/nowplaying/beijing/"
# 输出为带缩进的，树状的，很漂亮的效果list:ensure_ascii=False是输出原有的语言文字; indent是缩进数量。
jsonStr = json.dumps(get_playing_films(film_url), ensure_ascii=False, indent=1)
print(jsonStr)

