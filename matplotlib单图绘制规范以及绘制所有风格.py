'''
matplotlib 绘图建议：
尽量使用 fig, ax = plt.subplots() 来绘制.
不要使用 plt.figure() 要不然一会牵扯到plt 一会牵扯到ax 很绕
'''
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

a = np.arange(1, 8)
b = a ** 2
c = a ** 3

'''
单图绘制规范
'''
# 创建一个画布, 可以理解为fig就为创建好的画布。ax代表一会要画在画布上的图像。
# 我们只会ax来调整各种图像参数
fig, ax = plt.subplots(figsize=(6, 4))

# 在axes上作图
ax.bar(a, b, label='bar')

# 在ax基础上调整各种细节
ax.set_title('Title', fontsize=15)
ax.set_xlabel('xlabel', fontsize=15)
ax.set_ylabel('ylabel', fontsize=15)
ax.legend()

'''
多图绘制规范

'''




'''
绘制所有的风格
目前没能找到一种方法能够在一张画布上的所有子图中分别显示不同的风格。
每次运行 plt.style.use(style) 都是改变整个画布的风格。
'''
all_styles = plt.style.available
for style in all_styles:
    # 变换风格
    plt.style.use(style)
    plt.figure(figsize=(2, 1))
    plt.bar(a, b)
    plt.title(style, fontsize=15)
    plt.show()
