# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindowPrincipale(object):
    def setupUi(self, WindowPrincipale):
        WindowPrincipale.setObjectName("WindowPrincipale")
        WindowPrincipale.resize(857, 643)
        WindowPrincipale.setMinimumSize(QtCore.QSize(857, 643))
        WindowPrincipale.setMaximumSize(QtCore.QSize(857, 643))
        self.centralwidget = QtWidgets.QWidget(WindowPrincipale)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(69, 169, 160, 63))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layoutToDoList = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutToDoList.setContentsMargins(0, 0, 0, 0)
        self.layoutToDoList.setObjectName("layoutToDoList")
        self.buttonConsulterToDoList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonConsulterToDoList.setObjectName("buttonConsulterToDoList")
        self.layoutToDoList.addWidget(self.buttonConsulterToDoList)
        self.labelCompteurIdeeTodo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCompteurIdeeTodo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCompteurIdeeTodo.setObjectName("labelCompteurIdeeTodo")
        self.layoutToDoList.addWidget(self.labelCompteurIdeeTodo)
        self.labelCompteurIdee_bis = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCompteurIdee_bis.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCompteurIdee_bis.setObjectName("labelCompteurIdee_bis")
        self.layoutToDoList.addWidget(self.labelCompteurIdee_bis)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 130, 111, 140))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layoutEtatNonAction = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutEtatNonAction.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.layoutEtatNonAction.setContentsMargins(0, 0, 0, 0)
        self.layoutEtatNonAction.setObjectName("layoutEtatNonAction")
        self.buttonCorbeille = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.buttonCorbeille.setAutoFillBackground(False)
        self.buttonCorbeille.setCheckable(False)
        self.buttonCorbeille.setFlat(False)
        self.buttonCorbeille.setObjectName("buttonCorbeille")
        self.layoutEtatNonAction.addWidget(self.buttonCorbeille)
        self.labelIdeeAttenteCorbeille = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelIdeeAttenteCorbeille.setObjectName("labelIdeeAttenteCorbeille")
        self.layoutEtatNonAction.addWidget(self.labelIdeeAttenteCorbeille)
        self.buttonEnattente = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.buttonEnattente.setEnabled(True)
        self.buttonEnattente.setObjectName("buttonEnattente")
        self.layoutEtatNonAction.addWidget(self.buttonEnattente)
        self.labelIdeeAttenteIncuabateur = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelIdeeAttenteIncuabateur.setObjectName("labelIdeeAttenteIncuabateur")
        self.layoutEtatNonAction.addWidget(self.labelIdeeAttenteIncuabateur)
        self.buttonArchive = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.buttonArchive.setObjectName("buttonArchive")
        self.layoutEtatNonAction.addWidget(self.buttonArchive)
        self.labelIdeeAttenteArchivage = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelIdeeAttenteArchivage.setObjectName("labelIdeeAttenteArchivage")
        self.layoutEtatNonAction.addWidget(self.labelIdeeAttenteArchivage)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(580, 360, 261, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layoutDelegue = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layoutDelegue.setContentsMargins(0, 0, 0, 0)
        self.layoutDelegue.setObjectName("layoutDelegue")
        self.labelDelegue = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelDelegue.setObjectName("labelDelegue")
        self.layoutDelegue.addWidget(self.labelDelegue)
        self.listDelegue = QtWidgets.QListView(self.verticalLayoutWidget_3)
        self.listDelegue.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listDelegue.setWordWrap(True)
        self.listDelegue.setObjectName("listDelegue")
        self.layoutDelegue.addWidget(self.listDelegue)
        self.buttonTermineDelegue = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.buttonTermineDelegue.setObjectName("buttonTermineDelegue")
        self.layoutDelegue.addWidget(self.buttonTermineDelegue)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(290, 360, 271, 191))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.layoutAFaire = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.layoutAFaire.setContentsMargins(0, 0, 0, 0)
        self.layoutAFaire.setObjectName("layoutAFaire")
        self.labelAFaire = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.labelAFaire.setObjectName("labelAFaire")
        self.layoutAFaire.addWidget(self.labelAFaire)
        self.listTodo = QtWidgets.QListView(self.verticalLayoutWidget_4)
        self.listTodo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listTodo.setWordWrap(True)
        self.listTodo.setObjectName("listTodo")
        self.layoutAFaire.addWidget(self.listTodo)
        self.buttonTerminerTodo = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.buttonTerminerTodo.setObjectName("buttonTerminerTodo")
        self.layoutAFaire.addWidget(self.buttonTerminerTodo)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 360, 271, 191))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.layoutPlanning = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.layoutPlanning.setContentsMargins(0, 0, 0, 0)
        self.layoutPlanning.setObjectName("layoutPlanning")
        self.labelPlanning = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.labelPlanning.setObjectName("labelPlanning")
        self.layoutPlanning.addWidget(self.labelPlanning)
        self.listPlanifier = QtWidgets.QListView(self.verticalLayoutWidget_5)
        self.listPlanifier.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listPlanifier.setWordWrap(True)
        self.listPlanifier.setObjectName("listPlanifier")
        self.layoutPlanning.addWidget(self.listPlanifier)
        self.buttonTerminerPlanifier = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.buttonTerminerPlanifier.setObjectName("buttonTerminerPlanifier")
        self.layoutPlanning.addWidget(self.buttonTerminerPlanifier)
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(140, 150, 20, 21))
        self.line1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(230, 180, 141, 16))
        self.line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setObjectName("line2")
        self.line6 = QtWidgets.QFrame(self.centralwidget)
        self.line6.setGeometry(QtCore.QRect(140, 300, 20, 61))
        self.line6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line6.setObjectName("line6")
        self.line7 = QtWidgets.QFrame(self.centralwidget)
        self.line7.setGeometry(QtCore.QRect(420, 280, 20, 81))
        self.line7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line7.setObjectName("line7")
        self.line8 = QtWidgets.QFrame(self.centralwidget)
        self.line8.setGeometry(QtCore.QRect(720, 300, 20, 61))
        self.line8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line8.setObjectName("line8")
        self.line2_2 = QtWidgets.QFrame(self.centralwidget)
        self.line2_2.setGeometry(QtCore.QRect(140, 240, 20, 41))
        self.line2_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line2_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2_2.setObjectName("line2_2")
        self.line5 = QtWidgets.QFrame(self.centralwidget)
        self.line5.setGeometry(QtCore.QRect(150, 290, 581, 16))
        self.line5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setObjectName("line5")
        self.line4 = QtWidgets.QFrame(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(150, 270, 281, 20))
        self.line4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setObjectName("line4")
        self.groupIdee = QtWidgets.QGroupBox(self.centralwidget)
        self.groupIdee.setGeometry(QtCore.QRect(10, 0, 331, 151))
        self.groupIdee.setObjectName("groupIdee")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupIdee)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 20, 321, 127))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layoutNouvelleIdee = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layoutNouvelleIdee.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layoutNouvelleIdee.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layoutNouvelleIdee.setContentsMargins(0, 0, 0, 0)
        self.layoutNouvelleIdee.setObjectName("layoutNouvelleIdee")
        self.TextIdee = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.TextIdee.setObjectName("TextIdee")
        self.layoutNouvelleIdee.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TextIdee)
        self.buttonAjouterToDoList = QtWidgets.QPushButton(self.formLayoutWidget)
        self.buttonAjouterToDoList.setObjectName("buttonAjouterToDoList")
        self.layoutNouvelleIdee.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonAjouterToDoList)
        self.buttonTacehFini = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTacehFini.setGeometry(QtCore.QRect(340, 570, 141, 23))
        self.buttonTacehFini.setObjectName("buttonTacehFini")
        self.labelDateToday = QtWidgets.QLabel(self.centralwidget)
        self.labelDateToday.setGeometry(QtCore.QRect(10, 340, 131, 16))
        self.labelDateToday.setText("")
        self.labelDateToday.setObjectName("labelDateToday")
        WindowPrincipale.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowPrincipale)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        WindowPrincipale.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowPrincipale)
        self.statusbar.setObjectName("statusbar")
        WindowPrincipale.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(WindowPrincipale)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionA_propos_de = QtWidgets.QAction(WindowPrincipale)
        self.actionA_propos_de.setObjectName("actionA_propos_de")
        self.menuFichier.addAction(self.actionQuitter)
        self.menuAide.addAction(self.actionA_propos_de)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(WindowPrincipale)
        self.actionQuitter.triggered.connect(WindowPrincipale.close)
        QtCore.QMetaObject.connectSlotsByName(WindowPrincipale)

    def retranslateUi(self, WindowPrincipale):
        _translate = QtCore.QCoreApplication.translate
        WindowPrincipale.setWindowTitle(_translate("WindowPrincipale", "Getting things done"))
        self.buttonConsulterToDoList.setText(_translate("WindowPrincipale", "Consulter ma ToDo List"))
        self.labelCompteurIdeeTodo.setText(_translate("WindowPrincipale", "X idées en attente"))
        self.labelCompteurIdee_bis.setText(_translate("WindowPrincipale", "X idées en attente"))
        self.buttonCorbeille.setText(_translate("WindowPrincipale", "Corbeille"))
        self.labelIdeeAttenteCorbeille.setText(_translate("WindowPrincipale", "(x) idée en attente"))
        self.buttonEnattente.setText(_translate("WindowPrincipale", "Incubateur"))
        self.labelIdeeAttenteIncuabateur.setText(_translate("WindowPrincipale", "(x) idée en attente"))
        self.buttonArchive.setText(_translate("WindowPrincipale", "Archivage"))
        self.labelIdeeAttenteArchivage.setText(_translate("WindowPrincipale", "(x) idée en attente"))
        self.labelDelegue.setText(_translate("WindowPrincipale", "Actions déléguées"))
        self.buttonTermineDelegue.setText(_translate("WindowPrincipale", "Marqué comme terminé"))
        self.labelAFaire.setText(_translate("WindowPrincipale", "A faire"))
        self.buttonTerminerTodo.setText(_translate("WindowPrincipale", "Marqué comme terminé"))
        self.labelPlanning.setText(_translate("WindowPrincipale", "Planning"))
        self.buttonTerminerPlanifier.setText(_translate("WindowPrincipale", "Marqué comme terminé"))
        self.groupIdee.setTitle(_translate("WindowPrincipale", "Mon idée :"))
        self.buttonAjouterToDoList.setText(_translate("WindowPrincipale", "Ajouter à la ToDo List"))
        self.buttonTacehFini.setText(_translate("WindowPrincipale", "Voir les taches terminées"))
        self.menuFichier.setTitle(_translate("WindowPrincipale", "Fichier"))
        self.menuAide.setTitle(_translate("WindowPrincipale", "Aide"))
        self.actionQuitter.setText(_translate("WindowPrincipale", "Quitter"))
        self.actionA_propos_de.setText(_translate("WindowPrincipale", "A propos de..."))

