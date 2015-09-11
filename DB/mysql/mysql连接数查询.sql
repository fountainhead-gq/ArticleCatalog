--  查看mysql的最大连接数
show variables like '%max_connections%';

-- 修改mysql的最大连接数
-- 需要重启数据库
set GLOBAL max_connections=600;
flush privileges;

-- 显示当前运行的线程
show processlist;

-- 显示当前状态
show STATUS;

--查看连接的时间
--如果没有global，则修改的变量只是当前这次开启的会话的而已

show global variables like '%timeout%';

set global wait_timeout = 120;

set global interactive_timeout = 120;

或，可以修改编辑 /etc/my.cnf,在mysqld 下 新增 timeout参数，设置为120秒
【mysqld】
wait_timeout=120
interactive_timeout=120
注意：要同时设置interactive_timeout和wait_timeout才会生效。
最后重启一下mysql 生效 即可！