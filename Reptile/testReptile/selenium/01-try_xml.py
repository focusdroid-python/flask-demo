# -*- coding:utf-8 -*-

from lxml import etree

text = '''
        <ul>
            <li width="100" class="top">
               <a class="nbg" href="https://movie.douban.com/subject/27662541/" title="福尔摩斯小姐：失踪的侯爵">
                   <img src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2617666143.webp" width="75" alt="福尔摩斯小姐：失踪的侯爵" class="">
               </a>
            </li>
            <li class="top">
                <div class="pl2">
                    <a href="https://movie.douban.com/subject/27662541/" title="消失的侯爵">
                        福尔摩斯小姐：失踪的侯爵
                        / <span style="font-size:13px;">福尔摩斯小姐 / 福尔摩斯小姐：消失的侯爵</span>
                    </a>
                    <p class="pl">2020-09-23(美国) / 2020-09-23(中国大陆网络) / 米莉·波比·布朗 / 路易斯·帕特里奇 / 山姆·克拉弗林 / 亨利·卡维尔 / 海伦娜·伯翰·卡特 / 阿迪勒·阿赫塔尔 / 费奥纳·肖 / 弗朗西斯·德·拉·图瓦 / 苏珊·沃卡曼 / 伯恩·戈曼 / 杰伊·辛普森...</p>
                        <div class="star clearfix">
                                <span class="allstar30"></span>
                                <span class="rating_nums">6.1</span>
                                <span class="pl">(12584人评价)</span>
                        </div>
                </div>
            </li>
            <li width="100" class="top">
                    <a class="nbg" href="https://movie.douban.com/subject/34960008/" title="监视资本主义：智能陷阱">
                        <img src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2618618715.webp" width="75" alt="监视资本主义：智能陷阱" class="">
                    </a>
            </li>
            <li class="top">
                <div class="pl2">
                    <a href="https://movie.douban.com/subject/34960008/">
                        监视资本主义：智能陷阱
                        / <span style="font-size:13px;">社交困境 / 愿者上网(港)</span>
                    </a>
                    <p class="pl">
                    2020-09-09(美国) / 杰伦·拉尼尔 / 罗杰·麦克纳米 / 斯凯勒·吉桑多 / 卡拉·海沃德 / 文森特·卡塞瑟 / 马蒂·林赛 / Ena Henderson / Chase Penny / 美国 / 杰夫·奥洛威斯基 / 94分钟 / 监视资本主义：智能陷阱 / 纪录片 / 戴维斯·库姆贝 Davis Coombe...</p>
                        <div class="star clearfix">
                                <span class="allstar45"></span>
                                <span class="rating_nums">8.6</span>
                                <span class="pl">(15448人评价)</span>
                        </div>
                </div>

            </li>
    </ul>
'''

html = etree.HTML(text)
print(html)
ret = html.xpath("//li[@class='top']//a")
print(ret)

for i in ret:
    item = {}
    item["title"] = i.xpath("./@title")[0] if len(i.xpath("./@title"))>0 else ''
    item["href"] = i.xpath("./@href")[0] if len(i.xpath("./@href"))>0 else ''
    item["name"] = i.xpath("..//p[@class='pl']/text()")[0] if len(i.xpath("..//p[@class='pl']/text()"))>0 else ''
    print(item)

# print(etree.tostring(html).decode())