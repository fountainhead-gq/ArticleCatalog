#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'shucun'

# 调用打开链接
import webbrowser
webbrowser.open_new_tab('http://baidu.com/')

# zip合并
a = [(1, 2), (3, 4), (5, 6)]
z = list(zip(*a))
print(z)
# [(1, 3, 5), (2, 4, 6)]

# 字典合并
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
d = dict(zip(t1, t2))
print(d)


# 列表的重构
a = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
s = sum(a, [])
print(s)
# 或者
import itertools
data = [[1, 2, 3], [4, 5, 6], [7, 8], [9]]
d = list(itertools.chain.from_iterable(data))
print(d)
# 再或者
from functools import reduce
from operator import add
data = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
dd = reduce(add, data)
print(dd)


# 字典生成
dt = {a: a*2 for a in range(1, 10)}
print(dt)


# 集合
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a | b)  # {1, 2, 3, 4, 5, 6}
print(a & b)  # {3, 4}
print(a ^ b)  # {1, 2, 5, 6}
print(a - b)  # {1, 2}

# 变量解包
first, second, *rest = (1, 2, 3, 4, 5, 6, 7, 8)
print(first)  # 1
print(second)  # 2
print(rest)  # [3, 4, 5, 6, 7, 8]

# 列表元素序号
l = ["spam", "ham", "dock"]
print(list(enumerate(l)))
print(list(enumerate(l, 10))) # 设置计数起点


# 列表拷贝
x = [1, 2, 3]
y = x[:]
print(y)


