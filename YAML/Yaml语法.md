## YAML 简介

YAML（YAML Ain’t Markup Language），一种直观的能够被电脑识别的数据序列化格式，是一个可读性高并且容易被人类阅读，容易和脚本语言交互，用来表达资料序列的编程语言。它参考了其它多种语言，包括：XML、C语言、Python、Perl以及电子邮件格式RFC2822，是类似于标准通用标记语言的子集XML的数据描述语言，语法比XML简单很多。


## YAML 语法
YAML使用 UTF-8 和 UTF-16 编码。

- 使用空格 `Space` 缩进表示分层，不同层次之间的缩进可以使用不同的空格数目，但是同层元素一定左对齐，即前面空格数目相同（不能使用 Tab，各个系统 Tab对应的 Space 数目可能不同，导致层次混乱）
- `#`表示注释，只能单行注释，从#开始处到行尾
- `-`破折号后面跟一个空格（一个横杠和一个空格）表示列表
- `:`冒号和空格表示键值对 `key: value`,字典是由一个简单的 `键: 值` 的形式组成(这个冒号后面必须是一个空格)
- 所有的 YAML 文件始行都应该是 `---`. 这是 YAML 格式的一部分, 表明一个文件的开始

简单数据（scalars，标量数据）可以不使用引号括起来，包括字符串数据。用单引号或者双引号括起来的被当作字符串数据，在单引号或双引号中使用C风格的转义字符


## Collections

**Sequence of Scalars**
```yaml
- Mark McGwire
- Sammy Sosa
- Ken Griffey
```
**Mapping Scalars to Scalars**
```yaml
hr:  65    # Home runs
avg: 0.278 # Batting average
rbi: 147   # Runs Batted In
```

**Mapping Scalars to Sequences**
```yaml
american:
  - Boston Red Sox
  - Detroit Tigers
  - New York Yankees
national:
  - New York Mets
  - Chicago Cubs
  - Atlanta Braves
```  

**Sequence of Mappings**
```yaml
-
  name: Mark McGwire
  hr:   65
  avg:  0.278
-
  name: Sammy Sosa
  hr:   63
  avg:  0.288
```  
**Sequence of Sequences**
```yaml
- [name        , hr, avg  ]
- [Mark McGwire, 65, 0.278]
- [Sammy Sosa  , 63, 0.288]
```
**Mapping of Mappings**
```yaml
Mark McGwire: {hr: 65, avg: 0.278}
Sammy Sosa: {
    hr: 63,
    avg: 0.288
  }
```  


## Structures
`---`三个破折号（three dashes）分隔指令和文档内容，如果没有指令，则表示文档的开始；用`...`三个点表示文档结束.

**Two Documents in a Stream**
```yaml
# Ranking of 1998 home runs
---
- Mark McGwire
- Sammy Sosa
- Ken Griffey

# Team ranking
---
- Chicago Cubs
- St Louis Cardinals
```
**Play by Play Feed**
```yaml
---
time: 20:03:20
player: Sammy Sosa
action: strike (miss)
...
---
time: 20:03:47
player: Sammy Sosa
action: grand slam
...
```
**Single Document with Two Comments**
```yaml
---
hr: # 1998 hr ranking
  - Mark McGwire
  - Sammy Sosa
rbi:
  # 1998 rbi ranking
  - Sammy Sosa
  - Ken Griffey
```

A question mark and space (“? ”) indicate a complex mapping key. Within a block collection, key: value pairs can start immediately following the dash, colon, or question mark.

**Mapping between Sequences**
```yaml
? - Detroit Tigers
  - Chicago cubs
:
  - 2001-07-23

? [ New York Yankees,
    Atlanta Braves ]
: [ 2001-07-02, 2001-08-12,
    2001-08-14 ]
```    

**Compact Nested Mapping**
```yaml
---
# Products purchased
- item    : Super Hoop
  quantity: 1
- item    : Basketball
  quantity: 4
- item    : Big Shoes
  quantity: 1
```  
