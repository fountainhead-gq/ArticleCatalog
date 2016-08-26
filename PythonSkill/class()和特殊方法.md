# class()和特殊方法

## class基本形式
class 定义如下：
```python
class ClassName(ParentClass):
    """class docstring"""
    def method(self):
        return
```        
- `class` 关键词在最前面
- `ClassName` 通常采用 CamelCase 记法
- 括号中的 `ParentClass` 用来表示继承关系
- 冒号不能缺少
- """""" 中的内容表示 docstring，可以省略
- 方法定义与函数定义十分类似，不过多了一个 `self` 参数表示这个对象本身
- `class` 中的方法要进行缩进


## 特殊方法
Python 使用 `__ `开头的名字来定义特殊的方法和属性，它们有：
- `__init__()`
- `__repr__()`
- `__str__()`
- `__call__()`
- `__iter__()`
- `__add__()`
- `__sub__()`
- `__mul__()`
- `__rmul__()`
- `__class__`
- `__name__`
