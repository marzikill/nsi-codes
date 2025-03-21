from ds import *

def tab_est_trie(tab):
    """ [int] -> bool
    Détermine si le tableau tab est trié par ordre croissant. """
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True

def liste_est_triee(l):
    """ Liste -> bool
    Détermine si la liste l est triée """
    if est_vide(l) or est_singleton(l):
        return True
    else:
        inter = liste_est_triee(queue(l))
        if tete(l) > tete(queue(l)):
            return False
        return True

def tri_insertion_iter(tab):
    """ [int] -> [int]
    Trie en place le tableau tab (tri par insertion) """
    n = len(tab)
    for i in range(...):
        # les éléments d'indice 0..i du tableau t
        # sont triés dans l'ordre croissant
        element = tab[i]
        trou = i
        # on cherche à insérer l'élément dans le tableau
        # constitué des éléments d'indice 0..i
        while ... > ... and trou > 0:
            tab[trou] = ...         # on décale l'élément précédent de tab
            trou = ...              # mise à jour de l'indice du trou
        # À la fin de la boucle soit
        # trou = 0 et tous les éléments de t sont supérieurs à élément
        # soit trou > 0, t[trou - 1] < element < t[i] pour tout i >= trou
        tab[trou] = ...
        # le tableau est alors trié
    return tab # que se passe-t-il si on ne le met pas ?

def insere_trie(l, e):
    """ Liste, int -> Liste
    l est triée par ordre croissant """
    pass

def trie_insertion_rec(l):
    """ Liste -> Liste
    Trie la liste l à l'aide de l'algorithme du tri par insertion """
    pass

def mini_a_partir(tab, i):
    """ [int], int -> int
    Renvoie l'indice du plus petit élément de tab à partir de l'indice i """
    pass

def tri_selection_iter(tab):
    """ [int] -> [int]
    Trie le tableau tab (tri par sélection) """
    pass

def minimum(l):
    """ Liste -> int
    l est non vide
    Renvoie le plus petit élément de la liste l """
    pass

def supprime(l, e):
    """ Liste, int -> Liste
    l est non vide, e appartient à l
    Renvoie la liste l où on a supprimé une occurence de e """
    pass

def tri_selection_rec(l):
    """ Liste -> Liste
    Trie la liste l (tri par sélection) """
    pass

def diviser(l):
    """ Liste -> Liste, Liste
    Divise la liste en deux listes """
    pass

def fusionner(l1, l2):
    """ Liste, Liste
    Renvoie la liste des éléments de l1 et l2 triés """
    pass

def tri_fusion(l):
    """ Liste -> Liste
    Trie la liste l (tri fusion) """
    pass


