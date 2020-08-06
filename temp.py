import cv2.cv2 as cv
import numpy as np
src=cv.imread("images/dog.jpg")
src=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
t=127
row,col=src.shape[:2]
for i in range(row):
    for j in range(col):
        val= src[i, j]
        if(val>t):
            src[i, j]=255
        else :
            src[i, j]=0

cv.imshow("dst",src)

cv.waitKey(0)
