#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re
import json
import os

__author__ = 'GQ'

# 伪装成浏览器访问，通过修改http包中的header来实现
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')

def get_dytt8_films(url):

    if os.path.isfile("movie.txt"):
        os.remove("movie.txt")
    if not os.path.isfile("movie.txt"):
        open("movie.txt", 'w')

    handler = urllib.request.ProxyHandler({'http': 'http://www.dytt8.net/'})
    opener = urllib.request.build_opener(handler)
    opener.add_handler=headers
    content = opener.open(url).read().decode('gbk', 'ignore')
    # content = opener.open(url).read()
    soup = BeautifulSoup(content, "html5lib")

    if soup.findAll('a', {'class': 'ulink'}):
        ulink = soup.findAll('a', {'class': 'ulink'})
    else:
        js = soup.findAll('script', {'language': 'javascript'})[0].string
        pick_js = js[11:-22] # 挑出js部分
        fix_js = pick_js.replace('url=', '')
        urls = fix_js.split(';')
        url = ''
        for i in range(len(urls)):
             url = eval(urls[i])
        url = "http://www.dytt8.net" + url
        content = opener.open(url).read().decode('gbk', 'ignore')
        soup = BeautifulSoup(content, "html5lib")
        ulink = soup.findAll('a', {'class': 'ulink'})

    films = []
    for film_link in ulink:
        film = {}
        film_href = 'http://www.dytt8.net' + film_link['href']
        film['film_href'] = film_href
        film_content = opener.open(film_href).read().decode('gbk', 'ignore')
        film_soup = BeautifulSoup(film_content, "html5lib")
        title_all = film_soup.findAll('div', {'class': 'title_all'})

        if title_all:
            film['film_title'] = title_all[-1].h1.font.string
            film['download_url'] = film_soup.findAll('td', {'style': 'WORD-WRAP: break-word'})[0].a['href']

        else:
            break


        with open('movie.txt', 'a') as f:
            f.write('\n')
            f.write(film['download_url']+'\n')

        films.append(film)

    return films

url = "http://www.dytt8.net/html/gndy/dyzz/index.html"
# url="http://www.ygdy8.net/html/gndy/oumei/index.html"
jsonStr = json.dumps(get_dytt8_films(url), ensure_ascii=False, indent=1)
print(jsonStr)