import os
import numpy as np

base = "test"
label = 0
number = 100

train_0 = np.empty([number, 1, 50176 * 9 + 1], np.int32)
for i in range(number):
    file_path = os.path.join(base, str(label), str(i + 1) + ".txt")
    np_array = np.loadtxt(file_path)
    np_array_regular = (255 * (np_array - np.min(np_array)) /
                        (np.max(np_array) - np.min(np_array))).astype(np.int32)
    np_array_regular = np_array_regular.reshape([1, 50176 * 9])
    np_add_label = np.insert(np_array_regular, 0, label, axis=1)
    train_0[i] = np_add_label
    print(i + 1)

train_0.tofile("test_0.bin")

# test code:
# a = np.fromfile('train_0.bin',np.int32)
# a = a.reshape([number,1,-1])
# label: a[0][0][0]
