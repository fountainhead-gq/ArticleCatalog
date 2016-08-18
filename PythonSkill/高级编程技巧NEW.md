## 列表推导式(list comprehensions)
是一种将for循环、if表达式以及赋值语句放到单一语句中的一种方法。就是能够通过一个表达式对一个列表做映射或过滤操作。


一个列表推导式包含以下几个部分：
- 一个输入序列
- 一个表示输入序列成员的变量
- 一个可选的断言表达式
- 一个将输入序列中满足断言表达式的成员变换成输出列表成员的输出表达式


举个例子，我们需要从一个输入列表中将所有大于0的整数平方生成一个新的序列。

```Python
num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = map(lambda x: x ** 2, filter(lambda x: x > 0, num))
print (list(filtered_and_squared))

# [1, 16, 100, 4, 9]
```
使用filter、lambda和map函数可以简化代码，列表推导能够进一步简化:
``` Python
num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = [ x**2 for x in num if x > 0]
print (list(filtered_and_squared))

# [1, 16, 100, 4, 9]
```

- 迭代器(iterator)遍历输入序列num的每个成员x
- 断言式判断每个成员是否大于零
- 如果成员大于零，则被交给输出表达式，平方之后成为输出列表的成员。


列表推导式被封装在一个列表中，所以很明显它能够立即生成一个新列表。这里只有一个type函数调用而没有隐式调用lambda函数，列表推导式正是使用了一个常规的迭代器、一个表达式和一个if表达式来控制可选的参数。另外，列表推导的缺点就是整个列表必须一次性加载于内存之中，如果达到极限的话，内存会被用完。


生成器(Generator)能够很好的解决。生成器表达式不会一次将整个列表加载到内存之中，而是生成一个生成器对象(Generator objector)，所以一次只加载一个列表元素。

生成器表达式同列表推导式有着几乎相同的语法结构，区别在于生成器表达式是 **圆括号**，而不是 *方括号*：

```Python
num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = (x**2 for x in num if x > 0)
print (list(filtered_and_squared))

# [1, 16, 100, 4, 9]
```
再改造下代码

```Python
num = [1, 4, -5, 10, -7, 2, 3, -1]

def square_generator(optional_parameter):
    return (x ** 2 for x in num if x > optional_parameter)

print(list(square_generator(0)))  

# [1, 16, 100, 4, 9]  
```


## 装饰器(Decorators)
装饰器为我们提供了一个增加已有函数或类的功能的有效方法。装饰器是一个包装了另一个函数的特殊函数：主函数被调用，并且其返回值将会被传给装饰器，接下来装饰器将返回一个包装了主函数的替代函数，程序的其他部分看到的将是这个包装函数。

装饰器是一个包装了另一个函数的特殊函数：主函数被调用，并且其返回值将会被传给装饰器，接下来装饰器将返回一个包装了主函数的替代函数，程序的其他部分看到的将是这个包装函数。

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
def countdown(n):
    while n > 0:
        n -= 1

countdown(100000)

# ('countdown', 0.006999969482421875)
```
语法糖@标识了装饰器。


## 描述器(Descriptors)

描述器决定了对象属性是如何被访问的。描述器的作用是定制当你想引用一个属性时所发生的操作。

构建描述器的方法是至少定义以下三个方法中的一个。需要注意，下文中的`instance`是包含被访问属性的对象实例，而`owner`则是被描述器修辞的类。

- `__get__(self, instance, owner)` – 这个方法是当属性被通过`(value = obj.attr)`的方式获取时调用，这个方法的返回值将被赋给请求此属性值的代码部分。
- `__set__(self, instance, value)` – 这个方法是当希望设置属性的值`(obj.attr = ‘value’)`时被调用，该方法不会返回任何值。
- `__delete__(self, instance)` – 当从一个对象中删除一个属性时`(del obj.attr)`，调用此方法。


考虑以下代码，instance指的是temp，而owner则是Temperature：
```Python
class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Temperature(object):
    celsius = Celsius()

temp=Temperature()
temp.celsius #calls Celsius.__get__
```
综上，描述器被赋值给类，而这些特殊的方法就在属性被访问的时候根据具体的访问类型自动地调用。


## 元类(MetaClasses)

元类提供了一个改变Python类行为的有效方式。元类的定义是“一个类的类”。任何实例它自己的类都是元类。

```Python
class demo(object):
    pass

obj = demo()

print ("Class of obj is {0}".format(obj.__class__))
print ("Class of obj is {0}".format(demo.__class__))

# Class of obj is <class '__main__.demo'>
# Class of obj is <class 'type'>
```

在上例中，我们定义了一个类demo，并且生成了一个该类的对象obj。首先，可以看到obj的`__class__`是demo。有意思的来了，那么demo的class又是什么呢？可以看到demo的`__class__`是type。

所以说type是python类的类，换句话说，上例中的obj是一个demo的对象，而demo本身又是type的一个对象。

所以说type就是一个元类，而且是python中最常见的元类，因为它使python中所有类的默认元类。

因为元类是类的类，所以它被用来创建类(正如类是被用来创建对象的一样)。但是，难道我们不是通过一个标准的类定义来创建类的么？的确是这样，但是python内部的运作机制如下：

当看见一个类定义，python会收集所有属性到一个字典中。
当类定义结束，python将决定类的元类，我们就称它为Meta吧。
最后，python执行Meta(name, bases, dct)，其中：

a. Meta是元类，所以这个调用是实例化它。
b. name是新建类的类名。
c. bases是新建类的基类元组
d. dct将属性名映射到对象，列出所有的类属性。

那么如何确定一个类(A)的元类呢？简单来说，如果一个类(A)自身或其基类(Base_A)之一有__metaclass__属性存在，则这个类(A/Base_A)就是类(A)的元类。否则type就将是类(A)的元类。
