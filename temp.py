import cv2.cv2 as cv
import numpy as np

src= cv.imread("images/dog.jpg")
# src = cv.UMat(src)
cv.imshow("original",src)
dst=cv.bilateralFilter(src,0,100,5)
h,w=src.shape[:2] # 不支持UMat
result=np.zeros((h,w*2,3),src.dtype)
result[0:h,0:w,:]=src
result[0:h,w:2*w,:]=dst
cv.imshow("result",result)
cv.waitKey(0)
