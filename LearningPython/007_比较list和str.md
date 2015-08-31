
# list和str

list和str两种类型数据，有不少相似的地方，也有很大的区别。本讲对她们做个简要比较。

## 相同点

### 都属于序列类型的数据

所谓序列类型的数据，就是说它的每一个元素都可以通过指定一个编号，行话叫做“偏移量”的方式得到，而要想一次得到多个元素，可以使用切片。偏移量从0开始，总元素数减1结束。

例如：

    >>> welcome_str = "Welcome you"
    >>> welcome_str[0]
    'W'
    >>> welcome_str[1]
    'e'
    >>> welcome_str[len(welcome_str)-1]
    'u'
    >>> welcome_str[:4]
    'Welc'
    >>> a = "python"
    >>> a*3
    'pythonpythonpython'

    >>> git_list = ["qiwsir","github","io"]
    >>> git_list[0]
    'qiwsir'
    >>> git_list[len(git_list)-1]
    'io'
    >>> git_list[0:2]
    ['qiwsir', 'github']
    >>> b = ['qiwsir']
    >>> b*7
    ['qiwsir', 'qiwsir', 'qiwsir', 'qiwsir', 'qiwsir', 'qiwsir', 'qiwsir']

对于此类数据，下面一些操作是类似的：

    >>> first = "hello,world"
    >>> welcome_str
    'Welcome you'
    >>> first+","+welcome_str   #用+号连接str
    'hello,world,Welcome you'
    >>> welcome_str             #原来的str没有受到影响，即上面的+号连接后重新生成了一个字符串
    'Welcome you'
    >>> first
    'hello,world'

    >>> language = ['python']
    >>> git_list
    ['qiwsir', 'github', 'io']
    >>> language + git_list     #用+号连接list，得到一个新的list
    ['python', 'qiwsir', 'github', 'io']
    >>> git_list
    ['qiwsir', 'github', 'io']
    >>> language
    ['python']

    >>> len(welcome_str)    #得到字符数
    11
    >>> len(git_list)       #得到元素数
    3


## 区别

list和str的最大区别是：list是可以改变的，str不可变。这个怎么理解呢？

首先看对list的这些操作，其特点是在原处将list进行了修改：

    >>> git_list
    ['qiwsir', 'github', 'io']
    
    >>> git_list.append("python")
    >>> git_list
    ['qiwsir', 'github', 'io', 'python']
    
    >>> git_list[1]               
    'github'
    >>> git_list[1] = 'github.com'
    >>> git_list
    ['qiwsir', 'github.com', 'io', 'python']
    
    >>> git_list.insert(1,"algorithm")
    >>> git_list
    ['qiwsir', 'algorithm', 'github.com', 'io', 'python']
    
    >>> git_list.pop()
    'python'
    
    >>> del git_list[1]
    >>> git_list
    ['qiwsir', 'github.com', 'io']

以上这些操作，如果用在str上，都会报错，比如：

    >>> welcome_str
    'Welcome you'
    
    >>> welcome_str[1]='E'
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    
    >>> del welcome_str[1]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'str' object doesn't support item deletion
    
    >>> welcome_str.append("E")
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'str' object has no attribute 'append'

如果要修改一个str，不得不这样。

    >>> welcome_str
    'Welcome you'
    >>> welcome_str[0]+"E"+welcome_str[2:]  #从新生成一个str
    'WElcome you'
    >>> welcome_str                         #对原来的没有任何影响
    'Welcome you'

其实，在这种做法中，相当于重新生成了一个str。

## 多维list

这个也应该算是两者的区别了，虽然有点牵强。在str中，里面的每个元素只能是字符，在list中，元素可以是任何类型的数据。前面见的多是数字或者字符，其实还可以这样：

    >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
    >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
    >>> matrix[0][1]
    2
    >>> mult = [[1,2,3],['a','b','c'],'d','e']
    >>> mult
    [[1, 2, 3], ['a', 'b', 'c'], 'd', 'e']
    >>> mult[1][1]
    'b'
    >>> mult[2]
    'd'

以上显示了多维list以及访问方式。在多维的情况下，里面的list被当成一个元素对待。

## list和str转化

以下涉及到的`split()`和`join()`在前面字符串部分已经见过。

### str.split()

这个内置函数实现的是将str转化为list。其中str=""是分隔符。

在看例子之前，请看官在交互模式下做如下操作：

    >>>help(str.split)

得到了对这个内置函数的完整说明。**特别强调：**这是一种非常好的学习方法


    >>> line = "Hello.I am qiwsir.Welcome you." 

    >>> line.split(".")     #以英文的句点为分隔符，得到list
    ['Hello', 'I am qiwsir', 'Welcome you', '']
    
    >>> line.split(".",1)   #这个1,就是根据第一个.分割
    ['Hello', 'I am qiwsir.Welcome you.']       
    
    >>> name = "Albert Ainstain"    #也有可能用空格来做为分隔符
    >>> name.split(" ")
    ['Albert', 'Ainstain']

下面的例子，让你更有点惊奇了。

    >>> s = "I am, writing\npython\tbook on line"   #这个字符串中有空格，逗号，换行\n，tab缩进\t 符号
    >>> print (s)         #输出之后的样式
    I am, writing
    python  book on line
    >>> s.split()       #用split(),但是括号中不输入任何参数
    ['I', 'am,', 'writing', 'python', 'book', 'on', 'line']

如果split()不输入任何参数，显示就是见到任何分割符号，就用其分割了。

### "[sep]".join(list)

join可以说是split的逆运算，举例：

    >>> name
    ['Albert', 'Ainstain']
    >>> "".join(name)       #将list中的元素连接起来，但是没有连接符，表示一个一个紧邻着
    'AlbertAinstain'
    >>> ".".join(name)      #以英文的句点做为连接分隔符
    'Albert.Ainstain'
    >>> " ".join(name)      #以空格做为连接的分隔符
    'Albert Ainstain'

回到上面那个神奇的例子中，可以这么使用join.

    >>> s = "I am, writing\npython\tbook on line" 
    >>> s.split()
    ['I', 'am,', 'writing', 'python', 'book', 'on', 'line']
    >>> " ".join(s.split())         #重新连接，不过有一点遗憾，am后面逗号还是有的。怎么去掉？
    'I am, writing python book on line'


