# 采用opencv的方式来扩充数据集20181016
# 水平翻转和左右翻转。cv2.flip(img,1)
# 其中参数2 =0；垂直翻转(沿x轴)，参数2>0；水平翻转(沿y轴)，参数2<0；水平垂直翻转。
import cv2
import os


for root, dirs, files in os.walk('pai/1/'):
    # print(root)
    # print(dirs)
    # print(files)
    if (files):
        for item in files:
            img = cv2.imread(os.path.join('pai/1', item))
            dst = cv2.flip(img, -1)
            cv2.imwrite('pai/11/' + item + '_filp.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/1', item))
            dst = cv2.flip(img, 0)
            cv2.imwrite('pai/11/' + item + '_hfilp.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/1', item))
            dst = cv2.flip(img, 1)
            cv2.imwrite('pai/11/' + item + '_vfilp.jpg', dst)
