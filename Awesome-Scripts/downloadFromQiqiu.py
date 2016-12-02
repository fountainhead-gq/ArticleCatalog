# -*- coding: utf-8 -*-

import requests
import os
from qiniu import Auth


#需要填写你的 Access Key 和 Secret Key
access_key = 'vTvNf********lLW'
secret_key = 'qUWut********SG'

url ='http://oh******.bkt.clouddn.com/'
para = '?imageMogr2/thumbnail/!300x300r|imageView2/4/w/1000/h/300|imageMogr2/gravity/North/crop/300x300'

# 照片的不同截取规则
# para = '?imageView2/5/w/150/h/150/format/jpg/interlace/0/q/80'
# para = '?imageMogr2/thumbnail/!300x300r|imageView2/0/w/1000/h/300|imageMogr2/gravity/North/crop/300x300'
# para = '?imageMogr2/thumbnail/!300x300r|imageView2/0/w/1000/h/300|imageMogr2/gravity/Center/crop/300x300'
# para = '?imageMogr2/thumbnail/!300x300r|imageView2/0/w/1000/h/300|imageMogr2/gravity/Center/crop/!300x300-10-40'

q = Auth(access_key, secret_key)

path = os.getcwd()
path = os.path.join(path, r'dest_photo')




for root, dirs, files in os.walk(path):
    print(files)
    fileLength = len(files)
    # filename = os.path.split(path)[1]

    for i in range(fileLength):
        localfile = path + "\%s" % files[i]  # 照片路径
        # file_name= os.path.splitext(files[i])  #文件名
        img_url = url + files[i] + para
        # 可以设置token过期时间
        private_url = q.private_download_url(img_url, expires=3600)
        r = requests.get(private_url)
        img_name = os.getcwd()
        img_name = os.path.join(img_name, r'restore_photo')
        if not os.path.isdir(img_name):
            os.mkdir(img_name)
        img_name =img_name + "\%s" % files[i]
        print(img_name)
        with open(img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
        





