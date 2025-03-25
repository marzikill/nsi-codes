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
    for i in range(n):
        # les éléments d'indice 0..i du tableau t
        # sont triés dans l'ordre croissant
        element = tab[i]
        trou = i
        # on cherche à insérer l'élément dans le tableau
        # constitué des éléments d'indice 0..i
        while trou > 0 and tab[trou-1] > element:
            tab[trou] = tab[trou-1]         # on décale l'élément précédent de tab
            trou = trou-1              # mise à jour de l'indice du trou
        # À la fin de la boucle soit
        # trou = 0 et tous les éléments de t sont supérieurs à élément
        # soit trou > 0, t[trou - 1] < element < t[i] pour tout i >= trou
        tab[trou] = element
        # le tableau est alors trié
    return tab # que se passe-t-il si on ne le met pas ?

def insere_trie(l, e):
    """ Liste, int -> Liste
    l est triée par ordre croissant """
    if est_vide(l):
        return ajoute(l, e)
    elif tete(l) > e:
        return ajoute(l, e)
    else:
        inter = insere_trie(queue(l), e)
        return ajoute(inter, tete(l))

def trie_insertion_rec(l):
    """ Liste -> Liste
    Trie la liste l à l'aide de l'algorithme du tri par insertion """
    if est_vide(l):
        return l
    else:
        queue_trie = trie_insertion_rec(queue(l))
        return insere_trie(queue_trie, tete(l))

def mini_a_partir(tab, i):
    """ [int], int -> int
    Renvoie l'indice du plus petit élément de tab à partir de l'indice i """
    mini = tab[i]
    indice_mini = i
    for j in range(i, len(tab)):
        if tab[j] < mini:
            mini = tab[j]
            indice_mini = j
    return indice_mini

def tri_selection_iter(tab):
    """ [int] -> [int]
    Trie le tableau tab (tri par sélection) """
    for i in range(len(tab)):
        indice_mini = mini_a_partir(tab, i)
        tab[i], tab[indice_mini] = tab[indice_mini], tab[i]
    return tab

def minimum(l):
    """ Liste -> int
    l est non vide
    Renvoie le plus petit élément de la liste l """
    if est_vide(l):
        return float("inf")
    else:
        inter = minimum(queue(l))
        if inter > tete(l):
            return tete(l)
        return inter

def maximum(l):
    """ Liste -> int
    l est non vide
    Renvoie le plus petit élément de la liste l """
    if est_vide(l):
        return -float("inf")
    else:
        inter = maximum(queue(l))
        if inter < tete(l):
            return tete(l)
        return inter

# le minimum du vide est +infini !
# le maximum du vide est -infini !
# lol

def supprime(l, e):
    """ Liste, int -> Liste
    l est non vide, e appartient à l
    Renvoie la liste l où on a supprimé une occurence de e """
    if est_singleton(l):
        return creer_vide()
    elif tete(l) == e:
        return queue(l)
    else:
        inter = supprime(queue(l), e)
        return ajoute(inter, tete(l))
    
def supprime_tout(l, e):
    if est_vide(l):
        return creer_vide()
    elif tete(l) == e:
        return supprime_tout(queue(l), e)
    else:
        inter = supprime_tout(queue(l), e)
        return ajoute(inter, tete(l))
    
def tri_selection_rec(l):
    """ Liste -> Liste
    Trie la liste l (tri par sélection) """
    if est_vide(l) or est_singleton(l):
        return l
    else:
        mini = minimum(l)
        lreste = supprime(l, mini)
        lreste_trie = tri_selection_rec(lreste)
        return ajoute(lreste_trie, mini)
    
def tri_selection_rec_sans_doublons(l):
    """ Liste -> Liste
    Trie la liste l (tri par sélection) """
    if est_vide(l) or est_singleton(l):
        return l
    else:
        mini = minimum(l)
        lreste = supprime_tout(l, mini)
        lreste_trie = tri_selection_rec_sans_doublons(lreste)
        return ajoute(lreste_trie, mini)

def diviser(l):
    """ Liste -> Liste, Liste
    Divise la liste en deux listes """
    if est_vide(l):
        return l, l
    elif est_singleton(l):
        return l, creer_vide()
    else:    
        # appel récursif
        inter = diviser(queue(queue(l)))
        # inter est un tuple ! (de listes)
        l1 = ajoute(inter[0], tete(l))
        l2 = ajoute(inter[1], tete(queue(l)))
        return l1, l2

# la première liste est diviser(l)[0]
# la deuxième liste est diviser(l)[1]

def fusionner(l1, l2):
    """ Liste, Liste
    On suppose que l1 et l2 sont triées
    Renvoie la liste des éléments de l1 et l2 triés """
    if est_vide(l1):
        return l2
    elif est_vide(l2):
        return l1
    else:
        if tete(l1) < tete(l2):
            fusionne = fusionner(queue(l1), l2)
            return ajoute(fusionne, tete(l1))
        else:
            fusionne = fusionner(l1, queue(l2))
            return ajoute(fusionne, tete(l2))
        
def tri_fusion(l):
    """ Liste -> Liste
    Trie la liste l (tri fusion) """
    if est_vide(l) or est_singleton(l):
        return l
    else:
        l1, l2 = diviser(l)
        inter1 = tri_fusion(l1)
        inter2 = tri_fusion(l2)
        return fusionner(inter1, inter2)

        
        
        
        
        
        
        
        
        


