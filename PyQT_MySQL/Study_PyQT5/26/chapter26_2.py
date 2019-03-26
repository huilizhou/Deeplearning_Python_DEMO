import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')     # 1
        self.db.setHostName('localhost')                 # 2
        self.db.setDatabaseName('test_db')               # 3
        self.db.setUserName('root')                      # 4
        self.db.setPassword('')                    # 5
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection',
                                 self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
