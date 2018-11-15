import os
import cv2

'''从中间裁剪并调整图片大小 '''
# def rectify_image(img, resized_shape=(128, 128)):


def rectify_image(img, resized_shape=(224, 224)):
    # def rectify_image(img, resized_shape=(32, 32)):
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


def folder_rectiry(base_path):
    generate_folder = os.path.join(os.path.dirname(
        base_path), 'new128' + os.path.basename(base_path))

    # 文件路径不存在，则创建该文件夹
    if(not os.path.exists(generate_folder)):
        os.makedirs(generate_folder)

    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)
        # print(file_path)

        image = cv2.imread(file_path)
        img, result = rectify_image(image)
        if result:
            print(os.path.join(generate_folder, file))
            cv2.imwrite(os.path.join(generate_folder, file), img)


# 测试代码
# base = "D:\\test\\chenbuhuotu\\0_20171202dz"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\1_20171202xj"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\2_20171203juzi"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\3_20171203mht"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\4_20171204pg"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\5_20121209hlg"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\6_20171210putao"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\7_20171217caomei_sxt1"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\8_20171218boluo_sxt1"
# folder_rectiry(base)
# base = "D:\\test\\chenbuhuotu\\9_20171220hamigua_sxt1"
# folder_rectiry(base)


base = "C:\\Users\\huili\\Desktop\\Make_dataset\\5huanggua"
folder_rectiry(base)
base = "C:\\Users\\huili\\Desktop\\Make_dataset\\6lajiao"
folder_rectiry(base)
base = "C:\\Users\\huili\\Desktop\\Make_dataset\\7bailuobo"
folder_rectiry(base)
