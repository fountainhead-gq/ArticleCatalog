--��ѯ���ݿ�������������
select * from v$parameter where name = 'processes';

-- ��ѯ���ݿ⵱ǰ���̵���������
select count(*) from v$process;

-- �鿴���ݿ⵱ǰ�Ự����������
select count(*) from v$session;

-- �鿴���ݿ�Ĳ�����������
select count(*) from v$session where status='ACTIVE';

-- �鿴��ǰ���ݿ⽨���ĻỰ��
select sid,serial#,username,program,machine,status from v$session;

--�鿴��ǰ����Щ�û�����ʹ������;
select osuser,a.username,cpu_time/executions/1000000||'s',sql_fulltext,machine from v$session a,v$sqlarea b where a.sql_address = b.address order by cpu_time/executions desc;

--�޸����ݿ�����������������
alter system set processes = 600 scope = spfile;

-- (��Ҫ�������ݿ����ʵ�����������޸�)
--�������ݿ⣺
--shutdown immediate;
--startup;