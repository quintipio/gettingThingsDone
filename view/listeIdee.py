# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListeIdee.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogListeIdee(object):
    def setupUi(self, DialogListeIdee):
        DialogListeIdee.setObjectName("DialogListeIdee")
        DialogListeIdee.resize(400, 300)
        self.buttonBoxListeIdee = QtWidgets.QDialogButtonBox(DialogListeIdee)
        self.buttonBoxListeIdee.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBoxListeIdee.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxListeIdee.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxListeIdee.setObjectName("buttonBoxListeIdee")
        self.tableListeIdee = QtWidgets.QTableView(DialogListeIdee)
        self.tableListeIdee.setGeometry(QtCore.QRect(10, 10, 381, 231))
        self.tableListeIdee.setObjectName("tableListeIdee")

        self.retranslateUi(DialogListeIdee)
        self.buttonBoxListeIdee.accepted.connect(DialogListeIdee.accept)
        self.buttonBoxListeIdee.rejected.connect(DialogListeIdee.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogListeIdee)

    def retranslateUi(self, DialogListeIdee):
        _translate = QtCore.QCoreApplication.translate
        DialogListeIdee.setWindowTitle(_translate("DialogListeIdee", "Dialog"))

