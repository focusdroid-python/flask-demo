from matplotlib import pyplot as plt
from matplotlib import font_manager

_font_manager = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

a = [131,98,125,131,124,139,121,117,128,108,135,138,121,102,107,114,119,128,121,152,127,130,125,101,110,116,117,110,1281,8,115,99,126,126,134,95,138,117,111,78,132,125,112,150,110,117,86,95,155,102,126,130,126,120,135,116,123,106,112,138,123,86,101,99,136,123,117,119,105,137,123,128,125,104,109,134,125,129,105, 55]


# 计算字数
d = 5
num_bins = (max(a) - min(a))//d
print(num_bins)

plt.figure(figsize=(20,8), dpi=80)

plt.hist(a, 300)

# 设置x刻度
plt.xticks(range(min(a), max(a)+d,d))

plt.show()