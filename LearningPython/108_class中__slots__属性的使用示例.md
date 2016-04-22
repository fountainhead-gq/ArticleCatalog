
`_slots__`方法是Python的一个重要内置类方法。python类在进行实例化的时候声明`__slots__`，实例就只会含有`__slots__`里有的属性名。

## 使用`__slots__`

如果我们想只允许对实例添加特定的属性时，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
```Python
>>> class Student(object):
...     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
...
```
然后，我们试试：

```Python
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
```

要注意的是`__slots__`定义的属性仅对当前类起作用，对继承的子类是不起作用的：
```Python
>>> class GraduateStudent(Student):
...     pass
...
>>> g = GraduateStudent()
>>> g.score = 9999
```
除非在子类中也定义`__slots__`，子类允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。


## 内存优化

定义`__slots__` 后，可以再实例上分配的属性名称将被限制为指定的名称。否则将引发AttributeError,这种限制可以阻止其他人向现有的实例添加新的属性。``

使用`__slots__`的类的实例不在使用字典来存储数据。相反，会使用基于数组的更加紧凑的数据结构。
在会创建大量对象的程序中，使用`__slots__`可以显著减少内存占用和使用时间
```Python
class Account(object):
  __slots__ = ('name' ,'balance')
class Test(object):
  def __init__(self ,name):
    self.name = name
```
