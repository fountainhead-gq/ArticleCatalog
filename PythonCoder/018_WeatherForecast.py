#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
城市ID：http://www.heweather.com/documents/cn-city-list

url示例： http://a.apix.cn/heweather/x3/pro/weather?cityid=CN101010100
'''

import requests
import json

# 专业版：免费使用1000次，超过次数的话，6RMB/10000次
#url = "http://a.apix.cn/heweather/x3/pro/weather"

# 免费版
url = "http://a.apix.cn/heweather/x3/free/weather"

# 城市ID
querystring = {"cityid": "CN101221202"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': "7d3090b692614a3e774acd24d30a76f7"  #apix-key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)