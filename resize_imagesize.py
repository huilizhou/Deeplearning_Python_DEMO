import cv2
import os
import numpy as np

for root, dirs, files in os.walk(r"C:\Users\huili\Desktop\goodstu"):
    # print(root)
    # print(dirs)
    # print(files)
    if(files):
        for item in files:
            img = cv2.imread(os.path.join(
                r"C:\Users\huili\Desktop\goodstu", item))
            # height, width, deep = img.shape
            print(img.shape[0])
            if (img.shape[0] > 3600):
                dst = cv2.resize(img, None, fx=0.25, fy=0.25)
                cv2.imwrite(os.path.join(root, item), dst)
            elif(img.shape[0] >= 1800 and img.shape[0] <= 3600):
                dst = cv2.resize(img, None, fx=0.5, fy=0.5)
                cv2.imwrite(os.path.join(root, item), dst)
            else:
                dst = img
