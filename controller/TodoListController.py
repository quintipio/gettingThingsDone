from models import get_all_idee_by_etat, changer_etat_idee, Etat, Idee


def charger_todo_liste():
    return get_all_idee_by_etat(Etat.TODO)


def idee_etat_corbeille(idee: Idee):
    if idee is not None:
        changer_etat_idee(idee.id, Etat.CORBEILLE)


def idee_etat_classer(idee: Idee):
    if idee is not None:
        changer_etat_idee(idee.id, Etat.CLASSER)


def idee_etat_incuber(idee: Idee):
    if idee is not None:
        changer_etat_idee(idee.id, Etat.INCUBATEUR)
