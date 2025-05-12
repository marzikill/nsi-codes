from ds import Graphe, Pile, File
from random import randint

def arcs_vers_graphe_no(aretes):
    """ [(Sommet, Sommet)] -> Graphe
    Sommet peut être de type int ou str
    Construit le graphe non orienté dont on donne la liste des arêtes. """
    g = Graphe()
    for arete in aretes:
        a, b = arete[0], arete[1]
        g.ajouter_sommet(a)
        g.ajouter_sommet(b)
        g.ajouter_arc(a, b)
        g.ajouter_arc(b, a)
    return g

aretes = [(0, 1), (0, 3), (0, 6),
    (0, 9), (1, 4), (1, 6),
    (2, 5), (3, 6), (3, 8),
    (4, 7), (5, 6), (5, 7)]
g1 = arcs_vers_graphe_no(aretes)
g1.decrire()

aretes = [(0, 1), (0, 5),
    (1, 2), (1, 6), (1, 5), (2, 3),
    (2, 7), (2, 6), (3, 7), (3, 4),
    (4, 5), (4, 6), (4, 7), (6, 7)]
g2 = arcs_vers_graphe_no(aretes)
g2.decrire()

aretes = [(0, 6), (0, 1),
    (0, 2), (0, 7), (1, 2), (1, 6),
    (1, 8), (1, 4), (2, 4), (2, 5),
    (2, 7), (3, 8), (4, 5),(4, 7)]
g3 = arcs_vers_graphe_no(aretes)
g3.decrire()

aretes = [(0, 1), (0, 2),
    (1, 2), (1, 3), (2, 3), (4, 5)]
g4 = arcs_vers_graphe_no(aretes)
g4.decrire()

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
    à_explorer = Pile()
    à_explorer.empiler(depart)
    while not à_explorer.est_vide():
        sommet = à_explorer.depiler()
        if sommet not in vus:
            vus.append(sommet)
            for destination in reversed(G.voisins(sommet)):
                à_explorer.empiler(destination)
    return vus, à_explorer

def parcours_largeur(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur
    (sachant que la liste des sommets présents dans vus ont déjà été visités). """
    vus = []
    à_explorer = File()
    à_explorer.enfiler(depart)
    while not à_explorer.est_vide():
        sommet = à_explorer.defiler()
        if sommet not in vus:
            vus.append(sommet)
            for destination in G.voisins(sommet):
                à_explorer.enfiler(destination)
    return vus, à_explorer        

# un parcours en largeur du graphe à partir
# du sommet départ renvoie la liste des sommets
# du graphe, triée par ordre croissant par
# rapport à leur distance par rapport au sommet
# de départ.

class MonTableau:
    def __init__(self, tab):
        """ MonTableau, [int] -> None """
        self.contenu = tab
    
    def __repr__(self):
        return str(self.contenu)
    
    def __contains__(self, e):
        # cette fonction a une complexité
        # linéaire en la taille de self.contenu
        for elem in self.contenu:
            if elem == e:
                return True
        return False
    
    def appartient(self, e):
        ...

montab = MonTableau([1, 2, 3])

class Ensemble:
    def __init__(self):
        """ Ensemble -> None """
        self.contenu = dict()

    def ajouter(self, elt):
        """ Ensemble, elt -> None """
        self.contenu[elt] = True

    def supprimer(self, elt):
        """ Ensemble, elt -> None """
        self.contenu[elt] = False
        
    def __contains__(self, elt):
        """ Ensemble, elt -> bool """
        if elt in self.contenu:
            return self.contenu[elt]
        return False
    # s'exécute en temps constant

def parcours_profondeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur """
    pass

def parcours_largeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur """
    ordre = [] # on y ajoute les éléments
    # dans l'ordre de parcours en largeur
    vus = Ensemble()
    à_explorer = File()
    à_explorer.enfiler(depart)
    while not à_explorer.est_vide():
        sommet = à_explorer.defiler()
        # vus est un ensemble : test
        # d'appartenance en temps constant
        if sommet not in vus: 
            vus.ajouter(sommet) # marquer le sommet comme visité
            ordre.append(sommet)
            for destination in G.voisins(sommet):
                à_explorer.enfiler(destination)
    return ordre

