from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter

from models import Idee
from view.dialogDelegue import Ui_DialogDelegue
from controller import dialogDelegueController as controller


class DialogDelegueViewChild(Ui_DialogDelegue):

    test = ["Ulysse","tyty", "toto"]

    def __init__(self):
        Ui_DialogDelegue.__init__(self)
        self.idee = None
        self.completer_text_delegue: QCompleter = None

    def setup_ui_with_idee(self, dialog_delegue, idee: Idee):
        Ui_DialogDelegue.setupUi(self, dialog_delegue)

        self.completer_text_delegue = QCompleter(self.textDelegue)
        self.completer_text_delegue.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer_text_delegue.setCompletionMode(QCompleter.PopupCompletion)
        self.completer_text_delegue.setWrapAround(False)
        self.textDelegue.setCompleter(self.completer_text_delegue)

        self.textDelegue.textEdited.connect(self.__autocomplete_delegue)
        self.buttonDelegue.accepted.connect(self.__action_delegue)

        self.idee = idee

    def __autocomplete_delegue(self):
        result = controller.rechercher_personne_delegue(self.textDelegue.text())
        self.completer_text_delegue.setModel(QStringListModel(result))

    def __action_delegue(self):
        controller.valider_delegation(self.idee, self.textDelegue.text())
