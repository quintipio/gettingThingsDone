from models import ajouter_idee, count_all_idee_by_etat, Etat, get_idee_delegue, changer_etat_idee, Idee, \
    get_etapes_todo, inverser_etat_etape, Etape, verif_fin_etapes_marque_idee_termine, get_etapes_planifie, \
    count_idee_todo_en_cours, count_idee_todo_todefine


def ajouter_idee_fm_view(texte):
    """
    Créer une nouvelle idée
    :param texte: le texte de l'idée
    :return:
    """
    ajouter_idee(texte)


def get_etapes_delegue_from_db():
    """
    Retourne les idées délégés d'une idée
    :return: la liste des idées déléguées
    """
    return get_idee_delegue()


def get_etapes_todo_from_db():
    """
    Retoune les étapes à faire sans date d'éxécution
    :return: la liste des étapes
    """
    return get_etapes_todo()


def get_etapes_planifie_from_db():
    """
    Retoune les étapes à faire avec une date d'éxécution
    :return: la liste des étapes
    """
    return get_etapes_planifie()


def changer_etat_idee_to_termine(idee: Idee):
    """
    Chang eune idée en état terminé
    :param idee: l'idée dont on veut changer l'état
    :return:
    """
    changer_etat_idee(idee.id, Etat.TERMINE)


def changer_etat_etape_to_termine(etape: Etape):
    """
    change à l'tat fait une étape termine une idée si toute ses étapes sont faites
    :param etape: l'étape
    :return:
    """
    inverser_etat_etape(etape.id)
    verif_fin_etapes_marque_idee_termine(etape)


def compter_idee_par_etat():
    """
    Compte le nombre d'idées en fonction des états
    :return: un dictionnaire etat:nombre
    """
    element = {Etat.TODO.name+"todo": count_idee_todo_en_cours(),
               Etat.CORBEILLE.name: count_all_idee_by_etat(Etat.CORBEILLE),
               Etat.INCUBATEUR.name: count_all_idee_by_etat(Etat.INCUBATEUR),
               Etat.CLASSER.name: count_all_idee_by_etat(Etat.CLASSER),
               Etat.TODO.name + "def": count_idee_todo_todefine()}
    return element

