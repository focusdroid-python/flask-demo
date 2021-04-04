from matplotlib import pyplot as plt
from matplotlib import font_manager
a = ["战狼2","速度与激情8","功夫瑜伽","西游降魔篇",]
b_16 = [15746,312,4497,235]
b_15 = [12345,458,4562,154]
b_14 = [5685,355,5488,124]
_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

x_14 = list(range(len(a)))
x_15 = [i+0.2 for i in x_14]
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