import cv2.cv2 as cv
import numpy as np
image=cv.imread(r"E:\practice\openCV\material\images\target.png")
cv.imshow("original",image)
theModel=cv.imread(r"E:\practice\openCV\material\images\sample.png")
# 颜色空间转换
image=cv.cvtColor(image,cv.COLOR_BGR2HSV)
theModel=cv.cvtColor(theModel,cv.COLOR_BGR2HSV)
# 计算model直方图,180/30,256/32
roiHist=cv.calcHist([theModel],(0,1),None,(30,32),(0,180,0,256))
# 归一化
roiHist=cv.normalize(roiHist,roiHist,255,0,cv.NORM_MINMAX)
# 计算直方图反向投影
dst=cv.calcBackProject([image],(0,1),roiHist,(0,180,0,256),1)
cv.imshow("result",dst)

cv.waitKey(0)