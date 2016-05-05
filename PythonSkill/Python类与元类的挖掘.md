## Python类与元类的挖掘


### 对象（object）
>对象是 Python 中对数据的一种抽象，Python 程序中所有数据都是通过对象或对象之间的关系来表示的。

在 Python 中，所有的对象都具有id、type、value三个属性：
- id 代表内存地址，可以通过内置函数 id() 查看，
-  type 表示对象的类别，不同的类别意味着该对象拥有的属性和方法等，可以通过 type() 方法查看：

```python
def who(obj):
    print(id(obj), type(obj))

who(1)
who(None)
who(who)

1452666672 <class 'int'>
1452507472 <class 'NoneType'>
10343560 <class 'function'>
```

对象作为 Python 中的基本单位，可以被创建、命名或删除。Python 中一般不需要手动删除对象，其垃圾回收机制会自动处理不再使用的对象。对于一些 Python 内置类型的对象，通常可以使用特定的语法生成，例如数字直接使用阿拉伯数字，字符串使用引号 ”，列表使用 []，字典使用 {} ，函数使用 def 语法等，这些对象的类型都是 Python 内置的.


### 类与实例

既然说 Python 是面向对象编程语言，也就允许用户自己创建对象，通常使用 class 语句，与其它对象不同的是，class 定义的对象（称之为类）可以用于产生新的对象（称之为实例）：

```python
class A:
pass
a = A()
who(A)
who(a)

140477703944616 <class 'type'>
4542635424 <class '__main__.A'>
```
A 是我们创建的一个新的类，而通过调用 A() 可以获得一个 A 类型的实例对象，我们将其赋值为 a，也就是说我们成功创建了一个与所有内置对象类型不同的对象 a，它的类型为 `__main__.A`！至此我们可以将 Python 中一切的对象分为两种：
- 可以用来生成新对象的类，包括内置的 int、str 以及自己定义的 A 等；
- 由类生成的实例对象，包括内置类型的数字、字符串以及自己定义的类型为 `__main__.A` 的 a。


### super, mro()
类或对象在 Python 中就承担了一部分命名空间的作用。比如说某些特定的方法或属性只有特定类型的对象才有，不同类型对象的属性和方法尽管名字可能相同，但由于隶属不同的命名空间，其值可能完全不同。

```python
class A(object):
    pass
class B(A):
    def method(self):
        print("B's method")
class C(A):
    def method(self):
        print("C's method")
class D(B, C):
    def __init__(self):
        super().method()
class E(C, B):
    def __init__(self):
        super().method()

d = D()
e = E()

#B's method
#C's method
```
Python 中提供了一个类方法 `mro()` 可以指定搜寻的顺序，mro 是Method Resolution Order 的缩写，它是类方法而不是实例方法，可以通过重载 `mro()` 方法改变继承中的方法解析顺序，但这需要在元类中完成，其结果：

```
D.mro()
[__main__.D, __main__.B, __main__.C, __main__.A, object]

E.mro()
[__main__.E, __main__.C, __main__.B, __main__.A, object]
```
super() 方法就是沿着 mro() 给出的顺序向上寻找起点的：

```
super(D, d).method()
super(E, e).method()

B's method
C's method

super(C, e).method()
super(B, d).method()

B's method
C's method
```
