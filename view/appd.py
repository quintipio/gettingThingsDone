# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appd.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAppd(object):
    def setupUi(self, DialogAppd):
        DialogAppd.setObjectName("DialogAppd")
        DialogAppd.resize(264, 135)
        self.formLayoutWidget = QtWidgets.QWidget(DialogAppd)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layoutAppd = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layoutAppd.setContentsMargins(0, 0, 0, 0)
        self.layoutAppd.setObjectName("layoutAppd")
        self.labelAppDesc = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelAppDesc.setObjectName("labelAppDesc")
        self.layoutAppd.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelAppDesc)
        self.labelApp = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelApp.setText("")
        self.labelApp.setObjectName("labelApp")
        self.layoutAppd.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelApp)
        self.labelVersionDesc = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelVersionDesc.setObjectName("labelVersionDesc")
        self.layoutAppd.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelVersionDesc)
        self.labelVersion = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelVersion.setText("")
        self.labelVersion.setObjectName("labelVersion")
        self.layoutAppd.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelVersion)
        self.labelDevDesc = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDevDesc.setObjectName("labelDevDesc")
        self.layoutAppd.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelDevDesc)
        self.labelDev = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDev.setText("")
        self.labelDev.setObjectName("labelDev")
        self.layoutAppd.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelDev)
        self.labelCopyDesc = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCopyDesc.setObjectName("labelCopyDesc")
        self.layoutAppd.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCopyDesc)
        self.labelCopy = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCopy.setText("")
        self.labelCopy.setObjectName("labelCopy")
        self.layoutAppd.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelCopy)
        self.buttonFermer = QtWidgets.QPushButton(self.formLayoutWidget)
        self.buttonFermer.setObjectName("buttonFermer")
        self.layoutAppd.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.buttonFermer)

        self.retranslateUi(DialogAppd)
        QtCore.QMetaObject.connectSlotsByName(DialogAppd)

    def retranslateUi(self, DialogAppd):
        _translate = QtCore.QCoreApplication.translate
        DialogAppd.setWindowTitle(_translate("DialogAppd", "A propos de..."))
        self.labelAppDesc.setText(_translate("DialogAppd", "Application"))
        self.labelVersionDesc.setText(_translate("DialogAppd", "Version"))
        self.labelDevDesc.setText(_translate("DialogAppd", "Développeur"))
        self.labelCopyDesc.setText(_translate("DialogAppd", "CopyRight"))
        self.buttonFermer.setText(_translate("DialogAppd", "Fermer"))

