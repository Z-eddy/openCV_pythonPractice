import cv2.cv2 as cv
import numpy as np
src=cv.imread("images/dog.jpg")
dst=cv.Canny(src,100,300)
cv.imshow("Canny", dst)

cv.waitKey(0)
