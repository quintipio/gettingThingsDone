# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToDoList.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogToDoList(object):
    def setupUi(self, DialogToDoList):
        DialogToDoList.setObjectName("DialogToDoList")
        DialogToDoList.setWindowModality(QtCore.Qt.WindowModal)
        DialogToDoList.resize(340, 359)
        DialogToDoList.setMinimumSize(QtCore.QSize(340, 359))
        DialogToDoList.setMaximumSize(QtCore.QSize(340, 359))
        DialogToDoList.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(DialogToDoList)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 320, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutPrincipal = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutPrincipal.setContentsMargins(0, 0, 0, 0)
        self.layoutPrincipal.setObjectName("layoutPrincipal")
        self.toDoListListView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.toDoListListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.toDoListListView.setWordWrap(True)
        self.toDoListListView.setObjectName("toDoListListView")
        self.layoutPrincipal.addWidget(self.toDoListListView)
        self.layoutBoutons = QtWidgets.QHBoxLayout()
        self.layoutBoutons.setObjectName("layoutBoutons")
        self.buttonReferencer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonReferencer.setObjectName("buttonReferencer")
        self.layoutBoutons.addWidget(self.buttonReferencer)
        self.buttonMediter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonMediter.setObjectName("buttonMediter")
        self.layoutBoutons.addWidget(self.buttonMediter)
        self.buttonJeter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonJeter.setObjectName("buttonJeter")
        self.layoutBoutons.addWidget(self.buttonJeter)
        self.layoutPrincipal.addLayout(self.layoutBoutons)
        self.buttonDefinirActions = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonDefinirActions.setObjectName("buttonDefinirActions")
        self.layoutPrincipal.addWidget(self.buttonDefinirActions)
        self.buttonDeleguer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonDeleguer.setObjectName("buttonDeleguer")
        self.layoutPrincipal.addWidget(self.buttonDeleguer)
        self.buttonTerminer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonTerminer.setObjectName("buttonTerminer")
        self.layoutPrincipal.addWidget(self.buttonTerminer)

        self.retranslateUi(DialogToDoList)
        self.buttonTerminer.clicked.connect(DialogToDoList.close)
        QtCore.QMetaObject.connectSlotsByName(DialogToDoList)

    def retranslateUi(self, DialogToDoList):
        _translate = QtCore.QCoreApplication.translate
        DialogToDoList.setWindowTitle(_translate("DialogToDoList", "ToDo Liste"))
        self.buttonReferencer.setText(_translate("DialogToDoList", "Référencer"))
        self.buttonMediter.setText(_translate("DialogToDoList", "A méditer..."))
        self.buttonJeter.setText(_translate("DialogToDoList", "Jeter"))
        self.buttonDefinirActions.setText(_translate("DialogToDoList", "Définir les étapes"))
        self.buttonDeleguer.setText(_translate("DialogToDoList", "Déléguer"))
        self.buttonTerminer.setText(_translate("DialogToDoList", "Terminer"))

