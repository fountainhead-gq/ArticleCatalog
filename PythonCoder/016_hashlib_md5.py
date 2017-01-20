#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os

path = os.getcwd()
path = os.path.join(path, 'README.md')


def md5_for_file(path, block_size=256*128, hr=True):
    md5 = hashlib.md5()  # 创建md5对象
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
             md5.update(chunk)  # 生成加密串，其中 chunk 是要加密的字符串
    if hr:
        return md5.hexdigest()  # 获取加密串
    return md5.digest()


def md5_for_str(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()


if __name__ == "__main__":
    print(md5_for_file(path))
    print(md5_for_str('直接加密字符串'))