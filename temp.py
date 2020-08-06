import cv2.cv2 as cv
import numpy as np

src= cv.imread("C:/Users/Zr/Desktop/temp/test.png")
returnVal,dst=cv.threshold(src,127,255,cv.THRESH_BINARY) # python会有2个返回值,第一个是阈值大小
cv.imshow("BINARY",dst)

cv.waitKey(0)