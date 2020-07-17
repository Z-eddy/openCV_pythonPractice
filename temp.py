import cv2.cv2 as cv
import numpy as np

src=cv.imread("./images/dog.jpg")
cv.imshow("original",src)

dst=cv.flip(src,0)
cv.imshow("x",dst)

dst=cv.flip(src,1)
cv.imshow("y",dst)

dst=cv.flip(src,-1)
cv.imshow("xy",dst)

cv.waitKey(0)
