# -*- coding: utf-8 -*-


from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os

#需要填写你的 Access Key 和 Secret Key
access_key = 'vTv6Q******ShWelLW'
secret_key = 'qUWut******V1aeSG'

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'toon-dest'


#上传文件的本地路径
path = os.getcwd()  
path = os.path.join(path, r'dest_photo')


for root, dirs, files in os.walk(path):
    print(files)
    fileLength = len(files)
    filename = os.path.split(path)[1]

    for i in range(fileLength):
        localfile = path + "\%s" % files[i]
        print(localfile)
		# 上传文件夹下的所有照片
        token = q.upload_token(bucket_name, files[i], 3600)
        ret, info = put_file(token, files[i], localfile)
        print(info)
        















