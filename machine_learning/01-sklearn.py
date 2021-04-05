from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import jieba

def dictvec():
    """
    字典数据抽取
     字典中数据抽取：把字典中一些类别数据，分别进行转换成特征值
     数组形式，有类别的这些特征值，先进性转换字典数据
    """
    # 实例化
    dict = DictVectorizer(sparse=False)

    # 调用fit_transform
    dict_arr = [{'city':'北京','template': 100},{'city':'上海','template': 45},{'city':'西安','template': 50},{'city':'新疆','template': 80},]
    data = dict.fit_transform(dict_arr)

    print(dict.get_feature_names()) # 获取类别
    print(dict.inverse_transform(data)) # 获取类别
    print(data)

    return True

def countvec():
    """
    对文本进行特征值化
    """
    cv = CountVectorizer()
    english = ["life is is short, i like python", 'but this is not long, so ...']
    zh = ["人生 苦短，我用python， 人生 漫长，我 不用 python"]
    data = cv.fit_transform(zh)

    print(cv.get_feature_names())
    print(data.toarray())


def cuted():
    """
        中文特征值化
        """
    cpn1 = jieba.cut(
        "随着科技的不断发展，人类对宙宇星河的探索也从未间断过，自上世纪60年代，美国建造了地球的第一只眼‘阿雷西博’电射望远镜，不间断的向着宇宙传送着地球的电波信号，以期在未来的某一天被宇宙中其他的智能生命所拦截，同时也在监测着宇宙中任何特殊的电波信号，期望着能够接收到到来自星空的友好问候。")
    cpn2 = jieba.cut(
        "   1981年8月25日，‘旅行者2号’首次拜访了木星之后，利用木星的引力加速飞往天王星，这也是人类首次进入太阳系的黑暗之地，直到8年后，‘旅行者2号’首次接近太阳系最后一颗行星冥王星之后，科学家们便不再理会它的飞行轨迹，自此‘旅行者2号’开始了孤独太空探索之旅，直到2018年11月到达了太阳圈的边界。")
    cpn3 = jieba.cut("   遥遥望去，这无垠的星河海洋散发着各色的光彩，为这黑暗冰冷的宇宙平添了些许颜色，或许这片星河海洋就是太阳系的边界线，穿过它便能走出太阳系，挺进星际空间。")

    # 转换成list
    content1 = list(cpn1)
    content2 = list(cpn2)
    content3 = list(cpn3)

    #
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1, c2, c3


def hanzivec():
    c1, c2, c3 = cuted()
    print(c1, c2, c3)
    cv = CountVectorizer()

    data_temp = cv.toarray([c1, c2, c3])

    data = cv.fit_transform(data_temp)

    print(cv.get_feature_names())
    print(data.toarray())


def tfidfvec():
    c1, c2, c3 = cuted()
    # print(c1, c2, c3)
    tf = TfidfTransformer()

    data = tf.fit_transform([c1, c2, c3]).shape()

    print(tf.get_feature_names())
    print(data.toarray())
    return None


if __name__ == '__main__':
    tfidfvec()