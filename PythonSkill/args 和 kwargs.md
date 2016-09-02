# `*args `和 `**kwargs`


`*args`和 `**kwargs`通常使用在函数定义里。`*args` 、 `**kwargs`允许给函数传不定数量的参数。其中，`*args`是可变的positional arguments列表，`**kwargs`是可变的keyword arguments列表。并且，`*args`必须位于`**kwargs`之前，因为positional arguments（位置参数）必须位于keyword arguments（关键字参数）之前。


示例：
```python
def test_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)
   for v in args:
      print('Optional argument (*args): ', v)
   for k, v in kwargs.items():
      print('Optional argument %s (*kwargs): %s' % (k, v))

test_kwargs(1, 2, 3, 4, k1=5, k2=6)

#Required argument:  1
#Optional argument (*args):  2
#Optional argument (*args):  3
#Optional argument (*args):  4
#Optional argument k1 (*kwargs): 5
#Optional argument k2 (*kwargs): 6
```


`*args`和`**kwargs`语法同样可以在函数调用的时候使用。

```python
def test_args(first, second, third, fourth, fifth):
    print('First argument: ', first)
    print('Second argument: ', second)
    print('Third argument: ', third)
    print('Fourth argument: ', fourth)
    print('Fifth argument: ', fifth)

# Use *args
args = [1, 2, 3, 4, 5]
test_args(*args)

#First argument:  1
#Second argument:  2
#Third argument:  3
#Fourth argument:  4
#Fifth argument:  5


# Use **kwargs
kwargs = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
    'fifth': 5
}

test_args(**kwargs)

#First argument:  1
#Second argument:  2
#Third argument:  3
#Fourth argument:  4
#Fifth argument:  5
```
