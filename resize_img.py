import cv2


img = cv2.imread('1.jpg')
dst = cv2.resize(img, (960, 720))
cv2.imwrite('1000.jpg', dst)
