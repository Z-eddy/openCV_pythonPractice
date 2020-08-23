import cv2.cv2 as cv
import numpy as np
src = cv.imread("E:/practice/openCV/material/images/contours.png")
canny = cv.Canny(src, 80, 160)
contours,hierarchy= cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    rotateRect = cv.minAreaRect(contours[i])
    x,y= rotateRect[0]
    x=np.int32(x)
    y= np.int32(y)
    curve = cv.approxPolyDP(contours[i], 4, True)
    vertex = curve.shape[0]
    if vertex == 3:
        cv.putText(src,"Triangle",(x,y),cv.FONT_ITALIC,0.8,(0,0,255))
    elif vertex == 4:
        cv.putText(src,"Rectangle",(x,y),cv.FONT_ITALIC,0.8,(0,0,255))
    elif vertex == 6:
        cv.putText(src,"Polygon",(x,y),cv.FONT_ITALIC,0.8,(0,0,255))
    elif vertex >= 10:
        cv.putText(src,"Cycle",(x,y),cv.FONT_ITALIC,0.8,(0,0,255))

cv.imshow("dst",src)

cv.waitKey(0)
