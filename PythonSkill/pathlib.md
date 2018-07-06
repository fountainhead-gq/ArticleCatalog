
## 列出所有子目录

 在linux环境下，WindowsPath都会变为PosixPath


```python
import pathlib
p = pathlib.Path('.')
[x for x in p.iterdir() if x.is_dir()]
```




    [WindowsPath('.ipynb_checkpoints'),
     WindowsPath('images'),
     WindowsPath('__pycache__')]



## 列出指定类型的文件


```python
list(p.glob('**/*.py'))
```




    [WindowsPath('utils.py')]



## 路径拼接


```python
p = pathlib.Path(r'F:\cookies\python')
q = p / 'learnPython'
print(q)
```

    F:\cookies\python\learnPython
    

## 查询属性


```python
q.exists()
```




    False




```python
q.is_dir()
```




    False




```python
pathlib.PureWindowsPath('c:/Windows', 'd:bar')
```




    PureWindowsPath('d:bar')



## 常用属性和方法


```python
pathlib.PureWindowsPath('c:/Program Files/').drive
```




    'c:'




```python
pathlib.PureWindowsPath('/user').root
```




    '\\'




```python
p = pathlib.PureWindowsPath('c:/foo/bar/setup.py')
print(p.parents[0], p.parents[1], p.parents[2])
print(p.name)
print(p.suffix)
print(p.stem)
print(p.as_posix())
```

    c:\foo\bar c:\foo c:\
    setup.py
    .py
    setup
    c:/foo/bar/setup.py
    


```python
# 当前路径
pathlib.Path.cwd()
```




    WindowsPath('F:/TEST/yolo1')




```python
# exists()判断文件或目录是否存在
pathlib.Path('/etc').exists()
```




    False




```python
found_images = glob.glob('/path/**/*.jpg', recursive=True)

# 等价
found_images = pathlib.Path('/path/').glob('**/*.jpg')
```


```python
from pathlib import Path

directory = Path("/etc")
filepath = directory / "hosts"

if filepath.exists():
    print('hosts exist')

# 等价于
import os
directory = "/etc"
filepath = os.path.join(directory, "hosts")

if os.path.exists(filepath):
    print('hosts exist')
```

is_dir()判断是否是目录

is_file()判断是否是文件

is_symlink()判断是否是链接文件

iterdir()如果path指向一个目录，则返回该目录下所有内容的生成器

mkdir(mode=0o777, parents=False)创建目录

open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)打开文件

owner()获取文件所有者

rename(target)修改名称
