# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogDelegue.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogDelegue(object):
    def setupUi(self, DialogDelegue):
        DialogDelegue.setObjectName("DialogDelegue")
        DialogDelegue.resize(184, 107)
        DialogDelegue.setMinimumSize(QtCore.QSize(184, 107))
        DialogDelegue.setMaximumSize(QtCore.QSize(184, 107))
        DialogDelegue.setSizeGripEnabled(True)
        DialogDelegue.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(DialogDelegue)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDelegue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelDelegue.setObjectName("labelDelegue")
        self.verticalLayout.addWidget(self.labelDelegue)
        self.textDelegue = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.textDelegue.setObjectName("textDelegue")
        self.verticalLayout.addWidget(self.textDelegue)
        self.buttonDelegue = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonDelegue.setOrientation(QtCore.Qt.Horizontal)
        self.buttonDelegue.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonDelegue.setObjectName("buttonDelegue")
        self.verticalLayout.addWidget(self.buttonDelegue)

        self.retranslateUi(DialogDelegue)
        self.buttonDelegue.accepted.connect(DialogDelegue.accept)
        self.buttonDelegue.rejected.connect(DialogDelegue.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDelegue)

    def retranslateUi(self, DialogDelegue):
        _translate = QtCore.QCoreApplication.translate
        DialogDelegue.setWindowTitle(_translate("DialogDelegue", "Dialog"))
        self.labelDelegue.setText(_translate("DialogDelegue", "Délégué à qui ?"))

