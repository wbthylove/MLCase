import jieba  # jieba中文分词库
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import imageio.v2
import numpy as np

mask = imageio.v2.imread('1.jpg')
mask = np.array(mask)
plt.rcParams["font.sans-serif"] = ["SimHei"]


def splitWord():
    with open('表白的话.txt', 'r', encoding='utf-8') as novelFile:
        novel = novelFile.read()
    # print(novel)
    stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
    novelList = list(jieba.lcut(novel))
    novelDict = {}
    # 统计出词频字典
    for word in novelList:
        if word not in stopwords:
            # 不统计字数为一的词
            if len(word) == 1:
                continue
            else:
                novelDict[word] = novelDict.get(word, 0) + 1

    # 对词频进行排序
    novelListSorted = list(novelDict.items())
    novelListSorted.sort(key=lambda e: e[1], reverse=True)

    # 打印前10词频
    topWordNum = 0
    for topWordTup in novelListSorted[:10]:
        print(topWordTup)

    x = [c for c, v in novelListSorted]
    y = [v for c, v in novelListSorted]
    plt.plot(x[:10], y[:10], color='r')
    plt.show()
    return novelDict


def wordCloud():
    # 生成词云图片
    wordcloud = WordCloud(mask=mask, background_color='white', scale=1.5, font_path=r'msyh.ttc').generate(
        ' '.join(splitWord().keys()))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    # 保存图片
    wordcloud.to_file('Confession.jpg')


if __name__ == "__main__":
    wordCloud()
