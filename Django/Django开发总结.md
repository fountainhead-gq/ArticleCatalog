# Django开发总结


整理下做从零开始到一个成型的网站所涉及到内容，记录下个人的做法，这里以Python的Web框架Django为例。

## 环境

开发环境是项目开始前就必须要准备好的事，这里的开发环境包括了下面的几个要素：

1. 操作系统环境
	主流的操作系统环境分别有Linux，OS X，Windows，这其中不同的操作系统的差异也不少，尤其是Windows系和*nix系。

2. 开发环境
	开发环境指的则是开发工具的组合，例如nginx+gunicorn+virtualenv。

3. 版本环境
	这里代表了开发工具的版本环境，例如Python 2.x和3.x，Django 1.4和1.9。

要保证开发的正确性，很重要的一点就是要维持环境的一致性，尤其是在多人协作的时候，不同的环境有可能导致运行正确性的不一致。

可以得出，一个好的环境需要三个要素：

1. 隔离性
2. 一致性
3. 可配置性

下面是针对环境问题的几个解决方案：

**虚拟机**

虚拟机使得电脑可以实现模拟出完全隔离环境的操作系统，可以做到在一个系统中直接运行多个虚拟的操作系统，流行的虚拟环境有VMWare，Virtual Box等等。

**Vagrant**

Vagrant是一个用来创建和部署虚拟操作环境的工具，本质上它使用了虚拟机作为虚拟化的实现，但它比传统虚拟机有更灵活的配置项，使得开发环境的配置更简单。

**Docker**

Docker是一个容器引擎，可以轻松地创建和配置一个应用的隔离系统环境，而且可以发布到任意机器上，保持环境的一致性，相比于虚拟机，它具有轻量级和启动快的优势。

**Virtualenv**

Virtualenv可以用来创建一个相对隔离的Python运行环境。

**Pyenv**

Pyenv是用来管理Python版本的一个工具。

## 编码风格

**PEP8**

PEE8是Python官方建议的编码风格，里面包含了一系列的编码规范。

**Flake8**

Flake8是检查Python代码健壮性的一个工具，它包括了PyFlake，pep8等，并提供了更清晰的接口。

## 项目结构

一般项目目录作为最外层目录，里层则是django的项目目录和virtualenv的虚拟环境目录，有时也可以是把django目录作为最外层目录，virtualenv目录作为里层目录，当用`django-admin startproject [projectname]`时，加上virtualenv目录后，会得到如下的目录结构：

```
[projectname]/
├── [projectname]/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── venv
```

在此基础上，如果想要细分配置文件，目录结构则变为如下：

```
[projectname]/
├── [projectname]/
│   ├── __init__.py
│   ├── settings/
│   │   ├── common.py
│   │   ├── dev.py
│   │   ├── __init__.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── venv
```

除此之外，项目还需要有`docs`(文档目录)，`conf`（配置目录），`static`（静态文件目录），`scripts`（配置脚本文件目录），以及各应用的模块目录，综上，项目目录结构如下划分：

```
[projectname]/
├── [projectname]/
│   ├── __init__.py
│   ├── settings/
│   │   ├── common.py
│   │   ├── dev.py
│   │   ├── __init__.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── app1/
├── app2/
├── app3/
├── conf/
├── scripts/
├── docs/
├── manage.py
├── README.rst
└── static/

```

## 配置

前面说过，配置项可以细分，这里一般情况可以分成三个文件，分别是common(或base，它包含了项目的通用配置)，dev（或local，它包含了项目开发调试环境的配置），prod（它包含了项目运行部署环境的配置）。

```
├── settings/
	├── common.py
	├── dev.py
	├── __init__.py
	└── prod.py
```

在运行服务器时，可以加上`--settings`选项，选择相应的配置项。

```
django-admin runserver --settings=[projectname].settings.dev
```

或者在服务器环境如下设置：

```python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pineapple.settings")
```

## 模版

下面是常见的模版结构，app的所有页面继承自base.html模版。

```
app/
└── templates
	└── base.html
	└── app/
		└── index.html # 继承 base.html
```

当每个app又需要各自定制时，也可以继续往下细分为三层结构。

模版引擎选择：

**DTL**

django内建引擎。

**Jinja2**

模版引擎，扩展性和灵活性更高。

**模版原则：**

**1.减少在模版中数据的处理量**

	尽量把数据处理交给后端处理，而不是在模版处理。

**2.不要在模版中处理大量数据的过滤**

	同上，应在后端使用queryset的filter方法进行过滤。

**3.尽量使用queryset的内建方法**

	当我们要统计一个queryset里面的数量时，应该使用`queryset.count()`，而不是python的`len(queryset)`或者模版的`{{ queryset|length }}`，因为前者的统计在数据库上进行操作，比后者快。

**4.使用缓存**

	使用Django内建的`'django.template.loaders.cached.Loader'`，能够大量地提高模版性能。

**5.避免在模版中进行隐蔽查询**

	先来看下面这段代码，它遍历用户列表（user_list由`User.objects.all()`产生）中的每个用户，并展示用户的出生日期，乍一看没什么问题，但这里实际上隐含了n+1问题，`user.profile.birth`在每次遍历中都进行了一次数据库查询，要解决这个问题也十分简单，只要用`select_related`操作把user关联的profile提前join取出来即可。

```
{% for user in user_list %}
    <li>{{ user.profile.birth }}</li>
{% endfor%}
```

## 静态资源

在项目的开发阶段，可以把静态文件统一放置在public(公共目录)下，或在各个app模块的static目录，在部署阶段再统一collectstatic到根目录的static中。

```
public/
└── static
    ├── css
    ├── font
    ├── images
    └── js
```

相应的，如果你想要指定了静态文件的目录，需要在settings中修改STATICFILES_DIRS的位置。

要在模版中使用`{% static %}`标签，需要在模版的顶部加上`{% load staticfiles %}`以加载模版标签。

静态资源的加速：

**CDN**

## 路由

添加错误代码的处理视图，使错误提示对用户更加友好。

```python
from django.conf.urls import handler404, handler500

handler404 = 'views.page_not_found'
handler500 = 'views.server_err'
```

把项目的路由分别分发给各个应用模块的urls.py配置，由namespace作识别，而不是将它们都包含在一个文件中。

```python
urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^topic/', include('topic.urls', namespace='topic')),
    url(r'^food/', include('food.urls', namespace='food')),
]
```

## 视图

Django中有两种视图，分别是Function Base View（函数视图）和Class Base View（类视图）。

函数视图的优势是：

1. 逻辑更清晰
2. 使用简单

类视图的优势是：

1. 更易重用代码
2. 灵活地利用mixin

视图编写原则：

1. 保持简洁，减少嵌套代码，适当使用decorator。
2. 保持视图名称多可读性。
3. 当业务复杂和可提取时，把业务转移到services层，保持视图的简洁。

## 模型

模型使用原则：

1. Django提供的ORM大大减轻了我们的工作，在开发时尽量使用ORM提供的方法，减少手动编写SQL语句。
2. 理解数据库设计规范，Model的好坏直接决定系统的稳定性。
3. 理解one-to-one（OneToOneField），one-to-manyhe（ForeignKey）和many-to-many（ManyToManyField）的使用场景。
4. 理解query和Aggregation。
5. 理解transaction和index的使用场景。


## 用户

Django在`django.contrib.auth.models`里提供了默认的用户模型，一般情况下我们只需要直接使用这个类就行了。如果需要扩展一个自定义的用户模型，最好是继承`django.contrib.auth.models`的`AbstractUser`类，如下所示：

```python
class User(AbstractUser):
    following = models.ManyToManyField('self', blank=True, related_name='followers', symmetrical=False)

```

默认的用户验证是通过`username`和`password`这两个字段，如果想要自定义用户验证，则可以如下建立一个验证的backend，然后在settings的`AUTHENTICATION_BACKENDS`中添加这个类。

```Python
class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
```

在`django.contrib.auth.views`中提供了许多用户相关的视图，例如：`login`，`logout`等，我们无须手动地实现登录和登出用户的操作，直接调用这两个视图即可。

## Admin

Django本身集成了一个功能强大的Admin，使得开发者不需要编写后台就能方便地对数据进行CURD操作，大多数情况下，我们直接使用Django提供的Admin即可完成需求。

Admin使用原则：

1. ModelAdmin中，用fields代替exclude。
2. 添加相应的verbose，使Admin的可读性更好。
3. 合适地添加Model Action。
4. 添加合适的list_display，ordering和filter，使数据的显示更加友好。

## 日志

日志使用原则：

1. 每个模块有独自的logger，可使用`logger = logging.getLogger(__name__)`实现。
2. 为log设置适当的等级，理解DEBUG、CRITICAL、ERROR、WARNING、INFO的差异，如：
	- DEBUG: 打印和调试使用（代替print）。
	- INFO: 普通的系统信息。
	- WARNING: 描述异常的错误信息。
	- ERROR: 描述严重错误发生的信息。
	- CRITICAL: 描述系统发生崩溃的错误信息。
3. 设置合适的Formatters，打印直观的信息。

## 表单

表单使用原则：

1. 使用`clean`或`clean_<field>`方法来验证表单字段。
2. 当表单与model有耦合时，使用ModelForm。
3. 不要忘记在模版中的`<form>`里添加`{% csrf_token %}`标签。
4. 用`form.field.errors`代替自定义的错误显示。
5. 用`form.is_valid()`来验证表单的合法性。
6. 当ModelForm的模型涉及关联字段时，通过form.save(commit=False)来保存模型，再在模型上添加关联信息。

## Signal

Django在`django.db.models.signals`里提供了许多关于Signal的钩子函数，例如`post_save`，`pre_save`等，使得模型在修改时可以触发一系列的自定义操作，但Signal在实际使用中不可滥用，并且在不是最佳情况下你应该避免使用它。

## 缓存

缓存可以减轻数据库查询的负担，合理使用缓存能对网站性能提升明显。

`django.core.cache`中提供了cache，它提供了类似dict的API，把数据存储在内存。但有些时候，只使用默认的cache往往是不够看的，这时候用外接的缓存数据库会是一个更好的选择，例如Memcached，Redis。

当我们决定了使用其它的缓存引擎时，需要在settings中作出相应的配置，如下所示（django-redis）：

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

接着我们便可以像使用原来接口那样调用新接口了

```python
datas = cache.get(DATA_KEY, None)
if not datas:
	datas = queryset.all()
    cache.set(DATA_KEY, datas, timestamp)
# 使用datas
```

## 会话

通过`request.cookie`和`request.session`能够方便地处理当前请求地会话。

会话使用原则：

1. 敏感信息切勿用cookie存储，多数情况下应使用session，并且考虑加密。
2. 适当设置会话的过期时间。
3. 妥当存储settings的SECRET_KEY。

## Util

在实际开发中，往往需要用到一些‘工具函数’，例如分页，view decorator等，这时候我们可以建一个叫utils(或者common)的模块，里面存放这些工具函数。

在我们编写工具函数／类时，首先要考虑我们是否在重复造轮子，django在`django.utils`中提供了许多有用的工具方法供我们使用。

## 数据迁移

django集成的Migrations提供了数据迁移的功能。假如你修改了数据库的schema（model），只需要两条命令便可实现数据的迁移。

```bash
python manage.py makemigrations
python manage.py migrate
```

## Fixture

在测试和部署项目时，会想用到一些初始化的假数据，这时候fixture就排得上用场了，使用`manage.py dumpdata`命令可以从数据库中把数据导出并硬编码为json、yaml等文件，使用`manage.py loaddata <fixturename>`命令则可以从fixture中读取数据并把数据迁移到数据库。

## 异步任务

在Web开发中有时会遇到一些耗时任务，但我们又不能让用户等待，那么异步任务队列就是一个不错的选择，具体做法是把耗时任务放进消息队列中，交给后台进程处理，web应用程序返回响应给用户。

**Celery**

Celery是一个分布式任务队列系统，它是一个专注于实时处理的任务队列，同时也支持任务调度。

使用celery还需要一个BROKER，可以是RabbitMQ或者Redis等。

在django使用Celery需要作一些配置：

```python
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
```

让celery检测任务：

```python
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks([])
```

定义任务：

```python
@task
def add(a, b):
    return a + b

# ... views.py
add.delay(1, 2) # 让celery执行任务
```

## REST

[Django-rest-framwork](https://github.com/tomchristie/django-rest-framework)是最好的选择。

## WSGI服务器

在wsgi服务器和http服务器的搭配上有常见的几种选择，如：

1. Nginx + uWSGI
2. Nginx + Gunicorn
3. Apache + mod_wsgi

应该根据实际情况选择合适的搭配。

## 邮件服务

要使用django的邮件服务，需要在settings里配置邮箱的设置，在使用之前，还需要在邮箱的服务商中开启smtp服务。

```
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 25
EMAIL_USE_TLS = True
```

## 全文搜索

**django-haystack＋solr**

## 第三方库

'Dont't Repeat Youself'是Django的信条，Django社区拥有大量地第三方库和模块，多数情况下我们都可以找到合适的库来应用到自己的项目中。

获取第三方库的渠道：

**PyPI**

**Gtihub**

**Django Packages**

## 安全

django自身包含了一些安全特性，如XSS，CSRF，SQL注入防护等。

安全原则：

1. 开启csrf保护
2. 妥善保管SECRET_KEY
3. 生产环境中关闭DEBUG
4. 谨慎处理用户上传内容
5. 有必要的话使用HTTPS

## 国际化

如果项目中需要用到国际化时，可以使用Django内建的[i18n支持](https://docs.djangoproject.com/es/1.9/topics/i18n/translation/)。

## 单元测试

单元测试编写原则：

1. 测试最小化。每个测试只测试一个view/model/method。
2. 使用mock代替耗时的数据库调用。
3. 分离测试文件，使测试扁平化。
4. 提高测试覆盖率。

测试工具：

**coverage**：代码测试覆盖率检测工具。

**nosetests**：Python的单元测试框架。

## 版本控制

版本控制的工具可根据情况选择Git或SVN。

版本控制的代码托管平台选择有不少，常用的是Github，Bitbucket，如果追求速度，可选择墙内的托管平台。

## 持续集成

`持续集成强调开发人员提交了新代码之后，立刻进行构建、（单元）测试。根据测试结果，我们可以确定新代码和原有代码能否正确地集成在一起。`

持续集成工具：

**jenkins**

**travis**

## 进程管理

**supervisor**

supervisor就是用Python开发的一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。

## 部署项目

**VPS**

**Paas**

**Docker**
