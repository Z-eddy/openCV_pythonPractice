import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
canny=cv.Canny(src,100,200)
contours,hierarchy=cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv.drawContours(src,contours, i,(0,0,255))

cv.imshow("dst",src)

cv.waitKey(0)
