#### 六种工件是
扳手(banshou)、测电笔(cedianbi)、锤子(chuizi)、卷尺(juanchi)、墙纸刀(qiangzhidao)、钳子(qianzi)



### 输入的指令
在research 目录下
1. 添加环境变量
` export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim `

2. 创建数据集
`python object_detection/dataset_tools/create_gongjian_tf_record_ex2tron.py --data_dir=object_detection/gongjian_datas --output_dir=object_detection/gongjian_datas/output_datasets`

3. 选择配置模型
这边选择的是“faster_rcnn_resnet101”
复制`object_detection/samples/configs`
修改其中的配置
（我已经修改好了，改名为`faster_rcnn_resnet101_gongjian.config`）：
```
num_classes # 分类数 9行
fine_tune_checkpoint # 调用的模型地址 106行

train_input_reader: input_path # 训练集的地址 116行
train_input_reader: label_map_path # 标签文件地址 118行
eval_input_reader: input_path # 评估集的地址 130行
eval_input_reader: label_map_path # 标签文件地址 132行
```
4. 开始训练
`python object_detection/train.py --logtostderr --pipeline_config_path=object_detection/samples/configs/faster_rcnn_resnet101_gongjian.config --train_dir=object_detection/gongjian_datas/tune_checkpoints`

5. 评估模型
`python object_detection/eval.py --logtostderr --checkpoint_dir=object_detection/gongjian_datas/tune_checkpoints --pipeline_config_path=object_detection/samples/configs/faster_rcnn_resnet101_gongjian.config --eval_dir=object_detection/gongjian_datas/eval_output`


6. 导出PB模型(可选)

`python object_detection//export_inference_graph.py --input_type=image_tensor --pipeline_config_path=object_detection/samples/configs/faster_rcnn_resnet101_gongjian.config --trained_checkpoint_prefix=object_detection/gongjian_datas/tune_checkpoints/model.ckpt-50237 --output_directory=object_detection/gongjian_datas/saved_model`

7. 调用生成的模型：

复制并修改`object_detection_tutorial.py`（我已经修改好了，改名为`object_detection_tutorial_ex2tron.py`）：

```
PATH_TO_CKPT # 模型地址 26行
PATH_TO_LABELS # 标签文件地址 28行
NUM_CLASSES # 分类数目 29行
```

最后将测试的图片放在`object_detection/test_images/`下，运行如下指令即可：

`python object_detection/object_detection_tutorial_ex2tron.py`