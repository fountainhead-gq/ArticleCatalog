<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python UnitTest](#python3%E5%8F%8A%E5%BA%94%E7%94%A86-unittest)
  - [Intro](#intro)
  - [Pylint](#pylint)
  - [UnitTest](#unittest)
  - [doctest](#doctest)
  - [debugger](#debugger)
  - [decorator](#decorator)
  - [nose](#nose)
    - [install](#install)
    - [usage](#usage)
  - [assert](#assert)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Python UnitTest

[如何测试Python应用](http://py.windrunner.info/great-code/testing.html)

[如何测试Django应用](http://py.windrunner.info/great-code/django-testing.html)

### Intro

- 每个测试单元应该关注于一个功能，并保证其正确性。

- 测试单元之间应该尽可能独立，也就是说可以独立运行，与顺序无关。

- 测试的速度应该尽可能快，过慢的测试速度会成为开发的瓶颈。对于耗费时间很长的重型测试，应该将其独立出来。

- 在集中编程前后都应该完整地运行一遍测试，以保证不会造成意外的破坏。

- 在编程过程中，如果需要中断工作，那么编写一个不能运行的测试对于恢复工作非常有帮助。

- debug 的第一步就是写一个针对性的单元测试，虽然这做起来并不一定容易，但却非常有价值。

- 虽然 PEP8 提倡简短的命名，但在测试函数名称应该长而有意义。比如，编程中你可能使用 `square()`甚至`sqr()`这样的函数名称，但是在测试中你应该写成：`test_square_of_number_2()`, `test_square_negative_number()`

### Pylint

使用Pylint来进行Python代码检测。[Pylint官网](http://www.pylint.org/)

```bash
# install
$ pip3 install pylint
# usage
$ pylint example.py
# 之后会打印检测结果和得分
```

### UnitTest

Python自带[unittest标准库](https://docs.python.org/3/library/unittest.html)。在unittest中，通过assert开头的断言方法，来检查返回的结果是否符合预期

```python
# 编写一个待测试的函数
def just_do_it(text):
	return text.capitalize()

import unittest # Python的内置标准库，依赖于Java的JUnit

class TestCap(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_one_word(self):
		text = 'duck'
		result = just_do_it(text)
		self.assertEqual(result, 'Duck')

	def test_multiple_words(self):
		text = 'a veritable flock of ducks'
		result = just_do_it(text)
		self.assertEqual(result, 'A Veritable Flock Of Duck')

if __name__ == '__main__':
	unittest.main()
```

- `setUp()`方法会在每个测试方法执行之前执行，常用来进行一些初始化和分配外部资源的操作
- `tearDown()`方法则在每个测试方法执行之后执行，常用来回收外部资源

*断言方法*

- `assertEqual(first, second, msg=None)`
- `assertNotEqual(first, second, msg=None)`
- `assertTrue(expr, msg=None)`
- `assertFalse(expr, msg=None)`
- `assertIs(first, second, msg=None)`
- `assertIsNot(first, second, msg=None)`
- `assertIsNone(expr, msg=None)`
- `assertIsNotNone(expr, msg=None)`
- `assertIn(first, second, msg=None)`
- `assertNotIn(first, second, msg=None)`
- `assertIsInstance(obj, cls, msg=None)`
- `assertNotIsInstance(obj, cls, msg=None)`
- `assertGreater(first, second, msg=None)`
- `assertGreaterEqual(first, second, msg=None)`
- `assertLess(first, second, msg=None)`
- `assertLessEqual(first, second, msg=None)`

### doctest

又一个Python[自带标准库doctest](https://docs.python.org/3/library/doctest.html)

使用这个包可以把测试写在文档字符串中，在测试的同时起到文档的作用。格式要求：

```python
# 先>>> 函数调用
# 下一行输出预期的结果
"""
>>> fun()
result
"""
```

EXAMPLE：

```python
import doctest

def list_generator(number):
	"""
	>>> list_generator(5)
	[0, 1, 2, 3, 4]
	"""
	return [n for n in range(number)]

if __name__ == '__main__':
	doctest.testmod()
```

运行Python文件，如果没有错误，则不会输出内容。现在把list_generator稍微改变一下：

```python
import doctest

def list_generator(number):
	"""
	>>> list_generator(5)
	[0, 1, 2, 3, 4]
	"""
	return [str(n) for n in range(number)]

if __name__ == '__main__':
	doctest.testmod()
```

运行文件，输出如下内容：

```bash
**********************************************************************
File "example.py", line 5, in __main__.list_generator
Failed example:
    list_generator(5)
Expected:
    [0, 1, 2, 3, 4]
Got:
    ['0', '1', '2', '3', '4']
**********************************************************************
1 items had failures:
   1 of   1 in __main__.list_generator
***Test Failed*** 1 failures.
```

By the way，如果你不想写：

```python
if __name__ == '__main__':
	doctest.testmod()
```

那么，在运行Python文件的时候，需要：

```bash
# python example.py 之前这样运行
$ python example.py -v # 现在这样运行才能进行代码测试
```

### debugger

[Python用于调试代码的标准库pdb](https://docs.python.org/3/library/pdb.html)

```python
import pdb
pdb.set_trace() # 设置一个断点

# example
print('debugger begin')
pdb.set_trace()
for i in range(5):
	print(i)

pdb.set_trace()
print('debugger end')
```

运行文件，会进入交互式debugger模式。在该模式下可以进行如下操作(仅列常用)：

- `c`: 继续执行代码，直至下一个断点
- `s`: 执行**当前代码行**，进入当前行调用的函数内部，并停在第一个能停的地方
- `n`: 继续执行，到当前函数的下一行停止，或者当前行直接返回（单步跳过）
- `w`: 显示当前正在执行的代码行的上下文信息
- `a`: 打印当前函数的参数列表
- `l`: 该命令后没有参数时，列出当前debug行附近的11行代码
- `q`: 退出运行的代码

```bash
# 在Pdb的debug模式下

# 以当前行为中心，上下各列出5行代码。共计11行
(Pdb) l
(Pdb) l .

# 以第一个参数为起点，往后列出共计11行代码
(Pdb) l 2

# 以第一个参数为行数起点，第二个参数作为终止行数，列出期间的代码
(Pdb) l 2, 5
```

### decorator

鉴于decorator可以人为的改变函数的行为，而可以不去影响它的内部逻辑，因此我们可以通过装饰器来增强函数行为，让它在执行前后打印出我们想要观测的数据。

```python
from time import sleep


def decorate_fun(fun):
	def new_fun(*args, **kwargs):
		print('got args: {}, {}'.format(args, kwargs))
		print('this is a fun\'s start')
		fun(*args, **kwargs)
		print('this is the fun\'s end')
	return new_fun

@decorate_fun
def fun(number, start_number=0):
	for n in range(number):
		start_number += n
		print(n)
		sleep(1)
	print('the final number is {}'.format(start_number))

print(fun.__name__) # new_fun
fun(5, start_number=5)
```

如上，通过装饰器修饰之后，之前的函数fun会被new_fun替代，被重写的函数名和注释文档。为了避免这个情况，可以使用`functools.wraps`：

```python
from functools import wraps

def decorate_fun(fun):
	@wraps(fun)
	def new_fun(*args, **kwargs):
		print('got args: {}, {}'.format(args, kwargs))
		print('this is a fun\'s start')
		fun(*args, **kwargs)
		print('this is the fun\'s end')
	return new_fun

# def fun..
print(fun.__name__) # fun
```

### [nose](https://nose.readthedocs.io/en/latest/index.html)

#### install

```bash
$ pip3 install nose
```

nose与其他测试框架或者unittest相比，其最大的特色是不需要专门创建一个包含测试方法的类。任何名称中带有test的函数都会被执行测试。
除此以外，在项目目录下运行:

```python
def test_example():
	a = 1
	b = 3
	assert a + b is 4
```

```bash
$ nosetests
```

都会监测到你的测试方法并运行测试

#### usage

nose会自动识别源文件，目录或包中的测试用例。任何符合正则表达式：

```python
(?:^|[b_.-])[Tt]est
```

的类、函数、文件或目录，以及TestCase的子类都会被识别并执行。除了自动搜索测试以外，可以显式的指定文件、模块或函数：

```bash
$ nosetests only_test_this.py
$ nosetests test.module
```

### assert

通过断言进行防御性的编程、代码检查以及运行时对程序逻辑的检测等等。详见：
[Python 使用断言的最佳时机](http://www.oschina.net/translate/when-to-use-assert)
