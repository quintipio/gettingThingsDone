from datetime import datetime, timedelta
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
    fait = Required(bool)


"""
    Méthode d'administration de la base
"""


def __get_database_file(chemmin_option: str):
    """
    Retourne la base de donnée
    :param chemmin_option: le chemin ou se trouve la base de donnée
    :return: le chemin complet de la BDD
    """
    return chemmin_option + "\\" + "gtd.sqlite"


def open_db(chemin_option: str):
    """
    ouvre la base de donnée
    :param chemin_option: le chemin ou se trouve la base
    :return:
    """
    chemin = __get_database_file(chemin_option)
    database.bind("sqlite", chemin, create_db=True)
    database.generate_mapping(create_tables=True)
    sql_debug(False)


"""
    Méthodes de gestion des données
"""


@db_session
def ajouter_idee(idee: str):
    """
    Ajoute une nouvelle idée en base de donnée
    :param idee: le texte de l'idée à ajouter
    :return:
    """
    Idee(
        texte=idee,
        etat=Etat.TODO.value,
        dateCreation=datetime.today(),
    )


@db_session
def get_idee_by_id(id_idee: int):
    """
    Récupère une idée avec le nom de son delegue éventule
    :param id_idee: l'id de l'idée recherchée
    :return: l'idée
    """
    idee = Idee[id_idee]
    if idee.delegue:
        idee.delegue.nom
    return idee


@db_session
def delete_idee_perime(nb_jours_en_moins: int, etat: Etat):
    """
    Efface les idées périmées depuis plus de
    :param nb_jours_en_moins: le nombre de jour à partir d'aujourd'hui ou la donnée est périmée
    :param etat: l'état dans lequel l'idée doit être pour être supprimée
    :return:
    """
    day = datetime.today() - timedelta(days=nb_jours_en_moins)
    delete(i for i in Idee if i.dateCreation <= day and i.etat == etat.value)


@db_session
def get_all_idee_by_etat(etat: Etat):
    """
     Récpère toute les idées à partir de leurs état
    :param etat: l'état dont on recherche les idées
    :return: une liste d'idée
    """
    result = select(i for i in Idee if i.etat is etat.value)
    retour = []
    for r in result:
        retour.append(r)
    return retour


@db_session
def count_all_idee_by_etat(etat_cherche: Etat):
    """
    Compte les idées par état
    :param etat_cherche: l'état dont on cherche les idées
    :return: le nombre de résultats
    """
    return count(i for i in Idee if i.etat is etat_cherche.value)


@db_session
def count_idee_todo_todefine():
    """
    Compte le nombre d'idées en cours mais dont les étapes sont à définir
    :return: le résultat
    """
    return count(i for i in Idee if i.etat == Etat.TODO.value and len(i.etapes) == 0)


@db_session
def count_idee_todo_en_cours():
    """
    Compte le nombre d'idées en cours mais dont les étapes sont définis
    :return: le résultat
    """
    return count(i for i in Idee if i.etat == Etat.TODO.value and len(i.etapes) > 0)


@db_session
def check_idee_a_definir(id_idee: int):
    """
    Vérifie si une idée possède des étapes ou non
    :param id_idee: l'id de l'idée en question
    :return:
    """
    idee = Idee[id_idee]
    return idee.etapes.count() > 0 and idee.etat != Etat.DELEGUER.value


@db_session
def changer_etat_idee(id_idee: int, etat: Etat):
    """
    change l'état d'une idée
    :param id_idee: l'id de l'idée à changer
    :param etat: le nouvel état
    :return:
    """
    idee = Idee[id_idee]
    if idee.etat == Etat.DELEGUER.value and etat.value != Etat.DELEGUER.value:
        idee.delegue = None
    idee.etat = etat.value


@db_session
def modifier_idee_db(id_idee: int, idee: str, delegue: str, commentaire: str, etat: Etat):
    """
    Modifie une idée en base
    :param id_idee: l'id de l'idée
    :param idee: le texte de l'idée
    :param delegue: le nom de la personne à qui l'idée peut être délégué
    :param commentaire: le commetnaire
    :param etat: le nouvel état
    :return:
    """
    idee_obj = Idee[id_idee]
    idee_obj.texte = idee
    idee_obj.commentaire = commentaire
    idee_obj.etat = etat.value

    if delegue:
        delegue_idee(id_idee, delegue)


@db_session
def __get_or_create_personne_delegue(nom: str):
    """
    Delegue une idée à quelqu'un (recherche en base si le nom existe déjà avant)
    :param nom: le nom de la personne à délégué
    :return: la personne trouvée ou crée
    """
    if PersonneDelegue.exists(lambda p: p.nom == nom):
        return PersonneDelegue.get(nom=nom)
    else:
        PersonneDelegue(
            nom=nom
        )
        return PersonneDelegue.get(nom=nom)


@db_session
def delegue_idee(id_idee: int, nom_delegue: str):
    """
    Délègue une idée
    :param id_idee: l'id de l'idée à déléguer
    :param nom_delegue: le nom de personne à qui on délègue
    :return:
    """
    personne = __get_or_create_personne_delegue(nom_delegue)
    Idee[id_idee].delegue = personne.id
    Idee[id_idee].etat = Etat.DELEGUER.value


@db_session
def recherche_delegue(nom: str):
    """
    recherche le nom d'une personne
    :param nom: le nom
    :return: la liste des noms trouvés
    """
    data = select(p.nom for p in PersonneDelegue if nom.upper() in p.nom.upper())
    retour = []
    for r in data:
        retour.append(r)
    return retour


@db_session
def get_etapes_idee(id_dee: int):
    """
    Retourne les étapes d'une idée
    :param id_dee: l'id de l'idée
    :return: la liste des étapes
    """
    data = Idee[id_dee].etapes

    retour = []
    for e in data:
        retour.append(e)
    retour.sort(key=lambda x: x.order)
    return retour


@db_session
def ajouter_modifier_etape(idee: Idee, ordre: int, texte: str, fait: bool, date: datetime = None, id_etape: int = None):
    """
    ajoute ou modifie une étape à une idée
    :param idee: l'idée concernée
    :param ordre: l'odre de l'étape
    :param texte: le texte de l'étape
    :param fait: l'état de l'étape
    :param date: la date d'éxécution éventuelle
    :param id_etape: l'id de l'étape si modification
    :return:
    """
    if id_etape:
        etape = Etape[id_etape]
        etape.dateExecution = date
        etape.texte = texte
        etape.order = ordre
        etape.fait = fait
    else:
        Etape(
            texte=texte,
            fait=fait,
            dateExecution=date,
            order=ordre,
            idee=Idee[idee.id],
        )
    __check_ordre_etape_idee(idee.id)


@db_session
def inverser_etat_etape(etape_id: int):
    """
    Change l'état d'une étape
    :param etape_id: l'id de l'étape
    :return:
    """
    etape = Etape[etape_id]
    etape.fait = not etape.fait


@db_session
def __check_ordre_etape_idee(id_idee: int):
    """
    vérifié l'ordre des étapes d'une idée
    :param id_idee: l'id de l'idée
    :return:
    """
    etapes = Idee[id_idee].etapes
    tmp = []
    for e in etapes:
        tmp.append(e)
    tmp.sort(key=lambda x: x.order)
    numero_attendu = 1
    for etape in tmp:
        if etape.order != numero_attendu:
            etape.order = numero_attendu
        numero_attendu = numero_attendu + 1


@db_session
def get_idee_delegue():
    """
    retourne les idées délégués
    :return:
    """
    retour = []
    data = select(i for i in Idee if i.etat == Etat.DELEGUER.value)
    for e in data:
        e.delegue.nom
        retour.append(e)
    return retour


@db_session
def get_etapes_todo():
    """
    retourne les prochaines étapes de chaque idée à faire (si elles n'ont pas de date d'éxécution)
    :return: la liste des étapes
    """
    retour = []
    liste = select(i for i in Idee if i.etat == Etat.TODO.value and len(i.etapes) > 0) \
        .order_by(lambda x: x.dateCreation)
    for idee in liste:
        etape = select(e for e in Etape if e.dateExecution is None and not e.fait and e.idee.id == idee.id
                       and e.order == min(ee.order for ee in Etape if ee.idee.id == idee.id
                                          and not ee.fait)).first()
        if etape:
            retour.append(etape)
    return retour


@db_session
def get_etapes_planifie():
    """
    retourne les prochaines étapes de chaque idée à faire (si elles ont de date d'éxécution)
    :return: la liste des étapes
    """
    retour = []
    liste = select(i for i in Idee if i.etat == Etat.TODO.value and len(i.etapes) > 0) \
        .order_by(lambda x: x.dateCreation)
    for idee in liste:
        etape = select(e for e in Etape if e.dateExecution is not None and not e.fait and e.idee.id == idee.id
                       and e.order == min(ee.order for ee in Etape if ee.idee.id == idee.id
                                          and not ee.fait)).first()
        if etape:
            retour.append(etape)
    return retour


@db_session
def verif_fin_etapes_marque_idee_termine(etape: Etape):
    """
    verifie si toute les étapes d'une idées sont éeffectuées. Si c'est le cas l'idée est marquée comme terminée
    :param etape: l'étape à vérifier
    :return:
    """
    nb_etape_non_fait = count(e for e in Etape if not e.fait and e.idee.id == etape.idee.id)
    if nb_etape_non_fait == 0:
        changer_etat_idee(etape.idee.id, Etat.TERMINE)
