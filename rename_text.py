import os
# 输入新的文件名

path = r"D:\11Graduate program\2019(5)huili_cloud_data_operate\test\1"
filelist = os.listdir(path)
count = 1
for file in filelist:
    print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    Newdir = os.path.join(path, str(count) + filetype)
    os.rename(Olddir, Newdir)

    count += 1
