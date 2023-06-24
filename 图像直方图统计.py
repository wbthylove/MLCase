import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot3():
    img = cv.imread('beautifulgirl.jpg', 1)
    # print(img.shape)
    # img_np = np.array(img)
    plt.hist(img.reshape([-1]), 256, [0, 256]);
    plt.show()

def plt2():
    img = cv.imread('beautifulgirl.jpg', 1)
    histr = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr, color='b')
    plt.xlim([0, 256])
    plt.show()


def plt1():
    img = cv.imread('beautifulgirl.jpg', 1)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        # hist是一个shape为(256,1)的数组，表示0-255每个像素值对应的像素个数，下标即为相应的像素值
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


def main():
    img = cv.imread('beautifulgirl.jpg', 0)
    # 得到计算灰度直方图的值
    n = np.array(img)
    xy = xygray(img)

    # 画出灰度直方图
    x_range = range(256)
    plt.plot(x_range, xy, "r", linewidth=2, c='black')
    # 设置坐标轴的范围
    y_maxValue = np.max(xy)
    plt.axis([0, 255, 0, y_maxValue])
    # 设置坐标轴的标签
    plt.xlabel('gray Level')
    plt.ylabel("number of pixels")
    plt.show()


def xygray(img):
    # 得到高和宽
    rows, cols = img.shape
    print(img.shape)
    # 存储灰度直方图
    xy = np.zeros([256], np.uint64)
    for r in range(rows):
        for c in range(cols):
            xy[img[r][c]] += 1
    # 返回一维ndarry
    print(xy.sum())
    return xy


if __name__ == "__main__":

    main()