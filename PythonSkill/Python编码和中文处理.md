## Python编码和中文处理

找到一个最言简意赅的入门教程：[揭秘Python Unicode](http://farmdev.com/talks/unicode/)


简要罗列一下最重要最实用的点：
1. **Decode early** （尽早`decode`, 将文件中的内容转化成 `unicode` 再进行下一步处理)
2. **Unicode everywhere** (程序内部处理都用`unicode`)
3. **Encode late** (最后`encode`回所需的`encoding`, 例如把最终结果写进结果文件)
