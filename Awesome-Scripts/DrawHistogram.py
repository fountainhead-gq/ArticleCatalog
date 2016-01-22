#!/usr/bin/env python
# coding: utf-8

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import os
# import os.path


# 必须配置中文字体，否则会显示成方块
# 注意所有希望图表显示的中文必须为unicode格式

fontPath = os.getcwd()
fontPath = os.path.join(fontPath, 'STKAITI.TTF')


#fontPath = os.path.dirname(__file__)
#filename = os.path.join(fontPath, 'STKAITI.TTF')

custom_font = mpl.font_manager.FontProperties(fname=fontPath)

font_size = 10  # 字体大小
fig_size = (10, 5)  # 图表大小,宽和高的值

names = (u'2013年度', u'2014年度', u'2015年度')  # 名称
subjects = (u'居家物业', u'行车交通', u'休闲娱乐', u'衣服饰品', u'学习进修')  # 支出项
scores = ((65000, 29000, 17500, 21800, 4000), (35000, 21900, 20500, 31000, 7000), (85000, 30800, 25200, 28500, 11500))  # 计值

mpl.rcParams['font.size'] = font_size   # 更新字体大小
mpl.rcParams['figure.figsize'] = fig_size   # 更新图表大小
bar_width = 0.3  # 设置柱形图宽度

index = np.arange(len(scores[0]))

rects1 = plt.bar(index, scores[0], bar_width, color='#EF476F', label=names[0])  # 绘制2013
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#118AB2', label=names[1])  # 绘制2014
rects3 = plt.bar(index + 2*bar_width, scores[2], bar_width, color='#7DDF64', label=names[2])  # 绘制2015


plt.xticks(index + 1.5 * bar_width, subjects, fontproperties=custom_font)  # X轴标题
plt.ylim(ymax=100000, ymin=0)  # Y轴范围
plt.title(u'总支出明细对比', fontproperties=custom_font)  # 图表标题
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5, prop=custom_font)  # 图例显示在图表下方


# 添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        rect.set_edgecolor('white')  # 柱形图边缘用白色填充，纯粹为了美观

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)

# 图表输出到本地
plt.savefig('outgoings_detial.png')
