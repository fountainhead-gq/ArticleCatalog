
*文件的复制*:

```python
import shutil
shutil.copyfile('d:/src/test.txt','d:/dst/test.txt')  # 从d:/src/复制test.txt到d:/dst/目录中
```


*文件的移动*
```python
import shutil
shutil.move('d:/code/test.txt','d:/')  # 移动了test.txt到d盘根目录中
```

*删除非空目录*
```python
import shutil
shutil.rmtree(dir)
```
