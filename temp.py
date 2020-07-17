import cv2.cv2 as cv
import numpy as np

video = cv.VideoCapture(
    r"D:\codeSofts\opencv\opencv\sources\samples\data\vtest.avi")
width = video.get(cv.CAP_PROP_FRAME_WIDTH)
height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv.CAP_PROP_FPS)

# writer=cv.VideoWriter("videoDemo.mp4",cv.CAP_PROP_FOCUS,fps,(np.int(width),np.int(height)),True)
writer = cv.VideoWriter("./videoDemo.mp4", cv.CAP_PROP_FOCUS,
                        fps, (np.int(width), np.int(height)), True)
while True:
    ok, frame = video.read()
    if ok:
        writer.write(frame)
    else:
        break

video.release()
writer.release()
