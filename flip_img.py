import cv2

img = cv2.imread('pingguo1.jpg')
rows, cols = img.shape[:2]
# dst = cv2.flip(img, 0)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 15, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('p_4.jpg', dst)
