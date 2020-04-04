import cv2
import os
import numpy as np

for root, dirs, files in os.walk(r"C:\Users\huili\Desktop\1"):
    # print(root)
    # print(dirs)
    print(files)
    if(files):
        for item in files:
            print(item)
            img = cv2.imread(os.path.join(
                r"C:\Users\huili\Desktop\1", item))
            # height, width, deep = img.shape
            dst = cv2.resize(img, (640, 480))
            cv2.imwrite(os.path.join(root, item), dst)
