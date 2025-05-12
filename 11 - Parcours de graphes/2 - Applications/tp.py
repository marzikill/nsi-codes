from ds import *

def existe_chemin(G, sommet, destination):
    """ Graphe, Sommet, Sommet -> bool
    Renvoie True si et seulement si il existe un chemin entre source et destination dans G. """
    l = parcours_largeur(G, sommet)
    for i in range(len(l)):
        if l[i] == destination:
            return True
    return False

def existe_chemin_rec(G, depart, destination, vus):
    """ Graphe, Sommet, Sommet, Ensemble -> bool
    Parcourt le graphe G depuis depart en profondeur (sachant que
    la liste des sommets présents dans vus ont déjà été visités). """
    # Cas de base
    if depart == destination:
        return True
    # Cas général
    if depart not in vus:
        vus.ajouter(depart)
        # appels récursif sur les voisins 
        for voisin in G.voisins(depart):
            if existe_chemin_rec(G, voisin, destination, vus):
                return True
    return False

def existe_chemin_file(G, depart, destination):
    # À MODIFIER : IL FAUT S'ARRÊTER DÈS QU'ON
    # A TROUVÉ UN CHEMIN
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

# Exemple d'application : est-ce que deux
# ordinateurs connectés sur le graphe "internet"
# peuvent communiquer entre eux ?

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
        elif ...:
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

