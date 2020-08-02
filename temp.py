import cv2.cv2 as cv
import numpy as np

src = cv.imread("images/dog.jpg")
sharpenAlgorithm = np.array([
        [0, -1, 0],
        [-1, 4.5, -1],
        [0, -1, 0]
    ], dtype=np.float32)
dst=cv.filter2D(src,cv.CV_32F,sharpenAlgorithm)
dst=cv.convertScaleAbs(dst)
cv.imshow("sharpen", dst)

cv.waitKey(0)
