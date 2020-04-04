# coding: utf-8


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import cv2
import jieba
from matplotlib import colors


with open('tmp1.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

cut_text = " ".join(jieba.cut(text))

color_list = ['#FF0000', '#a41a1a']  # 建立颜色数组
colormap = colors.ListedColormap(color_list)  # 调用

color_mask = cv2.imread('8.png')

cloud = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path=" C:\\Windows\\Fonts\\STXINGKA.TTF",
    # font_path=path.join(d,'simsun.ttc'),
    # 设置背景色
    background_color='white',
    # 词云形状
    mask=color_mask,
    # 允许最大词汇
    max_words=2000,
    random_state=30,
    # 最大号字体
    max_font_size=96,
    colormap=colormap  # 设置颜色
)

wCloud = cloud.generate(cut_text)

image_colors = ImageColorGenerator(color_mask)

wCloud.to_file('cloud1.jpg')

plt.imshow(wCloud.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis('off')
