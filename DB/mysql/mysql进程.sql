-- Aborted_clients 由于客户没有正确关闭连接已经死掉，已经放弃的连接数量
-- Aborted_connects 尝试已经失败的连接MYSQL服务器的次数
-- Connections 试图连接MYSQL服务器的次数
-- Flush_commands 执行FLUSH命令的次数
-- Max_used_connections 同时使用的连接的最大数目
-- Threads_connected 当前打开的连接的数量
-- Threads_running 不在睡眠的线程数量
-- Uptime 服务器工作时间
show status;


-- 查看连接数
show processlist ;

-- 查看全部连接数
show full processlist ;

-- 杀死锁的process
-- 造成sleep睡眠连接过多的原因：
-- 1使用了太多持久连接
-- 2程序中，没有及时关闭mysql连接
-- 3数据库查询不够优化，过度耗时。

-- kill id

-- 查询是否锁表
show OPEN TABLES where In_use > 0 ;