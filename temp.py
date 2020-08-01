import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)
if True:
    dst=cv.GaussianBlur(src,(3,3),0)
    dst=cv.Laplacian(dst,cv.CV_32F,delta=150)
else:
    dst=cv.Laplacian(src,cv.CV_32F,delta=150)
dst=cv.convertScaleAbs(dst)
cv.imshow("Laplacian",dst)

cv.waitKey(0)