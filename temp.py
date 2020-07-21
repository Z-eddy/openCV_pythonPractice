import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)

chanls=cv.split(src)
for i in range(3):
    chanls[i]=cv.equalizeHist(chanls[i])
dst=cv.merge(chanls)
cv.imshow("equalizeHist",dst)

cv.waitKey(0)
