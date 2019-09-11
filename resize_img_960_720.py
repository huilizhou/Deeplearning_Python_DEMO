import cv2
import os
import numpy as np

for root, dirs, files in os.walk(r'I:\rivertest\SegmentationClassRaw'):
    if(files):
        for item in files:
            img = cv2.imread(os.path.join(
                r'I:\rivertest\SegmentationClassRaw', item))
            # height, width, deep = img.shape
            dst = cv2.resize(img, (476, 270))
            cv2.imwrite(os.path.join(root, item), dst)
