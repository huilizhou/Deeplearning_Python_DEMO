import os
import cv2

root_dir = r"C:\Users\huili\Desktop\image_preprocess\pai\1"
save_dir = r"C:\Users\huili\Desktop\image_preprocess\pai\11"

for root, dirs, files in os.walk(root_dir):
    if (files):
        for item in files:
            img = cv2.imread(os.path.join(root_dir, item))
            dst = cv2.resize(img, (224, 224))
            cv2.imwrite(root_dir + item.split('.jpg')[0] + 'new.jpg', dst)
