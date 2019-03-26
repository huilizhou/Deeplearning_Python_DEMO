import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QColorDialog, QFontDialog, QPushButton, \
                            QHBoxLayout, QVBoxLayout
 
 
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)                 # 1
 
        self.color_btn = QPushButton('Color', self)      # 2
        self.font_btn = QPushButton('Font', self)
        self.color_btn.clicked.connect(lambda: self.open_dialog_func(self.color_btn))
        self.font_btn.clicked.connect(lambda: self.open_dialog_func(self.font_btn))
 
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.color_btn)
        self.h_layout.addWidget(self.font_btn)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)
 
    def open_dialog_func(self, btn):
        if btn == self.color_btn:                        # 3
            color = QColorDialog.getColor()
            if color.isValid():
                self.text_edit.setTextColor(color)
        else:                                            # 4
            font, ok = QFontDialog.getFont()
            if ok:
                self.text_edit.setFont(font)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
