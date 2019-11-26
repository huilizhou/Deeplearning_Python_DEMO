import os


# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字


def main():
    rootdir = "C:\\Users\\huili\\Desktop\\JPEGImages"
    for _, _, filenames in os.walk(rootdir):
        new_suffix = '.jpg'
    for filename in filenames:
        if filename.endswith('.png'):
            name_without_suffix = filename[:-4]
            os.rename(os.path.join(rootdir, filename), os.path.join(
                rootdir, name_without_suffix + new_suffix))


if __name__ == "__main__":
    main()
