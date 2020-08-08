import cv2.cv2 as cv
import numpy as np
src=cv.imread("images/dog.jpg")
src=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
dst=cv.adaptiveThreshold(src,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,25,10)
cv.imshow("adaptiveThreshhold",dst)

cv.waitKey(0)