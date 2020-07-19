import cv2.cv2 as cv
import numpy as np

src = cv.imread("G:/Practice/openCV/images/TinyGreen.PNG")
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)  # hsv
mask = cv.inRange(hsv, (36, 43, 46), (99, 255, 255))  # 掩膜
blueBg = np.zeros(src.shape, src.dtype)
blueBg[:, :, 0] = 255
dst = cv.bitwise_and(blueBg, blueBg, src, mask)
cv.imshow("dst", dst)

cv.waitKey(0)
