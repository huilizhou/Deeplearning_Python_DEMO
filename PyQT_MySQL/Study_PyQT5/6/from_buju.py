from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from buju import Ui_Form


class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def text_edit_init(self):
        self.textEdit.textChanged.connect(self.show_text_func)

    def show_text_func(self):
        self.textBrowser.setText(self.textEdit.toPlainText())


app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
