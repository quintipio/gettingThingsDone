from models import recherche_delegue, delegue_idee, Idee


def rechercher_personne_delegue(recherche: str):
    if recherche:
        return recherche_delegue(recherche)


def valider_delegation(idee: Idee, nom: str):
    if nom:
        delegue_idee(idee.id, nom)
