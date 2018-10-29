# 采用图像处理的方式来扩充数据集
# 随机裁剪，由于实际拍摄的图片一般在正中央
# 拟采取的方式是一张大图裁剪4张小图之后再resize

import cv2
import os
for root, dirs, files in os.walk('pai/1/'):
    # print(root)
    # print(dirs)
    # print(files)
    if (files):
        # for item in files:
        #     img = cv2.imread(os.path.join('pai/1', item))
        #     dst = img[0:400, 0:400]
        #     cv2.imwrite('pai/11/' + item + '_dstcrop1.jpg', dst)

        for item in files:
            img = cv2.imread(os.path.join('pai/1', item))
            dst = img[80:480, 0:400]
            cv2.imwrite('pai/11/' + item + '_dstcrop2.jpg', dst)

    print("ok")
