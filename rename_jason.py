import os
# 输入新的文件名

path = r"C:\Users\huili\Desktop\pic"
filelist = os.listdir(path)
# for file in filelist:
#     print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    # Newdir = os.path.join(path, str(count).zfill(3) + filetype)
    Newdir = os.path.join(path, 'img' + filename + filetype)
    os.rename(Olddir, Newdir)
