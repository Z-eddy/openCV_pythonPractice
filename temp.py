import cv2 as cv
import time
fileName = "images/dog.jpg"
src = cv.imread(fileName)
winTitle = "dogPic"
cv.namedWindow(winTitle, cv.WINDOW_AUTOSIZE)
cv.imshow(winTitle, src)
cv.waitKey(0)
row, col, chn = src.shape
start = time.perf_counter_ns()
for i in range(row):
    for j in range(col):
        b, g, r = src[i, j]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        src[i, j] = [b, g, r]
print(time.perf_counter_ns() - start)
cv.imshow(winTitle, src)
cv.waitKey(0)
