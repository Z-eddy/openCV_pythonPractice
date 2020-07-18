import cv2.cv2 as cv
import numpy as np

dst=np.zeros((400,400,3),np.uint8)
cv.line(dst,(100,100),(200,200),(255,0,0),1)
cv.rectangle(dst,(200,200),(300,300),(0,0,255),-1)
cv.imshow("test",dst)
cv.waitKey(0)