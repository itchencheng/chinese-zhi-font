#coding:utf-8
import os
import sys
import cv2
import numpy as np
# https://blog.csdn.net/qq_40414818/article/details/84349232
import matplotlib.pyplot as plt


class Seperator():
    def __init__(self):
        pass

class ProjectionSeperator(Seperator):
    def __init__(self):
        print("construct")
    
    def process(self, image_path):
        print(image_path)
        img = cv2.imread(image_path, 0)
        print(img.size)
        print(img.shape)
        h = img.shape[0]
        w = img.shape[1]
        print(h, w)
        vert_array = np.zeros(h)
        hori_array = np.zeros(w)

        threshold = 100
        for i in range(h):
            print(i)
            for j in range(w):
                #print("value={}".format(img[i][j]))
                if (img[i][j] < threshold):
                    #print("({}, {}) + 1".format(i, j))
                    vert_array[i] += 1
                    hori_array[j] += 1
        print("hello")
        plt.plot(range(h), vert_array)
        plt.plot(range(w), hori_array)
        plt.show()


def main():
    file_path = sys.argv[1]

    project = ProjectionSeperator()
    project.process(file_path)


if __name__ == "__main__":
    main()
