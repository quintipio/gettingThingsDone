from models import ajouter_idee, count_all_idee_by_etat, Etat


def ajouter_idee_fm_view(texte):
    ajouter_idee(texte)


def compter_idee_par_etat():
    element = {Etat.TODO.name: count_all_idee_by_etat(Etat.TODO),
               Etat.CORBEILLE.name: count_all_idee_by_etat(Etat.CORBEILLE),
               Etat.INCUBATEUR.name: count_all_idee_by_etat(Etat.INCUBATEUR),
               Etat.CLASSER.name: count_all_idee_by_etat(Etat.CLASSER)}
    return element

