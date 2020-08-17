import cv2.cv2 as cv
import numpy as np
src= cv.imread("E:/practice/openCV/material/images/zhifang_ball.png")
cv.imshow("src",src)
gauss= cv.GaussianBlur(src,(3,3),0)
canny=cv.Canny(src,100,200)
k=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
dilate=cv.dilate(canny,k)
contours,hierarchy=cv.findContours(dilate,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    theArea=cv.contourArea(contours[i])
    theArcLength=cv.arcLength(contours[i],True)
    if theArea<100 or theArcLength<100:
        continue
    rect=cv.minAreaRect(contours[i])
    x,y= rect[0]
    box=cv.boxPoints(rect)
    box=np.int0(box)
    cv.drawContours(src,[box],0,(0,0,255))
    cv.circle(src,(np.int32(x),np.int32(y)),2,(255,0,0),-1)
cv.imshow("dst",src)

cv.waitKey(0)
