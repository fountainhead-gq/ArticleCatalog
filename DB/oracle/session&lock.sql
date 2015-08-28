SELECT s.username,
decode(l.type,'TM','TABLE LOCK',
'TX','ROW LOCK',
NULL) LOCK_LEVEL,
o.owner,o.object_name,o.object_type,
s.sid,s.serial#,s.terminal,s.machine,s.program,s.osuser
FROM v$session s,v$lock l,dba_objects o
WHERE l.sid = s.sid
AND l.id1 = o.object_id(+)
AND s.username is NOT Null



SELECT object_name, machine, s.sid, s.serial#,s.username
FROM gv$locked_object l, dba_objects o, gv$session s
WHERE l.object_id　= o.object_id
AND l.session_id = s.sid; 


select object_name,machine,s.sid,s.serial# from v$locked_object l,dba_objects o ,v$session s 
where l.object_id　=　o.object_id and l.session_id=s.sid;

--1.查出锁定object的session的信息以及被锁定的object名
SELECT l.session_id sid, s.serial#, l.locked_mode,l.oracle_username,
l.os_user_name,s.machine, s.terminal, o.object_name, s.logon_time
FROM v$locked_object l, all_objects o, v$session s
WHERE l.object_id = o.object_id
AND l.session_id = s.sid
ORDER BY sid, s.serial# ;

--2.查出锁定表的session的sid, serial#,os_user_name, machine name, terminal和执行的语句
SELECT l.session_id sid, s.serial#, l.locked_mode, l.oracle_username, s.user#,
l.os_user_name,s.machine, s.terminal,a.sql_text, a.action
FROM v$sqlarea a,v$session s, v$locked_object l
WHERE l.session_id = s.sid
AND s.prev_sql_addr = a.address
and sql_text<>'select 1 from dual'
ORDER BY sid, s.serial#;

--3.查出锁定表的sid, serial#,os_user_name, machine_name, terminal，锁的type,mode
SELECT s.sid, s.serial#, s.username, s.schemaname, s.osuser, s.process, s.machine,
s.terminal, s.logon_time, l.type
FROM v$session s, v$lock l
WHERE s.sid = l.sid
AND s.username IS NOT NULL
ORDER BY sid;

--kill命令
alter system kill session '1013,6066'

--查看当前的session
select * from v$mystat where rownum = 1;

--查被锁对象
select sid,serial#,username,SCHEMANAME,osuser,MACHINE,terminal,PROGRAM,owner,object_name,object_type,o.object_id
from dba_objects o,v$locked_object l,v$session s
where o.object_id=l.object_id and s.sid=l.session_id;





select * from v$locked_object

select object_name, object_type from dba_objects where object_id ='126721'

select sid, serial#, machine, program from v$session where sid <'990'

select * from dba_objects where object_id ='126721'






