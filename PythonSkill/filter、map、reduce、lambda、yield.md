# 特殊语法：filter、map、reduce、lambda、yield

Python内置了一些非常有趣但非常有用的函数，充分体现了Python的语言魅力！

## filter

filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回。
filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

    >>> def f(x): return x % 2 != 0 and x % 3 != 0

    >>> list(filter(f, range(2, 25)))

    [5, 7, 11, 13, 17, 19, 23]

    >>> def f(x): return x != 'a'

    >>> list(filter(f, "abcdef"))

    ['b', 'c', 'd', 'e', 'f']
    
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
    
## map

map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回.
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

    >>> def cube(x): return x*x*x
    >>> list(map(cube, range(1, 11)))
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    >>> def cube(x) : return x + x
    >>> list(map(cube , "abcde"))
    ['aa', 'bb', 'cc', 'dd', 'ee']

另外map也支持多个sequence，这就要求function也支持相应数量的参数输入：

    >>> def add(x, y): return x+y
    >>> list(map(add, range(8), range(8)))
    [0, 2, 4, 6, 8, 10, 12, 14]

## reduce

reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和.
reduce()必须接收两个参数，并把一个函数作用在一个序列[x1, x2, x3, ...]上，然后把计算的结果继续和序列的下一个元素做累积计算

    >>> from functools import reduce
    >>> def add(x,y): return x + y
    >>> reduce(add, range(1, 11))
    55
    （注：1+2+3+4+5+6+7+8+9+10）
    >>> reduce(add, range(1, 11), 20)
    75
    （注：1+2+3+4+5+6+7+8+9+10+20）

## lambda

lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方：

    >>> g = lambda x: x * 2
    >>> g(3)
    6
    >>> (lambda x: x * 2)(3)
    6

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数。

## yield

带有 yield 的函数在 Python 中被称之为 generator（生成器）.
generator归根到底是一个函数的返回值，这个函数是包含“yield”关键字的python函数。

是不是可以这么说(不是很确定，似乎可以这么理解)

1. 凡包含“yield”关键字的函数，都返回generator
2. generator不是函数，而是函数执行后构造的对象，是一种iterator。
3. generator可以像iterator一样的用。

```
>>> def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
```

而yield的作用就是，每次发生next()调用，函数执行完yield语句之后在挂起，这时返回yield的值，整个函数状态被保存，等待下一次next()调用； 下次next()调用发生时，从yield后的语句开始执行(有yiled也在循环体内，未必一定是顺序的)，直到再次遇到yield为止，然后重复删除动作。

yield 可以解读为"返回然后等待"。知道所有yield语句完成，这时如果再次调用next()，则发生StopIteration异常，当然，在for循环之类的语句中会被自动处理。

得出以下结论：
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
使用 isgeneratorfunction 判断
```
 >>> from inspect import isgeneratorfunction 
 >>> isgeneratorfunction(fab) 
 True
```

#### 另一个yield例子
另一个yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：
```
 def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return
```




