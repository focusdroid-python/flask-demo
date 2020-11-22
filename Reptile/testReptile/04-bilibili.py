# -*- coding:utf-8 -*-
import requests
import json

class BiliBili:
    def __init__(self, site_name):
        self.url = "https://api.bilibili.com/x/web-interface/search/type?context=&search_type=video&page={}&order=&keyword="+site_name+"&tids_1=&tids_2=&__refresh__=true&_extra=&highlight=1&single_column=0"
        self.headers = {
            "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "cookie":"_uuid=FDA0E6C6-969D-F5DB-AB50-96A8E70DE50188272infoc; buvid3=05855B56-14D7-4FB0-8119-8E64659792F9138403infoc; bfe_id=5db70a86bd1cbe8a88817507134f7bb5"
        }

    def createUrl(self, url):
        # return [url.format(i) for i in range(1, 14)]
        return url.format(1)

    def get_parse(self, url):
        res = requests.get(url, headers=self.headers)
        return json.loads(res.content.decode())

    def save_data(self, data):
        with open("blibli.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False,indent=2))

    def run(self):
        url = self.createUrl(self.url)
        data = self.get_parse(url)
        print(data)
        self.save_data(data.data.result)




if __name__ =="__main__":
    site_name = "鬼畜调教"
    bli = BiliBili(site_name)
    bli.run()

