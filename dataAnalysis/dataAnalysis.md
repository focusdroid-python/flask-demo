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