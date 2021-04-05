## 机器学习

- 算法、案例为驱动的学习，浅显易懂的数学知识
- 全部的安装使用阿里源
- sudo pip3 install matplotlib -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```
pandas:读取工具  真正的多线程

numpy释放GIL锁

可用数据集
scikit-learn特点：  https://scikit-learn.org/stable/
    1. 数据量小 2. 方便学习
Kaggle特点：https://www.kaggle.com/datasets
    1. 大数据竞赛平台
    2. 真实数据
    3. 数据量大
UCI特点： http://archive.ics.uci.edu/ml/datasets.php
    1. 收录360数据集
    2. 覆盖科学生活经济领域
    3. 数据量几十万
```
### 常用数据及数据的构成
```
结构：特征值 + 目标值

```
### 数据的特征工程
- 1、特征工程是什么
    特征工程是将原始数据转换为更好的代表预测模型的潜在问题的特征的过程，从未提高对未知数据的预测的准确性
- 2、特征工程的意思
    直接预测结果
- 3、scikit-learn库介绍
    python语言的机器学习工具
    许多知名机器学习算法的实现
- 4、数据的特征提取
- 5、数据的特征与处理
- 6、数据的降维
### 数据对于特征的处理
- panads：一个数据读取非常方便以及基本的处理格式的工具
- sklearn：对于特征的处理提供了强大的接口

### 安装scikit-learn
```
创建一个给予python3的虚拟环境
    mkvirtualenv -p /usr/bin/python3.6
在ubuntu的虚拟环境当中运行以下命令
pip3 install scikit-learn

然后通过导入命令查看是否可以使用
import cklearn

****安装scikitlearn需要安装Numpy,panads等库

pip 和 apt 安装的位置不一样。
pip 安装的包位于 /usr/local/lib/python2.7/dist-packages/
apt 安装的包位于 /usr/lib/python2.7/dist-packages/
这里是使用apt安装的
```

### 特征抽取
```
使用scikit-learn进行特征处理



sklearn.feature_extraction
作用：对字典数据进行特征值化
类： sklearn.feature_extraction.DictVectorizer()
    
```
### 文本特征抽取
```
作用： 对文本数据进行特征值化  # pip3 install jieba
文本处理，情感分析，

sklearn.feature_extraction.text.CountVectorizer()
    CountVectorizer.fit_transform(x)
        x: 文本或者包含文本字符串的可迭代对象
        返回值： 返回sparse矩阵
    CountVectorizer.inverse_transform(x)
        x: array数组或者sparse矩阵
        返回值：转换之前数据格式
    CountVectorizer.get_feature_names()
        返回值：单词列表
 # pip3 install jieba使用
jieba.cut('')
```
### TD-IDF
```
TD-IDF的主要思想是：如果某个词语或短语在一篇文章中出现的频率高，并且在其他文章中很少出现，则认为此词或短语具有很好的类别区分能力，适合用来分类

TD-IDF的作用：用以评估一字词对于一个文件或一个语料库其中一份文件的重要程度

类： sklearn.feature_extraction.text.TfidfVectorizer

TfidfTransformer(stop_words=None, ...)
返回词的权重矩阵
TfidfTransformer.fit_transform(x)
    x: 文本或者包含字符串的可迭代对象
    返回值：返回sparse矩阵
TfidfTransformer.inverse_transform(x)
    x: array数组或者sparse矩阵
    返回值： 转换之前数据格式
TfidfTransformer.get_feature_names()
    返回值：单词列表
```