#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
查询手机归属地，GET请求，JSON格式数据
http://a.apix.cn/apixlife/phone/phone?phone=value
'''

import requests

# 接口地址
url = "http://a.apix.cn/apixlife/phone/phone"

# 参数，手机号
querystring = {"phone": "182xxxxxxx"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': "05928e129da74151614259915a63e5d6"  # 登录的apix-key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

