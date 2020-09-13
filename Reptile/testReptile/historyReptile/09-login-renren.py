# -*- coding:utf-8 -*-

import requests


headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

cookies = "anonymid=k9s0c65y2om8pj; _r01_=1; taihe_bi_sdk_uid=dc98311ffc7de226cb1f79afdd705b6f; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C18333670b0ee1f54e006adc80fdd7f23%7C1588568014097%7C1%7C1588568014407; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C92e70cb2bde7172939cddc8f15fdd3b4%7C1588663804895%7C1%7C1588663805116; depovince=GW; JSESSIONID=abcQCcacpRCLo6Lv4O4qx; ick_login=c4088f0e-05b4-45aa-bdf0-9b08f1473ad5; taihe_bi_sdk_session=02916b8090c4c5873f420e06488a9481; ick=2cb82a29-88ff-4992-af3c-666c7117e519; __utma=151146938.1079666667.1598678110.1598678110.1598678110.1; __utmc=151146938; __utmz=151146938.1598678110.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _de=D5FD513C20B9124F1FF9E00605E6865D; __utmt=1; __utmb=151146938.5.10.1598678110; jebecookies=a83fe94f-bb8d-4a00-90ea-c063cdb4a65a|||||; p=32d0ca098d880623d09023785ef7117d8; first_login_flag=1; ln_uact=15701229789; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=028857504aa85b7281b1625a0bee47098; societyguester=028857504aa85b7281b1625a0bee47098; id=974361808; xnsid=c74ef2cb; ver=7.0; loginfrom=null; wp_fold=0"
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}

print(cookies)

# 在使用session进行请求登陆之后才能访问的地址
# res = requests.get("http://www.renren.com/327550029/profile", headers=headers)
res = requests.get("http://www.renren.com/974361808/profile", headers=headers, cookies=cookies)


print(res)

# 保存页面w
with open("renren4.html", "w", encoding="utf-8") as f:
    f.write(res.content.decode())
