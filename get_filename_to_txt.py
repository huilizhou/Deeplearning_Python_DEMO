import os
import os.path
rootdir = r"C:\Users\huili\Desktop\kneedatas"

file_object = open('trainval.txt', 'w')
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        # print(filename)
        fname = os.path.splitext(filename)[0]
        # print(fname)
        file_object.write(fname + '.jpg' + '\n')
file_object.close()
