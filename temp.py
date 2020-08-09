import cv2.cv2 as cv
import numpy as np
src=cv.imread("E:/practice/openCV/material/images/coins.jpg")
# src=cv.blur(src,(3,3))
src=cv.pyrMeanShiftFiltering(src,10,100)
src=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
val,dst= cv.threshold(src,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
cv.imshow("dst", dst)

cv.waitKey(0)
