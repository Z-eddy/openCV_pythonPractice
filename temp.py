import cv2 as cv
import numpy as np
src = cv.imread("images/dog.jpg")
winTitle = "dogPic"
cv.namedWindow(winTitle, cv.WINDOW_AUTOSIZE)
# clone图片 原图
m1 = np.copy(src)
cv.imshow(winTitle, m1)
cv.waitKey(0)
# 指针赋值 带黄色方块图
m2 = src
# w:100到200 h:200:300 通道(0b,1g,2r):1、2 的元素改色为255
src[100:200, 200:300, 1:3] = 255
cv.imshow(winTitle, m2)
cv.waitKey(0)
# 建立数组 黑色图
m3 = np.zeros(src.shape, src.dtype)
cv.imshow(winTitle, m3)
cv.waitKey(0)
# 建立数组 指定颜色 灰色图
m4 = np.zeros([512, 512], np.uint8)
m4[:, :] = 127  # 所有通道都是127
cv.imshow(winTitle, m4)
cv.waitKey(0)
# 建立数组 指定颜色 蓝色
m5 = np.zeros(shape=[512, 512, 3], dtype=np.uint8) #512*512,3通道,数据类型为uint8
m5[:, :, 0] = 255
cv.imshow(winTitle, m5)
cv.waitKey(0)
