import random
import os
import numpy as np


# 将按顺序写入的训练数组置软
zlshuzhutrain = random.sample(range(800), 800)

# 将按顺序写入的测试置软
zlshuzhutest = random.sample(range(200), 200)


############################################################
# 读取按顺序存储的文件
###########################################################

# tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\train_0.bin"
# data1 = np.fromfile(tmp_filename, dtype=np.int32)
# # print(data1.shape)
# data1 = data1.reshape(400, 224 * 224 * 9 + 1)
# # print(data1.shape)
# tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\train_1.bin"
# data2 = np.fromfile(tmp_filename, dtype=np.int32)
# data2 = data2.reshape(400, 224 * 224 * 9 + 1)


# dataquan = np.concatenate((data1, data2), axis=0)  # 函数


tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\test_0.bin"
datatest1 = np.fromfile(tmp_filename, dtype=np.int32)
datatest1 = datatest1.reshape(100, 224 * 224 * 9 + 1)

tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\test_1.bin"
datatest2 = np.fromfile(tmp_filename, dtype=np.int32)
datatest2 = datatest2.reshape(100, 224 * 224 * 9 + 1)

datatestquan = np.concatenate((datatest1, datatest2), axis=0)  # 函数
print(datatestquan.shape)

############################################################
# 写入新的文件
###########################################################
# tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\train_0.bin"
# fo = open(tmp_filename, "ab")
# for i in range(0, 400):
#     fo.write(dataquan[zlshuzhutrain[i]])
# fo.close()

# tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\train_1.bin"
# fo = open(tmp_filename, "ab")
# for i in range(400, 800):
#     fo.write(dataquan[zlshuzhutrain[i]])
# fo.close()


tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\test_0.bin"
fo = open(tmp_filename, "ab")
for i in range(0, 100):
    fo.write(datatestquan[zlshuzhutest[i]])
fo.close()


tmp_filename = "D:\\11Graduate program\\2019(5)huili_cloud_data_operate\\bin\\test_1.bin"
fo = open(tmp_filename, "ab")
for i in range(100, 200):
    fo.write(datatestquan[zlshuzhutest[i]])
fo.close()


'''
print(dataquan.shape)
print(dataquan[0][0])
print(dataquan[500][0])
print(dataquan[1600][0])
#read_data_from_binary_file(tmp_filename, list_data1)
'''
