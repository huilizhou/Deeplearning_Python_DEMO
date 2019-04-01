# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(80, 40, 320, 240))
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setGeometry(QtCore.QRect(80, 300, 320, 240))
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(480, 40, 640, 480))
        self.labelResult.setObjectName("labelResult")
        self.pushButtonCamera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCamera.setGeometry(QtCore.QRect(80, 640, 112, 34))
        self.pushButtonCamera.setObjectName("pushButtonCamera")
        self.pushButtonCapture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCapture.setGeometry(QtCore.QRect(230, 640, 112, 34))
        self.pushButtonCapture.setObjectName("pushButtonCapture")
        self.pushButtonDetect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDetect.setGeometry(QtCore.QRect(860, 640, 112, 34))
        self.pushButtonDetect.setObjectName("pushButtonDetect")
        self.lineEditShow = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditShow.setGeometry(QtCore.QRect(1000, 640, 113, 34))
        self.lineEditShow.setObjectName("lineEditShow")
        self.pushButtonSaveImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSaveImage.setGeometry(QtCore.QRect(550, 640, 112, 34))
        self.pushButtonSaveImage.setObjectName("pushButtonSaveImage")
        self.pushButtonReadImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReadImage.setGeometry(QtCore.QRect(710, 640, 112, 34))
        self.pushButtonReadImage.setObjectName("pushButtonReadImage")
        self.pushButtonSetFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetFile.setGeometry(QtCore.QRect(400, 640, 112, 34))
        self.pushButtonSetFile.setObjectName("pushButtonSetFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.pushButtonCapture.clicked.connect(MainWindow.btnCapture_Clicked)
        self.pushButtonDetect.clicked.connect(MainWindow.btnDetect_Clicked)
        self.pushButtonSaveImage.clicked.connect(
            MainWindow.btnSaveImage_Clicked)
        self.pushButtonReadImage.clicked.connect(
            MainWindow.btnReadImage_Clicked)
        self.pushButtonSetFile.clicked.connect(MainWindow.btnSetFile_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YLAi"))
        self.labelCamera.setText(_translate("MainWindow", "摄像头"))
        self.labelCapture.setText(_translate("MainWindow", "捕获图"))
        self.labelResult.setText(_translate("MainWindow", "结果图"))
        self.pushButtonCamera.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButtonCapture.setText(_translate("MainWindow", "捕获图片"))
        self.pushButtonDetect.setText(_translate("MainWindow", "检测图片"))
        self.pushButtonSaveImage.setText(_translate("MainWindow", "保存图片"))
        self.pushButtonReadImage.setText(_translate("MainWindow", "读入图片"))
        self.pushButtonSetFile.setText(_translate("MainWindow", "设定目录"))
