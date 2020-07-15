import cv2.cv2 as cv
import numpy as np

src = cv.imread("./images/dog.jpg")
winTitle = "dogImg"
cv.namedWindow(winTitle, cv.WINDOW_AUTOSIZE)
cv.imshow(winTitle, src)
cv.waitKey(0)

# 求取平均值、方差
means, stdDev = cv.meanStdDev(src)
for i in range(len(means)):
    print("平均值:%.2f,方差:%.2f" % (means[i], stdDev[i]))

# 输出黑白色
src1 = cv.split(src)[0]  # 蓝色通道的值
cv.imshow(winTitle, src1)
cv.waitKey(0)
minV, maxV, minLoc, maxLoc = cv.minMaxLoc(src1)
mean = src1.mean()
print(minV, maxV, minLoc, maxLoc)
src1[np.where(src1 >= mean)] = 255
src1[np.where(src1 < mean)] = 0
cv.imshow(winTitle, src1)
cv.waitKey(0)
