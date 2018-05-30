from datetime import datetime

from models import Idee, get_etapes_idee, ajouter_modifier_etape, inverser_etat_etape, Etape, supprimer_etape_db, inverser_ordre_etape_db


def charger_etapes(idee: Idee):
    """
    Charge les étapes d'une idée
    :param idee: l'idée dont on cherche les étapes
    :return: la liste des étapes
    """
    return get_etapes_idee(idee.id)


def modifier_etape(id_etape: int, idee: Idee, ordre: int, texte: str, fait: bool, date: datetime = None):
    """
    Modifie une étape
    :param id_etape: l'id de l'étape à modifier
    :param idee: l'idée de l'étape
    :param ordre: l'ordre d'emplacement de l'étape
    :param texte: le texte
    :param fait: fait ou non (bool)
    :param date: la date d'éxécution (optionnel)
    :return:
    """
    ajouter_modifier_etape(idee, ordre, texte, fait, date, id_etape)


def ajouter_etape(idee: Idee, ordre: int, texte: str, fait=False, date=None):
    """
    Créer une nouvelle étape
    :param idee: l'idée de l'étape
    :param ordre: l'ordre de l'étape
    :param texte: le texte
    :param fait: fait ou non (bool)
    :param date: la date d'éxécution de l'étape (optionnelà
    :return:
    """
    ajouter_modifier_etape(idee, ordre, texte, fait, date)


def inverser_etat(etape: Etape):
    """
    Inverse l'état d'une étape de faire à fiat ou vice versa
    :param etape: l'étape dotn on change l'état
    :return:
    """
    inverser_etat_etape(etape.id)


def supprimer_etape(etape : Etape):
    """
    Supprime une étape de la base
    :param etape: l'étape à supprimer
    :return:
    """
    supprimer_etape_db(etape)


def inverser_ordres_etapes(etape_a: Etape, etape_b: Etape):
    """
    Inverse l'ordre de deux étapes
    :param etape_a: une étape
    :param etape_b: l'autre étape
    :return:
    """
    inverser_ordre_etape_db(etape_a, etape_b)
