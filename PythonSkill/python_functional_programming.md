#python的函数式编程-高阶函数

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

#### 高阶函数
python中变量可以指向函数
```python
>>> f = abs
>>> f(-10)
10
```
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
```python
def add(x, y, f):
    return f(x) + f(y)



>>> add(-5, 6, abs)
11
```


#### 迭代器(Iterator)、iterable、生成器(Generator)
python 标准库中提供了 `itertools`, `functools`, `operator` 三个库支持函数式编程，对高阶函数的支持，python 提供 `decorator` 语法糖。 迭代器 (`iterator`)和生成器(`generator`)概念是 python 函数式编程的基础，利用迭代器和生成器可以实现函数式编程中经常用到的 `map()`, `filter()`, `reduce()` 等过程以及 `itertools`, `functools` 中提供的绝大部分功能。

迭代器(·)必须至少要定义 `__iter__()` 和 `__next__()` 两个方法，通过 `iter()` 和 `next()` 函数调用。 `iter()` 生成一个迭代器， `next()` 每调用一次都会返回下一个值。

生成器(`generator`)是用来生成迭代器的函数。与普通函数相同，只是返回值时用 `yield` 而不是 `return`。

`yield`构造的生成器
```python
def squares(start, stop):
    for i in range(start, stop):
        yield i*i
```

等同于生成器表达式：
```python
（i*i for i in range(start, stop))
```
列表推倒式是：
```python
[i*i for i in range(start, stop)]
```

如果是构建一个自定义的迭代器：
```python
class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current
```
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
- 一类是集合数据类型，如`list`、`tuple`、`dict`、`set`、`str`等；
- 一类是`generator`，包括生成器和带`yield`的generator function。  
这些可以直接作用于for循环的对象统称为可迭代对象：`Iterable`。

可以使用`isinstance()`判断一个对象是否是`Iterable`对象
```python
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
```
而生成器不但可以作用于for循环，还可以被`next()`函数不断调用并返回下一个值，直到最后抛出`StopIteration`错误表示无法继续返回下一个值了。
可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象
```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
```
生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```



#### map/reduce

`map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。

```python
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

`reduce`把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算

```python
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579
```

#### filter
和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的时，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。
```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
```


####  sorted
```python
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

`sorted()`函数是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```


#### 装饰器decorator
使用语法糖`@`来装饰函数，相当于“myfunc = deco(myfunc)”  
但发现新函数只在第一次被调用，且原函数多调用了一次
```python
def deco(func):  
    print("before myfunc() called.")  
    func()  
    print("  after myfunc() called.")  
    return func  

@deco  
def myfunc():  
    print(" myfunc() called.")  

myfunc()  
```

其实任何时候你定义装饰器的时候，都应该使用 `functools` 库中的 `@wraps` 装饰器来注解底层包装函数。
```python
import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):

     while n > 0:
         n -= 1

countdown(100000)  #结果输出：countdown 0.016767024993896484
```

假设装饰器是通过 `@wraps` 来实现的，那么你可以通过访问`__wrapped__`属性来访问原始函数：

```python
>>> @somedecorator
>>> def add(x, y):
...     return x + y
...
>>> orig_add = add.__wrapped__
>>> orig_add(3, 4)
7
>>>
```
