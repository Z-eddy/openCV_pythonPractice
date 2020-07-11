import cv2
matSrc = cv2.imread("images/dog.jpg")
cv2.namedWindow("picture", cv2.WINDOW_AUTOSIZE)
cv2.imshow("picture", matSrc)
cv2.waitKey(0)
cv2.destroyAllWindows()
