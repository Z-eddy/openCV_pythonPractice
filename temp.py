import cv2.cv2 as cv
import numpy as np

src=cv.imread("E:/openCV/opencv_tutorial/data/images/example.png")
src=cv.UMat(src)
cv.imshow("original",src)
dst=cv.edgePreservingFilter(src,None,1,100,0.4)
cv.imshow("edgePreservingFilter",dst)
cv.waitKey(0)
