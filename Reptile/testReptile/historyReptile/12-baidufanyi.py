# -*- coding:utf-8 -*-
import requests
import json
import sys

class Baidufanyi:
    def __init__(self, trans_str):
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.trans_str = trans_str
        self.headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36",
            "cookie":"BIDUPSID=99D3906B2891117DD45F5E491132A0E6; PSTM=1571475292; BAIDUID=99D3906B2891117DC7D702BD4C3AB910:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=E2T0pZb0k2VWdrN2RoSTAwN2hwWlN0QkN0RER2fmh2cEVMSzF1RUtsRXRhMFpmRVFBQUFBJCQAAAAAAAAAAAEAAABiK9vku-6xpnRyZWVob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC3eHl8t3h5fOW; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1596959482; H_WISE_SIDS=148078_152480_151473_151746_149355_150968_150076_147090_141748_150084_151863_148867_151313_150746_147280_152309_150036_153101_150361_152593_153244_151017_151561_152591_148523_151033_127969_153226_146549_150560_152902_152981_146652_151319_146732_153058_152741_150764_131423_152022_128698_147588_152934_107318_152724_151582_152716_151170_140311_144966_153118_152273_152513_152456_151494_152249_147546_148868_150667_151704_110085; BDUSS_BFESS=E2T0pZb0k2VWdrN2RoSTAwN2hwWlN0QkN0RER2fmh2cEVMSzF1RUtsRXRhMFpmRVFBQUFBJCQAAAAAAAAAAAEAAABiK9vku-6xpnRyZWVob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC3eHl8t3h5fOW; BDSFRCVID=U-tOJeC62ZrlNhor-YM_KwXskgKKQYJTH6ao6s0Evk_vy54QxAqzEG0PoU8g0KubZoYLogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJKJoDt-JKK3fP36qR6sMJ8thmT22-usQ4jJ2hcH0KLKo4o1X47oKCu4XJni-hve2KviaMjwWfb1MRjvjR-2QJKfBpj8t63IMg6DXq5TtUJoSDnTDMRh-lIeWtvyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjj0DGDe3f; H_PS_PSSID=32647_32606_1449_32328_31254_32046_32679_32115_32691_26350_32506; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; H_BDCLCKID_SF_BFESS=tJKJoDt-JKK3fP36qR6sMJ8thmT22-usQ4jJ2hcH0KLKo4o1X47oKCu4XJni-hve2KviaMjwWfb1MRjvjR-2QJKfBpj8t63IMg6DXq5TtUJoSDnTDMRh-lIeWtvyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjj0DGDe3f; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1599273661; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1599273662; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1599273662; yjs_js_security_passport=bcac0ddc8477b24ba99ac7b5382488d37f6562fa_1599273666_js"
        }

    def parse_url(self, url, data):
        res = requests.post(url, data=data, headers=self.headers)
        return json.loads(res.content.decode())

    def get_ret(self, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print(ret)
        return ret


    def run(self): # 实现主要逻辑
        # 1. 获取语言类型
        lang_detect_data = {"query": self.trans_str}
            # 1.1 准备
            # 1.1
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
            # 1.1
        # ２. 发送post请求
        trans_data = {
            "query": self.trans_str,
            "from": "zh",
            "to": "en",
            "token": "4df0e2d73753ea261214fad1ba5fcbb7",
            "sign": "232427.485594"
        } if lang == 'zh' else {
            "query": self.trans_str,
            "from": "en",
            "to": "zh",
            "token": "4df0e2d73753ea261214fad1ba5fcbb7",
            "sign": "232427.485594"
        }

        dict_res = self.parse_url(self.trans_url, trans_data)
        # 4. 提取翻译结果
        response = self.get_ret(dict_res)
        print(response)

if __name__== "__main__":
    trans_str = sys.argv[1]
    baidu_fanyi = Baidufanyi(trans_str)
    baidu_fanyi.run()

