import os
import numpy as np

base = "train"
label = 0
number = 400

train_0 = np.empty([number,50176,9])
for i in range(number):
    file_path = os.path.join(base,str(label),str(i+1)+".txt")
    np_array = np.loadtxt(file_path)
    # 归一化(小数)
    np_array_regular = (np_array - np.min(np_array))/(np.max(np_array)-np.min(np_array))
    train_0[i]= np_array_regular

train_0.tofile("train_0.bin")