from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pylab as plt

#   解析图片
back_color = imread("1.png")
#   设置字体路径
font = "C:\Windows\Fonts\STXINGKA.TTF"
wc = WordCloud(background_color="white",  # 背景颜色
               max_words=500,  # 最大词数
               mask=back_color,  # 掩膜，产生词云背景的区域，以该参数值作图绘制词云，这个参数不为空时，width,height会被忽略
               max_font_size=80,  # 显示字体的最大值
               #    stopwords=STOPWORDS.add("差评"),  # 使用内置的屏蔽词，再添加一个
               font_path=font,  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               random_state=142,  # 为每一词返回一个PIL颜色
               prefer_horizontal=10)  # 调整词云中字体水平和垂直的多少
#   打开词源的文本文件
text = open("./tmp.txt", "r", encoding="utf-8").read()

#   生成词云
wc.generate(text)
#   从背景图片生成颜色值
image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis("off")
# 绘制词云
plt.figure()

plt.imshow(wc.recolor(color_func=image_colors))

plt.axis("off")
# 保存图片
wc.to_file("text2.png")
