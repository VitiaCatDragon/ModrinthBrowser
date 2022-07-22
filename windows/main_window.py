# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setObjectName("searchBar")
        self.verticalLayout.addWidget(self.searchBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.version = QtWidgets.QComboBox(self.centralwidget)
        self.version.setObjectName("version")
        self.version.addItem("")
        self.horizontalLayout.addWidget(self.version)
        self.category = QtWidgets.QComboBox(self.centralwidget)
        self.category.setObjectName("category")
        self.category.addItem("")
        self.horizontalLayout.addWidget(self.category)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.page = QtWidgets.QSpinBox(self.centralwidget)
        self.page.setMinimumSize(QtCore.QSize(1085, 0))
        self.page.setWrapping(False)
        self.page.setFrame(True)
        self.page.setAlignment(QtCore.Qt.AlignCenter)
        self.page.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.page.setAccelerated(False)
        self.page.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.page.setProperty("showGroupSeparator", False)
        self.page.setMinimum(1)
        self.page.setMaximum(999)
        self.page.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.page.setObjectName("page")
        self.gridLayout.addWidget(self.page, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minusPage = QtWidgets.QToolButton(self.centralwidget)
        self.minusPage.setObjectName("minusPage")
        self.horizontalLayout_2.addWidget(self.minusPage)
        self.plusPage = QtWidgets.QToolButton(self.centralwidget)
        self.plusPage.setObjectName("plusPage")
        self.horizontalLayout_2.addWidget(self.plusPage)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.list = QtWidgets.QTableWidget(self.centralwidget)
        self.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.list.setObjectName("list")
        self.list.setColumnCount(9)
        self.list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.list.setHorizontalHeaderItem(8, item)
        self.gridLayout.addWidget(self.list, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 21))
        self.menubar.setObjectName("menubar")
        self.program = QtWidgets.QMenu(self.menubar)
        self.program.setTearOffEnabled(False)
        self.program.setObjectName("program")
        self.packsMenu = QtWidgets.QMenu(self.menubar)
        self.packsMenu.setObjectName("packsMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.action10 = QtWidgets.QAction(MainWindow)
        self.action10.setObjectName("action10")
        self.action20 = QtWidgets.QAction(MainWindow)
        self.action20.setObjectName("action20")
        self.action50 = QtWidgets.QAction(MainWindow)
        self.action50.setObjectName("action50")
        self.action75 = QtWidgets.QAction(MainWindow)
        self.action75.setObjectName("action75")
        self.action100 = QtWidgets.QAction(MainWindow)
        self.action100.setObjectName("action100")
        self.createPack = QtWidgets.QAction(MainWindow)
        self.createPack.setObjectName("createPack")
        self.program.addAction(self.settings)
        self.packsMenu.addAction(self.createPack)
        self.packsMenu.addSeparator()
        self.menubar.addAction(self.program.menuAction())
        self.menubar.addAction(self.packsMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modrinth Browser"))
        self.version.setCurrentText(_translate("MainWindow", "Любая"))
        self.version.setItemText(0, _translate("MainWindow", "Любая"))
        self.category.setItemText(0, _translate("MainWindow", "Любая"))
        self.page.setSuffix(_translate("MainWindow", " страница"))
        self.minusPage.setText(_translate("MainWindow", "<--"))
        self.plusPage.setText(_translate("MainWindow", "-->"))
        item = self.list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Иконка"))
        item = self.list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Версия"))
        item = self.list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Скачиваний"))
        item = self.list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Подписок"))
        item = self.list.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Клиент"))
        item = self.list.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Сервер"))
        item = self.list.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Автор"))
        item = self.list.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ID"))
        self.program.setTitle(_translate("MainWindow", "Программа"))
        self.packsMenu.setTitle(_translate("MainWindow", "Сборки"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.action10.setText(_translate("MainWindow", "10"))
        self.action20.setText(_translate("MainWindow", "20"))
        self.action50.setText(_translate("MainWindow", "50"))
        self.action75.setText(_translate("MainWindow", "75"))
        self.action100.setText(_translate("MainWindow", "100"))
        self.createPack.setText(_translate("MainWindow", "Создать"))
