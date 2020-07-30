import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
src=cv.UMat(src)
xDst=cv.Sobel(src,cv.CV_32F,1,0)
xDst=cv.convertScaleAbs(xDst)
cv.imshow("xDst",xDst)
yDst = cv.Sobel(src,cv.CV_32F,0,1)
yDst = cv.convertScaleAbs(yDst)
cv.imshow("yDst",yDst)

dst=cv.add(xDst,yDst,dtype=cv.CV_16S)
dst=cv.convertScaleAbs(dst)
cv.imshow("dst",dst)

cv.waitKey(0)
