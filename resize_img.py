import cv2


img = cv2.imread(r"C:\Users\huili\Desktop\Deeplearning_Python_DEMO\huilir.jpg")
# dst = img[120:360, 160:480]
dst = cv2.resize(img, (354, 472))
cv2.imwrite('p.jpg', dst)
