import os
import os.path
rootdir = r"C:\Users\huili\Desktop\0"

file_object = open('file.txt', 'w')
for parent, dirnames, filenames in os.walk(rootdir):
    print(parent[23:])
    file_object.write(parent[23:])
    # print(dirnames)
    # print(parent, '/', dirnames)
    # for filename in filenames:
    #     # print(filename)
    #     fname = os.path.splitext(filename)[0]
    #     # print(fname)
    #     file_object.write(fname + '\n')
    #     # file_object.write(fname + '.jpg' + '\n')
file_object.close()
