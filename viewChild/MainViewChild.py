from view.mainView import Ui_WindowPrincipale
from PyQt5 import QtWidgets

from viewChild.AppdViewChild import AppdChild
from viewChild.TodoListViewChlid import TodoListViewChlid
from models import Etat
from controller import MainViewController as controller


class MainViewChild(Ui_WindowPrincipale):

    phrase_compteur = " idées en attente"

    def __init__(self):
        Ui_WindowPrincipale.__init__(self)
        self.window: Ui_WindowPrincipale = None

    def setupUi(self, window_principale):
        self.window = window_principale
        Ui_WindowPrincipale.setupUi(self, window_principale)

        self.actionA_propos_de.triggered.connect(self.__dialog_appd)
        self.buttonAjouterToDoList.clicked.connect(self.__ajouter_idee)
        self.buttonConsulterToDoList.clicked.connect(self.__dialog_todolist)

        self.rafraichir_element_vue()

    def __dialog_appd(self):
        dialog_appd = QtWidgets.QDialog(parent=self.window)
        ui = AppdChild()
        ui.setupUi(dialog_appd)
        dialog_appd.show()
        dialog_appd.exec_()

    def __dialog_todolist(self):
        dialog_todolist = QtWidgets.QDialog(parent=self.window)
        ui = TodoListViewChlid()
        ui.setupUi(dialog_todolist)
        dialog_todolist.show()
        dialog_todolist.exec_()
        self.rafraichir_element_vue()

    def __ajouter_idee(self):
        if self.TextIdee.toPlainText():
            controller.ajouter_idee_fm_view(self.TextIdee.toPlainText())
            self.rafraichir_element_vue()
            self.TextIdee.clear()

    def rafraichir_element_vue(self):
        compteur = controller.compter_idee_par_etat()
        self.labelCompteurIdeeTodo.setText(str(compteur[Etat.TODO.name]) + self.phrase_compteur)
        self.labelIdeeAttenteCorbeille.setText(str(compteur[Etat.CORBEILLE.name]) + self.phrase_compteur)
        self.labelIdeeAttenteArchivage.setText(str(compteur[Etat.CLASSER.name]) + self.phrase_compteur)
        self.labelIdeeAttenteIncuabateur.setText(str(compteur[Etat.INCUBATEUR.name]) + self.phrase_compteur)