import cv2.cv2 as cv
import numpy as np

src0=cv.imread("D:/codeSofts/opencv/sources/samples/data/lena.jpg");
src1=cv.imread("D:/codeSofts/opencv/sources/samples/data/lena_tmpl.jpg");
src2=cv.imread("D:/codeSofts/opencv/sources/samples/data/aero1.jpg");
src3=cv.imread("D:/codeSofts/opencv/sources/samples/data/aero3.jpg");

src0=cv.cvtColor(src0,cv.COLOR_BGR2HSV)
src1=cv.cvtColor(src1,cv.COLOR_BGR2HSV)
src2=cv.cvtColor(src2,cv.COLOR_BGR2HSV)
src3=cv.cvtColor(src3,cv.COLOR_BGR2HSV)

src0=cv.calcHist([src0],[0,1],None,[60,64],[0,180,0,256])
src1=cv.calcHist([src1],[0,1],None,[60,64],[0,180,0,256])
src2=cv.calcHist([src2],[0,1],None,[60,64],[0,180,0,256])
src3=cv.calcHist([src3],[0,1],None,[60,64],[0,180,0,256])

cv.normalize(src0,src0,1,0,cv.NORM_MINMAX)
cv.normalize(src1,src1,1,0,cv.NORM_MINMAX)
cv.normalize(src2,src2,1,0,cv.NORM_MINMAX)
cv.normalize(src3,src3,1,0,cv.NORM_MINMAX)

v01=cv.compareHist(src0,src1,cv.HISTCMP_CORREL)
v23=cv.compareHist(src2,src3,cv.HISTCMP_CORREL)
print(v01,v23)

v01=cv.compareHist(src0,src1,cv.HISTCMP_BHATTACHARYYA)
v23=cv.compareHist(src2,src3,cv.HISTCMP_BHATTACHARYYA)
print(v01,v23)