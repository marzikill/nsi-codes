def arcs_vers_graphe_no(aretes):
    """ [(Sommet, Sommet)] -> Graphe
    Sommet peut être de type int ou str
    Construit le graphe non orienté dont on donne la liste des arêtes. """
    pass

def parcours_aleatoire(G, depart, nombre_sauts):
    """ Graphe, Sommet, int -> {Sommet: int}
    Parcourt aléatoirement le graphe G depuis le sommet depart
    en effectuant nombre_sauts choix de sommets. """
    pass

def parcours_profondeur(G, depart, vus):
    """ Graphe, Sommet, [Sommet] -> [Sommet]
    Parcourt le graphe G depuis depart en profondeur (sachant que
    la liste des sommets présents dans vus ont déjà été visités). """
    if depart not in vus:
        vus.append(depart)
        # appels récursif sur les voisins 
        for destination in G.voisins(depart):
            parcours_profondeur(G, destination, vus)
    return vus

def parcours_profondeur_pile(G, depart):
    """ Graphe, Sommet, [Sommet] -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur
    (sachant que la liste des sommets présents dans vus ont déjà été visités). """
    vus = []
    à_explorer = ...
    ...
    while ...:
        sommet = ...
        if ...:
            vus.append(sommet)
            for destination in reversed(G.voisins(sommet)):
                ...
    return vus

def parcours_largeur(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur
    (sachant que la liste des sommets présents dans vus ont déjà été visités). """
    vus = []
    à_explorer = ...
    ...
    while ...:
        sommet = ...
        if ...:
            vus.append(sommet)
            for destination in G.voisins(sommet):
                ...
    return vus        

class MonTableau:
    def __init__(self, tab):
        """ MonTableau, [int] -> None """
        self.contenu = tab

class Ensemble:
    def __init__(self):
        """ Ensemble -> None """
        self.contenu = dict()

    def ajouter(self, elt):
        """ Ensemble, elt -> None """
        pass

    def supprimer(self, elt):
        """ Ensemble, elt -> None """
        pass

    def __contains__(self, elt):
        """ Ensemble, elt -> bool """
        pass

def parcours_profondeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur """
    pass

def parcours_largeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur """
    pass

