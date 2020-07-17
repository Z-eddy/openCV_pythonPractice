import cv2.cv2 as cv
import numpy as np

src = cv.imread("./images/dog.jpg")
cv.imshow("original", src)

# 转为灰度图(1通道)
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src = np.float32(src)


# MINMAX归一化
dst = np.zeros(src.shape, np.float32)
cv.normalize(src, dst, 1, 0, cv.NORM_MINMAX)
dst *= 255
dst = np.uint8(dst)
cv.imshow("MINMAX", dst)

# INF归一化
dst = np.zeros(src.shape, np.float32)  # Python每次需要手动去初始化!
cv.normalize(src, dst, 1, 0, cv.NORM_INF)
dst *= 255
dst = np.uint8(dst)
cv.imshow("INF", dst)

# L1归一化
dst = np.zeros(src.shape, np.float32)
cv.normalize(src, dst, 1, 0, cv.NORM_L1)
dst = np.uint8(dst*10000000)
cv.imshow("L1", dst)

# L2归一化
dst = np.zeros(src.shape, np.float32)
cv.normalize(src, dst, 1, 0, cv.NORM_L2)
dst = np.uint8(dst*10000)
cv.imshow("L2", dst)

cv.waitKey(0)
