import cv2.cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def image_hist(src):
    color=("blue","green","red")
    for key,value in enumerate(color):
        hist=cv.calcHist([src],[key],None,[256],[0,256])
        plt.plot(hist,value)
    plt.show()

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)
image_hist(src)