import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)
gaussian=cv.GaussianBlur(src,(3,3),5)
dst = cv.addWeighted(src, 1.5, gaussian, -0.5, 0)
cv.imshow("USM",dst)

cv.waitKey(0)
