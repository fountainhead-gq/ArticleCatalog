#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GQ'

from tkinter import *
import tkinter.font
import urllib.request
import urllib.parse
import json
import re




'''
百度翻译API
URL:http://openapi.baidu.com/public/2.0/bmt/translate
Header: 无要求
from:语言/auto
to:语言/auto
client_id:API key
q:翻译内容（必须utf-8编码）

输出JSON格式：
{
    “from”:”zh”,
	“to”:”en”,
	“trans_result”:[
	{
    “src”:””,
    “dst”:””
    }]
}

trans_result:输出结果体 （数组）
src:原文
dst:译文

接口限制：1000次/小时，免费
'''

def BaiduTrans(word):

    url = 'http://openapi.baidu.com/public/2.0/bmt/translate'
    values = {'client_id': 'N1BvN4BPHIQXP1kipLO0GInQ',
              'q': word,
              'from': 'auto',
              'to': 'auto'
              }
    #API好像不太识别'\r'字符，最后翻译的结果会出现很奇怪的缺少字符的情况，先用正则表达式去掉'\r'
    values['q'] = re.sub('\r', '', values['q'])
    data = urllib.parse.urlencode(values)

    # response = urllib.request.urlopen(url, data)
    #解决问题：TypeError: the JSON object must be str, not 'bytes'
    binary_data = data.encode('utf-8')
    response = urllib.request.urlopen(url, binary_data)
    result = json.loads(response.read().decode('utf-8'))['trans_result']

    transResult = ''
    for i in result:
        transResult += i['dst'] + '\n'
    return transResult





'''
有道翻译API:
url：http://fanyi.youdao.com/openapi.do?keyfrom=shucun&key=902984324&type=data&doctype=<doctype>&version=1.1&q=要翻译的文本
version: 目前版本1.1
type:返回结果类型，固定为data
q:翻译内容（utf-8）
doctype:输出格式
keyfrom：网站名
key：API key

输出JSON格式：
translation：翻译内容
'''

def YoudaoTrans(word):
    url = 'http://fanyi.youdao.com/openapi.do?'
    values = {'keyfrom':'shucun',
              'key':'902984321',
              'type':'data',
              'doctype':'json',
              'version':'1.1',
              'q':word
              }

    data = urllib.parse.urlencode(values)
    binary_data = data.encode('utf-8')
    response = urllib.request.urlopen(url, binary_data)
    result = json.loads(response.read().decode('utf-8'))['translation']

    transResult = ''
    for i in result:
        transResult += (i + '\n')
    return transResult



def trans():
    if bdText.get(0.0, END) == '' and ydText.get(0.0, END) == '':
        bdText.insert(0.0, BaiduTrans(oriText.get(0.0, END)))
        ydText.insert(0.0, YoudaoTrans(oriText.get(0.0, END)))
    else:
        bdText.delete(0.0, END)
        ydText.delete(0.0, END)
        bdText.insert(0.0, BaiduTrans(oriText.get(0.0, END)))
        ydText.insert(0.0, YoudaoTrans(oriText.get(0.0, END)))

def clear():
    oriText.delete(0.0, END)
    bdText.delete(0.0, END)
    ydText.delete(0.0, END)


# GUI
frame = Tk()


# 字体名称、大小、样式
ft = tkinter.font.Font(family = 'PMingLiU', size = 20, weight = tkinter.font.BOLD)
lft = tkinter.font.Font(family = 'PMingLiU', size = 14, weight = tkinter.font.BOLD)

frame.title('翻译小助手  @郭澍存')
frame.resizable(0, 0)

oriLabel = Label(frame, text = '原文', font = ft, fg="black")
oriText = Text(frame, width = 80, height = 8)
transBtn = Button(frame, text = '翻译', width = 39, fg="red",  command = trans)
clearBtn = Button(frame, text = '清空', width = 39, fg="blue",  command = clear)

bdLabel = Label(frame, text = '百度翻译', font = lft)
bdText = Text(frame, width = 80, height = 8)
ydLabel = Label(frame, text = '有道翻译', font = lft)
ydText = Text(frame, width = 80, height = 8)


oriLabel.grid(row = 0, columnspan = 2)
oriText.grid(row = 1, columnspan = 2)
transBtn.grid(row = 2, column = 0)
clearBtn.grid(row = 2, column = 1)


bdLabel.grid(row = 3, columnspan = 2)
bdText.grid(row = 4, columnspan = 2)
ydLabel.grid(row = 5, columnspan = 2)
ydText.grid(row = 6, columnspan = 2)

if __name__ == '__main__':
    frame.mainloop()