import os
import cv2
import numpy as np
from scipy import ndimage
'''从中间裁剪并调整图片大小 '''
# def rectify_image(img, resized_shape=(64, 64)):


def rectify_image(img, resized_shape=(32, 32)):
    try:

        # 防止存在灰度图，一般写法：rows,cols=img.shape
        rows, cols = img.shape[0], img.shape[1]
        if(rows <= cols):
            crop_image = img[:, cols // 2 - rows // 2: cols // 2 + rows // 2]
        else:
            crop_image = img[rows // 2 - cols // 2: rows // 2 + cols // 2, :]

        # 调整图片大小
        crop_image = cv2.resize(crop_image, resized_shape)

        return crop_image, True
    except:
        return None, False


def folder_read(base_path, m_label, fname):
    tmp_biaoqian = np.zeros((1, 1), dtype=np.uint8)  # 初始化一个和原图像大小相同的三维数组
    tmp_biaoqian[0] = m_label
    tmp_imr = np.zeros((128, 128, 1), dtype=np.uint8)  # 初始化一个和原图像大小相同的三维数组
    tmp_img = np.zeros((128, 128, 1), dtype=np.uint8)  # 初始化一个和原图像大小相同的三维数组
    tmp_imb = np.zeros((128, 128, 1), dtype=np.uint8)  # 初始化一个和原图像大小相同的三维数组
    tmp_filename = "D:\\Operate_BIN\\cifar128\\" + fname
    fo = open(tmp_filename, "ab")
    #fo = open("D:\\test\\shujuji64\\data_batch_1.bin", "ab")
    #fo = open("D:\\test\\shujuji\\data_batch_1.bin", "ab")
    #fo = open("D:\\test\\shujuji\\data_batch_2.bin", "ab")
    #fo = open("D:\\test\\shujuji\\data_batch_3.bin", "ab")
    #fo = open("D:\\test\\shujuji\\data_batch_4.bin", "ab")
    #fo = open("D:\\test\\shujuji\\data_batch_5.bin", "ab")
    ftest = open("D:\\Operate_BIN\\cifar128\\test_batch.bin", "ab")
    i = 0
    for file in os.listdir(base_path):

        file_path = os.path.join(base_path, file)
        print(file_path)
        read_image = np.array(ndimage.imread(file_path), dtype=np.float32)
        tmp_imr[:, :, 0] = read_image[:, :, 0]
        tmp_img[:, :, 0] = read_image[:, :, 1]
        tmp_imb[:, :, 0] = read_image[:, :, 2]

        xwriter = tmp_imr.reshape(1, 128 * 128)
        lbxwriter = np.insert(xwriter, 0, tmp_biaoqian, axis=1)

        xwriteg = tmp_img.reshape(1, 128 * 128)
        xwriteb = tmp_imb.reshape(1, 128 * 128)

        if i < 500:
            fo.write(lbxwriter)
            fo.write(xwriteg)
            fo.write(xwriteb)

        elif 500 <= i < 600:
            ftest.write(lbxwriter)
            ftest.write(xwriteg)
            ftest.write(xwriteb)

        print(i)
        i = i + 1
    fo.close()
    ftest.close()


# 测试代码
base = "D:\\Operate_BIN\\image\\new1280"
folder_read(base, 0, "data_batch_1.bin")
base = "D:\\Operate_BIN\\image\\new1281"
folder_read(base, 1, "data_batch_2.bin")

base = "D:\\Operate_BIN\\image\\new1282"
folder_read(base, 2, "data_batch_3.bin")
# base = "D:\\Operate_BIN\\image\\new1283pingguo"
# folder_read(base, 3, "data_batch_2.bin")

# base = "D:\\Operate_BIN\\image\\new1284huolongguo"
# folder_read(base, 4, "data_batch_3.bin")
# base = "D:\\Operate_BIN\\image\\new128huanggua"
# folder_read(base, 5, "data_batch_3.bin")

# base = "D:\\Operate_BIN\\image\\new1286lajiao"
# folder_read(base, 6, "data_batch_4.bin")
# base = "D:\\Operate_BIN\\image\\new1287bailuobo"
# folder_read(base, 7, "data_batch_4.bin")

# base = "D:\\Operate_BIN\\image\\new1288_20171218boluo_sxt1"
# folder_read(base, 8, "data_batch_5.bin")
# base = "D:\\Operate_BIN\\image\\new1289_20171220hamigua_sxt1"
# folder_read(base, 9, "data_batch_5.bin")
