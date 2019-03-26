import cv2


img = cv2.imread('100.JPG')
dst = cv2.resize(img, (400, 600))
cv2.imwrite('1000.jpg', dst)
