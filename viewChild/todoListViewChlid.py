from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets

from view.todoList import Ui_DialogToDoList
from controller import todoListController as ControllerView
from viewChild.dialogDelegueViewChild import DialogDelegueViewChild
from viewChild.editerIdeeViewChild import EditerIdeeViewChild
from viewChild.gererActionViewChild import GererActionViewChild


class TodoListViewChlid(Ui_DialogToDoList):

    RoleIdee = Qt.UserRole+1

    def __init__(self):
        self.selected_idee = None
        self.dialog = None

    def setupUi(self, dialog_todo_list):
        """
        Charge la fenêtre
        :param dialog_todo_list: la boite de dialogue
        :return:
        """
        Ui_DialogToDoList.setupUi(self, dialog_todo_list)
        self.toDoListListView.clicked.connect(self.__select_element_listbox)
        self.toDoListListView.doubleClicked.connect(self.__open_idee)
        self.buttonJeter.clicked.connect(self.__jeter_idee)
        self.buttonReferencer.clicked.connect(self.__classer_idee)
        self.buttonMediter.clicked.connect(self.__incuber_idee)
        self.buttonDeleguer.clicked.connect(self.__delegue_idee)
        self.buttonDefinirActions.clicked.connect(self.__definir_etape_idee)
        self.dialog = dialog_todo_list
        self.__charger_todo_list()

    def __charger_todo_list(self):
        """
        Charge la liste des idées
        :return:
        """
        liste = ControllerView.charger_todo_liste()
        model = QStandardItemModel(self.toDoListListView)
        model.clear()
        for todo in liste:
            item = QStandardItem(todo.texte if ControllerView.check_idee_define(todo.id)
                                 else todo.texte + " - A DEFINIR -")
            item.setData(todo, self.RoleIdee)
            model.appendRow(item)
        self.toDoListListView.setModel(model)
        self.toDoListListView.show()

    def __select_element_listbox(self, index: QStandardItem):
        """
        Evenement de sélection d'une idée
        :param index:
        :return:
        """
        self.selected_idee = index.data(self.RoleIdee)

    def __classer_idee(self):
        """
        Classe une idée
        :return:
        """
        ControllerView.idee_etat_classer(self.selected_idee)
        self.__charger_todo_list()

    def __jeter_idee(self):
        """
        Met à la corbeille une idée
        :return:
        """
        ControllerView.idee_etat_corbeille(self.selected_idee)
        self.__charger_todo_list()

    def __incuber_idee(self):
        """
        Met à l'état incuber une idée
        :return:
        """
        ControllerView.idee_etat_incuber(self.selected_idee)
        self.__charger_todo_list()

    def __delegue_idee(self):
        """
        Délègue une idée
        :return:
        """
        if self.selected_idee:
            dialog_delegue = QtWidgets.QDialog(self.dialog)
            ui = DialogDelegueViewChild()
            ui.setup_ui_with_idee(dialog_delegue, self.selected_idee)
            retour = dialog_delegue.exec_()
            if retour:
                self.__charger_todo_list()

    def __definir_etape_idee(self):
        """
        Ouvre la dialog de gestion des étapes d'une idée
        :return:
        """
        if self.selected_idee:
            dialog_etapes = QtWidgets.QDialog(self.dialog)
            ui = GererActionViewChild()
            ui.setup_ui_with_idee(dialog_etapes, self.selected_idee)
            dialog_etapes.exec_()
            self.__charger_todo_list()

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
            self.__charger_todo_list()
