import os
import os.path

root_dir = r"C:\Users\huili\Desktop\ka"

with open('trian.txt', 'w') as file:
    for foldername, subfloders, filenames in os.walk(root_dir):
        for filename in filenames:
            fname = os.path.splitext(filename)[0]
            file.write(fname + '\n')
