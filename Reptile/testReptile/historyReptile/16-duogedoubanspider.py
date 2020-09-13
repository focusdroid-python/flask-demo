# -*- coding:utf-8 -*-
import requests
import json

class DoubanSpider:
    def __init__(self):
        self.url_temp_list = [
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288",
                "country":"US"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=ios&for_mobile=&start=0&count=18&loc_id=108288",
                "country": "CN"
            }
        ]

        self.headers = [{
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Mobile Safari/537.36",
            "Cookie": "bid=quMYYD7N8VI; _ga=GA1.3.1850976928.1599290585; _gid=GA1.3.3881402.1599290585; _vwo_uuid_v2=DCDE9713EF77FF106BE85FE28C92D8438|1ada8c0ac93246e78a1edcd8e9402d78; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1599285498,1599355723; _ga=GA1.2.1850976928.1599290585; _gid=GA1.2.3881402.1599290585; talionnav_show_app=0; ll=108288; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1599376904",
            "Referer": "https://m.douban.com/tv/american"
        }, {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Mobile Safari/537.36",
            "Cookie": "bid=quMYYD7N8VI; _ga=GA1.3.1850976928.1599290585; _gid=GA1.3.3881402.1599290585; _vwo_uuid_v2=DCDE9713EF77FF106BE85FE28C92D8438|1ada8c0ac93246e78a1edcd8e9402d78; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1599285498,1599355723; _ga=GA1.2.1850976928.1599290585; _gid=GA1.2.3881402.1599290585; talionnav_show_app=0; ll=108288; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1599376904",
            "Referer": "https://m.douban.com/tv/chinese"
        }]
        self.total = 1

    def parse_url(self, url, headers):
        print(url)
        response = requests.get(url, headers=headers)
        print(response)
        return response.content.decode()

    def get_content_list(self, json_str):
        print(json_str)
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        self.total = dict_ret["total"]
        return content_list

    def save_content_list(self, content_list, country):
        with open("doubanSpiderAddCountry.json", "a", encoding="utf-8") as f:
            for content in content_list:
                content["country"] = country
                f.write(json.dumps(content, ensure_ascii=False, indent=4))
                f.write("\n")
        print('保存成功')


    def run(self): # 实现主要逻辑
        for header_temp in self.headers:
            for url_temp in self.url_temp_list:

                num = 0
                while num < self.total:
                    # 1. start_url
                    url = url_temp["url_temp"].format(num)
                    # 2.发送请求．获取响应
                    json_str = self.parse_url(url, header_temp)
                    # 3. 提取的是数据
                    print(json_str)
                    content_list = self.get_content_list(json_str)
                    # 4. 保存
                    print(url_temp["country"])
                    self.save_content_list(content_list, url_temp["country"])
                    # if len(content_list) < 18: 另外一种方法跳出循环
                    #     break
                    # 5. 构造下一页的url地址，进入循环
                    num += 18



if __name__== '__main__':
    douban = DoubanSpider()
    douban.run()
