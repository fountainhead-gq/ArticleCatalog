# operator, functools, itertools


## operator 模块
operator 模块提供了比较大小、运算符的操作

简单示例：
```python
from functools import reduce
import operator as op

# 加法
print(reduce(op.add, range(10)))  # 45
print(op.add(1, 5))  # 6

# 乘法
print(reduce(op.mul, range(1, 5)))  # 24
print(op.mul(2, 5))  # 10

# 使用元素的第二个元素排序
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = op.itemgetter(1)
print(sorted(inventory, key=getcount))  # [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

# 比较
print(op.gt(1, 2))  # False
```


## functools 模块
functools 包含很多跟函数相关的工具，比如`reduce`、`wraps`、`partial` 等

- `wraps`用来消除装饰器添加后导致函数名和函数doc改变的副作用  
- `partial` 通过包装"重新定义" 函数,作用就是把函数参数传入到`func`中后，生成一个新的函数
-

```python
# -*- coding: utf-8 -*-

from functools import reduce, partial, wraps
import operator as op


# 将 reduce 的第一个参数指定为加法，得到的是类似求和的函数
sum_ = partial(reduce, op.add)

# 将 reduce 的第一个参数指定为乘法，得到的是类似求连乘的函数
prod_ = partial(reduce, op.mul)

print(sum_([1, 2, 3, 4]))  # 10
print(prod_([1, 2, 3, 4], 2))  # 48
print(prod_([1, 2, 3, 4]))  # 24

# 十进制
basetwo = partial(int, base=2)
print(basetwo('1001'))  # 9

# reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))  # 15


# @wraps()
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

print(example())
# Calling decorated function
# Called example function

print(example.__name__)  # 不添加装饰器@wrap，结果是wrapper
# example

print(example.__doc__)  # 不添加装饰器@wrap，结果为空
# Docstring
```


## itertools 模块
itertools 包含很多与迭代器对象相关的工具，比如 `permutations`、 `combinations`，`groupby`

示例代码：
```python
# -*- coding: utf-8 -*-

from itertools import cycle, groupby, islice, permutations, combinations, accumulate
import operator

# cycle() 返回一个无限的迭代器，按照顺序重复输出输入迭代器中的内容

# islice 返回一个迭代器中的一段内容
print(list(islice(cycle('abcd'), 0, 10)))  # ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']

# groupby 返回一个字典，按照指定的 key 对一组数据进行分组，字典的键是 key，值是一个迭代器：
animals = sorted(['pig', 'cow', 'giraffe', 'elephant',
                  'dog', 'cat', 'hippo', 'lion', 'tiger'], key=len)

for k, g in groupby(animals, key=len): # 按照长度进行分组
    print(k, list(g))

# 3 ['pig', 'cow', 'dog', 'cat']
# 4 ['lion']
# 5 ['hippo', 'tiger']
# 7 ['giraffe']
# 8 ['elephant']

# 排列 permutations('str', r), 尽可能多的排列，不重复
print([''.join(p) for p in permutations('abc', 3)])  # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print([list(c) for c in permutations([1, 2, 3], 2)])  # [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]

# 组合 combinations('xx', r)，按照顺序，不重复
print([list(c) for c in combinations([1, 2, 3], 2)])  # [[1, 2], [1, 3], [2, 3]]

# accumulate
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(accumulate(data, operator.mul)))  # [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
print(list(accumulate(data, max)))  #  [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
```
