from view.appd import Ui_DialogAppd
from constantes import *


class AppdChild(Ui_DialogAppd):

    def setupUi(self, dialog_appd):
        Ui_DialogAppd.setupUi(self, dialog_appd)

        self.buttonFermer.clicked.connect(dialog_appd.close)

        self.labelApp.setText(nom_application)
        self.labelCopy.setText(copyright_text)
        self.labelDev.setText(developpeur)
        self.labelVersion.setText(version_application)
