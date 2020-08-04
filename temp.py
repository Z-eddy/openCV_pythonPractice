import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)
temp0=cv.pyrDown(src) # 先reduce
h,w=src.shape[:2]
temp1=cv.pyrUp(temp0,dstsize=(w,h)) # 然后expand
laplacian=cv.subtract(src,temp1) #计算拉普拉斯金字塔
cv.imshow("laplacian",laplacian)
dst=cv.add(temp1,laplacian) # 拉普拉斯+expand还原模糊图像
cv.imshow("revert",dst)

cv.waitKey(0)
