import cv2.cv2 as cv
import numpy as np

src = cv.imread("E:/practice/openCV/material/images/stuff.jpg")
canny = cv.Canny(src, 80, 160)
k=cv.getStructuringElement(cv.MORPH_RECT,(3,3)) # 膨胀需要的
dilate=cv.dilate(canny,k)
contours,hierarchy=cv.findContours(dilate,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    rect=cv.minAreaRect(contours[i])
    box=cv.boxPoints(rect)
    box=np.int0(box)
    cv.drawContours(src,[box],0,(0,0,255),1)
cv.imshow("dst",src)

cv.waitKey(0)
