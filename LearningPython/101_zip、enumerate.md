## 并行迭代


现实中迭代不都是那么简单的，比如这个问题：

**问题：**有两个列表，分别是：a = [1,2,3,4,5], b = [9,8,7,6,5]，要计算这两个列表中对应元素的和。

**解析：**

观察发现两个列表的长度一样，都是5。那么对应元素求和，就是相同的索引值对应的元素求和，即a[i]+b[i],(i=0,1,2,3,4)，这样一个一个地就把相应元素和求出来了。当然，要用for来做这个事情了。

    >>> a = [1,2,3,4,5]
    >>> b = [9,8,7,6,5]
    >>> c = []
    >>> for i in range(len(a)):
    ...     c.append(a[i]+b[i])
    ... 
    >>> c
    [10, 10, 10, 10, 10]

看来for的表现还不错。不过，这种方法虽然解决问题了，但python总不会局限于一个解决之道。于是又有一个内建函数`zip()`，可以让同样的问题有不一样的解决途径。

    >>> a = "shucun"
    >>> b = "github"
    >>> zip(a,b)
    [('s', 'g'), ('h', 'i'), ('u', 't'), ('c', 'h'), ('u', 'u'), ('n', 'b')]
    
如果序列长度不同，那么就以"短的为准。

    >>> c = [1,2,3]
    >>> d = [9,8,7,6]
    >>> list(zip(c,d))
    [(1, 9), (2, 8), (3, 7)]

zip是一个内置函数，它的参数必须是某种序列数据类型，如果是字典，那么键视为序列。然后将序列对应的元素依次组成元组，做为一个list的元素。


    
zip解决上面实例：

    >>> d = []
    >>> for x,y in zip(a,b):
    ...     d.append(x+y)
    ... 
    >>> d
    [10, 10, 10, 10, 10]

多么优雅的解决！

比较这个问题的两种解法，似乎第一种解法适用面较窄，比如，如果已知给定的两个列表长度不同，第一种解法就出问题了。而第二种解法还可以继续适用。的确如此，不过，第一种解法也不是不能修订的。


以上两种写法那个更好呢？

    >>> result=[(2, 11), (4, 13), (6, 15), (8, 17)]
    >>> list(zip(*result))
    [(2, 4, 6, 8), (11, 13, 15, 17)]
    
`zip()`还能这么干，是不是有点意思？

下面延伸一个问题：

**问题**：myinfor = {"name":"qiwsir","site":"qiwsir.github.io","lang":"python"},将这个字典变换成：infor = {"qiwsir":"name","qiwsir.github.io":"site","python":"lang"}

**解析：**

解法有几个，如果用for循环，可以这样做

    >>> infor = {}
    >>> for k,v in myinfor.items():
    ...     infor[v]=k
    ... 
    >>> infor
    {'python': 'lang', 'qiwsir.github.io': 'site', 'qiwsir': 'name'}

下面用zip()来试试：

    >>> dict(zip(myinfor.values(),myinfor.keys()))
    {'python': 'lang', 'qiwsir.github.io': 'site', 'qiwsir': 'name'}

原来这个zip()还能这样用。是的，本质上是这么回事情。

    >>> myinfor.values()    #得到两个list
    ['python', 'qiwsir', 'qiwsir.github.io']
    >>> myinfor.keys()
    ['lang', 'name', 'site']
    >>> temp = zip(myinfor.values(),myinfor.keys())     #压缩成一个list，每个元素是一个tuple
    >>> temp
    [('python', 'lang'), ('qiwsir', 'name'), ('qiwsir.github.io', 'site')]

    >>> dict(temp)                          #这是函数dict()的功能，将上述列表转化为dictionary
    {'python': 'lang', 'qiwsir.github.io': 'site', 'qiwsir': 'name'}

至此，是不是明白zip()和循环的关系了呢？有了它可以让某些循环简化。

## enumerate

    >>> for (i,day) in enumerate(week):
    ...     print day+' is '+str(i)
    ... 
    monday is 0
    sunday is 1
    friday is 2


几个例子：

    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

对于这样一个列表：

    >>> mylist = ["qiwsir",703,"python"]
    >>> enumerate(mylist)
    <enumerate object at 0xb74a63c4>    
    >>> list(enumerate(mylist))
    [(0, 'qiwsir'), (1, 703), (2, 'python')]
    

## list解析

    >>> power2 = []
    >>> for i in range(1,10):
    ...     power2.append(i*i)
    ... 
    >>> power2
    [1, 4, 9, 16, 25, 36, 49, 64, 81]

python有一个非常有意思的功能，就是list解析，就是这样的：

    >>> squares = [x**2 for x in range(1,10)]
    >>> squares
    [1, 4, 9, 16, 25, 36, 49, 64, 81]


其实，不仅仅对数字组成的list，所有的都可以如此操作。

    >>> mybag = [' glass',' apple','green leaf ']   #有的前面有空格，有的后面有空格
    >>> [one.strip() for one in mybag]              #去掉元素前后的空格
    ['glass', 'apple', 'green leaf']

