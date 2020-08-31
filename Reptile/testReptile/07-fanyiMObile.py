# -*- coding:utf-8 -*-
import requests
import json
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "cookie": "BIDUPSID=99D3906B2891117DD45F5E491132A0E6; PSTM=1571475292; BAIDUID=99D3906B2891117DC7D702BD4C3AB910:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=E2T0pZb0k2VWdrN2RoSTAwN2hwWlN0QkN0RER2fmh2cEVMSzF1RUtsRXRhMFpmRVFBQUFBJCQAAAAAAAAAAAEAAABiK9vku-6xpnRyZWVob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC3eHl8t3h5fOW; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1596113665; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1596959482; H_WISE_SIDS=148078_152480_151473_151746_149355_150968_150076_147090_141748_150084_151863_148867_151313_150746_147280_152309_150036_153101_150361_152593_153244_151017_151561_152591_148523_151033_127969_153226_146549_150560_152902_152981_146652_151319_146732_153058_152741_150764_131423_152022_128698_147588_152934_107318_152724_151582_152716_151170_140311_144966_153118_152273_152513_152456_151494_152249_147546_148868_150667_151704_110085; BDUSS_BFESS=E2T0pZb0k2VWdrN2RoSTAwN2hwWlN0QkN0RER2fmh2cEVMSzF1RUtsRXRhMFpmRVFBQUFBJCQAAAAAAAAAAAEAAABiK9vku-6xpnRyZWVob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC3eHl8t3h5fOW; BCLID=10521574840715570735; BDSFRCVID=U-tOJeC62ZrlNhor-YM_KwXskgKKQYJTH6ao6s0Evk_vy54QxAqzEG0PoU8g0KubZoYLogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJKJoDt-JKK3fP36qR6sMJ8thmT22-usQ4jJ2hcH0KLKo4o1X47oKCu4XJni-hve2KviaMjwWfb1MRjvjR-2QJKfBpj8t63IMg6DXq5TtUJoSDnTDMRh-lIeWtvyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjj0DGDe3f; H_BDCLCKID_SF_BFESS=tJKJoDt-JKK3fP36qR6sMJ8thmT22-usQ4jJ2hcH0KLKo4o1X47oKCu4XJni-hve2KviaMjwWfb1MRjvjR-2QJKfBpj8t63IMg6DXq5TtUJoSDnTDMRh-lIeWtvyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKu-n5jHjj0DGDe3f; H_PS_PSSID=1449_32439_32361_32328_31254_32046_32393_32405_32115_26350_32506; __yjsv5_shitong=1.0_7_ddbc84ab077787f77ddf0196fdfb0df91974_700_1597555251128_111.198.229.148_9fd71050; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1597555728; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1597555728; yjs_js_security_passport=7db1f81a63928dd40056ed2b28736410b0b4443d_1597555735_js",
    "content-type": "application/x-www-form-urlencoded"
}

data = {
    "query": "成功",
    "from": "zh",
    "to": "en",
    "token": "4df0e2d73753ea261214fad1ba5fcbb7",
    "sign": "940983.702598"
}

post_url = "https://fanyi.baidu.com/basetrans"

res = requests.post(post_url, data=data, headers=headers)

print(res.content.decode())

# dict_ret = json.loads(res.content.decode())
# ret = dict_ret["trans"][0]["dst"]
# print(ret)