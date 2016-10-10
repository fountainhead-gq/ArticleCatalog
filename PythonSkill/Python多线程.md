<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python多线程](#python3%E5%8F%8A%E5%BA%94%E7%94%A85-%E5%A4%9A%E7%BA%BF%E7%A8%8B)
  - [`threading`模块](#threading%E6%A8%A1%E5%9D%97)
  - [线程锁](#%E7%BA%BF%E7%A8%8B%E9%94%81)
  - [使用实例](#%E4%BD%BF%E7%94%A8%E5%AE%9E%E4%BE%8B)
  - [`queue`](#queue)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Python多线程

[Python模块学习：threading 多线程控制和处理](http://python.jobbole.com/81546/)

### [`threading`模块](https://docs.python.org/3/library/threading.html)

线程运行在进程内部，可以访问进程的所有内容。

**线程内尽量不要共享全局变量**，在需要修改共同数据的情况下，使用**线程锁**

threading模块的常用方法：

```python
thread = threading.Thread(target=None, name=None, daemon=None, group=None, args=(), kwargs={})
# 实例化一个线程
# target是线程调用run()方法的时候会调用的函数
# 参数args和kwargs分别表示调用target时的参数列表和关键字参数
# name是该线程名称
# daemon=True时，thread dies when main thread (only non-daemon thread) exits.

thread.start() # 一个线程最多只能调用该方法一次，如果多次调用则会报RuntimeError错误。它会调用run方法
thread.run() # 在这里运行线程的具体任务
thread.join(timeout=None) # 阻塞全部线程直到当前线程任务结束，timeout为阻塞时间，None时会一直阻塞

thread.name
thread.getName()
thread.setName()

thread.is_alive() # 判断当前进程是否存活

threading.active_count()  # 返回当前线程对象Thread的个数
threading.current_thread()  # 返回当前的线程对象Thread
threading.current_thread().name # 返回当前线程的名称
```

简单实例：

```python
import datetime
import threading

class ThreadClass(threading.Thread):
	def run(self):
		now = datetime.datetime.now()
		print("%s says Hello World at time: %s" % (self.getName(), now))

for i in range(2):
	t = ThreadClass()
	t.start()

# Thread-1 says Hello World at time: 2008-05-13 13:22:50.252069
# Thread-2 says Hello World at time: 2008-05-13 13:22:50.252576
```

```python
# 启动一个线程
thread.start()

# 继承threading.Thread
import threading
class ThreadClass(threading.Thread):
	# 初始化方法
	def __init__(self, threadName):
		threading.Thread.__init__(self)
		self.threadName = threadName
	# 运行线程时会被调用的run方法
	def run(self):
		print('{0} is start'.format(self.threadName))

# 关闭一个进程
thread.join()
# join方法会暂时阻塞进程，等待子进程结束后再继续往下运行
```

### 线程锁

```python
import threading

lock = threading.Lock() # 线程锁应该只在主线程实例化一个

lock.acquire() # 调用线程锁，阻塞其他线程
lock.release() # 释放线程锁
lock.locked() # 获取当前锁的状态，若锁已经被某个线程获取,返回True, 否则为False
```

### 使用实例

```python
import threading
import time

lock = threading.Lock()
thread_list = []

class ThreadClass(threading.Thread):
	def __init__(self, threadName):
		threading.Thread.__init__(self)
		self.threadName = threadName

	def run(self):
		lock.acquire()
		for i in range(0, 10):
			print('{}'.format(self.threadName), ':', str(i))
			time.sleep(2)
		lock.release()

for i in range(3):
	thread = ThreadClass('thread {}'.format(i))
	thread_list.append(thread)
	thread.start()

for thread in thread_list:
	if thread:
		thread.join()
```

输出结果：

```python
thread 0 : 0
...
thread 0 : 9
thread 1 : 0
...
thread 1 : 9
thread 2 : 0
...
thread 2 : 9
```

### [`queue`](https://docs.python.org/3/library/queue.html)

queue 模块中提供了同步的、线程安全的队列类，这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

```python
import queue

q = queue.Queue(number) # 新建一个队列，默认情况下先进先出。number代表新建队列的大小，不写则默认为无限大

q.put(item, block=True, timeout=None) # 入栈，默认情况下Block为True，代表当队列已满时会造成阻塞，timeout表示阻塞时间，为None则一直阻塞
q.put_nowait(item) # 非阻塞的入栈，相当于 q.put(item, False)

q.get(block=True, timeout=None) # 出栈，默认情况下Block为True，代表当队列为空时会造成阻塞，timeout表示阻塞时间，为None则一直阻塞
q.get_nowait() # 非阻塞的出栈，相当于 q.get(False)，它在向一个空队列取值的时候会抛一个Empty异常

q.empty() # 如果队列对空则返回True
q.full() # 如果队列满了则返回True

q.task_done() # 告诉queue这个队列item的任务已经完成了
q.join() # 在queue里的任务完成之前阻塞线程，直到队列里所有的任务都是task_done()
```

可以将queue看做是一个储存任务所需数据的队列，以此来控制线程的数目。当queue内储存的数量达到线程数量最大值时，再向queue中put则会造成阻塞，直到某线程完成任务`q.get()` + `task_done()`

```python
import queue
from time import sleep
import random

q = queue.Queue(1) # 限制队列大小为1

for i in range(5):
	q.put(i)
print('all put in queue')
# 无输出，队列阻塞

for i in range(5):
    if q.full():
        item = q.get() # 这个举动会从queue队列里取出一个元素
        print('queue is full, get {}'.format(item))
        sleep(random.randrange(2, 5))
        q.task_done()
    q.put(i) # 当队列已满，而又没有item取出时会造成阻塞

print(q.full())
# 依次输出
# queue is full, get 0
# queue is full, get 1
# queue is full, get 2
# queue is full, get 3
# True
```

`queue`结合`threading`：

```python
import queue
from time import sleep
import random
import threading


class TestThread(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.queue = que

    def run(self):
        while True: # 需要通过循环来不断的运行任务
            item = self.queue.get()
            sleep(random.randrange(2, 3))
            print('queue is full, get {}'.format(item))
            self.queue.task_done()

def start_thread():
    for thread in threads:
        thread.start()

q = queue.Queue(5)

# 开启5个线程
for i in range(5):
    t = TestThread(q)
    t.daemon = True
    t.start()

# 总共有20个数据跑在五个线程里
for i in range(20):
    q.put(i)

q.join()
```
