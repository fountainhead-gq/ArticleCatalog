# collections中的Counter计数器

python模块collections提供了内置容器类型dict,list,set,tuple更专业的容器数据类型。

## Counter计数器

计数器（Counter）是一个容器，用来跟踪值出现了多少次。

计数器支持三种形式的初始化。构造函数可以调用序列，包含key和计数的字典，或使用关键词参数。
```python
>>> import collections
>>> print collections.Counter(['a','b','c','a','b','b'])
Counter({'b': 3, 'a': 2, 'c': 1})
>>> print collections.Counter({'a':2,'b':3,'c':1})
Counter({'b': 3, 'a': 2, 'c': 1})
>>> print (collections.Counter(a=2,b=3,c=1))
Counter({'b': 3, 'a': 2, 'c': 1})
```
注意key的出现顺序是根据计数的从大到小

也可以创建空的计数器，在update:
```python
>>> c=collections.Counter()     #创建空计数器
>>> print ('Initial:',c)
Initial: Counter()
    
>>> c.update("abcdaab")         #update
>>> print ('Sequence:',c)
Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
    
>>> c.update({'a':1,'d':5})
>>> print ('Dict:',c)               #追加次数
Dict: Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
    
>>> d=collections.Counter("abbccdde")
>>> d
Counter({'c': 2, 'b': 2, 'd': 2, 'a': 1, 'e': 1})
```

访问计数：
```python
>>> d=collections.Counter("abbccdde")
>>> d
Counter({'c': 2, 'b': 2, 'd': 2, 'a': 1, 'e': 1})
>>> for letter in 'abcde':
...     print ('%s:%d'%(letter,d[letter]))
... 
a:1
b:2
c:2
d:2
e:1
```

elements可以列出所有的元素
```python
>>> m = collections.Counter('helloworld')
>>> m
Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
>>> m['e'] = 0  #将e这个值设置为0
>>> m
Counter({'l': 3, 'o': 2, 'd': 1, 'h': 1, 'r': 1, 'w': 1, 'e': 0})
>>> print (list(m.elements()))
['d', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']   
```
most_common([n]),列出最常出现的。例如：
```python
>>> collections.Counter('abracadabra').most_common(3)   #最常出现的前三个
[('a', 5), ('r', 2), ('b', 2)]
```
关于collections.Counter()的其它方法，和collections的deque	、defaultdict、UserList、ChainMap等其他方法请参考官方文档。
