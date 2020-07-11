import cv2
# 读取并显示原始图片
src = cv2.imread("images/dog.jpg")
winTitle = "dogPic"
cv2.namedWindow(winTitle, cv2.WINDOW_AUTOSIZE)
cv2.imshow(winTitle, src)
cv2.waitKey(0)
# 转换并显示灰度图
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow(winTitle, gray)
cv2.waitKey(0)
# 保存转换的灰度图
filePath = "images/grayDog.jpg"
ok = cv2.imwrite(filePath, gray)
if ok:
    print("图片生成完毕")
else:
    print("图片生成失败")

cv2.destroyAllWindows()
