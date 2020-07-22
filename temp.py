import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)

src=cv.blur(src,(5,5))
cv.imshow("blur",src)
src=cv.GaussianBlur(src,(5,5),0,15)
cv.imshow("gaussianBlur",src)

cv.waitKey(0)
