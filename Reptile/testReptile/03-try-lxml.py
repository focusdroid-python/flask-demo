# -*- coding:utf-8 -*-

from lxml import etree


text = '''
    <section id="list" class="grid">
<a href="https://m.douban.com/movie/subject/27126336/" class="item">
    <div class="cover">
        <div class="wp ratio3_4">
            <img src="https://img2.doubanio.com/view/photo/m_ratio_poster/public/p2616924633.jpg" alt="假面饭店" data-x="1080" data-y="1463" class="img-show" style="width: 100%;">
            
        </div>
    </div>

    <div class="info">
        <h4></h4>
        <h3>假面饭店 </h3>
        <p class="rank">
                    <span class="rating-stars" data-rating="3.2"><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-gray"></span><span class="rating-star rating-star-small-gray"></span></span> <span>6.4</span>
        </p>
        <p class="meta">日本 / 剧情 犯罪 悬疑 / 铃木雅之 / 木村拓哉 长泽雅美</p>
        <cite></cite>
    </div>
</a>
<a href="https://m.douban.com/movie/subject/26348103/" class="item">
    <div class="cover">
        <div class="wp ratio3_4">
            <img src="https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2616349755.jpg" alt="小妇人" data-x="1080" data-y="1512" class="img-show" style="width: 100%;">
            
        </div>
    </div>

    <div class="info">
        <h4></h4>
        <h3>小妇人 </h3>
        <p class="rank">
                    <span class="rating-stars" data-rating="4.0"><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-gray"></span></span> <span>8.1</span>
        </p>
        <p class="meta">美国 / 剧情 爱情 / 格蕾塔·葛韦格 / 西尔莎·罗南 艾玛·沃森</p>
        <cite></cite>
    </div>
</a>
<a href="https://m.douban.com/movie/subject/30252495/" class="item">
    <div class="cover">
        <div class="wp ratio3_4">
            <img src="https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2615015805.jpg" alt="1917" data-x="3000" data-y="4200" class="img-show" style="width: 100%;">
            
        </div>
    </div>

    <div class="info">
        <h4></h4>
        <h3>1917 </h3>
        <p class="rank">
                    <span class="rating-stars" data-rating="4.3"><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-gray"></span></span> <span>8.5</span>
        </p>
        <p class="meta">美国 英国 印度 西班牙 加拿大 中国大陆 / 剧情 战争 / 萨姆·门德斯 / 乔治·麦凯 迪恩·查尔斯·查普曼</p>
        <cite></cite>
    </div>
</a>
<a href="https://m.douban.com/movie/subject/30170833/" class="item">
    <div class="cover">
        <div class="wp ratio3_4">
            <img src="https://img1.doubanio.com/view/photo/m_ratio_poster/public/p2616740389.jpg" alt="荞麦疯长" data-x="5906" data-y="8268" class="img-show" style="width: 100%;">
            
        </div>
    </div>

    <div class="info">
        <h4></h4>
        <h3>荞麦疯长 </h3>
        <p class="rank">
                    <span class="rating-stars" data-rating="2.3"><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-gray"></span><span class="rating-star rating-star-small-gray"></span><span class="rating-star rating-star-small-gray"></span></span> <span>4.5</span>
        </p>
        <p class="meta">中国大陆 / 剧情 爱情 / 徐展雄 / 马思纯 钟楚曦</p>
        <cite></cite>
    </div>
</a>
<a href="https://m.douban.com/movie/subject/26661193/" class="item">
    <div class="cover">
        <div class="wp ratio3_4">
            <img src="https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2614225081.jpg" alt="我在时间尽头等你" data-x="1080" data-y="1512" class="img-show" style="width: 100%;">
            
        </div>
    </div>

    <div class="info">
        <h4></h4>
        <h3>我在时间尽头等你 </h3>
        <p class="rank">
                    <span class="rating-stars" data-rating="2.5"><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-full"></span><span class="rating-star rating-star-small-gray"></span><span class="rating-star rating-star-small-gray"></span><span class="rating-star rating-star-small-gray"></span></span> <span>5.1</span>
        </p>
        <p class="meta">中国大陆 / 爱情 奇幻 / 姚婷婷 / 李鸿其 李一桐</p>
        <cite></cite>
    </div>
</a>
</section>
'''

html = etree.HTML(text)
print(html)
# 查看element对象中包含的字符串
print(etree.toString(html).decode())

