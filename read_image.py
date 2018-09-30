import numpy as np
import os
from PIL import Image

# root_dir="C:/Users/sh/Desktop/data"
root_dir = "C:/Users/huili/Desktop/fruitdatas"
image_folders = os.listdir(root_dir)
floders_num = 0
for i in image_folders:
    image_list = os.listdir(root_dir + '/' + i)
    for j in image_list:
        # if os.path.splitext(j)[1] != ".png":
        if os.path.splitext(j)[1] != ".jpg":
            image_list.remove(j)
        else:
            pass
    print(len(image_list))
    image = np.zeros((len(image_list), 480, 640, 3))
    num = 0
    for j in image_list:
        im = Image.open(root_dir + '/' + i + '/' + j)
        # print(np.shape(np.array(im)))
        image[num, :, :, :] = np.array(im)
        num = num + 1
    np.save('image/' + image_folders[floders_num] + '.npy', image)
    floders_num = floders_num + 1
    print(np.shape(image))

print('finish')
