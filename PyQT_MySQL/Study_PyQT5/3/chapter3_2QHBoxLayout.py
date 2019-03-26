import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout

"""
实例化一个水平布局
将控件从左到右依次水平摆放
"""


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)                # 1

        self.h_layout = QHBoxLayout()                   # 2
        self.h_layout.addWidget(self.user_label)        # 3
        self.h_layout.addWidget(self.user_line)         # 4

        self.setLayout(self.h_layout)                   # 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
