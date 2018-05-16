import os
import sys

from PyQt5 import QtWidgets
import pony.orm.dbproviders.sqlite
from models import open_db, delete_idee_perime, Etat
from viewChild.MainViewChild import MainViewChild


def main():
    # démarrage de la base
    cwd = os.getcwd()
    open_db(cwd)

    # supression des données trop vieilles
    delete_idee_perime(30, Etat.TERMINE)
    delete_idee_perime(30, Etat.CORBEILLE)

    # démarrage de l'IHM (fenêtre principale)
    app = QtWidgets.QApplication(sys.argv)
    window_principale = QtWidgets.QMainWindow()
    ui = MainViewChild()
    ui.setupUi(window_principale)
    window_principale.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
