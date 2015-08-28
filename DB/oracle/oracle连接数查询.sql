--查询数据库的最大连接数：
select * from v$parameter where name = 'processes';

-- 查询数据库当前进程的连接数：
select count(*) from v$process;

-- 查看数据库当前会话的连接数：
select count(*) from v$session;

-- 查看数据库的并发连接数：
select count(*) from v$session where status='ACTIVE';

-- 查看当前数据库建立的会话：
select sid,serial#,username,program,machine,status from v$session;

--查看当前有哪些用户正在使用数据;
select osuser,a.username,cpu_time/executions/1000000||'s',sql_fulltext,machine from v$session a,v$sqlarea b where a.sql_address = b.address order by cpu_time/executions desc;

--修改数据库允许的最大连接数：
alter system set processes = 600 scope = spfile;

-- (需要重启数据库才能实现连接数的修改)
--重启数据库：
--shutdown immediate;
--startup;