## PyMongo操作方法


### 通过MongoClient建立一个连接。

开始使用PyMongo的第一步是创建一个MongoClient，对应于MongoDB实例。

```python
>>> from pymongo import MongoClient
>>> client = MongoClient()
```
将会连接默认的host和port。当然也可指定：

```python
>>> client = MongoClient('localhost', 27017)
```
或者用 MongoDB URI 格式:
```python
>>> client = MongoClient('mongodb://localhost:27017/')
```


### 获取一个数据库

一个MongoDB实例可以支持多个独立的数据库。使用PyMongo时，可以通过访问`MongoClient`的属性的方式来访问数据库:

```python
>>> db = client.test_database
```
也可以通过访问字典值的方式：
```python
>>> db = client['test-database']
```

### 获取一个Collection

一个collection指一组存在MongoDB中的文件，大致可以认为是关系型数据库中表的概念。获取Collection方法与获取数据库方法一致:

```python
>>> collection = db.test_collection
```

或字典方式:

```python
>>> collection = db['test-collection']
```
需要强调的一点是，MongoDB里的collection和数据库都是惰性创建的 - 之前我们提到的所有命令实际没有对`MongoDB server`进行任何操作。直到第一个文件插入后，才会创建。

### 文件（Documents）

数据在MongoDb中是以JSON类文件的形式保存起来的。在PyMongo中用字典来代表文件。例如，下面这个字典就可以代表一篇博文:
```python
>>> import datetime
>>> post = {"author": "Mike",
...         "text": "My first blog post!",
...         "tags": ["mongodb", "python", "pymongo"],
...         "date": datetime.datetime.utcnow()}
```
注意，文件里可以保存python原生类型（datetime.datetime），这些类型的值会被自动在原生类型和BSON格式之间转换。

### 文件插入操作

要把一个文件插入collection，可以使用insert()方法:
```python
>>> posts = db.posts
>>> post_id = posts.insert(post)
>>> post_id
ObjectId('...')
```

文件被插入之后，如果文件内没有`_id`这个键值，那么系统自动添加一个到文件里。这是一个特殊键值，它的值在整个collection里是唯一的。`insert()`返回这个文件的`_id`值。

插入第一个文件后，这个posts collection 就真实的在server上创建了。可以通过查看数据库上的所有collection来验证：

```python
>>> db.collection_names()
[u'system.indexes', u'posts']
```
这个名为 system.indexes的 collection是个特殊的内部collection，这是自动创建的。


### 单个文件获取 find_one()

MongoDB中最基本的查询就是`find_one`。这个函数返回一个符合查询的文件，或者在没有匹配的时候返回None。这在你知道只有一个文件符合条件的时候，或者只对第一个符合条件的文件感兴趣的时候，很有用。下面用 `find_one()` 来获取 posts collection里的第一个文件:
```python
>>> posts.find_one()
{u'date': datetime.datetime(...), u'text': u'My first blog post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
```
返回结果是一个我们之前插入的符合条件的字典类型值。
注意，返回的文件里已经有了_id这个键值，这是自动添加的。
`find_one()`还支持对特定元素进行匹配的查询。筛选出作者是“Mike”的文件：
```python
>>> posts.find_one({"author": "Mike"})
{u'date': datetime.datetime(...), u'text': u'My first blog post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
```
如果换个作者名，像 “Eliot”,就查不到结果:
```python
>>> posts.find_one({"author": "Eliot"})
>>>
```

### 按照ObjectId查询

通过_id也可以进行查询, 在例子中就是ObjectId:
```python
>>> post_id
ObjectId(...)
>>> posts.find_one({"_id": post_id})
{u'date': datetime.datetime(...), u'text': u'My first blog post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
```
注意 ObjectId 并不等价于他的字符串形式。
```python
>>> post_id_as_str = str(post_id)
>>> posts.find_one({"_id": post_id_as_str}) # No result
>>>
```
web应用的一个常见任务就是在requset的URL里获取ObjectId然后找到与之匹配的文件。在本例中，必须要先从字符串转换为ObjectId然后传给find_one:
```python
from bson.objectid import ObjectId

# 框架从URL里获取post_id，然后把他作为字符串传入
def get(post_id):
    # 从字符串转换为ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
```

### 批量插入

为了让查询更有趣点，我们多插入几个文件。除了单个文件插入，也可以通过给insert()方法传入可迭代的对象作为第一个参数，进行批量插入操作。这将会把迭代表中的每个文件插入，而且只向server发送一条命令:
```python
>>> new_posts = [{"author": "Mike",
...               "text": "Another post!",
...               "tags": ["bulk", "insert"],
...               "date": datetime.datetime(2009, 11, 12, 11, 14)},
...              {"author": "Eliot",
...               "title": "MongoDB is fun",
...               "text": "and pretty easy too!",
...               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
>>> posts.insert(new_posts)
[ObjectId('...'), ObjectId('...')]
```
这个例子里有一些比较有趣的地方：

`insert()`现在返回两个ObjectId实例，每个代表一个插入的文件。

`new_posts[1]`与其他的posts内容格式不相同：里面没有"tags”，另外我们增加了一个新的“title”域。这就是MongoDB所提到的无schema特点。


### 查询多个文件

想获取多个文件的时候，可以使用find()方法。find()返回一个 Cursor 实例,通过它我们可以便利每个符合查询条件的文件。比如便利每个 posts collection里的文件:
```python
>>> for post in posts.find():
...   post
...
{u'date': datetime.datetime(...), u'text': u'My first blog post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
{u'date': datetime.datetime(2009, 11, 12, 11, 14), u'text': u'Another post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'bulk', u'insert']}
{u'date': datetime.datetime(2009, 11, 10, 10, 45), u'text': u'and pretty easy too!', u'_id': ObjectId('...'), u'author': u'Eliot', u'title': u'MongoDB is fun'}
```

与使用find_one()时候相同,可以传入一个文件来限制查询结果。比如查询所有作者是 “Mike”的文章:
```python
>>> for post in posts.find({"author": "Mike"}):
...   post
...
{u'date': datetime.datetime(...), u'text': u'My first blog post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'mongodb', u'python', u'pymongo']}
{u'date': datetime.datetime(2009, 11, 12, 11, 14), u'text': u'Another post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'bulk', u'insert']}
```


### Counting

如果只想知道符合查询条件的文件有多少，可以用count()操作，而不必进行完整的查询。查询collection的文件总数:
```python
>>> posts.count()
3
```
或者只是特定的一些文件：
```prthon
>>> posts.find({"author": "Mike"}).count()
2
```
### 限定范围的查询

MongoDB 支持多种高级查询。例如，查询晚于某个特定时间的post,结果按作者名排序:
```python
>>> d = datetime.datetime(2009, 11, 12, 12)
>>> for post in posts.find({"date": {"$lt": d}}).sort("author"):
...   print post
...
{u'date': datetime.datetime(2009, 11, 10, 10, 45), u'text': u'and pretty easy too!', u'_id': ObjectId('...'), u'author': u'Eliot', u'title': u'MongoDB is fun'}
{u'date': datetime.datetime(2009, 11, 12, 11, 14), u'text': u'Another post!', u'_id': ObjectId('...'), u'author': u'Mike', u'tags': [u'bulk', u'insert']}
```
这里使用了特殊的”$lt"操作符来进行范围查询,并调用sort()对结果按照作者排序。

### 索引（Indexing）

为了让上述查询更快一点，可以添加一个在"date” 和 “author"上添加复合索引。首先，使用explain()方法来了解查询在没有添加索引情况下如何执行:
```python
>>> posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
u'BasicCursor'
>>> posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]
3
```

可以看，查询使用的是BasicCursor,而且扫描了全部的三个文件。现在添加一个复合索引，再看看同样的操作：
```python
>>> from pymongo import ASCENDING, DESCENDING
>>> posts.create_index([("date", DESCENDING), ("author", ASCENDING)])
u'date_-1_author_1'
>>> posts.find({"date": {"$lt": d}}).sort("author").explain()["cursor"]
u'BtreeCursor date_-1_author_1'
>>> posts.find({"date": {"$lt": d}}).sort("author").explain()["nscanned"]
2
```
现在查询使用的是BtreeCursor(利用这个索引)，并且只扫描了两个符合条件的文件。


### 关于Unicode字符串的一点说明

你可能已经注意到，之前存入数据库的事常规的Python字符串，这与我们从数据库服务器里取回来的看起来不同（比如 u’Mike’ 而不是‘Mike’）。下面简单解释一下。

MongoDB 以格式保存数据. BSON 字符串都是 UTF-8编码的， 所以PyMongo必须确保它保存的字符串值包含有效地 UTF-8数据.常规字符串 ( )都是有效的，可以不改变直接保存。Unicode 字符串( )就需要先编码成 UTF-8 格式.例子里的字符串显示为u’Mike’ 而不是 ‘Mike’是因为 PyMongo 会把每个BSON 字符串转换成 Python 的unicode 字符串, 而不是常规的 str.
