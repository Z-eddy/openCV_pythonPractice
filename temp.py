import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)
# 算子0
kernel0 = np.ones([5, 5], np.float32)/25
dst=cv.filter2D(src,-1,kernel0)
cv.imshow("kernel0",dst)
# 算子1
kernel1=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
],np.float32)
dst=cv.filter2D(src,-1,kernel1)
cv.imshow("kernel1",dst)
# 算子2
kernel2=np.array([
    [1,0],
    [0,-1]
],np.float32)
dst=cv.filter2D(src,-1,kernel2)
cv.convertScaleAbs(dst,dst)
cv.imshow("kernel2",dst)

cv.waitKey(0)
