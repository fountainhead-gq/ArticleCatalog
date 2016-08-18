
## 易出错的一些细节

1 不要使用可变对象作为函数默认值

错误的方法：
```python
def append_to_list(value, def_list=[]):
    def_list.append(value)
    return def_list
```  

正确的方法：  
```python
def append_to_list(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```    


2 生成器不保留迭代过后的结果
``` python
In [12]: gen = (i for i in range(5))

In [13]: 2 in gen
Out[13]: True

In [14]: 3 in gen
Out[14]: True

In [15]: 1 in gen
Out[15]: False # 1为什么不在gen里面了? 因为调用1->2,这个时候1已经不在迭代器里面了,被按需生成过了

In [20]: gen = (i for i in range(5))

In [21]: a_list = list(gen) # 可以转化成列表，当然a_tuple = tuple(gen) 也可以

In [22]: 2 in a_list
Out[22]: True

In [23]: 3 in a_list
Out[23]: True

In [24]: 1 in a_list # 就算循环过,值还在
Out[24]: True
```

3  lambda在闭包中会保存局部变量
```python
In [29]: my_list = [lambda: i for i in range(5)]

In [30]: for l in my_list:
   ....:         print(l())
   ....:
4
4
4
4
4
```

用生成器，代码如下:
```python
In [31]: my_gen = (lambda: n for n in range(5))

In [32]: for l in my_gen:
   ....:         print(l())
   ....:
0   
1
2
3
4
```
用list，代码如下:
```python
In [33]: my_list = [lambda x=i: x for i in range(5)] # 看我给每个lambda表达式赋了默认值

In [34]: for l in my_list:
   ....:         print(l())
   ....:
0
1
2
3
4
```

python的另外一个魔法，代码如下:
```python
In [35]: def groupby(items, size):
   ....:     return zip(*[iter(items)]*size)
   ....:

In [36]: groupby(range(9), 3)
Out[36]: [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
```


4 列表的+和+=, append和extend
```python
In [17]: print('ID:', id(a_list))
('ID:', 4481323592)

In [18]: a_list += [1]

In [19]: print('ID (+=):', id(a_list))
('ID (+=):', 4481323592) # 使用+= 还是在原来的列表上操作

In [20]: a_list = a_list + [2]

In [21]: print('ID (list = list + ...):', id(a_list))
('ID (list = list + ...):', 4481293056) # 简单的+其实已经改变了原有列表
In [28]: a_list = []

In [29]: id(a_list)
Out[29]: 4481326976

In [30]: a_list.append(1)

In [31]: id(a_list)
Out[31]: 4481326976 # append 是在原有列表添加

In [32]: a_list.extend([2])

In [33]: id(a_list)
Out[33]: 4481326976 # extend 也是在原有列表上添加
```

浅拷贝和深拷贝
```python
In [65]: list1 = [1, 2]

In [66]: list2 = list1 # 就是个引用, 你操作list2,其实list1的结果也会变

In [67]: list3 = list1[:]

In [69]: import copy

In [70]: list4 = copy.copy(list1) # 他和list3一样 都是浅拷贝

In [71]: id(list1), id(list2), id(list3), id(list4)
Out[71]: (4480620232, 4480620232, 4479667880, 4494894720)

In [72]: list2[0] = 3

In [73]: print('list1:', list1)
('list1:', [3, 2])

In [74]: list3[0] = 4

In [75]: list4[1] = 4

In [76]: print('list1:', list1)
('list1:', [3, 2]) # 对list3和list4操作都没有对list1有影响

# 再看看深拷贝和浅拷贝的区别

In [88]: from copy import copy, deepcopy

In [89]: list1 = [[1], [2]]

In [90]: list2 = copy(list1) # 还是浅拷贝

In [91]: list3 = deepcopy(list1) # 深拷贝

In [92]: id(list1), id(list2), id(list3)
Out[92]: (4494896592, 4495349160, 4494896088)

In [93]: list2[0][0] = 3

In [94]: print('list1:', list1)
('list1:', [[3], [2]]) # 看到了吧 假如你操作其子对象 还是和引用一样 影响了源

In [95]: list3[0][0] = 5

In [96]: print('list1:', list1)
('list1:', [[3], [2]]) # 深拷贝就不会影响
```


bool其实是int的子类
```python
In [97]: isinstance(True, int)
Out[97]: True

In [98]: True + True
Out[98]: 2

In [99]: 3 * True + True
Out[99]: 4

In [100]: 3 * True - False
Out[100]: 3

In [104]: True << 10
Out[104]: 1024
```
