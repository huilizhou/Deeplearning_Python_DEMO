import sys
import cv2

import numpy as np
import os.path
import argparse

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from mainForm import Ui_MainWindow


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = cv2.VideoCapture(0)
        self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)

        # 初始化参数
        self.confThreshold = 0.5  # Confidence threshold
        self.nmsThreshold = 0.4  # Non-maximum suppression threshold
        self.inpWidth = 416  # Width of network's input image
        self.inpHeight = 416  # Height of network's input image

        # Load names of classes
        self.classesFile = "voc_YLgj.names"
        self.classes = None
        with open(self.classesFile, 'rt') as f:
            self.classes = f.read().rstrip('\n').split('\n')

        # 加载模型和类
        self.modelConfiguration = "yolov3-tiny-YLgj.cfg"
        self.modelWeights = "yolov3-tiny-YLgj_90000.weights"

        self.net = cv2.dnn.readNetFromDarknet(
            self.modelConfiguration, self.modelWeights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)

    def btnOpenCamera_Clicked(self):
        '''
        打开和关闭摄像头
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.pushButtonOpenCamera.setText('关闭摄像头')
            self._timer.start()
        else:
            self.pushButtonOpenCamera.setText("打开摄像头")
            self._timer.stop()

    def btnDetect_Clicked(self):
        # 摄像头未打开，不执行任何操作
        if not self.is_camera_opened:
            return

        def getOutputsNames(net):
            layersNames = self.net.getLayerNames()
            return [layersNames[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        def drawPred(classId, conf, left, top, right, bottom):
            # Draw a bounding box.
            cv2.rectangle(self.frame, (left, top),
                          (right, bottom), (255, 178, 50), 3)

            label = '%.2f' % conf

            # Get the label for the class name and its confidence
            if self.classes:
                assert(classId < len(self.classes))
                label = '%s:%s' % (self.classes[classId], label)
                print(label)

            # Display the label at the top of the bounding box
            labelSize, baseLine = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            top = max(top, labelSize[1])
            cv2.rectangle(self.frame, (left, top - round(1.5 * labelSize[1])), (left + round(
                1.5 * labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
            cv2.putText(self.frame, label, (left, top),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)

        def postprocess(frame, outs):
            self.frameHeight = self.frame.shape[0]
            self.frameWidth = self.frame.shape[1]

            classIds = []
            confidences = []
            boxes = []
            # Scan through all the bounding boxes output from the network and keep only the
            # ones with high confidence scores. Assign the box's class label as the class with the highest score.
            classIds = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]
                    if confidence > self.confThreshold:
                        center_x = int(detection[0] * self.frameWidth)
                        center_y = int(detection[1] * self.frameHeight)
                        width = int(detection[2] * self.frameWidth)
                        height = int(detection[3] * self.frameHeight)
                        left = int(center_x - width / 2)
                        top = int(center_y - height / 2)
                        classIds.append(classId)
                        confidences.append(float(confidence))
                        boxes.append([left, top, width, height])

            # Perform non maximum suppression to eliminate redundant overlapping boxes with
            # lower confidences.
            indices = cv2.dnn.NMSBoxes(
                boxes, confidences, self.confThreshold, self.nmsThreshold)
            for i in indices:
                i = i[0]
                box = boxes[i]
                left = box[0]
                top = box[1]
                width = box[2]
                height = box[3]
                drawPred(classIds[i], confidences[i], left,
                         top, left + width, top + height)

        self.captured = self.frame
        self.blob = cv2.dnn.blobFromImage(
            self.captured, 1 / 255, (self.inpWidth, self.inpHeight), [0, 0, 0], 1, crop=False)
        self.net.setInput(self.blob)
        self.outs = self.net.forward(getOutputsNames(self.net))
        postprocess(self.captured, self.outs)
        t, _ = self.net.getPerfProfile()
        self.label = 'Inference time: %.2f ms' % (
            t * 1000.0 / cv2.getTickFrequency())
        cv2.putText(self.captured, self.label, (0, 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        # 后面这几行代码几乎都一样，可以尝试封装成一个函数
        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # Qt显示图片时，需要先转换成QImgage类型
        QImg = QImage(self.captured.data, cols, rows,
                      bytesPerLine, QImage.Format_RGB888)
        self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        循环捕获图片
        '''
        ret, self.frame = self.camera.read()

        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols

        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows,
                      bytesPerLine, QImage.Format_RGB888)
        self.labelCamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labelCamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())
