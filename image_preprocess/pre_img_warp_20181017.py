import cv2
import os


for root, dirs, files in os.walk('pai/1/'):
    # print(root)
    # print(dirs)
    # print(files)
    if (files):
        for item in files:
            img = cv2.imread(os.path.join('pai/1', item))
            rows, cols = img.shape[:2]
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 15, 1.2)
            dst = cv2.warpAffine(img, M, (cols, rows))
            cv2.imwrite('pai/11/' + item + '_warp.jpg', dst)
