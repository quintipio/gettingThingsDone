from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox

from models import Etape
from utils import string_to_int
from view.gererActions import Ui_DialogGererActions
from controller import gererActionController as ControllerView


class GererActionViewChild(Ui_DialogGererActions):

    etape_idee_key = Qt.UserRole + 2

    def __init__(self):
        self.selected_idee = None
        self.etape_en_cours: Etape = None
        self.dialog = None
        self.ordre_en_cours = 1
        self.liste_etape_obj = []

    def setup_ui_with_idee(self, dialog_etapes, idee):
        """
        Charge la fenêtre
        :param dialog_etapes: la boite de dialogue
        :param idee: l'idée dont on modifie les étapes
        :return:
        """
        Ui_DialogGererActions.setupUi(self, dialog_etapes)

        self.listeEtape.clicked.connect(self.__select_element_listbox)
        self.buttonAjouterModifier.clicked.connect(self.__valider_etape)
        self.buttonChangerEtat.clicked.connect(self.__changer_etat)
        self.checkBoxDate.clicked.connect(self.__afficher_masquer_date)
        self.buttonMonter.clicked.connect(self.__monter_etape)
        self.buttonDescendre.clicked.connect(self.__descendre_etape)
        self.buttonSupprimer.clicked.connect(self.__supprimer_etape)

        self.dialog = dialog_etapes
        self.selected_idee = idee

        self.__charger_etapes()

    def __changer_etat(self):
        """
        Inverse l'état d'une étape
        :return:
        """
        if self.etape_en_cours:
            ControllerView.inverser_etat(self.etape_en_cours)
            self.__charger_etapes()

    def __afficher_masquer_date(self):
        """
        Affiche ou masque le champ date
        :return:
        """
        self.inputDate.setDisabled(not self.checkBoxDate.isChecked())

    def __select_element_listbox(self, index: QStandardItem):
        """
        event de selection de la listbox
        :param index: l'item choisi
        :return:
        """
        self.etape_en_cours = index.data(self.etape_idee_key)
        if self.etape_en_cours:
            self.__afficher_etape()
        else:
            self.__reset_champs()

    def __valider_etape(self):
        """
        Valide la modification d'une étape
        :return:
        """
        if self.textEtape.toPlainText() and string_to_int(self.textOrdre.text()):

            my_date = None
            if self.checkBoxDate.isChecked():
                my_date = self.inputDate.dateTime().toPyDateTime()

            if self.etape_en_cours:
                ControllerView.modifier_etape(self.etape_en_cours.id, self.selected_idee, string_to_int(
                    self.textOrdre.text()), self.textEtape.toPlainText(), self.etape_en_cours.fait, my_date)
            else:
                etat = False

                deux_min_question = QMessageBox()
                deux_min_question.setIcon(QMessageBox.Question)
                deux_min_question.setText(" Cette étape vous prend-elle moins de deux minutes à être réalisé ?")
                deux_min_question.setWindowTitle("Moins de deux minutes ?")
                deux_min_question.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                result = deux_min_question.exec_()

                if result == QMessageBox.Yes:
                    fin_deux_min_question = QMessageBox()
                    fin_deux_min_question.setIcon(QMessageBox.Warning)
                    fin_deux_min_question.setText(" Alors faites le maintenant!")
                    fin_deux_min_question.setWindowTitle("Faites-le!")
                    fin_deux_min_question.setInformativeText("La tache sera automatiquement validé")
                    fin_deux_min_question.setStandardButtons(QMessageBox.Ok)
                    fin_deux_min_question.exec_()
                    etat = True
                    self.inputDate.date = None

                ControllerView.ajouter_etape(self.selected_idee, string_to_int(self.textOrdre.text()),
                                             self.textEtape.toPlainText(), etat, my_date)
            self.__charger_etapes()

    def __charger_etapes(self):
        """
        Affiche les étapes d'unée idée
        :return:
        """
        etapes = ControllerView.charger_etapes(self.selected_idee)
        model = QStandardItemModel(self.listeEtape)
        model.clear()
        self.liste_etape_obj.clear()

        item_base = QStandardItem("Nouvelle étape")
        model.appendRow(item_base)

        for etape in etapes:

            self.liste_etape_obj.append(etape)

            text_item = etape.texte
            if etape.fait:
                text_item = text_item + " - FAIT"
            item = QStandardItem(text_item)
            item.setData(etape, self.etape_idee_key)
            model.appendRow(item)
            if etape.order >= self.ordre_en_cours:
                self.ordre_en_cours = etape.order+1
        self.listeEtape.setModel(model)
        self.listeEtape.show()
        self.__reset_champs()

    def __afficher_etape(self):
        """
        Affiche les éléments d'une étape
        :return:
        """
        if self.etape_en_cours:
            self.labelFaitValue.setText("Fait" if self.etape_en_cours.fait else "A faire")
            self.textOrdre.setText(str(self.etape_en_cours.order))
            self.textEtape.setText(self.etape_en_cours.texte)
            self.buttonChangerEtat.setDisabled(False)
            if self.etape_en_cours.dateExecution:
                self.checkBoxDate.setChecked(True)
                self.inputDate.setDate(self.etape_en_cours.dateExecution)
            else:
                self.checkBoxDate.setChecked(False)
                self.inputDate.setDate(datetime.today())
            self.__afficher_masquer_date()

    def __reset_champs(self):
        """
        Efface tout les champs
        :return:
        """
        self.labelFaitValue.setText("A faire")
        self.buttonChangerEtat.setDisabled(True)
        self.inputDate.setMinimumDate(datetime.today())
        self.inputDate.setDate(datetime.today())
        self.textOrdre.setText(str(self.ordre_en_cours))
        self.textEtape.setText("")
        self.checkBoxDate.setChecked(False)
        self.__afficher_masquer_date()

    def __monter_etape(self):
        """
        Inverse l'ordre de l'étape avec celle au dessus d'elle
        :return:
        """
        if self.etape_en_cours and self.etape_en_cours.order > 1:
            etape_filtre = [i for i in self.liste_etape_obj if i.order == self.etape_en_cours.order-1]
            if etape_filtre:
                ControllerView.inverser_ordre_etape_db(self.etape_en_cours, etape_filtre[0])
                self.__charger_etapes()

    def __descendre_etape(self):
        """
                Inverse l'ordre de l'étape avec celle au dessous d'elle
                :return:
                """
        if  self.etape_en_cours and self.etape_en_cours.order < max(i.order for i in self.liste_etape_obj):
            etape_filtre = [i for i in self.liste_etape_obj if i.order == self.etape_en_cours.order + 1]
            if etape_filtre:
                ControllerView.inverser_ordre_etape_db(self.etape_en_cours, etape_filtre[0])
                self.__charger_etapes()

    def __supprimer_etape(self):
        """
        Supprime une étape de la liste
        :return:
        """
        if self.etape_en_cours:
            ControllerView.supprimer_etape(self.etape_en_cours)
            self.__charger_etapes()
            self.ordre_en_cours = self.listeEtape.model().rowCount()

