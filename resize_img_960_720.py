import cv2
import os
import numpy as np

for root, dirs, files in os.walk(r"C:\Users\huili\Desktop\segtest\JPEGImages"):
    if(files):
        for item in files:
            img = cv2.imread(os.path.join(
                r"C:\Users\huili\Desktop\segtest\JPEGImages", item))
            # height, width, deep = img.shape
            dst = cv2.resize(img, (960, 720))
            cv2.imwrite(os.path.join(root, item), dst)
