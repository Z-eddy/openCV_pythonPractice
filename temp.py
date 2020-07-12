import cv2 as cv

filePath = "G:/Practice/openCV/images/LUT_test.PNG"
src = cv.imread(filePath)
winTitle = "picTest"
cv.namedWindow(winTitle)
# 原图展示
cv.imshow(winTitle, src)
cv.waitKey(0)
# LUT转换
src = cv.applyColorMap(src, cv.COLORMAP_JET)
cv.imshow(winTitle, src)
cv.waitKey(0)
