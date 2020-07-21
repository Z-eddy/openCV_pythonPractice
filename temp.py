import cv2.cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 使用函数批量解析
def image_hist(img):
    color=("blue","green","red")
    for key,value in enumerate(color):
        hist=cv.calcHist([img],[key],None,[256],[0,256])
        plt.plot(hist,value)
    plt.show()

src=cv.imread("images/dog.jpg")
image_hist(src)
'''
# 手动解析
bHist=cv.calcHist([src],[0],None,[256],[0,256])
gHist=cv.calcHist([src],[1],None,[256],[0,256])
rHist=cv.calcHist([src],[2],None,[256],[0,256])
plt.plot(bHist,"blue")
plt.plot(gHist,"green")
plt.plot(rHist,"red")
plt.show()
'''
