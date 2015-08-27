## math模块

math模块是标准库中的，所以不用安装，可以直接使用。使用方法是：
```python
>>> import math
>>> math.pi
3.141592653589793
```

```python
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
```

这些我们称之为函数，也就是在模块math中提供了各类计算的函数，比如计算乘方，可以使用pow函数。
```pyton
>>> help(math.pow)
Help on built-in function pow in module math:

pow(...)
    pow(x, y)

    Return x**y (x to the power of y).
```
这里展示了math模块中的pow函数的使用方法和相关说明。

第一行意思是说这里是math模块的内建函数pow帮助信息（所谓built-in，称之为内建函数，是说这个函数是python默认就有的)  
第三行，表示这个函数的参数，有两个，也是函数的调用方式  
第四行，是对函数的说明，返回x**y的结果，并且在后面解释了的含义。  

```pyton
>>> 4**2
16
>>> math.pow(4,2)
16.0
>>> 4*2
8
```

用类似的方法，可以查看math模块中的任何一个函数的使用方法。
```python
>>> math.sqrt(9)
3.0
>>> math.floor(3.14)
3
>>> math.floor(3.999122)
3
>>> math.fabs(-2)    #等价于abs(-2)
2.0
>>> abs(-2)
2
>>> math.fmod(5,3)    #等价于5%3
2.0
>>> 5%3
2
```

## 几个常见函数


### 求绝对值
```python
>>> abs(10)
10
>>> abs(-10)
10
>>> abs(-1.2)
1.2
```
### 四舍五入
```python
>>> round(1.234)
1
>>> round(1.234,1)
1.2
>>> round(1.234,2)
1.23
```

## 运算优先级

运算符:

>lambda	Lambda表达式
or	布尔“或”
and	布尔“与”
not x	布尔“非”
in，not in	
is，is not	
<，<=，>，>=，!=，==	比较
|	按位或
^	按位异或
&	按位与
<<，>>	移位
+，-	加法与减法
*，/，%	乘法、除法与取余
+x，-x	正负号
~x	按位翻转
**	指数
x.attribute	属性参考
x[index]	下标
x[index:index]	寻址段
f(arguments...)	函数调用
(experession,...)	绑定或元组显示
[expression,...]	列表显示
{key:datum,...}	字典显示
'expression,...'	字符串转换

上面的内容是按照从低到高的顺序列出的。虽然有很多还不知道是怎么回事，不过先列出来，等以后用到了，还可以回来查看。

最后，要提及的是：括号()。只要有括号，就先计算括号里面的。无需解释。