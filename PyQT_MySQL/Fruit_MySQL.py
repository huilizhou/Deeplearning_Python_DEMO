import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView, QDialogButtonBox


class Demo(QTableView):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()
        self.sql_exec()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('fruitpricedb')
        self.db.setUserName('root')
        self.db.setPassword('')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection',
                                 self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()

    def sql_exec(self):
        model = QSqlTableModel()
        model.setTable('fruittb')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, 'id')
        model.setHeaderData(1, Qt.Horizontal, 'name')
        model.setHeaderData(2, Qt.Horizontal, 'price')
        model.select()

        self.setModel(model)

        prices = []
        for i in range(model.rowCount()):               # 3
            # id = model.record(i).value('id')
            # name = model.record(i).value(1)
            price = model.record(i).value('price')
            # print(id, name, price)
            prices.append(price)
        print(prices)
        # return prices
        # print('---------------------')

        # for i in range(model.rowCount()):               # 4
        #     id = model.data(model.index(i, 0))
        #     name = model.data(model.index(i, 1))
        #     print(id, name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
