import cv2.cv2 as cv
import numpy as np
src = cv.imread("images/dog.jpg")
src = cv.UMat(src)
# robert_x
robert_x = np.array(
    [[1, 0],
     [0, -1]],
    dtype=np.float32)
dst = cv.filter2D(src, cv.CV_16S, robert_x)
dst=cv.convertScaleAbs(dst)
cv.imshow("robertX", dst)
# robert_y
robert_y = np.array(
    [[0, 1],
    [-1, 0]],
    dtype=np.float32)
dst = cv.filter2D(src,cv.CV_16S,robert_y)
dst=cv.convertScaleAbs(dst)
cv.imshow("robertY", dst)
# prewitt_x
prewitt_x=np.array(
    [ [-1,0,1],
    [-1,0,1],
    [-1,0,1] ],
    dtype=np.float32
)
dst=cv.filter2D(src,cv.CV_32F,prewitt_x)
dst = cv.convertScaleAbs(dst)
cv.imshow("prewitt_x", dst)
# prewitt_y
prewitt_y=np.array(
    [ [-1,-1,-1],
    [0,0,0],
    [1,1,1] ],
    dtype=np.float32
)
dst = cv.filter2D(src,cv.CV_32F,prewitt_y)
dst=cv.convertScaleAbs(dst)
cv.imshow("prewitt_y", dst)

cv.waitKey(0)
