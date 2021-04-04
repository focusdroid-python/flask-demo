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

# 绘制网格
plt.grid(alpha=0.1)


plt.show()