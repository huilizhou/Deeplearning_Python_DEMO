import cv2
import numpy as np

img1 = cv2.imread('h0.jpg')
img2 = cv2.imread('y0.jpg')


dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow("dst", dst)
cv2.imwrite("ds.jpg", dst)
cv2.waitKey(0)
