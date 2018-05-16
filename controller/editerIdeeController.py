from models import modifier_idee_db, Etat, Idee, get_idee_by_id


def get_idee_fm_db(idee: Idee):
    """
    recherche une idée en base de donnée
    :param idee: l'idée
    :return: l'idée
    """
    return get_idee_by_id(idee.id)


def modifier_idee(id: int, idee: str, delegue: str, commentaire: str, etat: Etat):
    """
    Modifie une idée
    :param id: l'id de l'idée
    :param idee: le texte
    :param delegue: le nom de la personne à qui la tache est délégué (optionnel)
    :param commentaire: le commentaire
    :param etat: l'état
    :return:
    """
    modifier_idee_db(id, idee, delegue, commentaire, etat)
