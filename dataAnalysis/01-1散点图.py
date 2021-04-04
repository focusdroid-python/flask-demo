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