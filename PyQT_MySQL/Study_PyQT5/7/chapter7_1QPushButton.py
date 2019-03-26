import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.test_button = QPushButton("Test", self)
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon('button.png'))
        self.test_button.toggled.connect(self.button_state_func)

    def button_state_func(self):
        print(self.test_button.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
