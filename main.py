import os
import sys

from PyQt5 import QtWidgets

from models import openDb
from viewChild.MainViewChild import MainViewChild


def main():
    #démarrage de la base
    cwd = os.getcwd()
    openDb(cwd)

    #démarrage de l'IHM (fenêtre principale)
    app = QtWidgets.QApplication(sys.argv)
    window_principale = QtWidgets.QMainWindow()
    ui = MainViewChild()
    ui.setupUi(window_principale)
    window_principale.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
