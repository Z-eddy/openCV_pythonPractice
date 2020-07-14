import cv2 as cv
import numpy as np

src = cv.imread("images/dog.jpg")
winTitle = "dogPic"
cv.namedWindow(winTitle, cv.WINDOW_AUTOSIZE)
cv.imshow(winTitle, src)  # 原图显示
cv.waitKey(0)

# 分别打印BGR通道置零时的图片
for i in range(3):
    mv = cv.split(src)
    mv[i][:, :] = 0
    rst = cv.merge(mv)
    cv.imshow(winTitle, rst)
    cv.waitKey(0)
