## any()
适用于2.5以上版本，兼容python3版本。  
any(iterable),如果iterable的任何元素不为（或所有的元素全为）0、''、False,结果返回True,否则返回False。等价于：
```
def any(iterable):
   for element in iterable:
       if  element:
           return False
   return True
```   

```
>>> any(['a', 'b', 'c', 'd'])  #列表list，元素都不为空或0
True
>>> any(['a', 'b', '', 'd'])  #列表list，存在一个为空的元素
True
>>> any([0, '', False])  #列表list,元素全为0,'',false
False

>>> any(('a', 'b', 'c', 'd'))  #元组tuple，元素都不为空或0
True
>>> any(('a', 'b', '', 'd'))  #元组tuple，存在一个为空的元素
True
>>> any((0, '', False))  #元组tuple，元素全为0,'',false
False

>>> any([]) # 空列表
False
>>> any(()) # 空元组
False
```


## all()
同样地，适用于2.5以上版本，兼容python3版本。  
如果iterable的所有元素中的任何一个元素为（或所有的元素都不为）0、''、False或者iterable为空，all(iterable)返回True，否则返回False。等价于：

```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```    


```
>>> all(['a', 'b', 'c', 'd'])  #列表list，元素都不为空或0
True
>>> all(['a', 'b', '', 'd'])  #列表list，存在一个为空的元素
False
>>> all([0, 1，2, 3])  #列表list，存在一个为0的元素
False

>>> all(('a', 'b', 'c', 'd'))  #元组tuple，元素都不为空或0
True
>>> all(('a', 'b', '', 'd'))  #元组tuple，存在一个为空的元素
False
>>> all((0, 1，2, 3))  #元组tuple，存在一个为0的元素
False


>>> all([]) # 空列表
True
>>> all(()) # 空元组
True
```
