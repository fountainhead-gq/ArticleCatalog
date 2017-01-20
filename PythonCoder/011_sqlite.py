#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'GQ'

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute(r"insert into user (id, name) values ('A0001', 'shucun')")
cursor.execute(r"insert into user (id, name) values ('A0002', 'lilac')")
cursor.execute(r"insert into user (id, name) values ('A0003', 'oasis')")
# 通过rowcount获得插入的行数:
print('rowcount =', cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
# cursor.execute('select * from user where id =?', 'A0001')   # ?占位符必须对应的参数
cursor.execute('select * from user ')
# 获得查询结果集:
values = cursor.fetchall()  # 结果集是一个list，每个元素都是一个tuple，对应行记录。
print(values)
cursor.close()
conn.close()
