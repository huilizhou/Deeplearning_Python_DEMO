import os
import os.path
import xml.dom.minidom

path = r"C:\Users\huili\Desktop\Annotations"
files = os.listdir(path)
s = []
for xmlFile in files:
    if not os.path.isdir(xmlFile):
        # print(xmlFile)

        fname = os.path.splitext(xmlFile)[0]

    # xml文件读取操作
        dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))
        root = dom.documentElement

        filename = root.getElementsByTagName('filename')
        f = filename[0]
        f.firstChild.data = (fname + '.jpg')
        print(f.firstChild.data)

    with open(os.path.join(path, xmlFile), 'w') as fh:
        dom.writexml(fh)
        print('写入filenameOK!')
