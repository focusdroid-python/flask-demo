import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Cookie": "anonymid=k9s0c65y2om8pj; depovince=GW; _r01_=1; JSESSIONID=abcNfoYyDySYUa1KYbEhx; ick_login=1f120d53-226f-48b0-85aa-6fa23c2aea8f; taihe_bi_sdk_uid=dc98311ffc7de226cb1f79afdd705b6f; taihe_bi_sdk_session=91d2d67ef0387cdfd5c5b98a2adb89de; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C18333670b0ee1f54e006adc80fdd7f23%7C1588568014097%7C1%7C1588568014407; ick=115383c1-78f2-4270-9a54-2136b5ae3d95; wp_fold=0; XNESSESSIONID=3ab59dd30b97; WebOnLineNotice_974361808=1; first_login_flag=1; ln_uact=15701229789; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=bf8a72df-0519-4da7-b1df-362082dfd8d0%7C92e70cb2bde7172939cddc8f15fdd3b4%7C1588570052591%7C1%7C1588570052691; jebecookies=fbd2ce92-afdd-406f-aa64-8c77424f55e6|||||; _de=D5FD513C20B9124F1FF9E00605E6865D; p=f4322106a294e3621012a0b8624141118; t=1c4aeb703428602f1361c3618e467c7e8; societyguester=1c4aeb703428602f1361c3618e467c7e8; id=974361808; xnsid=21d68637; loginfrom=syshome"
}

res = requests.get("http://www.renren.com/974361808/profile", headers=headers)

with open("renren2.html", "w", encoding="utf-8") as f:
    f.write(res.content.decode())