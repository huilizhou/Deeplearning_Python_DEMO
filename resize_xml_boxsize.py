import os
import os.path
import xml.dom.minidom

path = r"C:\Users\huili\Desktop\goodsxml"
files = os.listdir(path)
s = []
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        # print(xmlFile)

        # xml文件读取操作
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        root = dom.documentElement

        # filename = root.getElementsByTagName('filename')
        # f = filename[0]
        # print(f.firstChild.data)

        height = root.getElementsByTagName('height')
        h = height[0]
        # print(h.firstChild.data)
        width = root.getElementsByTagName('width')
        w = width[0]

        xmin = root.getElementsByTagName('xmin')
        xmax = root.getElementsByTagName('xmax')
        ymin = root.getElementsByTagName('ymin')
        ymax = root.getElementsByTagName('ymax')

        # print('len的值')
        # print(len(xmin))
        # print('xmin的大小')
        # for i in range(0, len(xmin)):
        #     xmin[i].firstChild.data = str(int(int(xmin[i].firstChild.data)))
        #     print(xmin[i].firstChild.data)

        if (int(h.firstChild.data) > 3600):
            h.firstChild.data = str(int(int(h.firstChild.data) / 4))
            w.firstChild.data = str(int(int(w.firstChild.data) / 4))

            for i in range(0, len(xmin)):
                xmin[i].firstChild.data = str(
                    int(int(xmin[i].firstChild.data) / 4))
                ymin[i].firstChild.data = str(
                    int(int(ymin[i].firstChild.data) / 4))
                xmax[i].firstChild.data = str(
                    int(int(xmax[i].firstChild.data) / 4))
                ymax[i].firstChild.data = str(
                    int(int(ymax[i].firstChild.data) / 4))

        elif(int(h.firstChild.data) <= 3600 and int(h.firstChild.data) > 1800):
            h.firstChild.data = str(int(int(h.firstChild.data) / 2))
            w.firstChild.data = str(int(int(w.firstChild.data) / 2))

            for i in range(0, len(xmin)):
                xmin[i].firstChild.data = str(
                    int(int(xmin[i].firstChild.data) / 2))
                ymin[i].firstChild.data = str(
                    int(int(ymin[i].firstChild.data) / 2))
                xmax[i].firstChild.data = str(
                    int(int(xmax[i].firstChild.data) / 2))
                ymax[i].firstChild.data = str(
                    int(int(ymax[i].firstChild.data) / 2))

        else:
            h.firstChild.data = h.firstChild.data
            w.firstChild.data = w.firstChild.data

            for i in range(0, len(xmin)):
                xmin[i].firstChild.data = xmin[i].firstChild.data
                ymin[i].firstChild.data = ymin[i].firstChild.data
                xmax[i].firstChild.data = xmax[i].firstChild.data
                ymax[i].firstChild.data = ymax[i].firstChild.data

                # print('xmin_value')
                # print(xmin[i].firstChild.data)
                # print("")
                # print('ymin_value')
                # print(ymin[i].firstChild.data)
                # print("")
                # print('xmax_value')
                # print(xmax[i].firstChild.data)
                # print("")
                # print('ymax_value')
                # print(ymax[i].firstChild.data)
                # print("")
        # print(h.firstChild.data)

        with open(os.path.join(path, xmlFile), 'w') as fh:
            dom.writexml(fh)
            print('写入filenameOK!')
