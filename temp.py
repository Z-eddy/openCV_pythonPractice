import cv2 as cv
import numpy as np
src = cv.imread("G:/Practice/openCV/images/TinyGreen.PNG")
res = cv.cvtColor(src, cv.COLOR_BGR2YUV)
cv.imshow("YUV", res)  # YUV
res = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
cv.imshow("YCrCb", res)  # YCrCb
res = cv.cvtColor(src, cv.COLOR_BGR2HSV)
cv.imshow("HSV", res)  # HSV

res = cv.inRange(res, (35, 43, 46), (77, 255, 255))  # 二值化
cv.imshow("inRange", res)

res = cv.cvtColor(res, cv.COLOR_GRAY2BGR)  # 灰度图转换3通道
res = cv.add(src, res)  # 抠图
cv.imshow("final", res)

cv.waitKey(0)
