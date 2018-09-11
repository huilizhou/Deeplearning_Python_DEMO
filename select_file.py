import os
import os.path
import shutil

root_dir = r"C:\Users\huili\Desktop\ka"

with open('trian.txt', 'w') as file:
    for foldername, subfloders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.jpg'):
                # print(filename)
                shutil.move(os.path.join(foldername, filename),
                            '.\\test')
