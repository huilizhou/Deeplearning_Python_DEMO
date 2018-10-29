import cv2
import os

for root, dirs, files in os.walk("pai/0/"):

    if (files):
        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = cv2.flip(img, -1)
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite("pai/00/" + item.split('.jpg')[0] + '_filp.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = cv2.flip(img, 0)
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite('pai/00/' + item.split('.jpg')[0] + '_hflip.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = cv2.flip(img, 1)
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite('pai/00/' + item.split('.jpg')[0] + '_vflip.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = img[0:400, 0:400]
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite('pai/00/' + item.split('.jpg')[0] + 'crop0.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = img[0:400, 240:640]
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite('pai/00/' + item.split('.jpg')[0] + 'crop1.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = img[80:480, 0:400]
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite('pai/00/' + item.split('.jpg')[0] + 'crop2.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/0', item))
            dst = img[80:480, 240:640]
            dst = cv2.resize(dst, (224, 224))
            cv2.imwrite('pai/00/' + item.split('.jpg')[0] + 'crop3.jpg', dst)

    print("OK")
