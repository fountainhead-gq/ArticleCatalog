#!/usr/bin/env python
# coding: utf-8

import zipfile
import os


path = os.getcwd()
path = os.path.join(path, 'forum.zip')

z = zipfile.ZipFile(path, "r")
for filename in z.namelist():
        print('名称', filename)
        bytes = z.read(filename)
        print('大小', len(bytes))
        print('内容', bytes)