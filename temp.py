import cv2 as cv
import numpy as np

pathRoot = "F:/Code/openCV/opencv/sources/samples/data/"
img0 = pathRoot + "WindowsLogo.jpg"
img1 = pathRoot + "LinuxLogo.jpg"
src0 = cv.imread(img0)
src1 = cv.imread(img1)
cv.imshow("img0", src0)
cv.imshow("img1", src1)

result = np.zeros(src1.shape, src1.dtype)
# result[100:200,50:250,:]=127
# cv.imshow("result",result)
cv.add(src0, src1, result)
cv.imshow("add", result)

cv.subtract(src0, src1, result)
cv.imshow("subtract", result)

cv.multiply(src0, src1, result)
cv.imshow("multiply", result)

cv.divide(src0, src1, result)
cv.imshow("divide", result)

cv.waitKey(0)
