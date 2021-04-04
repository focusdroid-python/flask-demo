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