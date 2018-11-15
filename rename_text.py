import os
# 输入新的文件名

path = r"C:\Users\huili\Desktop\任务1：批量重命名（只命名1-200.txt）\任务1：批量重命名（只命名1-200.txt）"
filelist = os.listdir(path)
count = 201
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
