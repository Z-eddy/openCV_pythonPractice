import cv2.cv2 as cv
import numpy as np

src=cv.imread("E:/practice/openCV/material/images/llk.jpg")
tpl=cv.imread("E:/practice/openCV/material/images/llk_tpl.png")
dst=cv.matchTemplate(src,tpl,cv.TM_CCORR_NORMED)
cv.imshow("dst",dst)

loc = np.where(dst > 0.95) # 获得坐标的索引
print(loc,'\n\n') # 打印两个array
print(loc[::],'\n\n') # 打印两个array
print(loc[::-1],'\n\n') # 倒着打印两个array
print(*loc[::-1],'\n\n') # 打印两个array转化的列表
print(zip(*loc[::-1]),'\n\n') # 打印两个array转换的列表,然后组合成的Point
h,w=tpl.shape[:2]
for p in zip(*loc[::-1]):
    cv.rectangle(src,p,(p[0]+w,p[1]+h),(0,0,255),1,8,0)
cv.imshow("rectangle",src)

cv.waitKey(0)
