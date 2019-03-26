import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QLabel, QHBoxLayout, QAbstractItemView


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.item_list = ['item %s' % i for i in range(11)]         # 1
        self.model_1 = QStringListModel(self)
        self.model_1.setStringList(self.item_list)

        self.model_2 = QStringListModel(self)                       # 2

        self.listview_1 = QListView(self)                           # 3
        self.listview_1.setModel(self.model_1)
        self.listview_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listview_1.doubleClicked.connect(
            lambda: self.change_func(self.listview_1))

        self.listview_2 = QListView(self)                           # 4
        self.listview_2.setModel(self.model_2)
        self.listview_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listview_2.doubleClicked.connect(
            lambda: self.change_func(self.listview_2))

        self.pic_label = QLabel(self)                               # 5
        self.pic_label.setPixmap(QPixmap('arrow.png'))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listview_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listview_2)
        self.setLayout(self.h_layout)

    def change_func(self, listview):
        if listview == self.listview_1:                             # 6
            self.model_2.insertRows(self.model_2.rowCount(), 1)

            data = self.listview_1.currentIndex().data()
            index = self.model_2.index(self.model_2.rowCount() - 1)
            self.model_2.setData(index, data)
        else:                                                       # 7
            self.model_2.removeRows(self.listview_2.currentIndex().row(), 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
