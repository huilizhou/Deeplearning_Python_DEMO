import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1015.png', 0)

# _, thresh = cv2.threshold(img, 20, 150, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# edges = cv2.Canny(thresh, 30, 70)
# cv2.imshow('canny', np.hstack((img, thresh, edges)))
# cv2.waitKey(0)

# 固定阈值
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 自适应阈值
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)
titles = ['Original', 'Global(v = 127)', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()
