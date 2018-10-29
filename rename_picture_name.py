import os
# 输入新的文件名

path = r"H:\1"
filelist = os.listdir(path)
count = 0
for file in filelist:
    print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    Newdir = os.path.join(path, 'dongzao_' + str(count).zfill(5) + filetype)
    os.rename(Olddir, Newdir)

    count += 1
