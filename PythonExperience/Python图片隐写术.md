# 图片隐写术

>[wikipedia](https://zh.wikipedia.org/wiki/%E9%9A%90%E5%86%99%E6%9C%AF)上的介绍：隐写术是一门关于信息隐藏的技巧与科学，所谓信息隐藏指的是不让除预期的接收者之外的任何人知晓信息的传递事件或者信息的内容。隐写术的英文叫做Steganography，来源于特里特米乌斯的一本讲述密码学与隐写术的著作Steganographia，该书书名源于希腊语，意为“隐秘书写”。


### 知识点
>[wikipedia](https://zh.wikipedia.org/wiki/%E9%9A%90%E5%86%99%E6%9C%AF)上的介绍: 载体文件（cover file）相对隐秘文件的大小（指数据含量，以比特计）越大，隐藏后者就越加容易。
因为这个原因，数字图像（包含有大量的数据）在因特网和其他传媒上被广泛用于隐藏消息。这种方法使用的广泛程度无从查考。例如：一个24位的位图中的每个像素的三个颜色分量（红，绿和蓝）各使用8个比特来表示。如果我们只考虑蓝色的话，就是说有28种不同的数值来表示深浅不同的蓝色。而像11111111和11111110这两个值所表示的蓝色，人眼几乎无法区分。因此，这个最低有效位就可以用来存储颜色之外的信息，而且在某种程度上几乎是检测不到的。如果对红色和绿色进行同样的操作，就可以在差不多三个像素中存储一个字节的信息。
更正式一点地说，使隐写的信息难以探测的，也就是保证“有效载荷”（需要被隐蔽的信号）对“载体”（即原始的信号）的调制对载体的影响看起来（理想状况下甚至在统计上）可以忽略。这就是说，这种改变应该无法与载体中的噪声加以区别。
（从信息论的观点来看，这就是说信道的容量必须大于传输“表面上”的信号的需求。这就叫做信道的冗余。对于一幅数字图像，这种冗余可能是成像单元的噪声；对于数字音频，可能是录音或者放大设备所产生的噪声。任何有着模拟放大级的系统都会有所谓的热噪声（或称“1/f”噪声)，这可以用作掩饰。另外，有损压缩技术（如JPEG）会在解压后的数据中引入一些误差，利用这些误差作隐写术用途也是可能的。）
隐写术也可以用作数字水印，这里一条消息（往往只是一个标识符）被隐藏到一幅图像中，使得其来源能够被跟踪或校验。

本实验将利用图片四个颜色（rgba）的最低有效位（英语：Least Significant Bit，lsb）来隐藏信息（本实验隐藏的是文字）


### 编码说明
首先设计将隐藏信息编码到图片中的函数 `encodeDataInImage()`，其有两个参数，分别是用作载体的图片对象和需要被隐藏的字符串。
`encodeDataInImage(Image.open("metaclass.png"), 'never ending tour -- bob dylan').save('encodeImage.png')`

`bytearray()` 将字符串转换为整数值序列（数字范围是 0 到 2^8-1），数值序列由字符串的字节数据转换而来,如下：
```python
>>> data = bytearray('从哪来到哪去','utf-8')
>>> data
bytearray(b'\xe4\xbb\x8e\xe5\x93\xaa\xe6\x9d\xa5\xe5\x88\xb0\xe5\x93\xaa\xe5\x8e\xbb')
>>> for i in data:
...     print(i,type(i))
...
228 <class 'int'>
187 <class 'int'>
142 <class 'int'>
229 <class 'int'>
147 <class 'int'>
170 <class 'int'>
230 <class 'int'>
157 <class 'int'>
165 <class 'int'>
229 <class 'int'>
136 <class 'int'>
176 <class 'int'>
229 <class 'int'>
147 <class 'int'>
170 <class 'int'>
229 <class 'int'>
142 <class 'int'>
187 <class 'int'>
```
utf-8 编码的中文字符一个就占了3个字节.然后 `map(constLenBin,bytearray(data, 'utf-8'))` 对数值序列中的每一个值应用`constLenBin()` 函数，将十进制数值序列转换为二进制字符串序列。`bin()` 的作用是将一个 int 值转换为二进制字符串


### 解码说明
`decodeImage()` 返回图片解码后的隐藏文字，其接受一个图片对象参数。
找到数据截止处所用的字符串 '0000000000000000' 很有意思，长度为16，而不是直觉上的 8，因为两个包含数据的字节的接触部分可能有 8 个 0。

`binaryToString()` 函数将提取出来的二进制字符串转换为隐藏的文本.要弄明白，必须要先搞懂 UTF-8 编码的方式，可以在 wikipedia 上了解  [UTF-8](https://zh.wikipedia.org/wiki/UTF-8)

UTF-8 是 UNICODE的一种变长的编码表达方式，也就是说一个字符串中，不同的字符所占的字节数不一定相同，这就给我们的工作带来了一点复杂度。因此我们使用下面两个匿名函数来提取出这些数据：
```
rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''
fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)
```

`fun()` 接受 2 个参数，第一个参数为表示一个字符的二进制字符串，这个二进制字符串可能有不同的长度（8、16、24...48）；第二个参数为这个字符占多少个字节。

`lambda x, i: x[i+1:8] + rec(x[8:], i-1)` 中 `x[i+1:8]` 获得第一个字节的数据，然后调用 `rec()`，以递归的方提取后面字节中的数据。

这里要提一句，`rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''`，你可能对在表达式里面引用了 rec 感到不可理解，的确，严格意义上这样是不能实现递归的，但在 python 里这样是可以的，这就是 python 的语法糖了。

注意到，字符的字节数据中，第一个字节开头 1 的数目便是字符所占的字节数：
`chartype = binary[index:].index('0') `

`string.append(chr(int(fun(binary[index:index+length],chartype),2)))` 这一行中用到的函数 `int()` 以及 `chr()` 的作用如下：
- `int()`: 接受两个参数，第一个参数为数字字符串，第二个参数为这个数字字符串代表的数字的进制。
- `chr()`：接受一个参数，参数为 int 值，返回 Unicode 码点为这个 int 值的字符。

函数使用参考：  
[Image.getdata()](https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.Image.getdata)  
[PIL.Image.new(mode, size, color=0)](https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.new)  
[Image.putdata(data, scale=1.0, offset=0.0)](https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#PIL.Image.Image.putdata)




### 参见代码
[完整代码](https://github.com/fountainhead-gq/ArticleCatalog/blob/master/Awesome-Scripts/steganography.py)


### 附录: UTF-8

`UTF-8（8-bit Unicode Transformation Format）`是一种针对Unicode的可变长度字符编码，也是一种前缀码。它可以用来表示Unicode标准中的任何字符，且其编码中的第一个字节仍与ASCII兼容，这使得原来处理ASCII字符的软件无须或只须做少部分修改，即可继续使用。因此，它逐渐成为电子邮件、网页及其他存储或发送文字的应用中，优先采用的编码。  
UTF-8使用一至六个字节为每个字符编码（尽管如此，2003年11月UTF-8被RFC 3629重新规范，只能使用原来Unicode定义的区域，U+0000到U+10FFFF，也就是说最多四个字节）：
1. 128个US-ASCII字符只需一个字节编码（Unicode范围由U+0000至U+007F）。
2. 带有附加符号的拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文及它拿字母则需要两个字节编码（Unicode范围由U+0080至U+07FF）。
3. 其他基本多文种平面（BMP）中的字符（这包含了大部分常用字，如大部分的汉字）使用三个字节编码（Unicode范围由U+0800至U+FFFF）。
4. 其他极少使用的Unicode 辅助平面的字符使用四至六字节编码（Unicode范围由U+10000至U+1FFFFF使用四字节，Unicode范围由U+200000至U+3FFFFFF使用五字节，Unicode范围由U+4000000至U+7FFFFFFF使用六字节）。

#### UTF-8编码字节含义
- 对于UTF-8编码中的任意字节B，如果B的第一位为0，则B独立的表示一个字符(ASCII码)；
- 如果B的第一位为1，第二位为0，则B为一个多字节字符中的一个字节(非ASCII字符)；
- 如果B的前两位为1，第三位为0，则B为两个字节表示的字符中的第一个字节；
- 如果B的前三位为1，第四位为0，则B为三个字节表示的字符中的第一个字节；
- 如果B的前四位为1，第五位为0，则B为四个字节表示的字符中的第一个字节；  
因此，对UTF-8编码中的任意字节，根据第一位，可判断是否为ASCII字符；根据前二位，可判断该字节是否为一个字符编码的第一个字节；根据前四位（如果前两位均为1），可确定该字节为字符编码的第一个字节，并且可判断对应的字符由几个字节表示；根据前五位（如果前四位为1），可判断编码是否有错误或数据传输过程中是否有错误。


**Unicode 和 UTF-8 之间的转换关系表** ( x 字符表示码点占据的位 )

|码点的位数	|码点起值	|码点终值	|字节数	|Byte 1	|Byte 2	|Byte 3	|Byte 4	|Byte 5	|Byte 6
|--- |--- |--- |--- |--- |--- |--- |--- |--- |---
|7	|U+0000	|U+007F	|1	|0xxxxxxx	|	|	| |	| |
|11	|U+0080	|U+07FF	|2	|110xxxxx	|10xxxxxx | | | | | 				
|16	|U+0800	|U+FFFF	|3	|1110xxxx	|10xxxxxx	|10xxxxxx | | | |			
|21	|U+10000 |U+1FFFFF	|4	|11110xxx	|10xxxxxx	|10xxxxxx	|10xxxxxx | | |		
|26	|U+200000	|U+3FFFFFF	|5	|111110xx	|10xxxxxx	|10xxxxxx	|10xxxxxx	|10xxxxxx | |
|31	|U+4000000	|U+7FFFFFFF	|6	|1111110x	|10xxxxxx	|10xxxxxx	|10xxxxxx	|10xxxxxx	|10xxxxxx

- 只有 `x `所在的位置（也即是字节中第一个 0 之后的数据）存储的是真正的字符数据.
- 在ASCII码的范围，用一个字节表示，超出ASCII码的范围就用字节表示，这就形成了我们上面看到的UTF-8的表示方法，这様的好处是当UNICODE文件中只有ASCII码时，存储的文件都为一个字节，所以就是普通的ASCII文件无异，读取的时候也是如此，所以能与以前的ASCII文件兼容。
- 大于ASCII码的，就会由上面的第一字节的前几位表示该unicode字符的长度，比如110xxxxx前三位的二进制表示告诉我们这是个2BYTE的UNICODE字符；1110xxxx是个三位的UNICODE字符，依此类推；xxx的位置由字符编码数的二进制表示的位填入。越靠右的x具有越少的特殊意义。只用最短的那个足够表达一个字符编码数的多字节串。注意在多字节串中，第一个字节的开头"1"的数目就是整个串中字节的数目。
