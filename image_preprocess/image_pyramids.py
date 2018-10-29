import cv2

img = cv2.imread('20171202174028.jpg')
lower = cv2.pyrDown(img)
higher = cv2.pyrUp(img)

cv2.imshow('lower', lower)
cv2.imshow('higher', higher)
cv2.imwrite('lower.jpg', lower)
cv2.imwrite('higher.jpg', higher)
cv2.waitKey(0)
