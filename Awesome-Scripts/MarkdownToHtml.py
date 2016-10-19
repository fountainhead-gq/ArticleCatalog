# coding:utf-8

import sys
import os
from bs4 import BeautifulSoup
import markdown


class MarkdownToHtml:

    headTag = '<head><meta charset="utf-8" /></head>'

    def __init__(self,cssFilePath = None):
        if cssFilePath != None:
            self.genStyle(cssFilePath)

    def genStyle(self,cssFilePath):
        with open(cssFilePath,'r') as f:
            cssString = f.read()
        self.headTag = self.headTag[:-7] + '<style type="text/css">{}</style>'.format(cssString) + self.headTag[-7:]

    def markdownToHtml(self, sourceFilePath, destinationDirectory = None, outputFileName = None):
        if not destinationDirectory:
            # 未定义输出目录则将源文件目录(注意要转换为绝对路径)作为输出目录
            destinationDirectory = os.path.dirname(os.path.abspath(sourceFilePath))
        if not outputFileName:
            # 未定义输出文件名则沿用输入文件名
            outputFileName = os.path.splitext(os.path.basename(sourceFilePath))[0] + '.html'
        if destinationDirectory[-1] != '/':
            destinationDirectory += '/'
        with open(sourceFilePath,'r', encoding='utf8') as f:
            markdownText = f.read()
        # 编译出原始 HTML 文本
        rawHtml = self.headTag + markdown.markdown(markdownText, output_format='html5')
        # 格式化 HTML 文本为可读性更强的格式
        beautifyHtml = BeautifulSoup(rawHtml, 'html.parser').prettify()
        with open(destinationDirectory + outputFileName, 'w', encoding='utf8') as f:
            f.write(beautifyHtml)


if __name__ == "__main__":
    mth = MarkdownToHtml()
    # 做一个命令行参数列表的浅拷贝，不包含脚本文件名
    argv = sys.argv[1:]
    # 目前列表 argv 可能包含源文件路径之外的元素（即选项信息）
    # 程序最后遍历列表 argv 进行编译 markdown 时，列表中的元素必须全部是源文件路径
    outputDirectory = None
    if '-s' in argv:
        cssArgIndex = argv.index('-s') +1
        cssFilePath = argv[cssArgIndex]
        # 检测样式表文件路径是否有效
        if not os.path.isfile(cssFilePath):
            print('Invalid Path: '+cssFilePath)
            sys.exit()
        mth.genStyle(cssFilePath)
        # pop 顺序不能随意变化
        argv.pop(cssArgIndex)
        argv.pop(cssArgIndex-1)
    if '-o' in argv:
        dirArgIndex = argv.index('-o') +1
        outputDirectory = argv[dirArgIndex]
        # 检测输出目录是否有效
        if not os.path.isdir(outputDirectory):
            print('Invalid Directory: ' + outputDirectory)
            sys.exit()
        # pop 顺序不能随意变化
        argv.pop(dirArgIndex)
        argv.pop(dirArgIndex-1)
    # 至此，列表 argv 中的元素均是源文件路径
    # 遍历所有源文件路径
    for filePath in argv:
        # 判断文件路径是否有效
        if os.path.isfile(filePath):
            mth.markdownToHtml(filePath, outputDirectory)
        else:
            print('Invalid Path: ' + filePath)
