import requests
import json


class BaiduFanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def run(self):
        # 1. 获取语言类型
            # 1.1 准备post的url地址，　post_data
        lang_detect_data = {"query": self.trans_str}
            # 1.2 发送post请求，获取相应
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
            # 1.3 提取语言类型
        # 2. 准备数据
        # ３. 发送post请求，获取响应
        # 4. 提取翻译结果


if __name__ == "__main__":
    baidufanyi = BaiduFanyi()
    baidufanyi.run()