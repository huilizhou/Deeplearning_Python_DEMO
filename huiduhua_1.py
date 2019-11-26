import cv2

img = cv2.imread('t1.png', 0)

cv2.imwrite('t2.png', img)
