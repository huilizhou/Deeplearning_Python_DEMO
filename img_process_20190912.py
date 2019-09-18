import cv2
import numpy as np
import matplotlib.pyplot as plt
# 灰度图读入
img = cv2.imread('0011_apple.jpg', 0)

# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()

# 阈值分割
ret, th = cv2.threshold(img, 150, 180, cv2.THRESH_BINARY)
cv2.imshow('thresh', th)
cv2.waitKey(0)
