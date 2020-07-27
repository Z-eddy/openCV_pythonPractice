import cv2.cv2 as cv
import numpy as np
src=cv.imread("images/dog.jpg")
src=cv.UMat(src)
dst=cv.pyrMeanShiftFiltering(src,15,30)
cv.imshow("result", dst)
cv.waitKey(0)