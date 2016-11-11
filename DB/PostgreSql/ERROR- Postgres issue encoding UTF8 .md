# ERROR:  character with byte sequence 0xef 0xb8 0x8f in encoding "UTF8" has no equivalent in encoding "GBK"


解决方法：

```sql
weibo=# \copy text_table_name to C:\Users\Downloads\test.csv
ERROR:  character with byte sequence 0xef 0xb8 0x8f in encoding "UTF8" has no equivalent in encoding "GBK"
weibo=# show client_encoding;
 client_encoding
-----------------
 GBK
(1 行记录)

weibo=# SET client_encoding = 'UTF8';
SET
weibo=# \copy text_table_name to C:\Users\Downloads\test.csv
COPY 100
weibo=#
```


[参考链接](http://stackoverflow.com/questions/14525505/postgres-issue-encoding-utf8-has-no-equivalent-in-encoding-latin1)
