from ds import Graphe, Pile, File
from random import randint

def arcs_vers_graphe_no(aretes):
    """ [(Sommet, Sommet)] -> Graphe
    Sommet peut être de type int ou str
    Construit le graphe non orienté dont on donne la liste des arêtes. """
    g = Graphe()
    for source, destination in aretes:
        g.ajouter_sommet(source)
        g.ajouter_sommet(destination)
        g.ajouter_arc(source, destination)
        g.ajouter_arc(destination, source)
    return g

aretes = [(0, 1), (0, 3),
            (0, 6), (1, 4), (1, 6),
            (2, 5), (3, 6), (3, 8),
            (4, 7), (5, 6), (5, 7)]    
g1 = arcs_vers_graphe_no(aretes)
g1.decrire()

aretes = [(0, 1), (0, 5),
    (1, 2), (1, 6), (1, 5), (2, 3),
    (2, 7), (2, 6), (3, 7), (3, 4),
    (4, 5), (4, 6), (4, 7), (5, 6),
    (6, 7)]    
g2 = arcs_vers_graphe_no(aretes)
g2.decrire()

aretes = [(0, 8), (0, 6), (0, 1),
    (0, 2), (0, 7), (1, 2), (1, 6),
    (1, 8), (1, 4), (2, 4), (2, 5),
    (2, 7), (3, 4), (3, 8), (4, 5),
    (4, 7), (5, 7), (6, 8)]    
g3 = arcs_vers_graphe_no(aretes)
g3.decrire()

g4 = Graphe()
aretes = [(0, 1), (0, 2),
    (1, 2), (1, 3), (2, 3), (4, 5)]
g4 = arcs_vers_graphe_no(aretes)
g4.decrire()

def parcours_aleatoire(G, depart, nombre_sauts):
    """ Graphe, Sommet, int -> {Sommet: int}
    Parcourt aléatoirement le graphe G depuis le sommet depart
    en effectuant nombre_sauts choix de sommets. """
    compte = {s:0 for s in G.sommets()}
    sommet_courant = depart
    compte[sommet_courant] += 1
    for i in range(nombre_sauts):
        tab = G.voisins(sommet_courant)
        choix = randint(0, len(tab)-1)
        sommet_courant = tab[choix]
        compte[sommet_courant] += 1
    return compte
        
def frequences(histo):
    """ {Sommet: int} -> {Sommet: float}
    Renvoie le dictionnaire des fréquences (arrondies au centième)
    associé au dictionnaire du nombre d'occurrences des histo du graphe """
    total = 0
    for k in histo:
        # k prend comme valeur les clés
        total = total + histo[k]
    # sum([v for v in histo.values()])
    reponse = dict()
    for k in histo:
        reponse[k] = round(histo[k]/total,2)
    return reponse

histo = parcours_aleatoire(g1, 0, 10000)
rep = frequences(histo)
print(rep)


def frequences(histo):
    """ {Sommet: int} -> {Sommet: float}
    Renvoie le dictionnaire des fréquences (arrondies au centième)
    associé au dictionnaire du nombre d'occurrences des histo du graphe """
    pass

def parcours_profondeur(G, depart, vus):
    """ Graphe, Sommet, [Sommet] -> [Sommet]
    Parcourt le graphe G depuis depart en profondeur (sachant que
    la liste des sommets présents dans vus ont déjà été visités).
    On suppose que depart n'est pas dans vus. """
    vus.append(depart)
    # appels récursif sur les voisins non visités
    for destination in G.voisins(depart):
        if not destination in vus:
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
        if sommet in vus:
            continue
        vus.append(sommet)
        # ajout des voisins non visités
        for destination in reversed(G.voisins(sommet)):
            if not destination in vus:
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
        # if sommet in vus:
        #     continue
        # pareil mais sans "continue"
        if not sommet in vus:
            # opération de traitement
            vus.append(sommet)
            # ajout des voisins non visités
            for destination in G.voisins(sommet):
                if not destination in vus:
                    à_explorer.enfiler(destination)
    return vus, à_explorer


class MonTableau:
    def __init__(self, tab):
        """ MonTableau, [int] -> Nonetype """
        self.contenu = tab
        
    def __contains__(self, elt):
        """ MonTableau, int -> bool """
        # pas le droit au mot clé
        # in
        # pourt tester l'appartenance ici !
        # les boucles sont autorisées
        for e in self.contenu:
            if e == elt:
                return True
        return False
        # la complexité est LINÉAIRE : on
        # parcours le tableau dans le pire des cas

# t = MonTableau([1, 2])
# >>> 1 in t
# True
# Opération "in" est linéaire en la taille du tableau

# >>> dico = {1:'a'}
# >>> 1 in dico
# True
# Opération "in" est en temps constant en la taille du dictionnaire
# = tps indépendant de la taille

class Ensemble:
    def __init__(self):
        """ Ensemble -> Nonetype """
        self.contenu = dict()

    def ajouter(self, elt):
        """ Ensemble, elt -> Nonetype """
        self.contenu[elt] = True

    def supprimer(self, elt):
        """ Ensemble, elt -> Nonetype """
        if elt in self.contenu:
            # in s'applique à un dictionnaire
            self.contenu.pop(elt)

    def __contains__(self, elt):
        """ Ensemble, elt -> bool """
        if elt in self.contenu:
            # in s'applique à un dictionnaire
            return self.contenu[elt]
        return False
    # Ensemble supporte "in" en temps constant
    # elt in e <=> e.__contains__(elt)

def parcours_profondeur_mieux(G, depart):
    """ Graphe, Sommet -> {Sommet}
    Parcours le graphe G depuis le sommet depart en profondeur """
    """ Graphe, Sommet, [Sommet] -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur
    (sachant que la liste des sommets présents dans vus ont déjà été visités). """
    vus = Ensemble()
    ordre = []
    à_explorer = Pile()
    à_explorer.empiler(depart)
    while not à_explorer.est_vide():
        sommet = à_explorer.depiler()
        if sommet in vus: # test en temps constant !!!
            # avant : test en temps linéaire
            continue
        vus.ajouter(sommet)
        ordre.append(sommet) # coute 1 opération
        # ajout des voisins non visités
        for destination in reversed(G.voisins(sommet)):
            if not destination in vus:
                # on passe d'un test en temps
                # linéaire à un test en temps
                # constant car vus est un Ensemble!
                # C'est fou !
                à_explorer.empiler(destination)
    return ordre

def parcours_largeur_mieux(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur """
    vus = Ensemble()
    ordre = []
    à_explorer = File()
    à_explorer.enfiler(depart)
    while not à_explorer.est_vide():
        sommet = à_explorer.defiler()
        if sommet in vus: # temps constant
             continue
        # opération de traitement
        vus.ajouter(sommet) # temps constant
        ordre.append(sommet) # temps constant
        # ajout des voisins non visités
        for destination in G.voisins(sommet):
            if not destination in vus: # temps constant
                à_explorer.enfiler(destination)
    return ordre