# -*- coding: utf-8 -*-


import os
import shutil

path = os.getcwd()
path = os.path.join(path, r'unqualified')

# 根据A文件夹来查找B文件夹中的同名文件，并将件复制到新文件夹
for root, dirs, files in os.walk(path):
    fileLength = len(files)
    # filename = os.path.split(path)[1]
    for i in range(fileLength):
        localfile = path + "\%s" % files[i]  # 照片路径
        img_name = os.getcwd()
        img_name = os.path.join(img_name, r'photo')
        img_name = img_name + "\%s" % files[i]
        
        img_dest = os.getcwd()
        img_dest = os.path.join(img_dest, r'dest_photo')
        if not os.path.isdir(img_dest):
            os.mkdir(img_dest)
        img_dest = img_dest + "\%s" % files[i]
        shutil.copyfile(img_name, img_dest)
        print(img_dest)






