from datetime import datetime
from enum import Enum

from pony.orm import *

"""
ENUM
"""


class Etat(Enum):
    TODO = 1
    CORBEILLE = 2
    INCUBATEUR = 3
    CLASSER = 4
    TERMINE = 5


"""
BASE DE DONNEE
"""

database = Database()


class Idee(database.Entity):
    texte = Required(str)
    etat = Required(int)
    dateCreation = Required(datetime)
    commentaire = Optional(str)
    delegue = Optional("PersonneDelegue")
    etapes = Set("Etape")


class PersonneDelegue(database.Entity):
    nom = Required(str)
    idee = Set(Idee)


class Etape(database.Entity):
    order = Required(int)
    texte = Required(str)
    dateExecution = Optional(datetime)
    idee = Required(Idee)


"""
    Méthode d'administration de la base
"""


def __get_database_file(chemmin_option):
    try:
        options = {}
        with open(chemmin_option + "\\" + "options.properties") as f:
            for line in f:
                k, v = line.strip().split('=')
                options[k.strip()] = v.strip()
        if options['dir'] != 'None':
            return options['dir']
        else:
            return chemmin_option + "\\" + "gtd.sqlite"
    except:
        return chemmin_option + "\\" + "gtd.sqlite"


def openDb(chemmin_option):
    chemin = __get_database_file(chemmin_option)
    database.bind("sqlite", chemin, create_db=True)
    database.generate_mapping(create_tables=True)


"""
    Méthodes de gestion de la base
"""


