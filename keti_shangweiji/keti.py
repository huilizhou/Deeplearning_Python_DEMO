# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keti.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(993, 738)
        self.pushButton_opencamera = QtWidgets.QPushButton(Form)
        self.pushButton_opencamera.setGeometry(QtCore.QRect(630, 50, 112, 34))
        self.pushButton_opencamera.setObjectName("pushButton_opencamera")
        self.pushButton_capturepic = QtWidgets.QPushButton(Form)
        self.pushButton_capturepic.setGeometry(QtCore.QRect(630, 100, 112, 34))
        self.pushButton_capturepic.setObjectName("pushButton_capturepic")
        self.pushButton_resize128 = QtWidgets.QPushButton(Form)
        self.pushButton_resize128.setGeometry(QtCore.QRect(630, 150, 112, 34))
        self.pushButton_resize128.setObjectName("pushButton_resize128")
        self.pushButton_recognzl = QtWidgets.QPushButton(Form)
        self.pushButton_recognzl.setGeometry(QtCore.QRect(630, 200, 112, 34))
        self.pushButton_recognzl.setObjectName("pushButton_recognzl")
        self.pushButton_setfile = QtWidgets.QPushButton(Form)
        self.pushButton_setfile.setGeometry(QtCore.QRect(630, 260, 112, 34))
        self.pushButton_setfile.setObjectName("pushButton_setfile")
        self.pushButton_savepic = QtWidgets.QPushButton(Form)
        self.pushButton_savepic.setGeometry(QtCore.QRect(630, 310, 112, 34))
        self.pushButton_savepic.setObjectName("pushButton_savepic")
        self.pushButton_save128 = QtWidgets.QPushButton(Form)
        self.pushButton_save128.setGeometry(QtCore.QRect(630, 360, 112, 34))
        self.pushButton_save128.setObjectName("pushButton_save128")
        self.pushButton_readpic = QtWidgets.QPushButton(Form)
        self.pushButton_readpic.setGeometry(QtCore.QRect(630, 410, 112, 34))
        self.pushButton_readpic.setObjectName("pushButton_readpic")
        self.pushButton_read128 = QtWidgets.QPushButton(Form)
        self.pushButton_read128.setGeometry(QtCore.QRect(630, 460, 112, 34))
        self.pushButton_read128.setObjectName("pushButton_read128")
        self.pushButton_onesteprcogn = QtWidgets.QPushButton(Form)
        self.pushButton_onesteprcogn.setGeometry(QtCore.QRect(440, 460, 112, 34))
        self.pushButton_onesteprcogn.setObjectName("pushButton_onesteprcogn")
        self.textEdit_show = QtWidgets.QTextEdit(Form)
        self.textEdit_show.setGeometry(QtCore.QRect(430, 510, 141, 51))
        self.textEdit_show.setObjectName("textEdit_show")
        self.label_orgin = QtWidgets.QLabel(Form)
        self.label_orgin.setGeometry(QtCore.QRect(60, 60, 200, 200))
        self.label_orgin.setObjectName("label_orgin")
        self.label_capture = QtWidgets.QLabel(Form)
        self.label_capture.setGeometry(QtCore.QRect(60, 300, 200, 200))
        self.label_capture.setObjectName("label_capture")
        self.label_128 = QtWidgets.QLabel(Form)
        self.label_128.setGeometry(QtCore.QRect(300, 60, 200, 200))
        self.label_128.setObjectName("label_128")
        self.pushButton_opencom = QtWidgets.QPushButton(Form)
        self.pushButton_opencom.setGeometry(QtCore.QRect(630, 520, 112, 34))
        self.pushButton_opencom.setObjectName("pushButton_opencom")
        self.pushButton_sendcmd = QtWidgets.QPushButton(Form)
        self.pushButton_sendcmd.setGeometry(QtCore.QRect(630, 570, 112, 34))
        self.pushButton_sendcmd.setObjectName("pushButton_sendcmd")
        self.label_weight = QtWidgets.QLabel(Form)
        self.label_weight.setGeometry(QtCore.QRect(430, 630, 50, 25))
        self.label_weight.setObjectName("label_weight")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(480, 630, 100, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(590, 630, 21, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(768, 523, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_price = QtWidgets.QLabel(Form)
        self.label_price.setGeometry(QtCore.QRect(430, 680, 50, 25))
        self.label_price.setObjectName("label_price")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(580, 680, 21, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_price = QtWidgets.QLineEdit(Form)
        self.lineEdit_price.setGeometry(QtCore.QRect(480, 680, 100, 25))
        self.lineEdit_price.setObjectName("lineEdit_price")

        self.retranslateUi(Form)
        self.pushButton_opencamera.clicked.connect(Form.opencamera)
        self.pushButton_resize128.clicked.connect(Form.resize128)
        self.pushButton_setfile.clicked.connect(Form.setfile)
        self.pushButton_onesteprcogn.clicked.connect(Form.onesteprecogn)
        self.pushButton_capturepic.clicked.connect(Form.capturepic)
        self.pushButton_recognzl.clicked.connect(Form.recognzl)
        self.pushButton_savepic.clicked.connect(Form.savepic)
        self.pushButton_save128.clicked.connect(Form.save128)
        self.pushButton_readpic.clicked.connect(Form.readpic)
        self.pushButton_read128.clicked.connect(Form.read128)
        self.pushButton_opencom.clicked.connect(Form.opencom)
        self.pushButton_sendcmd.clicked.connect(Form.sendcomcmd)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_opencamera.setText(_translate("Form", "打开摄像头"))
        self.pushButton_capturepic.setText(_translate("Form", "捕获图片"))
        self.pushButton_resize128.setText(_translate("Form", "调整为128"))
        self.pushButton_recognzl.setText(_translate("Form", "识别种类"))
        self.pushButton_setfile.setText(_translate("Form", "设定目录"))
        self.pushButton_savepic.setText(_translate("Form", "保存原图"))
        self.pushButton_save128.setText(_translate("Form", "保存128图"))
        self.pushButton_readpic.setText(_translate("Form", "读取原图"))
        self.pushButton_read128.setText(_translate("Form", "读取128图"))
        self.pushButton_onesteprcogn.setText(_translate("Form", "一键识别"))
        self.label_orgin.setText(_translate("Form", "TextLabel"))
        self.label_capture.setText(_translate("Form", "TextLabel"))
        self.label_128.setText(_translate("Form", "TextLabel"))
        self.pushButton_opencom.setText(_translate("Form", "打开串口"))
        self.pushButton_sendcmd.setText(_translate("Form", "命令发送"))
        self.label_weight.setText(_translate("Form", "重量："))
        self.label.setText(_translate("Form", "g"))
        self.comboBox.setItemText(0, _translate("Form", "COM1"))
        self.comboBox.setItemText(1, _translate("Form", "COM2"))
        self.comboBox.setItemText(2, _translate("Form", "COM3"))
        self.comboBox.setItemText(3, _translate("Form", "COM4"))
        self.comboBox.setItemText(4, _translate("Form", "COM5"))
        self.comboBox.setItemText(5, _translate("Form", "COM6"))
        self.comboBox.setItemText(6, _translate("Form", "COM7"))
        self.comboBox.setItemText(7, _translate("Form", "COM8"))
        self.comboBox.setItemText(8, _translate("Form", "COM9"))
        self.comboBox.setItemText(9, _translate("Form", "COM10"))
        self.comboBox.setItemText(10, _translate("Form", "COM11"))
        self.comboBox.setItemText(11, _translate("Form", "COM12"))
        self.comboBox.setItemText(12, _translate("Form", "COM13"))
        self.comboBox.setItemText(13, _translate("Form", "COM14"))
        self.label_price.setText(_translate("Form", "价格："))
        self.label_2.setText(_translate("Form", "元"))
