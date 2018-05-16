from models import get_all_idee_by_etat, changer_etat_idee, Etat, Idee, check_idee_a_definir


def charger_todo_liste():
    """
    Récupère la liste des idées en état TODO
    :return: la liste des idées
    """
    return get_all_idee_by_etat(Etat.TODO)


def idee_etat_corbeille(idee: Idee):
    """
    Met une idée à la corbeille
    :param idee: l'idée
    :return:
    """
    if idee is not None:
        changer_etat_idee(idee.id, Etat.CORBEILLE)


def idee_etat_classer(idee: Idee):
    """
    Met une idée à l'état cléssé
    :param idee: l'idée
    :return:
    """
    if idee is not None:
        changer_etat_idee(idee.id, Etat.CLASSER)


def idee_etat_incuber(idee: Idee):
    """
    Met une idée à l'état incuber
    :param idee: l'idée
    :return:
    """
    if idee is not None:
        changer_etat_idee(idee.id, Etat.INCUBATEUR)


def check_idee_define(id_idee: int):
    """
    Vérifie si une idée à besoin d'avoir des étapes
    :param id_idee: l'id de l'idée
    :return: true si oui
    """
    return check_idee_a_definir(id_idee)
