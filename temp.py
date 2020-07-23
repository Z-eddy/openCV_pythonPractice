import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)

src=cv.medianBlur(src,3)
cv.imshow("mediaBlur",src)

cv.waitKey(0)
