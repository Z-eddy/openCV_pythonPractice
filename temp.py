import cv2.cv2  as cv
import numpy as np
src=cv.imread("E:/practice/openCV/material/images/rice.png") # 获得原图
cv.imshow("original",src)
src=cv.GaussianBlur(src,(3,3),0) # 高斯滤波
gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY) # 灰度图转换
val,threshold=cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU) # 阈值分割
num,labs=cv.connectedComponents(threshold) # 寻找到的数量,分布图
colors=[]
for i in range(num):
    b=np.random.randint(20,255)
    g=np.random.randint(20,255)
    r=np.random.randint(20,255)
    colors.append((b,g,r))
colors[0]=(0,0,0)

dst=np.zeros(src.shape,src.dtype)
h,w=dst.shape[:2] # 如果是gray的图则无需[:2],因为没有第三个通道参数
for i in range(h):
    for j in range(w):
        dst[i,j]=colors[labs[i,j]]
cv.putText(dst, "find nums:"+str(num-1), (20, 50), cv.FONT_ITALIC, 1.0, (0, 0, 255))
cv.imshow("dst",dst)

cv.waitKey(0)
