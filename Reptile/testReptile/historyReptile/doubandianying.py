# -*- coding:utf-8 -*-

import requests
import json
from pprint import pprint

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36",
    "Cookie":"ll='108288'; bid=51rz71pD9Bg; ap_v=0,6.0; __utma=30149280.425351927.1599285204.1599285204.1599285204.1; __utmc=30149280; __utmz=30149280.1599285204.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D0F6F3969D5FE3CCF35168329EAD8DE9C|34915b99f4d3cc72d500b6d61ff95dd8; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1599285498; _ga=GA1.2.425351927.1599285204; _gid=GA1.2.1833855976.1599285500; UM_distinctid=1745cddd5d2485-02c04a6016b6bd-631f1934-38400-1745cddd5d354c; Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1599285877; Hm_lpvt_19fc7b106453f97b6a84d64302f21a04=1599285877; talionnav_show_app='0'; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1599286001; _ga=GA1.3.425351927.1599285204; _gid=GA1.3.1833855976.1599285500",
    "Referer":"https://m.douban.com/movie/nowintheater?ioc_id=108288"
}


url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288"


res = requests.get(url, headers=headers)

# json.loads把json字符串转化为python类型
ret = json.loads(res.content.decode())
pprint(ret)


# json.dumps能够把python类型转化为json字符串
# 写入之前需要说明文件的编码
# 写入之后需要使用ensure_ascii=False让编码显示中文
# indent自动显示每个字段的空格
with open('douban.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=4))

# with open("douban.json", "r", encoding="utf-8") as f:
#     ret2 = f.read()
#     ret3 = json.loads(ret2)
#     print(3)

# 使用json.load提取类文件对象中的数据
# with open('douban.json', 'w', encoding='utf-8') as f:
#     ret4 = json.load(f)
#     print(ret4)
#     print(type(ret4))

# 使用json.dump提取类文件对象中的数据
with open('douban1.json', 'w', encoding='utf-8') as f:
    json.dump(ret, f)