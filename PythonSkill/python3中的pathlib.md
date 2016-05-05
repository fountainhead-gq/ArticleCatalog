## Mpython3中的pathlib

pathlib比os.path更简单更好用。简单示例：

```python
#coding=utf-8
from pathlib import Path
import os


cwd_path = Path.cwd()  # 返回当前路径，相当于os.getcwd()
print(cwd_path)

home_path = Path.home()  # 返回用户主目录，相当于os.path.expanduser('~')
print(home_path)


root = Path(r"F:/")
exist = Path.exists(root)  # 判断路径是否存在
print(exist)


is_dir = Path.is_dir(root)  # 判断是否是路径
print(is_dir)

is_file = Path.is_file(root)  # 判断是否是文件
print(is_file)


config_dir = root / Path("pytest")  # 路径的连接
print(config_dir)

config_file = config_dir / Path("newtest.py")

# 读取文件
with config_file.open("r") as f:
    print(f.read())

# 读取文件，更简单的方法
txt_read = config_file.read_text()
print(txt_read)

```
