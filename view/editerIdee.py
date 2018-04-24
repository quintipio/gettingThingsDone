# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditerIdee.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogEditerIdee(object):
    def setupUi(self, DialogEditerIdee):
        DialogEditerIdee.setObjectName("DialogEditerIdee")
        DialogEditerIdee.resize(404, 401)
        self.formLayoutWidget = QtWidgets.QWidget(DialogEditerIdee)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 381))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layoutMain = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layoutMain.setContentsMargins(0, 0, 0, 0)
        self.layoutMain.setObjectName("layoutMain")
        self.labelDateDesc = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDateDesc.setObjectName("labelDateDesc")
        self.layoutMain.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDateDesc)
        self.labelDate = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDate.setText("")
        self.labelDate.setObjectName("labelDate")
        self.layoutMain.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelDate)
        self.labelIdee = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelIdee.setObjectName("labelIdee")
        self.layoutMain.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelIdee)
        self.textIdee = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.textIdee.setObjectName("textIdee")
        self.layoutMain.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textIdee)
        self.labelDelegue = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelDelegue.setObjectName("labelDelegue")
        self.layoutMain.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelDelegue)
        self.textDelegue = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.textDelegue.setObjectName("textDelegue")
        self.layoutMain.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textDelegue)
        self.labelCommentaire = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelCommentaire.setObjectName("labelCommentaire")
        self.layoutMain.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelCommentaire)
        self.textCommentaire = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.textCommentaire.setObjectName("textCommentaire")
        self.layoutMain.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textCommentaire)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutMain.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.labelEmplacement = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelEmplacement.setObjectName("labelEmplacement")
        self.layoutMain.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelEmplacement)
        self.comboEtat = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboEtat.setObjectName("comboEtat")
        self.layoutMain.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboEtat)

        self.retranslateUi(DialogEditerIdee)
        self.buttonBox.accepted.connect(DialogEditerIdee.accept)
        self.buttonBox.rejected.connect(DialogEditerIdee.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogEditerIdee)

    def retranslateUi(self, DialogEditerIdee):
        _translate = QtCore.QCoreApplication.translate
        DialogEditerIdee.setWindowTitle(_translate("DialogEditerIdee", "Editer une idée"))
        self.labelDateDesc.setText(_translate("DialogEditerIdee", "Date :"))
        self.labelIdee.setText(_translate("DialogEditerIdee", "Idée :"))
        self.labelDelegue.setText(_translate("DialogEditerIdee", "Délégué  à:"))
        self.labelCommentaire.setText(_translate("DialogEditerIdee", "Commentaire :"))
        self.labelEmplacement.setText(_translate("DialogEditerIdee", "Emplacement :"))

