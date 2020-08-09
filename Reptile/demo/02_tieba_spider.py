
import requests

class TiebaSpider:
    def __init__(self, name):
        self.tieba_name = name
        self.url = "https://tieba.baidu.com/f?kw="+name+"ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

    def get_url_list(self): # 1. 构造url列表
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url.format(i+50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]

    def parse_url(self, url):
        # 发送请求
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w") as f:
            f.write(html_str)

    def run(self): # 实现主要逻辑
        # １．　构造url列表
        url_list = self.get_url_list()
        #　２．遍历，发送请求。获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # ３．保存
            page_num = url_list.index(url) + 1 # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()