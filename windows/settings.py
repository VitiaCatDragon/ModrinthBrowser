# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(593, 210)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.minecraftPath = QtWidgets.QLineEdit(Dialog)
        self.minecraftPath.setReadOnly(True)
        self.minecraftPath.setObjectName("minecraftPath")
        self.verticalLayout.addWidget(self.minecraftPath)
        self.minecraftPathVariants = QtWidgets.QComboBox(Dialog)
        self.minecraftPathVariants.setObjectName("minecraftPathVariants")
        self.verticalLayout.addWidget(self.minecraftPathVariants)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.iconsInTable = QtWidgets.QCheckBox(Dialog)
        self.iconsInTable.setChecked(True)
        self.iconsInTable.setObjectName("iconsInTable")
        self.verticalLayout_2.addWidget(self.iconsInTable)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.rowsCount = QtWidgets.QComboBox(Dialog)
        self.rowsCount.setObjectName("rowsCount")
        self.rowsCount.addItem("")
        self.rowsCount.addItem("")
        self.rowsCount.addItem("")
        self.rowsCount.addItem("")
        self.verticalLayout_2.addWidget(self.rowsCount)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.label.setText(_translate("Dialog", "Путь к папке .minecraft:"))
        self.minecraftPath.setPlaceholderText(_translate("Dialog", ".minecraft"))
        self.iconsInTable.setText(_translate("Dialog", "Иконки в таблице"))
        self.label_2.setText(_translate("Dialog", "Кол-во строк"))
        self.rowsCount.setItemText(0, _translate("Dialog", "20"))
        self.rowsCount.setItemText(1, _translate("Dialog", "50"))
        self.rowsCount.setItemText(2, _translate("Dialog", "75"))
        self.rowsCount.setItemText(3, _translate("Dialog", "100"))
