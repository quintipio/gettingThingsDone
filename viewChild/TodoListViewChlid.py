from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtWidgets

from view.todoList import Ui_DialogToDoList
from controller import TodoListController as controller
from viewChild.DialogDelegueViewChild import DialogDelegueViewChild


class TodoListViewChlid(Ui_DialogToDoList):

    RoleIdee = Qt.UserRole+1

    def __init__(self):
        self.selectedIdee = None
        self.dialog = None

    def setupUi(self, dialog_todo_list):
        Ui_DialogToDoList.setupUi(self, dialog_todo_list)
        self.toDoListListView.clicked.connect(self.__select_element_listbox)
        self.buttonJeter.clicked.connect(self.__jeter_idee)
        self.buttonReferencer.clicked.connect(self.__classer_idee)
        self.buttonMediter.clicked.connect(self.__incuber_idee)
        self.buttonDeleguer.clicked.connect(self.__delegueIdee)
        self.dialog = dialog_todo_list
        self.__charger_todo_list()

    def __charger_todo_list(self):
        liste = controller.charger_todo_liste()
        model = QStandardItemModel(self.toDoListListView)
        model.clear()
        for todo in liste:
            item = QStandardItem(todo.texte)
            item.setData(todo, self.RoleIdee)
            model.appendRow(item)
        self.toDoListListView.setModel(model)
        self.toDoListListView.show()

    def __select_element_listbox(self, index: QStandardItem):
        self.selectedIdee = index.data(self.RoleIdee)

    def __classer_idee(self):
        controller.idee_etat_classer(self.selectedIdee)
        self.__charger_todo_list()

    def __jeter_idee(self):
        controller.idee_etat_corbeille(self.selectedIdee)
        self.__charger_todo_list()

    def __incuber_idee(self):
        controller.idee_etat_incuber(self.selectedIdee)
        self.__charger_todo_list()

    def __delegueIdee(self):
        if self.selectedIdee:
            dialog_delegue = QtWidgets.QDialog(self.dialog)
            ui = DialogDelegueViewChild()
            ui.setup_ui_with_idee(dialog_delegue, self.selectedIdee)
            dialog_delegue.show()
            retour = dialog_delegue.exec_()
            if retour:
               self.__charger_todo_list()

    def __definir_etape_idee(self):
        print("TODO")


