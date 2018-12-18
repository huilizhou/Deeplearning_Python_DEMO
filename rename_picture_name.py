import os
# 输入新的文件名

path = r"C:\Users\huili\Desktop\Capture"
filelist = os.listdir(path)
count = 1040
for file in filelist:
    print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    Newdir = os.path.join(path, str(count).zfill(5) + filetype)
    # Newdir = os.path.join(path, 'rotten_' + str(count).zfill(4) + filetype)
    os.rename(Olddir, Newdir)

    count += 1
