import cv2 as cv
import numpy as np

# 黄色方块
yelloBlock=np.zeros(shape=[400,400,3],dtype=np.uint8)
yelloBlock[100:200,100:200,1:3]=255
cv.imshow("yelloBlock",yelloBlock)
# 红色方块
redBlock=np.zeros(shape=[400,400,3],dtype=np.uint8)
redBlock[150:250,150:250,2]=255
cv.imshow("redBlock",redBlock)
# and
andSrc=cv.bitwise_and(yelloBlock,redBlock)
cv.imshow("and",andSrc)
# or
orSrc=cv.bitwise_or(yelloBlock,redBlock)
cv.imshow("or",orSrc)
# xor
xorSrc=cv.bitwise_xor(yelloBlock,redBlock)
cv.imshow("xor",xorSrc)
# not
notSrc=cv.imread("./images/dog.jpg")
cv.imshow("originalDog",notSrc)
notSrc=cv.bitwise_not(notSrc)
cv.imshow("not",notSrc)

cv.waitKey(0)
