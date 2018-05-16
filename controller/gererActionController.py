from datetime import datetime

from models import Idee, get_etapes_idee, ajouter_modifier_etape, inverser_etat_etape, Etape


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
    inverser_etat_etape(etape.id)
