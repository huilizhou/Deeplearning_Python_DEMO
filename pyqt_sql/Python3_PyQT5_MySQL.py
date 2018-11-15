#!/usr/bin/env python3
import os
import sys
from PyQt5.QtCore import (QFile, QVariant, Qt)
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QMenu,
                             QMessageBox, QTableView, QVBoxLayout)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel)

MAC = True
try:
    from PyQt5.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

ID, NAME, Description, AGE = range(4)


class ReferenceDataDlg(QDialog):

    def __init__(self, parent=None):
        super(ReferenceDataDlg, self).__init__(parent)

        self.model = QSqlTableModel(self)
        self.model.setTable("reference")
        self.model.setSort(ID, Qt.AscendingOrder)
        self.model.setHeaderData(ID, Qt.Horizontal, "ID")
        self.model.setHeaderData(NAME, Qt.Horizontal, "NAME")
        self.model.setHeaderData(Description, Qt.Horizontal, "Description")
        self.model.setHeaderData(AGE, Qt.Horizontal, "AGE")
        self.model.select()

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSelectionMode(QTableView.SingleSelection)
        self.view.setSelectionBehavior(QTableView.SelectRows)
        self.view.setColumnHidden(ID, True)
        self.view.resizeColumnsToContents()

        buttonBox = QDialogButtonBox()
        addButton = buttonBox.addButton("&Add",
                                        QDialogButtonBox.ActionRole)
        deleteButton = buttonBox.addButton("&Delete",
                                           QDialogButtonBox.ActionRole)
        sortButton = buttonBox.addButton("&Sort",
                                         QDialogButtonBox.ActionRole)
        if not MAC:
            addButton.setFocusPolicy(Qt.NoFocus)
            deleteButton.setFocusPolicy(Qt.NoFocus)
            sortButton.setFocusPolicy(Qt.NoFocus)

        menu = QMenu(self)
        sortByNAMEAction = menu.addAction("Sort by &NAME")
        sortByDescriptionAction = menu.addAction("Sort by &Description")
        sortByIDAction = menu.addAction("Sort by &ID")
        sortButton.setMenu(menu)
        closeButton = buttonBox.addButton(QDialogButtonBox.Close)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

        addButton.clicked.connect(self.addRecord)
        deleteButton.clicked.connect(self.deleteRecord)
        sortByNAMEAction.triggered.connect(lambda: self.sort(NAME))
        sortByDescriptionAction.triggered.connect(
            lambda: self.sort(Description))
        sortByIDAction.triggered.connect(lambda: self.sort(ID))
        closeButton.clicked.connect(self.accept)
        self.setWindowTitle("数据库小程序")

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, NAME)
        self.view.setCurrentIndex(index)
        self.view.edit(index)

    def deleteRecord(self):
        index = self.view.currentIndex()
        if not index.isValid():
            return
        record = self.model.record(index.row())
        NAME = record.value(NAME)
        desc = record.value(Description)
        if (QMessageBox.question(self, "数据库小程序",
                                 ("Delete {0} from NAME {1}?"
                                  .format(desc, NAME)),
                                 QMessageBox.Yes | QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRow(index.row())
        self.model.submitAll()
        self.model.select()

    def sort(self, column):
        self.model.setSort(column, Qt.AscendingOrder)
        self.model.select()


def main():
    app = QApplication(sys.argv)

    filename = os.path.join(os.path.dirname(__file__), "reference.db")
    create = not QFile.exists(filename)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(None, "数据库小程序",
                            "Database Error: {0}".format(db.lastError().text()))
        sys.exit(1)

    if create:
        query = QSqlQuery()
        query.exec_("""CREATE TABLE reference (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                NAME VARCHAR(30) NOT NULL,
                Description VARCHAR(20) NOT NULL,
                AGE VARCHAR(80))""")

    form = ReferenceDataDlg()
    form.show()
    sys.exit(app.exec_())


main()
