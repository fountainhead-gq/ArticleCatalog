## python面试题
1.How are arguments passed – by reference of by value?

2.Do you know what list and dict comprehensions are? Can you give an example?

3.What is PEP 8?

4.Do you use virtual environments?

5.Can you sum all of the elements in the list, how about to multuply them and get the result?

6.Do you know what is the difference between lists and tuples? Can you give me an example for their usage?

7.Do you know the difference between range and xrange?

8.Tell me a few differences between Python 2.x and 3.x

9.What are decorators and what is their usage?

10.The with statement and its usage.

11.说说你对zen of python的理解，你有什么办法看到它

12.github上都fork过哪些python库，列举一下你经常使用的，每个库用一句话描述下其功能

13.你调试python代码的方法有哪些

14.什么是GIL

15.什么是元类(meta_class)

16.对比一下dict中 items 与 iteritems

17.是否遇到过python的模块间循环引用的问题，如何避免它

18.有用过with statement吗？它的好处是什么？

19.说说decorator的用法和它的应用场景，如果可以的话，写一个decorator

20.inspect模块有什么用

21.写一个类，并让它尽可能多的支持操作符

22.说一说你见过比较cool的python实现

23.python下多线程的限制以及多进程中传递参数的方式

24.Python是如何进行内存管理的？

25.什么是lambda函数？它有什么好处?

26.如何用Python输出一个Fibonacci数列？

27.介绍一下Python中webbrowser的用法？

28.解释一下python的and-or语法

29.Python是如何进行类型转换的？

30.Python如何实现单例模式？其他23种设计模式python如何实现？

31.如何用Python来进行查询和替换一个文本字符串？

32.如何用Python来发送邮件？

33.有没有一个工具可以帮助查找python的bug和进行静态的代码分析？

34.有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。

35.如何用Python删除一个文件？

36.Python如何copy一个文件？

37.python程序中文输出问题怎么解决？

38.python代码得到列表list的交集与差集

39.写一个简单的python socket编程

40.python如何捕获异常

41.在Python中, list, tuple, dict, set有什么区别, 主要应用在什么样的场景?

42.静态函数, 类函数, 成员函数的区别?

43.a=1, b=2, 不用中间变量交换a和b的值

44.写一个函数, 输入一个字符串, 返回倒序排列的结果: 如: string_reverse(‘abcdef’), 返回: ‘fedcba’

45.请用自己的算法, 按升序合并如下两个list, 并去除重复的元素:
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]

46.说一下以下代码片段存在的问题
```python
from amodule import * # amodule is an exist module

class dummyclass(object):
    def __init__(self):
        self.is_d = True
        pass

class childdummyclass(dummyclass):
    def __init__(self, isman):
        self.isman = isman

    @classmethod
    def can_speak(self): return True

    @property
    def man(self): return self.isman

if __name__ == "__main__":
    object = new childdummyclass(True)
    print object.can_speak()
    print object.man()
    print object.is_d
```    
47.介绍一下python的异常处理机制和自己开发过程中的体会

48.解释一下 WSGI 和 FastCGI 的关系？

49.解释一下 Django 和 Tornado 的关系、差别

50.解释下Django使用redis缓存服务器

51.如何进行Django单元测试

52.解释下Http协议

53.解释下Http请求头和常见响应状态码

54.分别简述OO，OOA

55.简述正则表达式中？p的含义

56.Python类中的self的具体含义是

57.请写出python的常用内置函数（至少3个），并描述它们具体含义

58.可以用python进行POST数据提交，可以加载什么模块来进行操作？在操作之前需要对数据进行什么操作？

59.说出python中间件Sqlalchemy的具体声明方式？以及模块与MySQLdb之间的区别？

60.描述出3中python常用框架，并简要描述这些框架的优缺点

61.reactor是什么？ 有什么作用？请简要描述。

62.请描述2种不同语言间数据流转通用格式。

63.简述我们使用多线程编程时，锁与信号量之间的关系。

64.通常在python编写tcp服务时，我们使用拆、粘包的模块是什么？如何加载这个模块？

65.两个整数数组各有100亿条数据，并已经排序，保存在磁盘上，内存10M。
问：
（1）如何取得交集？时间和空间效率分别是多少？Python 集合set()操作方法
（2）如果其中一个数组只有100条数据，如何优化算法取得交集？时间和空间效率分别是多少？
（3）用自己熟悉的语言实现第2个问题，要求可以正确运行；假设已经提供函数read_elt(arrary_name, index)可以用来读取某个数组的第index个元素，元素个数分别用m=100和n=10^10表示。

66.有100个磁盘组成的存储系统，当有3个磁盘同时损坏时，才会发生数据丢失。如果1个磁盘的损坏率是p，请问整个存储系统丢失数据的概率是多少？

67.请描述B-Tree插入值的过程

67.一个管道可以从a端发送字符到b端，只能发送0-9这10个数字，设计消息的协议，让a可以通知b任意大小的数字，并讨论这种消息协议可能发送的错误的处理能力。

68.假设fd是一个socket，read(fd, buf, 1024)
问：可能返回哪些值？其代表什么含义？

69.自旋锁适合哪些场合应用，不适合哪些场合？

70.假设网络会丢失消息，进程可能意外终止，磁盘可靠（写入数据后不会丢失）；
问：
如何构建一个可靠的分布式key-value存储系统？
答题要求如下：
1.客户端向系统发送1条写入请求(例如key=x, value=1)，系统返回'成功'，客户端一定可以正确读取到key=y的值
2.在你设计的系统中，要满足上面第1条，并有一定对故障的容错能力。
3.如果要尽可能提高写入或读写成功率，如果改进系统设计？分别会有哪些问题？

71.假设你的键盘只有以下键:
A
Ctrl + A
Ctrl + C
Ctrl + V
这里Ctrl+A,Ctrl+C,Ctrl+V分别代表"全选",“复制”，“粘贴”。
如果你只能按键盘N次，请写一个程序可以产生最多数量的A。也就是说输入是N(你按键盘的次数)， 输出是M(产生的A的个数)。

加分项：
打印出中间你按下的那些键。


72.假设给你一个月的日志，格式如下：
[I 130403 17:26:40] 1 200 GET /question/123 (8.8.9.9) 200.39ms
[I 130403 17:26:90] 1 200 GET /topic/456 (8.8.9.9) 300.85ms
[I 130403 17:26:90] 1 200 POST /answer/789 (8.8.9.9) 300.85ms
...
方括号中依次是：级别，日期，时间，后面依次是用户id，返回码，访问方式，访问路径，用户ip，响应时间
日志文件名格式为：年-月-日-小时.log，如：2013-01-01-18.log，共30*24个文件。
写个程序，算出一个用户列表和一个路径列表符合以下要求：
(1).这些用户每天都会访问（GET）/topic/ 这个路径两次以上（*代表数字）
(2).这些用户每天访问（GET）的/topic/*** 路径中，至少会包含两个不同的路径（后面的数字不一样）
(3).统计出所有以上用户所访问的路径中每天都出现两次以上的路径列表

73.有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；

要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小

74.Python语言的有哪些缺陷？

75.What are some key differences to bear in mind when coding in Python vs. Java?

76.有哪些CPython的替代实现？什么时候，为什么会使用他们？

77. Python是解释型的还是编译型的？

78.为什么要用函数装饰器？请举例

78.现在有一个 dict 对象 adict，里面包含了一百万个元素，查找其中的某个元素的平均需要多少次比较？一千万个元素呢？

79.现在有一个 list 对象 alist，里面的所有元素都是字符串，编写一个函数对它实现一个大小写无关的排序。

80.python 里关于“堆”这种数据结构的模块是哪个？“堆”有什么优点和缺点？举一个游戏开发中可能会用到堆的问题（不限是于 python 的堆，可以是其它语言的相关实现）。

81.set 是在哪个版本成为 build-in types 的？举一个你在以往项目中用到这种数据结构的问题（不限是于 python 的 set ，可以是其它语言的相关实现），并说明为什么当时选择了 set 这种数据结构。

82.有一个排好序地 list 对象 alist，查找其中是否有某元素 a（尽可能地使用标准库函数）

83.实现一个 stack。

84.编写一个简单的 ini 文件解释器。

85.现有 N 个纯文本格式的英文文件，实现一种检索方案，即做一个小搜索引擎。
