# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(709, 521)
        self.pushButton_close = QtWidgets.QPushButton(Form)
        self.pushButton_close.setGeometry(QtCore.QRect(270, 210, 112, 34))
        self.pushButton_close.setObjectName("pushButton_close")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 410, 45, 25))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 410, 81, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(90, 320, 105, 22))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        self.pushButton_close.clicked.connect(Form.close)
        self.checkBox.clicked['bool'].connect(self.lineEdit.setEnabled)
        self.checkBox.clicked['bool'].connect(self.label.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_close.setText(_translate("Form", "关闭窗口"))
        self.label.setText(_translate("Form", "显示1"))
        self.lineEdit.setText(_translate("Form", "显示2"))
        self.checkBox.setText(_translate("Form", "选择"))
