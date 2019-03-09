# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(50, 50, 640, 480))
        self.labelCamera.setObjectName("labelCamera")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(790, 50, 640, 480))
        self.labelResult.setObjectName("labelResult")
        self.pushButtonOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpenCamera.setGeometry(QtCore.QRect(250, 640, 112, 34))
        self.pushButtonOpenCamera.setObjectName("pushButtonOpenCamera")
        self.pushButtonDetect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDetect.setGeometry(QtCore.QRect(990, 640, 112, 34))
        self.pushButtonDetect.setObjectName("pushButtonDetect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.pushButtonDetect.clicked.connect(MainWindow.btnDetect_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCamera.setText(_translate("MainWindow", "摄像头"))
        self.labelResult.setText(_translate("MainWindow", "结果图"))
        self.pushButtonOpenCamera.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButtonDetect.setText(_translate("MainWindow", "检测图片"))

