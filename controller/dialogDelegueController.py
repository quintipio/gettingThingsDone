from models import recherche_delegue, delegue_idee, Idee


def rechercher_personne_delegue(recherche: str):
    """
    recherche une liste de personnes à partir du noù
    :param recherche: la recherche de personnes
    :return: la liste des noms touvés
    """
    if recherche:
        return recherche_delegue(recherche)


def valider_delegation(idee: Idee, nom: str):
    """
    Dlègue une idée à une perosnne
    :param idee: l'idée à délégué
    :param nom: le nom d ela personne
    :return:
    """
    if nom:
        delegue_idee(idee.id, nom)
