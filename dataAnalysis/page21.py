
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


# font = {'family': 'monospace',
#         'weight': 'bold',
#         'size': 'larger'}
#
#
# matplotlib.rc(font, **font)
# matplotlib.rc(font, family='MicroSoft YaHei', weight='blod')

_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")



x = range(0,120)
y = [random.randint(20,35) for i in range(120)]


plt.figure(figsize=(20,8), dpi=80)
plt.plot(x, y)
# 调整x的刻度
_x = list(x)
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=60, fontproperties=_font_manager)


plt.xlabel("时间", fontproperties=_font_manager)
plt.ylabel("温度 单位", fontproperties=_font_manager)
plt.title("10点到12点每分钟的气温变化情况", fontproperties=_font_manager)

plt.show()