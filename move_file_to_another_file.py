'''
徐基业的需求
从第一个文件夹读取一个文件名字，在第二个文件夹找到同样的，然后把找到的文件移到第三个文件夹
'''

import os
import shutil
import os.path
rootdir1 = r"C:\Users\huili\Desktop\a1"
rootdir2 = r"C:\Users\huili\Desktop\a2"
rootdir3 = r"C:\Users\huili\Desktop\a3"
for parent, dirnames, filenames1 in os.walk(rootdir1):
    for parent, dirnames, filenames2 in os.walk(rootdir2):
        for filename in filenames2:
            if filename in filenames1:
                print(filename)
                shutil.copy(os.path.join(rootdir2, filename),
                            os.path.join(rootdir3))
