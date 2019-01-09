# SegNet使用示例


如果拷贝的是本教程已经修改过的代码，则无需关注下面的流程。如果需要从头开始搭建的话，请按照下面的流程走：

## 环境搭建

本教程使用的软件环境：

- Anaconda(Python 3.6.5)
- Tensorflow 1.10.1

## 1.安装KittiSeg示例网络

项目地址: https://github.com/MarvinTeichmann/KittiSeg
详情可参考项目README.md

``` bash
git clone https://github.com/MarvinTeichmann/KittiSeg.git

# 初始化子模块
cd KittiSeg/
git submodule update --init --recursive

# 下载预训练模型到RUNS目录(一定记得解压)
cd RUNS/
wget ftp://mi.eng.cam.ac.uk/pub/mttt2/models/KittiSeg_pretrained.zip
unzip KittiSeg_pretrained.zip

# 下载VGG-16模型vgg16.npy到DATA目录
mkdir ../DATA
cd ../DATA/
wget ftp://mi.eng.cam.ac.uk/pub/mttt2/models/vgg16.npy

```

> p.s.预训练模型2.57GB，VGG16参数模型553MB，都有点大，所以下载好之后以防万一，这几个文件可以单独备份下。

## 2.单张图片测试

切换到KittiSeg目录，运行：

``` bash
python demo.py --input_image data/demo/demo.png
```

运行完成后，会生成下面三个结果文件：

```
demo_green.png
demo_raw.png
demo_rb.png
```

## 3.视频文件测试

原版的KittiSeg网络并没有测试视频的案例，需要修改，我这里已经改好了：


地址：[ex2tron_kittiseg_video_demo.py]()


运行：

```
python ex2tron_kittiseg_video_demo.py --input_video data/demo/demo.mp4
```

## 4.使用Kitti的数据集训练

因为前面把vgg16.npy直接放在了DATA目录下，源码中有个地方路径不一致，需要修改过来：打开`/encoder/fcn8_vgg.py`，把第32行的weights去掉。修改download_data.py文件的87行，去掉weights

下载Kitti数据集：

[下载链接](https://s3.eu-central-1.amazonaws.com/avg-kitti/data_road.zip)

下载`data_road.zip`到DATA文件夹下，然后运行下面的指令生成/DATA/train3.txt等文件：


``` bash
python download_data.py
```

Kitti模型的参数通过hypes/KittiSeg.json控制，里面有很多参数可以设置，目前保持默认。


- 由于Python2和3版本的原因，一些地方需要修改：`/optimizer/generic_optimizer.py`文件中的83行改成`grads_and_vars = list(zip(clipped_grads, tvars))`
- `/inputs/kitti_seg_input.py`355行改成`next(gen)`
- `/incl/train.py`163行改成`print_str = ', '.join([nam + ": %.2f" for nam in eval_names])`
- 搜索出现xrange的地方改成range

然后终于可以训练了：

```
python train.py --hypes hypes/KittiSeg.json 
```

默认情况下，输出目录是`/RUNS/KittiSeg_date/`下面。


## 5.建立自己的数据集训练


