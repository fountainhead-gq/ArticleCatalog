<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python打包发布自己的库](#python3%E5%8F%8A%E5%BA%94%E7%94%A87-%E6%89%93%E5%8C%85%E5%8F%91%E5%B8%83%E8%87%AA%E5%B7%B1%E7%9A%84%E5%BA%93)
  - [setup.py](#setuppy)
    - [目录结构](#%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84)
    - [编写文件](#%E7%BC%96%E5%86%99%E6%96%87%E4%BB%B6)
    - [本地安装](#%E6%9C%AC%E5%9C%B0%E5%AE%89%E8%A3%85)
  - [upload to pip](#upload-to-pip)
    - [register](#register)
    - [upload](#upload)
    - [upgrade](#upgrade)
  - [pip常用命令](#pip%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Python打包发布自己的库

撸完自己的代码，本地跑起来畅爽无阻~这种时候自己一个人痛快怎么行，是时候把代码上传到pip&github让大家一起爽爽了。但如果只是源码就太low了，要怎么才能做成第三方库那样安装后使用呢？

### setup.py

如果想让别人能够安装你的源码，作为第三方库那样使用的话，就需要编写`setup.py`文件了。

#### 目录结构

在项目根目录下建立`setup.py`文件

假设项目目录如下：

```bash
project/
    example/
        __init__.py
        entry.py
    setup.py
    run.py
    LICENSE
```

题外话：不知道给自己的开源项目用哪种LICENSE？可以看看这个网站：

[Choose an open source license](http://choosealicense.com/)

#### 编写文件

废话少说，直接在代码中学习如何编写

```python
# 引用包管理工具setuptools，其中find_packages可以帮我们便捷的找到自己代码中编写的库
from setuptools import setup, find_packages

setup(
    name='example', # 包名称，之后如果上传到了pypi，则需要通过该名称下载
    version='0.1', # version只能是数字，还有其他字符则会报错
    keywords=('setup', 'example'),
    description='setup example',
    long_description='',
    license='MIT', # 遵循的协议
    install_requires=[], # 这里面填写项目用到的第三方依赖
    author='ecmadao',
    author_email='wlec@outlook.com',
    packages=find_packages(), # 项目内所有自己编写的库
    platforms='any',
    url='' # 项目链接,
    include_package_data = True,
    entry_points={
        'console_scripts':[
            'example=run:main'
        ]
    },
)
```

着重了解下`entry_points`：

当你写的Python项目可以在命令行里，通过运行某个文件跑起来的时候，则可以配置`entry_points`

`console_scripts`接受一个list作为值，list里的各个value配置了命令行的语句。以上面的`example=run:main`为里，它表明，当你安装了该项目之后，就可以在命令行中通过：

```bash
$ example
```

来运行项目根目录下`run.py`内的`main`函数。即是说：

`entry_points : [可执行程序名]=引入的包名.子包名.模块名:入口函数`

#### 本地安装

编写好了setup，尝试下本地安装：

```bash
# 在项目根目录下
$ python setup.py install
```

so easy!

### upload to pip

`setup.py`写好了，本地测试安装也ok了，那么我们还可以把代码上传到pip，那样的话别人就能够通过`pip install XXX`来直接安装我们编写的库。

#### register

先到[pypi](https://pypi.python.org/pypi)注册一个账号，之后可以在上传代码的过程中绑定预先注册好的账号

#### upload

```bash
# 在项目根目录下
$ python setup.py register
# 之后安装提示登录pypi账号
$ python setup.py sdist
# 生成支持pip的文件
$ python setup.py sdist upload
# 生成支持pip的文件并上传代码
```

注：在第一步`setup.py register`时，可能会因为代码中的中文字符串产生如下错误：

```bash
$ python setup.py register
# SyntaxError: Non-ASCII character '\xe4' in file /Users/ecmadao1/Dev/Python/Spider-12306/train/__init__.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

则需要在使用中文的文件开头添加注释`# -*- coding: UTF-8 -*-`

#### upgrade

- 更新代码里的版本号
- 重复upload的步骤，会自动上传并升级库至新版

### pip常用命令

```bash
# 查看具体安装文件
$ pip3 show --files SomePackage
# 列出所有的包
$ pip3 list
# 检查有无升级
$ pip3 list --outdated
# 更新包
$ pip3 install -U|--upgrade <package>
# 卸载包
$ pip3 uninstall <package>
```
