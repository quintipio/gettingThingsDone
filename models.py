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
    DELEGUER = 6


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


def __get_database_file(chemmin_option: str):
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


def openDb(chemin_option: str):
    chemin = __get_database_file(chemin_option)
    database.bind("sqlite", chemin, create_db=True)
    database.generate_mapping(create_tables=True)
    sql_debug(True)
    


"""
    Méthodes de gestion des données
"""

@db_session
def ajouter_idee(idee: str):
    Idee(
        texte=idee,
        etat=Etat.TODO.value,
        dateCreation=datetime.today(),
    )


@db_session
def get_all_idee_by_etat(etat: Etat):
    result = select(i for i in Idee if i.etat is etat.value)
    retour = []
    for r in result:
        retour.append(r)
    return retour


@db_session
def count_all_idee_by_etat(etat_cherche: Etat):
    return count(i for i in Idee if i.etat is etat_cherche.value)


@db_session
def changer_etat_idee(id_idee: int,etat: Etat):
    Idee[id_idee].etat = etat.value


@db_session
def __get_or_create_personne_delegue(nom: str):

    if PersonneDelegue.exists(lambda p: p.nom == nom):
        return PersonneDelegue.get(nom=nom)
    else:
        PersonneDelegue(
            nom=nom
        )
        return PersonneDelegue.get(nom=nom)


@db_session
def delegue_idee(id_idee: int, nom_delegue: str):
    personne = __get_or_create_personne_delegue(nom_delegue)
    Idee[id_idee].delegue = personne.id
    Idee[id_idee].etat = Etat.DELEGUER.value


@db_session
def recherche_delegue(nom: str):
    data = select(p.nom for p in PersonneDelegue if nom.upper() in p.nom.upper())
    retour = []
    for r in data:
        retour.append(r)
    return retour

