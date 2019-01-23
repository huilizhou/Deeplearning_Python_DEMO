import cv2


img = cv2.imread('00000.png')
dst = cv2.resize(img, (960, 720))
cv2.imwrite('000.png', dst)
