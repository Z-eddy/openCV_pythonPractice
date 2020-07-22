import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)

src=cv.blur(src,(3,3))
cv.imshow("卷积后",src)

cv.waitKey(0)
