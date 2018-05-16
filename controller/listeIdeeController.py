from models import Etat, get_all_idee_by_etat


def charger_idees_par_etat(etat: Etat):
    """
    Récupère une liste d'idée à partir de l'étape
    :param etat: l'état dont ont cherche les idées
    :return: la liste d'idée
    """
    return get_all_idee_by_etat(etat)
