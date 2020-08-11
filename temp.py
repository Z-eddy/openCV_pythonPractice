import cv2.cv2 as cv
import numpy as np
src = cv.imread("E:/practice/openCV/material/images/rice.png")
cv.imshow("origianl",src)
gaussian = cv.GaussianBlur(src, (3, 3), 0)
gray = cv.cvtColor(gaussian, cv.COLOR_BGR2GRAY)
n,thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
nums,labels,status,centers=cv.connectedComponentsWithStats(thresh)
dst=src.copy()
for i in range(1, nums, 1):
    cx,cy=centers[i]
    cv.circle(dst,(np.int32(cx),np.int32(cy)),2,(0,255,0),-1) # 绘制圆心
    x,y,w,h,area=status[i]
    cv.rectangle(dst,(x,y),(x+w,y+h),(0,255,0))
    cv.putText(dst,"index:"+str(i),(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)

cv.imshow("dst",dst)

cv.waitKey(0)
