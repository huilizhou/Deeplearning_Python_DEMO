from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
import sys
import cv2
import numpy as np
from keti import Ui_Form    # 导入生成form.py里生成的类
from PIL import Image, ImageFilter
import datetime
import serial
import serial.tools.list_ports
import threading
import binascii
import Vgg16test


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.chenopencloseflag = 0
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(150)
        self.frame = None

        self.piccapture = None
        self.piccapturerecord = None

        self.picresize = None
        self.picresizerecord = None
        self.cap = cv2.VideoCapture(0)

        self.mflag = 0
        self.nowleibie = 0

        self.pathname = ""
        self.nnet = Vgg16test.chenvgg16_convol()
        # self.nnet.initnet()
        self.fruits = ['冬枣', '香蕉', '桔子', '猕猴桃',
                       '苹果', '火龙果', '葡萄', '草莓', '菠萝', '哈密瓜']
        self.fruitprice = [6.0, 6.0, 5.0, 12.0,
                           6.0, 10.0, 8.0, 12.0, 8.0, 16.0]
    # 定义槽函数
        self.opencamera()
        self.ser = serial.Serial()

    def opencamera(self):
        if self.chenopencloseflag == 0:
            self.pushButton_opencamera.setText("停止采集")
            self.chenopencloseflag = 1
            self._timer.start()
        else:
            self.pushButton_opencamera.setText("开始采集")
            self.chenopencloseflag = 0
            self._timer.stop()

    @QtCore.pyqtSlot()
    def _queryFrame(self):
        ret, self.frame = self.cap.read()
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        height, width, bytesPerComponent = self.frame.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, width, height,
                      bytesPerLine, QImage.Format_RGB888)
        self.label_orgin.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.label_orgin.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if self.mflag == 1:
            self.onesteprecogn()
            print(self.nowleibie)

            m_jiage = int(self.lineEdit.text()) * \
                    self.fruitprice[self.nowleibie] / 1000
            self.lineEdit_price.setText(str(m_jiage))
            self.mflag = 0

    # 定时器调用的捕获图像

    def capturepic(self):
        self.piccapture = self.frame
        #self.piccaptureshow = self.frame
        # 变换彩色空间顺序
        height, width, bytesPerComponent = self.piccapture.shape
        bytesPerLine = 3 * width
        #cv2.cvtColor(self.piccapture, cv2.COLOR_BGR2RGB, self.piccapture)
        self.piccapturerecord = cv2.cvtColor(
            self.piccapture, cv2.COLOR_BGR2RGB)
        QImg = QImage(self.piccapture.data, width, height,
                      bytesPerLine, QImage.Format_RGB888)
        self.label_capture.setPixmap(QPixmap.fromImage(QImg).scaled(+
                                                                    self.label_capture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.textEdit_show.setText("捕获图片")
        # 转为QImage对象
        #self.imageshow = QImage(self.piccapture.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # self.label_capture.setPixmap(QPixmap.fromImage(QImg))
        # self.label_capture.setPixmap(QPixmap.fromImage(self.imageshow))

    # 调整图像为128分辨率
    def resize128(self):
        try:
            # 防止存在灰度图，一般写法：rows,cols=img.shape
            rows, cols = self.piccapture.shape[0], self.piccapture.shape[1]
            if(rows <= cols):
                crop_image = self.piccapture[:, cols //
                                             2 - rows // 2: cols // 2 + rows // 2]
            else:
                crop_image = self.piccapture[rows //
                                             2 - cols // 2: rows // 2 + cols // 2, :]

            # 调整图片大小
            self.picresize = cv2.resize(crop_image, (224, 224))
            self.picresizerecord = cv2.resize(crop_image, (224, 224))
            height, width, bytesPerComponent = self.picresize.shape
            bytesPerLine = 3 * width
            cv2.cvtColor(self.picresizerecord,
                         cv2.COLOR_BGR2RGB, self.picresizerecord)
            QImg = QImage(self.picresize.data, width, height,
                          bytesPerLine, QImage.Format_RGB888)
            self.label_128.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_128.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.textEdit_show.setText("调整图片128*128")
        except:
            pass

    # 保存原图
    def savepic(self):
        now_time = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(now_time, '%Y%m%d%H%M%S')
        filename = self.pathname + "/" + time1_str + ".jpg"
        cv2.imwrite(str(filename), self.piccapturerecord)
        # print(filename)
        self.textEdit_show.setText("保存图片" + filename)

    # 保存调整后的128图
    def save128(self):
        now_time = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(now_time, '%Y%m%d%H%M%S')
        filename = self.pathname + "/" + time1_str + ".jpg"
        # print(filename)
        cv2.imwrite(str(filename), self.picresizerecord)
        self.textEdit_show.setText("保存128图片" + filename)

    # 设定保存的目录
    def setfile(self):
        self.pathname = QFileDialog.getExistingDirectory(
            self, "请选择保存路径...", "./")
        self.textEdit_show.setText(self.pathname)

    # 识别种类
    def recognzl(self):
        #cv2.cvtColor(self.picresize, cv2.COLOR_BGR2RGB, self.picresizerecord)
        # self.nnet.readimage(self.picresizerecord)
        # self.nnet.readimage(self.picresize)
        i = self.nnet.recognpic(self.picresizerecord)
        # print('chen',str(i))
        # print(self.fruits[i])
        # print(i)
        self.textEdit_show.setText("识别结果:" + str(int(i)) + self.fruits[int(i)])

    # 读入原图
    def readpic(self):
        #self.pathname =  QFileDialog.getExistingDirectory(self,"请选择保存路径...","./") ####
        # self.textEdit.setText(self.pathname)
        filename,  _ = QFileDialog.getOpenFileName(self, 'a')
        if filename:
            # print("ok",filename)
            self.piccapturerecord = cv2.imread(str(filename))

            #self.picresize=cv2.cvtColor(self.piccapturerecord, cv2.COLOR_BGR2RGB)
            height, width, bytesPerComponent = self.piccapturerecord.shape
            bytesPerLine = 3 * width
            cv2.cvtColor(self.piccapturerecord,
                         cv2.COLOR_BGR2RGB, self.piccapturerecord)
            self.piccapture = self.piccapturerecord
            QImg = QImage(self.piccapturerecord.data, width,
                          height, bytesPerLine, QImage.Format_RGB888)
            self.label_capture.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_capture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.textEdit_show.setText("读取原图")
        else:
            self.textEdit_show.setText("未能读取原图")

    # 读入128图
    def read128(self):
        filename,  _ = QFileDialog.getOpenFileName(self, 'a')
        if filename:
            # print("ok",filename)
            self.picresizerecord = cv2.imread(str(filename))
            self.picresize = cv2.cvtColor(
                self.picresizerecord, cv2.COLOR_BGR2RGB)
            height, width, bytesPerComponent = self.picresize.shape
            bytesPerLine = 3 * width
            cv2.cvtColor(self.picresizerecord,
                         cv2.COLOR_BGR2RGB, self.picresizerecord)
            QImg = QImage(self.picresize.data, width, height,
                          bytesPerLine, QImage.Format_RGB888)
            self.label_128.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_128.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.textEdit_show.setText("调整图片128*128")
        else:
            self.textEdit_show.setText("未能读取图片")

    def onesteprecogn(self):

        #（1）捕获
        # 变换彩色空间顺序
        self.piccapture = self.frame
        height, width, bytesPerComponent = self.piccapture.shape
        bytesPerLine = 3 * width
        self.piccapturerecord = cv2.cvtColor(
            self.piccapture, cv2.COLOR_BGR2RGB)
        QImg = QImage(self.piccapture.data, width, height,
                      bytesPerLine, QImage.Format_RGB888)
        self.label_capture.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.label_capture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.textEdit_show.setText("捕获图片")

        #（2）调整图像分辨率
        try:
            # 防止存在灰度图，一般写法：rows,cols=img.shape
            rows, cols = self.piccapture.shape[0], self.piccapture.shape[1]
            if(rows <= cols):
                crop_image = self.piccapture[:, cols //
                                             2 - rows // 2: cols // 2 + rows // 2]
            else:
                crop_image = self.piccapture[rows //
                                             2 - cols // 2: rows // 2 + cols // 2, :]

            # 调整图片大小
            self.picresize = cv2.resize(crop_image, (224, 224))
            self.picresizerecord = cv2.resize(crop_image, (224, 224))
            height, width, bytesPerComponent = self.picresize.shape
            bytesPerLine = 3 * width
            cv2.cvtColor(self.picresizerecord,
                         cv2.COLOR_BGR2RGB, self.picresizerecord)
            QImg = QImage(self.picresize.data, width, height,
                          bytesPerLine, QImage.Format_RGB888)
            self.label_128.setPixmap(QPixmap.fromImage(QImg).scaled(
                self.label_128.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.textEdit_show.setText("调整图片128*128")
        except:
            pass
        #（3）识别种类
        # self.nnet.readimage(self.picresize)
        i = self.nnet.recognpic(self.picresizerecord)
        self.nowleibie = int(i)
        # print(i)
        self.textEdit_show.setText("识别结果:" + str(int(i)) + self.fruits[int(i)])

    def opencom(self):
        # print(self.comboBox.currentText())

        Com_List = []
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBox.addItem(port[0])
        if(len(Com_List) == 0):
            self.textEdit_show.setText("没串口")

        self.ser.port = self.comboBox.currentText()
        # str(self.comboBox.currentText())
        # print(self.ser.port)

        self.ser.baudrate = 9600
        self.ser.bytesize = 8
        self.ser.stopbits = 1
        self.ser.parity = "N"
        try:
            self.ser.open()
            # print(self.ser.isOpen())
            if(self.ser.isOpen()):
                # print("chenok")
                self.textEdit_show.setText(self.ser.port + "打开成功")
                self.t1 = threading.Thread(target=self.receive_data)
                self.t1.setDaemon(True)
                self.t1.start()
            else:
                # print("chenshibai")
                self.textEdit_show.setText(self.ser.port + "打开失败")
        except:
            self.textEdit_show.setText(self.ser.port + "打开失败,有错误")

    # def receive_data(self):
    #     print("The receive_data threading is start")
    #     res_data = ''
    #     num = 0
    #     if (self.ser.isOpen()):
    #         size = self.ser.inWaiting()
    #         if size:
    #             res_data = self.ser.read_all()
    #             # self.textEdit.append(res_data.decode())
    #             # self.textEdit_2.insertPlainText(res_data.decode())
    #             self.lineEdit.insertPlainText(res_data.decode())

    def receive_data(self):
        print("The receive_data threading is start")
        res_data = ''
        num = 0
        while (self.ser.isOpen()):
            size = self.ser.inWaiting()
            if size:
                res_data = self.ser.read_all()
                # self.textEdit_show.append(res_data.decode())
                self.lineEdit.setText(res_data.decode())

                self.mflag = 1

    def sendcomcmd(self):
        if(self.ser.isOpen()):
            self.ser.write(self.textEdit_show.toPlainText().encode('utf-8'))
            self.textEdit_show.setText("发送成功")
            # self.ser.flushOutput()
        else:
            self.textEdit_show.setText("发送失败")


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
