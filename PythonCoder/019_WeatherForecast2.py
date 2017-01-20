#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
接口示例： https://api.heweather.com/x3/weather?cityid=城市ID&key=你的认证key
查询城市ID：http://www.heweather.com/documents/cn-city-list
'''

'''
# 示例一

import urllib.request
import json

url = 'https://api.heweather.com/x3/weather?cityid=CN101010100&key=aff7593e9c9c4b0eae75b458e81e6fcb'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content = response.read()
print(content)
'''

import http.client

conn = http.client.HTTPConnection("api.heweather.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'key': "aff7593e9c9c4b0eae75b458e81e6fcb"
    }

conn.request("GET", "/x3/weather?cityid=CN101010100&key=aff7593e9c9c4b0eae75b458e81e6fcb", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
