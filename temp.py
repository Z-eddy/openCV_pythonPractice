import cv2.cv2 as cv
import numpy as np

src=cv.imread("images/dog.jpg")
cv.imshow("original",src)

w,h=src.shape[:2]
size=(np.int(w*0.75),np.int(h*0.75))

dst=cv.resize(src,size,0,0,cv.INTER_NEAREST)
cv.imshow("NEARST",dst)

dst=cv.resize(src,size,0,0,cv.INTER_LINEAR)
cv.imshow("LINEAR",dst)

dst=cv.resize(src,size,0,0,cv.INTER_CUBIC)
cv.imshow("CUBIC",dst)

dst=cv.resize(src,size,0,0,cv.INTER_LANCZOS4)
cv.imshow("LANCZOS4",dst)

cv.waitKey(0)