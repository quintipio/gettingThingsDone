from PyQt5.QtGui import QStandardItemModel, QStandardItem

from view.mainView import Ui_WindowPrincipale
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from viewChild.AppdViewChild import AppdChild
from viewChild.EditerIdeeViewChild import EditerIdeeViewChild
from viewChild.ListIdeeViewChild import ListeIdeeViewChild
from viewChild.TodoListViewChlid import TodoListViewChlid
from models import Etat
import datetime
from controller import MainViewController as ControllerView


class MainViewChild(Ui_WindowPrincipale):

    phrase_compteur = " idées en attente"

    role_idee = Qt.UserRole + 6

    def __init__(self):
        Ui_WindowPrincipale.__init__(self)
        self.window: Ui_WindowPrincipale = None
        self.selected_idee_delegue = None
        self.selected_etape_todo = None
        self.selected_idee_planifie = None

    def setupUi(self, window_principale):
        """
        Charge la fenêtre
        :param window_principale: la fenêtre
        :return:
        """
        self.window = window_principale
        Ui_WindowPrincipale.setupUi(self, window_principale)

        self.actionA_propos_de.triggered.connect(self.__dialog_appd)

        self.buttonAjouterToDoList.clicked.connect(self.__ajouter_idee)
        self.buttonConsulterToDoList.clicked.connect(self.__dialog_todolist)
        self.buttonEnattente.clicked.connect(self.__consulter_idee_en_attente)
        self.buttonCorbeille.clicked.connect(self.__consulter_idee_corbeille)
        self.buttonArchive.clicked.connect(self.__consulter_idee_classe)
        self.buttonTacehFini.clicked.connect(self.__consulter_idee_termine)

        self.listDelegue.doubleClicked.connect(self.__ouvrir_idee)
        self.listPlanifier.doubleClicked.connect(self.__ouvrir_idee_par_etape)
        self.listTodo.doubleClicked.connect(self.__ouvrir_idee_par_etape)
        self.listDelegue.clicked.connect(self.__selected_idee_delegue)
        self.listPlanifier.clicked.connect(self.__selected_idee_planifie)
        self.listTodo.clicked.connect(self.__selected_idee_todo)

        self.buttonTermineDelegue.clicked.connect(self.__marque_termine_idee_delegue)
        self.buttonTerminerTodo.clicked.connect(self.__marquer_termine_idee_todo)
        self.buttonTerminerPlanifier.clicked.connect(self.__marquer_termine_idee_planifie)

        self.__rafraichir_element_vue()

    def __dialog_appd(self):
        """
        Ouvre la boite de dialogue A propos de
        :return:
        """
        dialog_appd = QtWidgets.QDialog(parent=self.window)
        ui = AppdChild()
        ui.setupUi(dialog_appd)
        dialog_appd.show()
        dialog_appd.exec_()

    def __ajouter_idee(self):
        """
        Ajoute une idée en base
        :return:
        """
        if self.TextIdee.toPlainText():
            ControllerView.ajouter_idee_fm_view(self.TextIdee.toPlainText())
            self.__rafraichir_element_vue()
            self.TextIdee.clear()

    def __dialog_todolist(self):
        """
        Ouvr ela boite de dialogue des idées à faire
        :return:
        """
        dialog_todolist = QtWidgets.QDialog(parent=self.window)
        ui = TodoListViewChlid()
        ui.setupUi(dialog_todolist)
        dialog_todolist.exec_()
        self.__rafraichir_element_vue()

    def __consulter_idee_en_attente(self):
        """
        Ouvre la boite de dialogue des idées en attente
        :return:
        """
        dialog_listeidee = QtWidgets.QDialog(parent=self.window)
        ui = ListeIdeeViewChild()
        ui.setup_ui_with_etat(dialog_listeidee, Etat.INCUBATEUR)
        dialog_listeidee.exec_()
        self.__rafraichir_element_vue()

    def __consulter_idee_corbeille(self):
        """
        Ouvre la boite de dialogue des idées jetés
        :return:
        """
        dialog_listeidee = QtWidgets.QDialog(parent=self.window)
        ui = ListeIdeeViewChild()
        ui.setup_ui_with_etat(dialog_listeidee, Etat.CORBEILLE)
        dialog_listeidee.exec_()
        self.__rafraichir_element_vue()

    def __consulter_idee_classe(self):
        """
        Ouvre la boite de dialogue des idées classés
        :return:
        """
        dialog_listeidee = QtWidgets.QDialog(parent=self.window)
        ui = ListeIdeeViewChild()
        ui.setup_ui_with_etat(dialog_listeidee, Etat.CLASSER)
        dialog_listeidee.exec_()
        self.__rafraichir_element_vue()

    def __consulter_idee_termine(self):
        """
        Ouvre la boite de dialogue des idées terminées
        :return:
        """
        dialog_listeidee = QtWidgets.QDialog(parent=self.window)
        ui = ListeIdeeViewChild()
        ui.setup_ui_with_etat(dialog_listeidee, Etat.TERMINE)
        dialog_listeidee.exec_()
        self.__rafraichir_element_vue()

    def __rafraichir_element_vue(self):
        """
        Rafraichi toute les informations à afficher provenant de la base
        :return:
        """
        compteur = ControllerView.compter_idee_par_etat()
        self.labelCompteurIdee_bis.setText(str(compteur[Etat.TODO.name+"def"]) + " à traiter")
        self.labelCompteurIdeeTodo.setText(str(compteur[Etat.TODO.name+"todo"]) + self.phrase_compteur)
        self.labelIdeeAttenteCorbeille.setText(str(compteur[Etat.CORBEILLE.name]) + self.phrase_compteur)
        self.labelIdeeAttenteArchivage.setText(str(compteur[Etat.CLASSER.name]) + self.phrase_compteur)
        self.labelIdeeAttenteIncuabateur.setText(str(compteur[Etat.INCUBATEUR.name]) + self.phrase_compteur)
        self.labelDateToday.setText("Aujourd'hui : "+datetime.date.today().strftime('%d/%m/%Y'))
        self.__rafraichir_list_delegue()
        self.__rafraichir_list_todo()
        self.__rafraichir_list_planifie()

    def __rafraichir_list_delegue(self):
        """
        Rafraichi la liste des idées déléguées
        :return:
        """
        liste = ControllerView.get_etapes_delegue_from_db()
        model = QStandardItemModel(self.listDelegue)
        model.clear()
        for todo in liste:
            item = QStandardItem(todo.delegue.nom+" : "+todo.texte)
            item.setData(todo, self.role_idee)
            model.appendRow(item)
        self.listDelegue.setModel(model)
        self.listDelegue.show()

    def __rafraichir_list_todo(self):
        """
        Rafraichi la liste des étapes à faire sans date
        :return:
        """
        liste = ControllerView.get_etapes_todo_from_db()
        model = QStandardItemModel(self.listTodo)
        model.clear()
        for todo in liste:
            item = QStandardItem(todo.idee.texte + "\r\n" + todo.texte)
            item.setData(todo, self.role_idee)
            model.appendRow(item)
        self.listTodo.setModel(model)
        self.listTodo.show()

    def __rafraichir_list_planifie(self):
        """
        Rafraichi la liste des étapes à faire avec une date
        :return:
        """
        liste = ControllerView.get_etapes_planifie_from_db()
        model = QStandardItemModel(self.listPlanifier)
        model.clear()
        for todo in liste:
            item = QStandardItem(todo.idee.texte + "\r\n" + todo.dateExecution.strftime('%d/%m/%Y')+" : " + todo.texte)
            item.setData(todo, self.role_idee)
            model.appendRow(item)
        self.listPlanifier.setModel(model)
        self.listPlanifier.show()

    def __ouvrir_idee(self, index: QStandardItem):
        """
        Ouvre la boite de dialogue de modification d'une idée
        :param index: l'idée sélectionnée
        :return:
        """
        idee = index.data(self.role_idee)
        if idee:
            dialog_editer_idee = QtWidgets.QDialog(self.window)
            ui = EditerIdeeViewChild()
            ui.setup_ui_with_idee(dialog_editer_idee, idee)
            dialog_editer_idee.exec_()
            self.__rafraichir_element_vue()

    def __ouvrir_idee_par_etape(self, index: QStandardItem):
        """
        ouvre la boite de dialogue d'une modification d'idée à partir de l'étape
        :param index:
        :return:
        """
        etape = index.data(self.role_idee)
        if etape and etape.idee:
            dialog_editer_idee = QtWidgets.QDialog(self.window)
            ui = EditerIdeeViewChild()
            ui.setup_ui_with_idee(dialog_editer_idee, etape.idee)
            dialog_editer_idee.exec_()
            self.__rafraichir_element_vue()

    def __selected_idee_delegue(self, index: QStandardItem):
        """
        Evnet de sélection d'idée délégué
        :param index:
        :return:
        """
        self.selected_idee_delegue = index.data(self.role_idee)

    def __selected_idee_todo(self, index: QStandardItem):
        """
        Event de sélection d'une étape à faire sans date
        :param index:
        :return:
        """
        self.selected_etape_todo = index.data(self.role_idee)

    def __selected_idee_planifie(self, index: QStandardItem):
        """
        Event de sélection d'une étape à faire avec date
        :param index:
        :return:
        """
        self.selected_idee_planifie = index.data(self.role_idee)

    def __marque_termine_idee_delegue(self):
        """
        Event de marquer une idée délégué comme terminée
        :return:
        """
        if self.selected_idee_delegue:
            ControllerView.changer_etat_idee_to_termine(self.selected_idee_delegue)
            self.__rafraichir_element_vue()

    def __marquer_termine_idee_todo(self):
        """
        Event de marqué une idée à faire sans date comme temriné
        :return:
        """
        if self.selected_etape_todo:
            ControllerView.changer_etat_etape_to_termine(self.selected_etape_todo)
            self.__rafraichir_element_vue()

    def __marquer_termine_idee_planifie(self):
        """
        Event de marqué une idée à faire avec date comme temriné
        :return:
        """
        if self.selected_idee_planifie:
            ControllerView.changer_etat_etape_to_termine(self.selected_idee_planifie)
            self.__rafraichir_element_vue()
