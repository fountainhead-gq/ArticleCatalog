# md5和sha加密

python提供了一个进行hash加密的模块：hashlib

在应用中，常用的是md5加密和sha1加密（注意，是数字1,不是字母l，这类命名，应该最大限度避免。）

## md5

md5的全称是Message-Digest Algorithm 5（信息-摘要算法）。128位长度。目前md5是一种不可逆算法。 具有很高的安全性。它对应任何字符串都可以加密成一段唯一的固定长度的代码。  

## sha1

sha1的全称是Secure Hash Algorithm(安全哈希算法) 。SHA1基于MD5，加密后的数据长度更长， 它对长度小于264的输入，产生长度为160bit的散列值。比md5多32位。 因此，比MD5更加安全，但SHA1的运算速度就比MD5要慢了。  

## Python中的用法 

Python 内置的 hashlib 模块就包括了 md5 、 sha1和sha256等算法。使用方法：

### 以MD5为例：

```
#! /usr/bin/evn python3
#coding:utf-8

import hashlib

data = 'This a test!'

hash_md5 = hashlib.md5(data.encode('utf-8'))
hash_sha256 = hashlib.sha256(data.encode('utf-8'))
hash_sha1 = hashlib.sha1(data.encode('utf-8'))
hash_sha384 = hashlib.sha384(data.encode('utf-8'))
hash_sha224 = hashlib.sha224(data.encode('utf-8'))
hash_sha512 = hashlib.sha512(data.encode('utf-8'))

pswd_md5 = hash_md5.hexdigest()
pswd_sha256 = hash_sha256.hexdigest()
pswd_sha512 = hash_sha512.hexdigest()
pswd_sha384 = hash_sha384.hexdigest()
pswd_sha224 = hash_sha224.hexdigest()
pswd_sha1 = hash_sha1.hexdigest()

print(pswd_md5)
print(pswd_sha1)
print(pswd_sha224)
print(pswd_sha256)
print(pswd_sha384)
print(pswd_sha512)
```
md5的输出结果：

    e1e058efeec878c45be77f41ec6650fe
  

MD5的用途：    

- 加密网站注册用户的密码。    
- 网站用户上传图片 / 文件后，计算出MD5值作为文件名。（MD5可以保证唯一性）    
- key-value数据库中使用MD5值作为key。    
- 比较两个文件是否相同。（大家在下载一些资源的时候，就会发现网站提供了MD5值，就是用来检测文件是否被篡改）    
  

### sha1等方法的使用

与MD5类似：

    import hashlib
    data = 'This a sha1 test!'
    hashlib.sha1(data.encode('utf-8')).hexdigest()      

### 处理大文件

上面说过可以用MD5来检测两个文件是否相同，但想想，如果是两个很大的文件，担心内存不够用，这时怎么办？ 这就要使用 update 方法了。

代码如下：

    import hashlib
    def get_file_md5(f):    
        m = hashlib.md5()    
        while True:        
            data = f.read(10240)        
            if not data:            
                break        
            m.update(data)    
        return m.hexdigest()

    with open(YOUR_FILE, 'rb') as f:    
        file_md5 = get_file_md5(f)


可以用下面这段代码验证一下：

    import hashlib

    x = hashlib.md5()
    x.update('hello, '.encode('utf-8'))
    x.update('python'.encode('utf-8'))
    pwd = x.hexdigest()
    pwd1 = hashlib.md5('hello, python'.encode('utf-8')).hexdigest()
    
    print(pwd)
    print(pwd1)


两次的输出是一样的。 其他的加密也是一样的。

## 密码加盐
为了提高密码安全，通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

    def calc_md5(password):
        return get_md5(password + 'the-Salt') #添加一个不易猜出的字符串，提高安全性
