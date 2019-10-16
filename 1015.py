import cv2
import numpy as np

img = cv2.imread('1015.png', 0)
gausssian = cv2.GaussianBlur(img, (3, 3), 1)
cv2.imshow('gausssian.png', gausssian)
cv2.imwrite('gausssian.png', gausssian)
cv2.waitKey(0)
