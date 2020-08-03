import cv2.cv2 as cv
import numpy as np
src=cv.imread("images/dog.jpg")
pyrDownDst=cv.pyrDown(src)
cv.imshow("pyrDown",pyrDownDst)
pyrUpDst=cv.pyrUp(pyrDownDst)
cv.imshow("pyrUp",pyrUpDst)

cv.waitKey(0)