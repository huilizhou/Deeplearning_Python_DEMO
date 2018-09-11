import os
import os.path
rootdir = r"C:\Users\huili\Desktop\货架商品\xml"

file_object = open('trainval.txt', 'w')
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        # print(filename)
        fname = os.path.splitext(filename)[0]
        # print(fname)
        file_object.write(fname + '\n')
file_object.close()
