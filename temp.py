import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
integralDst=cv.integral(src) # 图像积分
for i in range(3):
    val=integralDst[15][15][i]
    print(val)