import colorlabel
import PIL.Image
import yaml
import os

label_color = {
    # 这个是你自己的类别和对应的颜色
    # 例如，'Dog': 'maroon'
    # 注意：这里的颜色需要是下面颜色列表color中的颜色
    'banana': 'yellow'
}

# path = 'D:\\data\\'  # 你执行第二步时的存储路径
path = 'C:\\Users\\huili\\Desktop\\json_1\\'
label_path = os.listdir(path)
for label_class in label_path:
    print(label_class)
    img = PIL.Image.open('%s\\label.png' % (path + label_class))
    import numpy as np
    from skimage import io, data, color
    label = np.array(img)

    yaml_file = path + label_class + '\\' + 'info.yaml'
    print(yaml_file)
    with open(yaml_file) as f:
        f = yaml.load(f)
        classes = f['label_names']

    color = ['yellow']  # 颜色列表
    c = 1
    for i in classes:
        if c == 1:
            c = c + 1
            continue

        color.append(label_color[i])

    # print (color)   #颜色列表
    dst = colorlabel.label2rgb(label, colors=(tuple)(
        color), bg_label=0, bg_color=(0, 0, 0))
    #final = PIL.Image.fromarray(np.uint8(dst * 255))
    # final.show()
    # final.save('000001.png')
    # save_path = 'D:\\data' + '\\' + label_class[:-5] + '.png'  # 你希望将标注图片存储的路径
    save_path = 'C:\\Users\\huili\\Desktop\\save1' + \
        '\\' + label_class[:-5] + '.png'

    #print('11111%s' % save_path)
    io.imsave(save_path, dst)
