import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)

src=cv.fastNlMeansDenoisingColored(src,None)
cv.imshow("mediaBlur",src)

cv.waitKey(0)
