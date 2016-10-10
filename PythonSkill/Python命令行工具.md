<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python命令行工具](#python3%E5%8F%8A%E5%BA%94%E7%94%A88-%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7)
  - [docopt](#docopt)
  - [click](#click)
    - [arguments](#arguments)
      - [基本用法](#%E5%9F%BA%E6%9C%AC%E7%94%A8%E6%B3%95)
      - [多参数](#%E5%A4%9A%E5%8F%82%E6%95%B0)
      - [文件参数](#%E6%96%87%E4%BB%B6%E5%8F%82%E6%95%B0)
    - [option](#option)
      - [基本用法](#%E5%9F%BA%E6%9C%AC%E7%94%A8%E6%B3%95-1)
      - [多参数的选项](#%E5%A4%9A%E5%8F%82%E6%95%B0%E7%9A%84%E9%80%89%E9%A1%B9)
      - [多参数作为元组传入](#%E5%A4%9A%E5%8F%82%E6%95%B0%E4%BD%9C%E4%B8%BA%E5%85%83%E7%BB%84%E4%BC%A0%E5%85%A5)
      - [多次传入option](#%E5%A4%9A%E6%AC%A1%E4%BC%A0%E5%85%A5option)
      - [boolen判断](#boolen%E5%88%A4%E6%96%AD)
      - [限制可输入的参数](#%E9%99%90%E5%88%B6%E5%8F%AF%E8%BE%93%E5%85%A5%E7%9A%84%E5%8F%82%E6%95%B0)
      - [输入提示](#%E8%BE%93%E5%85%A5%E6%8F%90%E7%A4%BA)
      - [带有默认提醒的输入提示](#%E5%B8%A6%E6%9C%89%E9%BB%98%E8%AE%A4%E6%8F%90%E9%86%92%E7%9A%84%E8%BE%93%E5%85%A5%E6%8F%90%E7%A4%BA)
      - [有关密码的输入提示](#%E6%9C%89%E5%85%B3%E5%AF%86%E7%A0%81%E7%9A%84%E8%BE%93%E5%85%A5%E6%8F%90%E7%A4%BA)
      - [带有回调的option](#%E5%B8%A6%E6%9C%89%E5%9B%9E%E8%B0%83%E7%9A%84option)
      - [是/否的选择性option](#%E6%98%AF%E5%90%A6%E7%9A%84%E9%80%89%E6%8B%A9%E6%80%A7option)
    - [其他](#%E5%85%B6%E4%BB%96)
      - [default](#default)
      - [click.echo](#clickecho)
      - [help](#help)
  - [setuptools](#setuptools)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Python命令行工具

### [docopt](http://docopt.org/)

### [click](http://click.pocoo.org/6/)

```bash
$ pip3 install click
```

```python
# clicker.py
import click
```

#### [arguments](http://click.pocoo.org/6/arguments/)

##### 基本用法

```python
@click.command()
@click.argument('name', default='ecmadao')
def arg_with_default(name):
	click.echo(name)
```

名为name的参数会传递给arg_with_default函数，而当我们不添加参数调用的时候则会使用默认值。

```bash
$ python3 clicker.py
# ecmadao
$ python3 clicker.py test
# test
```

##### 多参数

需要传递多个参数时，可以设定`nargs`。`nargs`为-1时代表可以接受多个参数，为1则只能接受一个参数。可以接受多个参数时，多参数以tuple的形式赋值

```python
@click.command()
@click.argument('says', nargs=-1)
@click.argument('name', nargs=1)
def hello_multiply_arg(says, name):
	print('{} says:'.format(name))
	for said in says:
		click.echo(said)
```

第一个参数`nargs=-1`，第二个`nargs=-1`，因此在调用时，整体从后往前匹配，最后一个参数赋值给name，其他的作为元组赋值给says

```bash
$ python3 clicker.py 1 2 ecmadao
# ecmadao says:
# 1
# 2
$ python3 clicker.py ecmadao
# ecmadao says:
```

##### 文件参数

传递一个文件路径作为参数，并设置`type=click.File(操作文件的形式)`，则在调用参数的函数内转化为文件对象。

```python
@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def inout(input, output):
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)
```

对于文件参数而言，可以使用一个默认的参数`-`，来作为特殊的文件输入/输出流

```bash
$ python3 clicker.py - hello.txt
# hello
$ python3 clicker.py hello.txt -
```

#### [option](http://click.pocoo.org/6/options/)

`option`有三种写法： 完整写法`--option`，缩写`-op`，不带`-`的写法

```python
@click.option('--save', '-s') # 在函数中作为参数名称为save
@click.option('-s') # 参数名称为s
@click.option('--save-local') # 参数名称为save_local
@click.option('--save', '-s', 'saved') # 参数名称为saved
```

##### 基本用法

```python
@click.command()
@click.option('--options', '-op', default=2)
def default_option(options):
	for option in range(options):
		click.echo(option)
```

```bash
$ python3 clicker.py
# 0
# 1
$ python3 clicker.py -op=3
# 0
# 1
# 2
```

##### 多参数的选项

每一个option只支持接收固定长度的参数(argument接收参数个数可以无限制)。多个参数作为元组赋值给option

多次重复调用option则可以不断传入参数(见下文**多次传入option**)

```python
@click.command()
@click.option('--op', nargs=2)
def multi_options(op):
	for option in op:
		click.echo(option)
```

如果传入的参数不是2个则无法正常运行

```bash
$ python3 clicker.py --op=0
# Error: --op option requires 2 arguments
$ python3 clicker.py --op=0 1
# 0
# 1
```

##### 多参数作为元组传入

这种方法传入option，不仅仅限制了option的数目，也同时限制了其type

实际作用等同于上面多参数的option，但限制了传递的类型

```python
@click.command()
@click.option('--item', type=(int, str, int))
def tuple_option(item):
	for i in item:
		click.echo(i)
```

```bash
$ python3 clicker.py --item=s 0 0
# Error: Invalid value for "--item": s is not a valid integer
$ python3 clicker.py --item=0 s 0
# 0
# s
# 0
```

##### 多次传入option

通过`multiple=True`可以在一次调用中无限次数的调用option，并最终将全部的值作为一个tuple代入函数

```python
@click.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
    click.echo(' '.join(message))
```

```bash
$ python3 clicker.py -m foo -m bar
# foo bar
```

##### boolen判断

option可以有True或False的判断，并且能够在不传入option使用默认值

```python
@click.command()
@click.option('--happy/--no-happy', default=True)
def boolean_option(happy):
	if happy:
		click.echo('happy')
	else:
		click.echo('sad')
```

```bash
$ python3 clicker.py --happy
# happy
$ python3 clicker.py --no-happy
# happy
$ python3 clicker.py
# happy
```

如果不想使用这种True/False的两个参数的判断，则可以使用`is_flag=True`

```python
@click.command()
@click.option('--happy', is_flag=True)
def boolean_option(happy):
	if happy:
		click.echo('happy')
	else:
		click.echo('sad')
```

若传入option则为True，否则是False

```bash
$ python3 clicker.py --happy
# happy
$ python3 clicker.py
# sad
```

##### 限制可输入的参数

通过`type=click.Choice(['a', 'b', 'c'])`，使得只有在Choice内定义的值才能够被接受

```python
@click.command()
@click.option('--arg-type', type=click.Choice(['a', 'b', 'c']))
def choice_option(arg_type):
	print(arg_type)
```

```bash
$ python3 clicker.py --arg-type=1
#Error: Invalid value for "--arg-type": invalid choice: 1. (choose from a, b, c)
$ python3 clicker.py --arg-type=a
# a
```

##### 输入提示

通过设置`prompt`可以使没有option输入时交互式的提醒输入：

- `prompt=True`，提醒信息为option名称，开头大写
- `prompt='Input your name please'`，提醒信息则为自定义内容

```python
@click.command()
@click.option('--name', prompt=True)
def prompt_option(name):
    click.echo('I am {}'.format(name))

# python3 clicker.py
# name: ecmadao
# I am ecmadao

# python3 clicker.py --name=ecmadao
# I am ecmadao
```

```python
@click.command()
@click.option('--name', prompt='Your name')
def prompt_option(name):
    click.echo('I am {}'.format(name))

# python3 clicker.py
# Your name: ecmadao
# I am ecmadao
```

##### 带有默认提醒的输入提示

同时设置`prompt`和`default`即可达到这个效果

```python
@click.command()
@click.option('--name', '-n', prompt=True, default='ecmadao')
@click.option('--age', '-a', prompt=True, default=24)
def prompt_option_with_default(name, age):
	click.echo('I am {}'.format(name))
	click.echo('and {} years old'.format(age))
```

```bash
$ python3 clicker.py
# Name [ecmadao]:
# Age [24]:
# I am ecmadao
# and 24 years old
```

##### 有关密码的输入提示

密码输入提示和一般输入提示不同的是，密码输入不会将密码显式的展现出来

`hide_input=True`可是隐藏用户的输入；

`confirmation_prompt=True`则让用户重复输入以避免输入错误。

```python
@click.command()
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def password_option(password):
	click.echo('your password is {password}'.format(password=password))
```

```bash
$ python3 clicker.py
# Password: 123
# Repeat for confirmation: 123
# your password is 123

$ python3 clicker.py
# Password: 123
# Repeat for confirmation: 321
# Error: the two entered values do not match
# Password:
```

##### 带有回调的option

通过设置`callback=fun`，可以在命令行调用的时候，触发调用设置好的回调函数。

```python
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()

@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def hello():
    click.echo('Hello World!')
```

在上面这个例子中，使用了配置`is_flag=True`，因此，传入`--version`时为True，否则为False，而这个True/False则会作为callback中的value参数传入

`expose_value=False`，代表了不需要在下面的hello函数中显式的将version参数传入

`ctx`代表`click.core.Context object`

`param`代表`click.core.Option object`

```bash
$ python3 clicker.py
# Hello World
$ python3 clicker.py --version
# Version 1.0
```

##### 是/否的选择性option

```python
def confirm_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@click.command()
@click.option('--yes', is_flag=True, callback=confirm_if_false,
              expose_value=False,
              prompt='Are you sure?')
def delete_all_info():
    click.echo('Delete all info!')
```

上面例子中，`ctx.abort()`代表输入操作被打断，会退出当前进程，并在command line中console `Aborted!`代表被打断

```bash
$ python3 clicker.py
# Are you sure? [y/N]: n
# Aborted!
$ python3 clicker.py --yes
# Delete all info!
```

#### 其他

##### default

默认值可以使用函数

```python
@click.command()
@click.option('--username', prompt=True,
			  default=lambda: os.environ.get('USER', ''))
def hello(username):
	print("Hello,", username)
```

```bash
$ python3 clicker.py
# Username [ecmadao1]:
# Hello, ecmadao1
```

##### [click.echo](http://click.pocoo.org/6/quickstart/#echoing)

click的`echo`是为了兼容Python2和Python3而存在的，其底层实现其实就是`print`

##### help

click会自动帮你生成`help`文档，可以通过`--help`查看

例如一个这样的文件：

```python
# clicker_help.py
import click

@click.command()
@click.option('--username', prompt=True,
			  default=lambda: os.environ.get('USER', ''))
def get_user_env(username):
	print("Hello,", username)


if __name__ == '__main__':
	get_user_env()
```

```bash
$ python3 clicker_help.py --help

Usage: clicker_help.py [OPTIONS]

Options:
  --username TEXT
  --help           Show this message and exit.
```

### [setuptools](http://click.pocoo.org/6/setuptools/)
