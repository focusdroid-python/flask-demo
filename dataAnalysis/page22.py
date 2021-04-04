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