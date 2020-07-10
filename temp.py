import cv2
src = cv2.imread("./images/dog.jpg")
cv2.imshow("picture", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
