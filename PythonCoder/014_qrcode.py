#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GQ'

# import Image 用于python2
from PIL import Image
import qrcode

'''
version：一个整数，范围为1到40，表示二维码的大小（最小值是1，是个12×12的矩阵），如果想让程序自动生成，将值设置为 None 并使用 fit=True 参数即可。
error_correction：二维码的纠错范围，可以选择4个常量
ERROR_CORRECT_L     7%以下的错误会被纠正
ERROR_CORRECT_M (default)    15%以下的错误会被纠正
ERROR_CORRECT_Q   25%以下的错误会被纠正
ERROR_CORRECT_H.    30%以下的错误会被纠正
boxsize:每个点（方块）中的像素个数
border:二维码距图像外围边框距离，默认为4，而且相关规定最小为4
'''
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
)
qr.add_data("http://www.guoshucun.gq")
qr.make(fit=True)

img = qr.make_image()
# img.save("qrcode.png")

# 二维码中添加logo
img = img.convert("RGBA")
icon = Image.open("girl.png")  # logo图片

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size

if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h

icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)  # 带ANTIALIAS滤镜缩放结果,极大弱化图片失真
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
img.paste(icon, (w, h), icon)

img.save("qrcode.png")
