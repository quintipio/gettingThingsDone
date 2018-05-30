from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QCompleter, QMessageBox

from models import Idee, Etat
from view.editerIdee import Ui_DialogEditerIdee
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5 import QtWidgets

from viewChild.gererActionViewChild import GererActionViewChild
from controller import dialogDelegueController as controllerDelegue
from controller import editerIdeeController as ControllerView


class EditerIdeeViewChild(Ui_DialogEditerIdee):

    role_etat = Qt.UserRole + 5

    def __init__(self):
        self.dialog = None
        self.idee: Idee = None
        self.completer_text_delegue: QCompleter = None

    def setup_ui_with_idee(self, dialog_editer_idee, idee: Idee):
        """
        Caharge la fenetre
        :param dialog_editer_idee: la boite de dialogue
        :param idee: l'idée devant être modifiée
        :return:
        """
        Ui_DialogEditerIdee.setupUi(self, dialog_editer_idee)

        # Evenements
        self.buttonEditerEtapes.clicked.connect(self.__open_etape)
        self.buttonValider.clicked.connect(self.__editer_action)
        self.textDelegue.textEdited.connect(self.__autocomplete_delegue)

        # AutoComplete Deleguation
        self.completer_text_delegue = QCompleter(self.textDelegue)
        self.completer_text_delegue.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer_text_delegue.setCompletionMode(QCompleter.PopupCompletion)
        self.completer_text_delegue.setWrapAround(False)
        self.textDelegue.setCompleter(self.completer_text_delegue)

        # populate QComboBox
        model = QStandardItemModel(self.comboEtat)
        model.clear()
        for etat in Etat:
            item = QStandardItem(etat.name)
            item.setData(etat, self.role_etat)
            model.appendRow(item)
        self.comboEtat.setModel(model)
        self.comboEtat.show()

        # mise en mémoire des infos récuéré
        self.dialog = dialog_editer_idee
        self.idee = ControllerView.get_idee_fm_db(idee)

        # affichage
        self.__afficher_idee()

    def __afficher_idee(self):
        """
        Rempli les élements à partir de l'idée demandée
        :return:
        """
        self.__select_etat_combobox(Etat(self.idee.etat))
        self.labelDate.setText(self.idee.dateCreation.strftime('%d/%m/%Y %H:%M:%S'))
        self.textIdee.setPlainText(self.idee.texte)
        self.textCommentaire.setPlainText(self.idee.commentaire)
        if self.idee.delegue and self.idee.delegue.nom:
            self.textDelegue.setText(self.idee.delegue.nom)

    def __open_etape(self):
        """
        Ouvre la dialgoue des étapes
        :return:
        """
        dialog_etapes = QtWidgets.QDialog(self.dialog)
        ui = GererActionViewChild()
        ui.setup_ui_with_idee(dialog_etapes, self.idee)
        dialog_etapes.exec_()

    def __autocomplete_delegue(self):
        """
        Autocomplete sur le champ Délègue
        :return:
        """
        result = controllerDelegue.rechercher_personne_delegue(self.textDelegue.text())
        self.completer_text_delegue.setModel(QStringListModel(result))
        if self.textDelegue.text():
            self.__select_etat_combobox(Etat.DELEGUER)

    def __editer_action(self):
        """
        Modifie une idée en controlant les champs
        :return:
        """
        if not self.textIdee.toPlainText():
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Le champ idée doit être rempli")
            error.setWindowTitle("Erreur")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            return

        if (self.textDelegue.text() and self.comboEtat.currentText() != Etat.DELEGUER.name) or \
                (not self.textDelegue.text() and self.comboEtat.currentText() == Etat.DELEGUER.name):
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setText("Si la tâche est déléguée, son état doit être à l'état délégué")
            error.setWindowTitle("Erreur")
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            return

        ControllerView.modifier_idee(self.idee.id, self.textIdee.toPlainText(), self.textDelegue.text(),
                                     self.textCommentaire.toPlainText(), self.comboEtat.currentData(self.role_etat))
        self.dialog.close()

    def __select_etat_combobox(self, etat: Etat):
        """
        Chnage l'état sélectionné par la comboBox
        :param etat: l'état à sélectionner
        :return:
        """
        index = self.comboEtat.findText(etat.name, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboEtat.setCurrentIndex(index)
