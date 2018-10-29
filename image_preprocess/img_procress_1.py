import cv2

img = cv2.imread('higher.jpg')
res = cv2.resize(img, (224, 224))
img2 = cv2.imread('lower.jpg')
res2 = cv2.resize(img2, (224, 224))

# cv2.imshow('zoom', res)
cv2.imwrite('z1.jpg', res)
cv2.imwrite('z2.jpg', res2)
cv2.waitKey(0)
