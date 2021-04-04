# 数据分析
### matplotlib基本要点
```
# 安装matplotlib
pip3 install matplotlib
# from matplotlib import pyplot as plt
[](sudo pip3 install matplotlib -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com)
mapplotlib安装链接https://blog.csdn.net/dianshu1593/article/details/101523714
目前存在以下几个问题：
1. 设置图片大小()一张高清图
2. 保存到本地
3. 描述信息
4. 调整x或者y刻度的间距
5. 线条的样式（颜色，透明度）
6. 标记处特殊的点(最高点和最低点)
7. 给图片添加一个水印（防伪）


1. 设置图片大小()一张高清图
    plt.figure(figsize=(20,8), dpi=80)
2. 保存到本地
    plt.savefig("./sig_size.png") 
3. 描述信息
4. 调整x或者y刻度的间距
plt.xticks(x_axios) -> 调整x的刻度
plt.yticks(x_axios) -> 调整x的刻度
5. 线条的样式（颜色，透明度）
6. 标记处特殊的点(最高点和最低点)
7. 给图片添加一个水印（防伪）
```
```python
# 两个小时天气预报变化

from matplotlib import pyplot as plt
import random

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]


plt.figure(figsize=(20,8), dpi=80)
plt.plot(x, y)
# 调整x的刻度
_x = list(x)
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=60)

plt.show()
```
- 设置中文
    - fc-list 查看支持的字体
    - fc-list :lang=zh 查看支持的中文

```python
# 设置标题
from matplotlib import pyplot as plt
from matplotlib import font_manager

x = range(11,31)
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

# 摄设置图形大小plt
plt.figure(figsize=(20,8), dpi=80)

plt.plot(x,y)
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

# 设置x轴刻度
_xtick_lavels = ["{}岁".format(i) for i in x]
_ytick_lavels = ["{}月".format(i) for i in y]
plt.xticks(x, _xtick_lavels, fontproperties=_font_manager)
plt.yticks(y,_ytick_lavels, fontproperties=_font_manager)

plt.xlabel('年龄', fontproperties=_font_manager)
plt.ylabel('月', fontproperties=_font_manager)
plt.title('谈恋爱数据展示', fontproperties=_font_manager)


plt.show()
```

```python
# 绘制多个图形，修改线形
from matplotlib import pyplot as plt
from matplotlib import font_manager

x = range(11,31)
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

plt.figure(figsize=(20,8), dpi=80)

plt.plot(x, a, label='自己', color='red', linestyle=':', linewidth=5)
plt.plot(x, b,label='别人', color='blue', linestyle='--')
plt.grid(alpha=0.3)
plt.legend(prop=_font_manager, loc='upper left')

plt.show()
```
```python
# 绘制散点图
from matplotlib import pyplot as plt
from matplotlib import font_manager

y_3 = [11,17,16,11,12,11,12,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23, 22]
y_10 = [26,26,28,19,21,17,16,19,18,20,2,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

x_3 = range(0,31)
x_10 = range(50,81)

plt.figure(figsize=(20,8), dpi=80)

plt.scatter(x_3, y_3)
plt.scatter(x_10, y_10)
# 调整x轴的刻度
_x = list(x_3) + list(x_10)
_xticks_labels = ['3月{}日'.format(i) for i in x_3]
_xticks_labels += ['10月{}日'.format(i-49) for i in x_10]


plt.xticks(_x[::3], _xticks_labels[::3], fontproperties=_font_manager, rotation=45)

plt.show()
```
```python
# 柱状图
from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ["战狼2","速度与激情8","功夫瑜伽","西游降魔篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","死无对证","极限特工","生化危机6"]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.12,10.15,45.22]
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")


# 设置图形大小
plt.figure(figsize=(20,16),dpi=80)



plt.bar(range(len(a)), b, width=0.3)

plt.xticks(range(len(a)), a, fontproperties=_font_manager, rotation=90)

plt.show()
```
```python
# 横着柱状图
from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ["战狼2","速度与激情8","功夫瑜伽","西游降魔篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","死无对证","极限特工","生化危机6"]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.12,10.15,45.22]
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")


# 设置图形大小
plt.figure(figsize=(20,16),dpi=80)



plt.barh(range(len(a)), b, height=0.2)

plt.yticks(range(len(a)), a, fontproperties=_font_manager, rotation=90)

plt.grid(alpha=0.2)
plt.show()

```

```python
# 多个直方图
from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ["战狼2","速度与激情8","功夫瑜伽","西游降魔篇",]
b_16 = [15746,312,4497,235]
b_15 = [12345,458,4562,154]
b_14 = [5685,355,5488,124]
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

x_14 = list(range(len(a)))
x_15 = [i+0.2 for i in x_14] # 设置偏移，不设置就会堆叠
x_16 = [i+0.2*2 for i in x_14]

#
plt.figure(figsize=(20,8), dpi=80)

plt.bar(range(len(a)), b_14, width=0.2, label='4月3日')
plt.bar(x_15, b_15, width=0.2, label='4月2日')
plt.bar(x_16, b_16, width=0.2, label='4月1日')

# 设置图例
plt.legend(prop=_font_manager)

# 设置x的刻度
plt.xticks(x_15, a, fontproperties=_font_manager)

plt.show()
```
