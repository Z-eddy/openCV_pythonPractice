import cv2.cv2 as cv
import numpy as np
src= cv.imread("images/dog.jpg")
src=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
dst=cv.threshold(src,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
cv.imshow("dst", dst)

cv.waitKey(0)
