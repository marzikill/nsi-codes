
def existe_chemin(G, sommet, destination):
    """ Graphe, Sommet, Sommet -> bool
    Renvoie True si et seulement si il existe un chemin entre source et destination dans G. """
    pass

def composantes_connexes(G):
    """ Graphe -> {Sommet:int}
    Détermine les composantes connexes du graphe G sous la forme d'un dictionnaire """
    pass

BLANC, GRIS, NOIR = 0, 1, 2

def parcours_cycle(G, depart, couleurs):
    """ Graphe, Sommet, {Sommet:Couleur} -> bool
    Renvoie True si et seulement si  il existe un cycle dans le graphe G dans la composante connexe de depart. 
    On suppose que depart est en BLANC. """
    couleurs[...] = GRIS
    for destination in G.voisins(depart):
        if ...:
            return ...
        elif ...
            return ...
    couleurs[...] = ...
    return ...

def contient_cycle(G):
    """ Graphe -> bool
    Renvoie True ssi le graphe orienté G contient un cycle """
    pass

def distance(G, depart, arrivee):
    """ Graphe, Sommet, Sommet -> int 
    Renvoie la longueur du plus petit chemin entre depart et arrivee dans G """
    pass

def diametre(G):
    """ Graphe -> int
    Renvoie la distance maximale entre deux sommets quelconques du graphe """
    pass

