# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

class BaiduSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"
        self.start_url = "https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+tieba_name+"&pn=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko)",
            "Cookie": "USER_RS=3839568738_20_30_1; BIDUPSID=99D3906B2891117DD45F5E491132A0E6; PSTM=1571475292; TIEBA_USERTYPE=181e5540ac50b5f78f29bd4f; bdshare_firstime=1590835257666; BDUSS=E2T0pZb0k2VWdrN2RoSTAwN2hwWlN0QkN0RER2fmh2cEVMSzF1RUtsRXRhMFpmRVFBQUFBJCQAAAAAAAAAAAEAAABiK9vku-6xpnRyZWVob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC3eHl8t3h5fOW; TIEBAUID=5f4d5be1b2fd0d30f0bb90e6; st_key_id=17; 3839568738_FRSVideoUploadTip=1; H_WISE_SIDS=148078_152480_151473_151746_149355_150968_150076_147090_141748_150084_151863_148867_151313_150746_147280_152309_150036_153101_150361_152593_153244_151017_151561_152591_148523_151033_127969_153226_146549_150560_152902_152981_146652_151319_146732_153058_152741_150764_131423_152022_128698_147588_152934_107318_152724_151582_152716_151170_140311_144966_153118_152273_152513_152456_151494_152249_147546_148868_150667_151704_110085; BDUSS_BFESS=E2T0pZb0k2VWdrN2RoSTAwN2hwWlN0QkN0RER2fmh2cEVMSzF1RUtsRXRhMFpmRVFBQUFBJCQAAAAAAAAAAAEAAABiK9vku-6xpnRyZWVob21lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC3eHl8t3h5fOW; mo_originid=2; IS_NEW_USER=902f5df69e4e8652253f42d0; USER_JUMP=-1; CLIENTWIDTH=375; CLIENTHEIGHT=667; close_live_auto_refresh=false; SET_PB_IMAGE_WIDTH=355; BDSFRCVID=JWCOJexroG3oFq7rtgSmKwXo1eKKvV3TDYLEFLHRkrTmE-PVNFcjEG0Pt_NNY_L-abvWogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JJAO_IKMtCvbfP0k2Jo_5-4Hbp7t2D62aKDsXpP2BhcqJ-ovQTboQRoWKl8eb5Qibabyo4b63q6zVxbeWfvpQxAn0xRHLPr4HGRp2qQJ2q5nhMJmb4bhQDuzqfQa-qby523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0j6Jbja_jJ6na--oa3RTeb6rjDnCrK4vTXUI82h5y05Jy3jCfQtbNfPOvfUnvDtovynKZDnORXx74B5vvbPOMthRnOlRKXxjjMxL1Db3JyM6wyGOrsRjtbf3oepvoD-Jc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEJJAO_IKMtCvbfP0k2Jo_5-4Hbp7t2D62aKDs3fJgBhcqJ-ovQTboQRoWKlO4qnJibabyoR5cW-Q4hUbeWfvpQxAn0xRHLPr4HGRp2qQJ2q5nhMJmBUTFWq4TqfQa-qby523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0j6Jbja_jJ6na--oa3RTeb6rjDnCr-UnUXUI82h5y05Jy3jCfQtbjLb6vfUnvDtovynKZDnORXx74B5vvbPOMthRnOlRKXxjjMxL1Db3JyM6wyGOrsRjtbf3oepvoD-Jc3MvByPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEJJAO_IKMtCvbfP0k2Jo_5-4Hbp7t2D62aKDsaf3nBhcqJ-ovQTboQRoWKlOMQ-ribabyoR5cW-Q4hUbeWfvpQxAn0xRHLPr4HGRp2qQJ2q5nhMJmBUTFWq4TqfQa-qby523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH-etjtj3H; tb_as_data=d128bef924346bdda6932682ef17b53eda816539861669eae9d08bc10303f4717f3dd335dd1ff06e3982889a4204430456c0910cd189fd5d23d1111aab309155586dcd021d8ae604fbb2ae9eaff94a81538c60f4ea4320f5d586aac17623f9d3; LASW=412; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1602379842,1602381741,1602926735,1602926746; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1602926746; st_data=538580a4c7c6973533e7662ed86e96761906552020c69e80d37f6919b8d38ab4dabb1c5e12c000c9de36cc4a1e2fca6e59cd78e206122a4914d3d6ad866c9274380f25165bf79cb4235c14bb8bac2916fda4e6e4d409efc128da042b28407c83c71508321e0a3411fa8ca344e1555b41e06777ce42e8f4fad65a76af49f4e1ba; st_sign=1a5e73f1; BAIDUID=454205F3146961F40F0FE1A817D0CA77:FG=1; delPer=0; PSINO=2; H_PS_PSSID=32817_1439_33046_32940_31254_32705_32961_26350; BAIDUID_BFESS=CEB1E7C7309584E0E317E4660612686E:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjsv5_shitong=1.0_7_ddbc84ab077787f77ddf0196fdfb0df91974_300_1604744041696_111.198.229.152_90f873a2; BAIDU_WISE_UID=wapp_1604752638199_356; SEENKW=%E6%9D%8E%E6%AF%85%23lol",
            "Host": "tieba.baidu.com"
        }

    def parse_url(self, url): # 发送请求.获取响应
        print("------请求数据start-----")
        print(url)
        response = requests.get(url, headers=self.headers)
        print("------请求数据end-----")
        return response.content.decode()

    def get_content_list(self, html_str):
        print("------提取数据start-----")
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class, i)]")
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None
            item["title_href"] = self.part_url + div.xpath("./a/@href")[0] if len(div.xpath("./a/@href")) > 0 else None
            item["img_list"] = self.get_img_list(item["title_href"], [])

            content_list.append(item)
        # print(content_list)
        next_url = self.part_url+html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']/@href")) > 0 else None
        print("------提取数据end-----")
        return content_list, next_url

    def get_img_list(self, detail_url, totle_img_list):
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        totle_img_list.extend(img_list)
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(detail_next_url) > 0:
            detail_next_url = self.part_url+detail_next_url[0]
            return self.get_img_list(detail_next_url,totle_img_list)

        return totle_img_list

    def save_content_list(self, content_list):
        file_path = self.tieba_name+".txt"
        with open(file_path, "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))


    def run(self):
        next_url = self.start_url
        while next_url is not None:
            print("------url start----")
            print(next_url)
            print("------url end----")
            # 1. start_url
            # 2. 发送请求 获取响应
            print("-----准备开始请求----")
            html_str = self.parse_url(next_url)
            print("-----数据以及完成请求----")
            print("-----数据开始处理start----")
            print(html_str)
            # 3. 提取数据, 提取下一页的url,循环2-5步
            content_list, next_url = self.get_content_list(html_str)
            print("-----数据提取处理完成end----")
            # 4. 保存
            self.save_content_list(content_list)


if __name__ == "__main__":
    baidu = BaiduSpider("李毅")
    baidu.run()