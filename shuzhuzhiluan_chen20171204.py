import random
import os
import numpy as np





#将按顺序写入的训练数组置软
zlshuzhutrain=random.sample(range(5000),5000)

#将按顺序写入的测试置软
zlshuzhutest=random.sample(range(1000),1000)


############################################################
#读取按顺序存储的文件
###########################################################

tmp_filename = "D:\\test\\chenfruit_128\\data_batch_1.bin"
data1 = np.fromfile(tmp_filename, dtype=np.int8)
#print(data1.shape)
data1=data1.reshape(1000,128*128*3+1)
#print(data1.shape)
tmp_filename = "D:\\test\\chenfruit_128\\data_batch_2.bin"
data2 = np.fromfile(tmp_filename, dtype=np.int8)
data2=data2.reshape(1000,128*128*3+1)

tmp_filename = "D:\\test\\chenfruit_128\\data_batch_3.bin"
data3 = np.fromfile(tmp_filename, dtype=np.int8)
data3=data3.reshape(1000,128*128*3+1)

tmp_filename = "D:\\test\\chenfruit_128\\data_batch_4.bin"
data4 = np.fromfile(tmp_filename, dtype=np.int8)
data4=data4.reshape(1000,128*128*3+1)

tmp_filename = "D:\\test\\chenfruit_128\\data_batch_5.bin"
data5 = np.fromfile(tmp_filename, dtype=np.int8)
data5=data5.reshape(1000,128*128*3+1)

dataquan=np.concatenate((data1,data2,data3,data4,data5), axis=0)#函数


tmp_filename = "D:\\test\\chenfruit_128\\test_batch.bin"
datatest = np.fromfile(tmp_filename, dtype=np.int8)
datatest=datatest.reshape(1000,128*128*3+1)
print(dataquan.shape)

############################################################
#写入新的文件
###########################################################
tmp_filename = "D:\\test\\chenfruit_128_sj\\data_batch_1.bin"
fo = open(tmp_filename, "ab")
for i in range(0,1000):   
    fo.write(dataquan[zlshuzhutrain[i]])
fo.close()

tmp_filename = "D:\\test\\chenfruit_128_sj\\data_batch_2.bin"
fo = open(tmp_filename, "ab")
for i in range(1000,2000):   
    fo.write(dataquan[zlshuzhutrain[i]])
fo.close()

tmp_filename = "D:\\test\\chenfruit_128_sj\\data_batch_3.bin"
fo = open(tmp_filename, "ab")
for i in range(2000,3000):   
    fo.write(dataquan[zlshuzhutrain[i]])
fo.close()

tmp_filename = "D:\\test\\chenfruit_128_sj\\data_batch_4.bin"
fo = open(tmp_filename, "ab")
for i in range(3000,4000):   
    fo.write(dataquan[zlshuzhutrain[i]])
fo.close()

tmp_filename = "D:\\test\\chenfruit_128_sj\\data_batch_5.bin"
fo = open(tmp_filename, "ab")
for i in range(4000,5000):   
    fo.write(dataquan[zlshuzhutrain[i]])
fo.close()

tmp_filename = "D:\\test\\chenfruit_128_sj\\test_batch.bin"
fo = open(tmp_filename, "ab")
for i in range(0,1000):   
    fo.write(datatest[zlshuzhutest[i]])
fo.close()

'''
print(dataquan.shape)
print(dataquan[0][0])
print(dataquan[500][0])
print(dataquan[1600][0])
#read_data_from_binary_file(tmp_filename, list_data1)
'''

