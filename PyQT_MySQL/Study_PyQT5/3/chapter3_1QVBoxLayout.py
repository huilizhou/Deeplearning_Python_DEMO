import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


"""
垂直布局方式
将各个控件从上到下垂直的方式摆放
"""


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel("Username:", self)
        self.pwd_label = QLabel('Password:', self)

        self.v_layout = QVBoxLayout()                   # 1
        self.v_layout.addWidget(self.user_label)        # 2
        self.v_layout.addWidget(self.pwd_label)         # 3

        self.setLayout(self.v_layout)                   # 4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
