#!/usr/bin/env python
# coding: utf-8

# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
from pylab import *

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8, 6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1, 1, 1)

# X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。
C, S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=2.0, linestyle="-", label="cosine")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-", label="sine")

# 设置横轴纵轴的上下限
#xlim(-4.0, 4.0)
#ylim(-1.0, 1.0)

# 设置横轴纵轴的上下限和图形边界
#xlim(X.min()*1.1, X.max()*1.1)
#ylim(C.min()*1.1, C.max()*1.1)

# 设置横轴纵轴的上下限和图形边界
xmin, xmax = X.min(), X.max()
ymin, ymax = C.min(), C.max()
dx = (xmax - xmin) * 0.1
dy = (ymax - ymin) * 0.1
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)


# 设置横轴记号
xticks(np.linspace(-4, 4, 9, endpoint=True))

# 设置纵轴记号
yticks(np.linspace(-1, 1, 5, endpoint=True))


# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# yticks([-1, 0, +1])

# 添加图例
legend(loc='upper left')


# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()