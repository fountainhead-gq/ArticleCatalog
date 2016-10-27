# PostgreSql的安装配置和入门


#### 修改端口绑定
默认情况下postgres像mysql一样只绑定本地127.0.0.1回环接口上的端口，这样使用网卡的正确IP却无法连接，编辑`D:\Program Files (x86)\PostgreSql\data\postgresql.conf`, 找到listen-addresses, 把前面"#"号去掉，并改为`listen-addresses = '*'`即绑定所有接口。  
`postgresql.conf` 定义了数据库服务器的参数，包括数据库文件的目录和其他其他配置文件的路径，以及服务器监听的IP地址和端口。

#### 修改IP连接限制
上述修改完成后使用外网机器pgadmin3可能依然无法连接，这时需要修改`D:\Program Files (x86)\PostgreSql\data\pg_hba.conf`文件来配置允许哪些IP可以访问，如下所示：
```sql
# TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD
# "local" is for Unix domain socket connections only
local   all         all                               ident
# IPv4 local connections:
#host    all         all         127.0.0.1/32          md5
host    all         all         0.0.0.0/0          md5
# IPv6 local connections:
host    all         all         ::1/128               md5
```
`pg_hba.conf` 定义了数据库客户端的访问规则（控制），它可以精确指定“谁”可以通过“什么方式”访问“什么数据库”。


#### 设置环境变量：
```sql
set PGHOME=D:\Program Files (x86)\PostgreSql
set PATH=D:\Program Files (x86)\PostgreSql\bin;
set PGHOST=localhost
set PGLIB=D:\Program Files (x86)\PostgreSql\lib
set PGDATA=D:\Program Files (x86)\PostgreSql\data
set PGUSER=postgres
```


#### 启动停止数据库
```sql
D:\Program Files (x86)\PostgreSql\bin>pg_ctl start
正在启动服务器进程

D:\Program Files (x86)\PostgreSql\bin>2016-10-24 17:26:23 HKT 日志:  日志输出重定向到日志收集进程
2016-10-24 17:26:23 HKT 提示:  后续的日志输出将出现在目录 "pg_log"中.

D:\Program Files (x86)\PostgreSql\bin>pg_ctl stop
```

#### 新开窗口操作,进入数据库
```sql
D:\Program Files (x86)\PostgreSql\data>psql
口令：
psql (9.6rc1)
输入 "help" 来获取帮助信息.

```

#### 创建查看数据库
```sql
postgres=# create database weibo;
CREATE DATABASE
postgres=# select oid,datname from pg_database;
  oid  |  datname
-------+-----------
 12401 | postgres
 24576 | weibo
     1 | template1
 12400 | template0
(4 行记录)
```


#### 创建查看用户
```sql
postgres=# create user test with password 'test';
CREATE ROLE
postgres=# select * from pg_user;
 usename  | usesysid | usecreatedb | usesuper | userepl | usebypassrls |  passwd  | valuntil | useconfig
----------+----------+-------------+----------+---------+--------------+----------+----------+-----------
 postgres |       10 | t           | t        | t       | t            | ******** |          |
 test     |    24577 | f           | f        | f       | f            | ******** |          |
(2 行记录)

```


#### 数据库的用户授权
```sql
postgres=# grant all privileges on database weibo to test;
GRANT
```

#### 列出所有的数据库
```sql
postgres=# \l

|   名称    |  拥有者  | 字元编码 | 校对规则   |    Ctype     |       存取权限
----------+----------+----------+-----------------------------------------------------+-----------------------------------------------------+-----------------------
 postgres  | postgres | UTF8     | Chinese (Simplified)_People's Republic of China.936 | Chinese (Simplified)_People's Republic of China.936 |
 template0 | postgres | UTF8     | Chinese (Simplified)_People's Republic of China.936 | Chinese (Simplified)_People's Republic of China.936 | =c/postgres          +
           |          |          |                                                     |                                                     | postgres=CTc/postgres
 template1 | postgres | UTF8     | Chinese (Simplified)_People's Republic of China.936 | Chinese (Simplified)_People's Republic of China.936 | =c/postgres          +
           |          |          |                                                     |                                                     | postgres=CTc/postgres
 weibo     | postgres | UTF8     | Chinese (Simplified)_People's Republic of China.936 | Chinese (Simplified)_People's Republic of China.936 | =Tc/postgres         +
           |          |          |                                                     |                                                     | postgres=CTc/postgres+
           |          |          |                                                     |                                                     | test=CTc/postgres
(4 行记录)

```
初始状态只有3个数据库：`template0`，`template1`和`postgres`。`template0`和`template1`是模版数据库，以后创建的数据库都以这些模版为基础。


#### 连接指定数据库
```sql
postgres-# \c weibo
您现在已经连接到数据库 "weibo",用户 "postgres".
```

#### 列出当前数据库的所有表格
```sql
# \dt 或 \d
weibo-# \d
                     关联列表
 架构模式 |         名称         |  类型  | 拥有者
----------+----------------------+--------+--------
 public   | comment_table_name   | 数据表 | test
 public   | fan_table_name       | 数据表 | test
 public   | follow_table_name    | 数据表 | test
 public   | forward_table_name   | 数据表 | test
 public   | image_table_name     | 数据表 | test
 public   | post_info_table_name | 数据表 | test
 public   | text_table_name      | 数据表 | test
 public   | thumbup_table_name   | 数据表 | test
 public   | user_info_table_name | 数据表 | test
(9 行记录)
```

### 列出所有表的更多信息
```sql
# \dt+ 或 \d+
weibo=# \d+
                             关联列表
 架构模式 |         名称         |  类型  | 拥有者 |  大小  | 描述
----------+----------------------+--------+--------+--------+------
 public   | comment_table_name   | 数据表 | test   | 72 kB  |
 public   | fan_table_name       | 数据表 | test   | 16 kB  |
 public   | follow_table_name    | 数据表 | test   | 16 kB  |
 public   | forward_table_name   | 数据表 | test   | 104 kB |
 public   | image_table_name     | 数据表 | test   | 16 kB  |
 public   | post_info_table_name | 数据表 | test   | 16 kB  |
 public   | text_table_name      | 数据表 | test   | 56 kB  |
 public   | thumbup_table_name   | 数据表 | test   | 112 kB |
 public   | user_info_table_name | 数据表 | test   | 16 kB  |
(9 行记录)
```
`\`开头的命令都有`+`这个选项，比如列出数据库命令`\l` 等

#### 列出某一张表格的结构
```sql
weibo=# \d fan_table_name
      数据表 "public.fan_table_name"
   栏位   |         类型          | 修饰词
----------+-----------------------+--------
 user_id  | character varying(20) |
 fan_list | text[]                |
```

#### 查看SQL命令的解释,比如\h select
```sql
weibo=# \h select
命令：       SELECT
描述：       从数据表或视图中读取数据
语法：
[ WITH [ RECURSIVE ] with查询语句(with_query) [, ...] ]
SELECT [ ALL | DISTINCT [ ON ( 表达式 [, ...] ) ] ]
    [ * | 表达式 [ [ AS ] 输出名称 ] [, ...] ]
    [ FROM from列表中项 [, ...] ]
    [ WHERE 条件 ]
    [ GROUP BY grouping_element [, ...] ]
    [ HAVING 条件 [, ...] ]
    [ WINDOW 窗口名称 AS ( 窗口定义 ) [, ...] ]
    [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] 查询 ]
    [ ORDER BY 表达式 [ ASC | DESC | USING 运算子 ] [ NULLS { FIRST | LAST } ] [, ...] ]
    [ LIMIT { 查询所用返回记录的最大数量 | ALL } ]
    [ OFFSET 起始值 [ ROW | ROWS ] ]
    [ FETCH { FIRST | NEXT } [ 查询所用返回记录的最大数量 ] { ROW | ROWS } ONLY ]
    [ FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE } [ OF 表名 [, ...] ] [ NOWAIT | SKIP LOCKED ] [...] ]
.....
```
### 添加一个超级用户
```sql
create role username login superuser password 'password';
```    
如果要添加一个普通用户，去掉上面的superuser。

### 删除一个用户
```sql
drop role username;
```
PostgreSQL（从9.0或者更早）的用户和用户角色都是role，所以创建、删除、更改用户就是create/drop/alter role命令。  
*注意: 在以上命令中以`\`开头的命令都是非sql命令，不需要以`;`结尾，其它的都是sql命令，需要以`;`结尾，否则不能执行。*

#### 查看命令列表
```sql
weibo=# \?
一般性
  \copyright            显示PostgreSQL的使用和发行许可条款
  \errverbose            以最冗长的形式显示最近的错误消息
  \g [文件] or;     执行查询 (并把结果写入文件或 |管道)
  \gexec                 执行策略，然后执行其结果中的每个值
  \gset [PREFIX]     执行查询并把结果存到psql变量中
  \q             退出 psql
  \crosstabview [COLUMNS] 执行查询并且以交叉表显示结果
  \watch [SEC]          每隔SEC秒执行一次查询

帮助
  \? [commands]          显示反斜线命令的帮助
  \? options             显示 psql 命令行选项的帮助
  \? variables           显示特殊变量的帮助
  \h [名称]          SQL命令语法上的说明，用*显示全部命令的语法说明

查询缓存区
  \e [FILE] [LINE]        使用外部编辑器编辑查询缓存区(或文件)
  \ef [FUNCNAME [LINE]]   使用外部编辑器编辑函数定义
  \ev [VIEWNAME [LINE]]  用外部编辑器编辑视图定义
  \p                    显示查询缓存区的内容
  \r                    重置(清除)查询缓存区
  \w 文件          将查询缓存区的内容写入文件

输入/输出
  \copy ...             执行 SQL COPY，将数据流发送到客户端主机
  \echo [字符串]       将字符串写到标准输出
  \i 文件          从文件中执行命令
  \ir FILE               与 \i类似, 但是相对于当前脚本的位置
  \o [文件]        将全部查询结果写入文件或 |管道
  \qecho [字符串]      将字符串写到查询输出串流(参考 \o)
 ...
 ```

#### 列出所有用户
```sql
weibo=# \du
                             角色列表
 角色名称 |                    属性                    | 成员属于
----------+--------------------------------------------+----------
 postgres | 超级用户, 建立角色, 建立 DB, 复制, 绕过RLS | {}
 test     |                                            | {}
```

#### 导出数据

导出数据到指定的路径  
```sql
weibo=# \copy user_info_table_name to C:\Users\Downloads\user_info.csv
COPY 100
```

####  列出当前数据库和连接的信息
```sql
weibo=# \conninfo
以用户 "postgres" 的身份, 在主机"localhost", 端口"5432"连接到数据库 "weibo"
weibo=#
```

#### 设置密码
为postgres用户设置一个密码  
```sql
weibo=# \password postgres
输入新的密码：
再次输入：
weibo=#
```

#### 退出命令
```sql
weibo=# \q

D:\Program Files (x86)\PostgreSql\data>
```
