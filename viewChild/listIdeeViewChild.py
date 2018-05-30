from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

from models import Etat
from view.listeIdee import Ui_DialogListeIdee
from controller import listeIdeeController as ControllerView
from viewChild.editerIdeeViewChild import EditerIdeeViewChild


class ListeIdeeViewChild(Ui_DialogListeIdee):

    role_idee = Qt.UserRole + 3

    def __init__(self):
        self.dialog = None
        self.etat: Etat = None
        self.selected_idee = None

    def setup_ui_with_etat(self, dialog_liste_idee, etat: Etat):
        """
        Charge la fenêtre
        :param dialog_liste_idee: la boite de dialogue
        :param etat: l'état des idées à afficher
        :return:
        """
        Ui_DialogListeIdee.setupUi(self, dialog_liste_idee)

        self.buttonEditer.clicked.connect(self.__open_idee)
        self.listViewListeIdee.clicked.connect(self.__select_idee)
        self.listViewListeIdee.doubleClicked.connect(self.__open_idee)

        self.dialog = dialog_liste_idee
        self.etat = etat

        self.__charger_liste()

    def __charger_liste(self):
        """
        Charge la liste des idées à afficher
        :return:
        """
        data = ControllerView.charger_idees_par_etat(self.etat)
        model = QStandardItemModel(self.listViewListeIdee)
        model.clear()
        for todo in data:
            item = QStandardItem(todo.texte)
            item.setData(todo, self.role_idee)
            model.appendRow(item)
        self.listViewListeIdee.setModel(model)
        self.listViewListeIdee.show()

    def __select_idee(self, index: QStandardItem):
        """
        event de sélection d'une idée
        :param index:
        :return:
        """
        self.selected_idee = index.data(self.role_idee)

    def __open_idee(self):
        """
        Ouvre une idée à modifier
        :return:
        """
        if self.selected_idee:
            dialog_editer_idee = QtWidgets.QDialog(self.dialog)
            ui = EditerIdeeViewChild()
            ui.setup_ui_with_idee(dialog_editer_idee, self.selected_idee)
            dialog_editer_idee.exec_()
            self.__charger_liste()
