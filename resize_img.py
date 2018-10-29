import cv2


img = cv2.imread('1.jpg')
dst = cv2.resize(img, (640, 480))
cv2.imwrite('dst.jpg', dst)
