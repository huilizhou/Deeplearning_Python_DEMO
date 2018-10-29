# 将一副图片裁剪成4份后，随机抽取。做data-agumentia

import cv2

img = cv2.imread("20181021105645.jpg")
# print(img.shape[0], img.shape[1])
dst1 = img[0:224, 0:224]
dst2 = img[0:400, 240:640]
dst3 = img[80:480, 0:400]
dst4 = img[80:480, 240:640]
# cv2.imshow("1", dst1)
# cv2.imshow('2', dst2)
# cv2.imshow('3', dst3)
# cv2.imshow('4', dst4)
# dst1 = cv2.resize(dst1, (224, 224))
cv2.imwrite('dst1.jpg', dst1)

cv2.waitKey(0)
