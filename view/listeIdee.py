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
        DialogListeIdee.resize(400, 278)
        DialogListeIdee.setMinimumSize(QtCore.QSize(400, 278))
        DialogListeIdee.setMaximumSize(QtCore.QSize(400, 278))
        DialogListeIdee.setModal(True)
        self.buttonBoxListeIdee = QtWidgets.QDialogButtonBox(DialogListeIdee)
        self.buttonBoxListeIdee.setGeometry(QtCore.QRect(10, 240, 371, 32))
        self.buttonBoxListeIdee.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxListeIdee.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxListeIdee.setObjectName("buttonBoxListeIdee")
        self.listViewListeIdee = QtWidgets.QListView(DialogListeIdee)
        self.listViewListeIdee.setGeometry(QtCore.QRect(10, 10, 371, 201))
        self.listViewListeIdee.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewListeIdee.setWordWrap(True)
        self.listViewListeIdee.setObjectName("listViewListeIdee")
        self.buttonEditer = QtWidgets.QPushButton(DialogListeIdee)
        self.buttonEditer.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.buttonEditer.setObjectName("buttonEditer")

        self.retranslateUi(DialogListeIdee)
        self.buttonBoxListeIdee.accepted.connect(DialogListeIdee.accept)
        self.buttonBoxListeIdee.rejected.connect(DialogListeIdee.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogListeIdee)

    def retranslateUi(self, DialogListeIdee):
        _translate = QtCore.QCoreApplication.translate
        DialogListeIdee.setWindowTitle(_translate("DialogListeIdee", "Liste des idées"))
        self.buttonEditer.setText(_translate("DialogListeIdee", "Editer"))

