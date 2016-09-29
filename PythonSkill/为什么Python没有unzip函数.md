## 为什么Python没有unzip函数


`zip`函数可以把多个序列打包到元组中,但Python有个很神奇的操作符 `*` 来 `unpack` 参数列表

```python
a, b = [1, 2, 3], [4, 5, 6]
c = zip(a, b)
print(list(c))

# [(1, 4), (2, 5), (3, 6)]

d = list(zip(*c))
print(d)
# [(1, 2, 3), (4, 5, 6)]
```
Python3中`zip()`返回的是元组组成的迭代器，而在Python2中返回的是元组组成的列表。
