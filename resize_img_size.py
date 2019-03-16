import cv2
import os
import numpy as np

for root, dirs, files in os.walk(r"C:\Users\huili\Desktop\Capture"):
    # print(root)
    # print(dirs)
    # print(files)
    if(files):
        for item in files:
            img = cv2.imread(os.path.join(
                r"C:\Users\huili\Desktop\Capture", item))
            # height, width, deep = img.shape
            dst = img[0:720, 560:1280]
            cv2.imwrite(os.path.join(root, item), dst)
