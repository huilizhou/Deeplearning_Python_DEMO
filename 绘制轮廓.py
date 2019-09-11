import cv2
import numpy as np
import matplotlib.pyplot as plt
# 加载灰度图
img = cv2.imread('yuantu1.jpg', 0)
cv2.namedWindow('lunkuo', cv2.WINDOW_NORMAL)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
ret, th = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
cv2.imshow('lunkuo', th)
cv2.waitKey(0)
