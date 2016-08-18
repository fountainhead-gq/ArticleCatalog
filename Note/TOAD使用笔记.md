## TOAD使用笔记


### toad 常用快捷键
- `F8` 调出历史的执行sql
- `F9` 执行全部sql
- `Ctrl+t` 补全table_name
- `alt+ 箭头上下` 看sql history
- `Ctrl+Enter` 直接执行当前sql
- `Ctrl+Shift+F`  格式化sql语句  
- `Ctrl+u` 变大写
- `Ctrl+l` 变小写
- `Ctrl+b` 注释
- `Ctrl+Shift+b` 取消注释
- `F4` 查看表结构
- 可以空白处点击右键，进入`Editor Options`-> `Toolbars`->`Shortcuts`，自行定义快捷键。


### 其他快捷操作

- 鼠标停在sql语句所在行，然后`Ctrl+Enter`直接执行当前sql
- 自动替换，输入`sf`后按空格键，自动替换成`SELECT * FROM `，设置路径`View`->`Toad Options`->`Editor`->`Behavior`
- 快速查询表数据和表的字段，设置路径`View`->`Object Paletee`,点击后在窗口右侧产生一个窗口，里面可以根据`schema`选择对象类型


### 修改表中字段的值：
首先在`Database`->`Schema Browser`下查找到相应的表，在右边点击`Data`栏，然后选中一条记录，再点击`Data`栏下面的`▲(Edit Record)`，即可修改字段里的值，然后点击`√(Post edit)`，最后`Commit`。
