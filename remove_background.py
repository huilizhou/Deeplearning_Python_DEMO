import numpy as np
import cv2

img = cv2.imread('1.png', 0)

_, thresh = cv2.threshold(img, 20, 150, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)
cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)
# edges = cv2.Canny(img, 30, 70)  # canny边缘检测
# cv2.imshow('canny', np.hstack((img, edges)))
# cv2.waitKey(0)
