#### 六种工件是
扳手(banshou)、测电笔(cedianbi)、锤子(chuizi)、卷尺(juanchi)、墙纸刀(qiangzhidao)、钳子(qianzi)

### 官网地址
https://pjreddie.com/darknet/yolo/

### 制作自己的VOC数据集
https://blog.csdn.net/qq_34806812/article/details/81673798


### Yolov3训练自己的数据集
https://blog.csdn.net/weixin_42731241/article/details/81352013

### 输入的指令

1. 整理数据集路径格式：
1.1 建立文件夹层次为 darknet / scripts / VOCdevkit / VOC2018，voc2018下面有三个文件夹：

```
VOC2018
|——JPEGImages
|   |——Main
|   |   |——train.text
|   |   |——test.txt
|——Annotations
|   |——0.xml...
|——ImageSets
|   |——0.jpg...

```
修改 Voc_label.py
根据自己的情况修改classes
2. 创建数据集
`python Voc_label.py`
同时发现在vocdevkit同目录下也生成了5个list文件

3. 修改需要配置的文件
3.1 新建cfg/voc_gongjian.data:(复制cfg/voc.data 根据自己的情况进行修改，我改成如下所示：)
classes= 6
train  = /home/chen_ubuntu/darknet/scripts/2018_train.txt
valid  = /home/chen_ubuntu/darknet/scripts/2018_val.txt
names = /home/chen_ubuntu/darknet/data/voc_gongjian.names
backup = /home/chen_ubuntu/darknet/backup

3.2 新建data/voc_gongjian.names:(复制data/voc.names 根据自己的情况进行修改，我的六类数据)

banshou
cedianbi
chuizi
juanchi
qiangzhidao
qianzi

新建cfg/yolov3-tiny-gongjian.cfg:(复制cfg/yolov3-tiny.cfg 根据自己的情况进行修改)
[convolutional]
size=1
stride=1
pad=1
filters=33  #修改这个值为filters=(类别+5)*3
activation=linear



[yolo]
mask = 3,4,5
anchors = 10,14,  23,27,  37,58,  81,82,  135,169,  344,319
classes=6
num=6       #修改类别
jitter=.3
ignore_thresh = .7
truth_thresh = 1
random=1


**注意：yolo层中的class 为类别数，每个yolo 层前的conv层中的filters=(类别+5)*3**

4. 在darknet目录下载权重文件：
wget https://pjreddie.com/media/files/darknet53.conv.74


4. 开始训练
`./darknet detector train cfg/voc_gongjian.data cfg/yolov3-tiny-gongjian.cfg darknet53.conv.74`

5. 评估模型
`./darknet detector test cfg/voc_gongjian.data cfg/yolov3-tiny-gongjian.cfg backup/yolov3-tiny-gongjian_xxxx.weights data/xxx.jpg `

6.检测视频
`./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights <video file>`


