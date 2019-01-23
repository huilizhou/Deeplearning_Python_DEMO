import os
from PIL import Image


def bmpToJpg(file_path):
    for filename in os.listdir(file_path):
        newfilename = filename[1:] + '.jpg'
        print(newfilename)
        im = Image.open(file_path + "\\" + filename)
        im.save(file_path + "\\" + newfilename)


def main():
    file_path = "C:\\Users\\huili\\Desktop\\gongjian_test_image"
    bmpToJpg(file_path)


if __name__ == "__main__":
    main()
