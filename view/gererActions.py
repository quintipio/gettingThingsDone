# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GererActions.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogGererActions(object):
    def setupUi(self, DialogGererActions):
        DialogGererActions.setObjectName("DialogGererActions")
        DialogGererActions.resize(515, 505)
        self.listeEtape = QtWidgets.QListView(DialogGererActions)
        self.listeEtape.setGeometry(QtCore.QRect(13, 12, 479, 261))
        self.listeEtape.setObjectName("listeEtape")
        self.horizontalLayoutWidget = QtWidgets.QWidget(DialogGererActions)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(13, 281, 479, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutEtape = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutEtape.setContentsMargins(0, 0, 0, 0)
        self.layoutEtape.setObjectName("layoutEtape")
        self.layoutSaisie = QtWidgets.QFormLayout()
        self.layoutSaisie.setObjectName("layoutSaisie")
        self.labelOrdre = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelOrdre.setObjectName("labelOrdre")
        self.layoutSaisie.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelOrdre)
        self.textOrdre = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.textOrdre.setObjectName("textOrdre")
        self.layoutSaisie.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textOrdre)
        self.labelEtape = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelEtape.setObjectName("labelEtape")
        self.layoutSaisie.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelEtape)
        self.textEtape = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEtape.setObjectName("textEtape")
        self.layoutSaisie.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEtape)
        self.labelDate = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelDate.setObjectName("labelDate")
        self.layoutSaisie.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelDate)
        self.inputDate = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.inputDate.setObjectName("inputDate")
        self.layoutSaisie.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.inputDate)
        self.buttonAjouterModifier = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonAjouterModifier.setObjectName("buttonAjouterModifier")
        self.layoutSaisie.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.buttonAjouterModifier)
        self.layoutEtape.addLayout(self.layoutSaisie)
        self.buttonCHeck = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonCHeck.setObjectName("buttonCHeck")
        self.layoutEtape.addWidget(self.buttonCHeck)
        self.buttonDialog = QtWidgets.QDialogButtonBox(DialogGererActions)
        self.buttonDialog.setGeometry(QtCore.QRect(13, 468, 481, 31))
        self.buttonDialog.setOrientation(QtCore.Qt.Horizontal)
        self.buttonDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonDialog.setObjectName("buttonDialog")

        self.retranslateUi(DialogGererActions)
        self.buttonDialog.accepted.connect(DialogGererActions.accept)
        self.buttonDialog.rejected.connect(DialogGererActions.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogGererActions)

    def retranslateUi(self, DialogGererActions):
        _translate = QtCore.QCoreApplication.translate
        DialogGererActions.setWindowTitle(_translate("DialogGererActions", "Gérer les étapes"))
        self.labelOrdre.setText(_translate("DialogGererActions", "Ordre"))
        self.labelEtape.setText(_translate("DialogGererActions", "Etape"))
        self.labelDate.setText(_translate("DialogGererActions", "Date"))
        self.buttonAjouterModifier.setText(_translate("DialogGererActions", "Ajouter"))
        self.buttonCHeck.setText(_translate("DialogGererActions", "Fait"))

