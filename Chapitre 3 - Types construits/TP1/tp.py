def longueur(iterable):
    """ Iterable -> int
    Compte le nombre d'éléments dont est constitué iterable """
    n = 0
    for e in iterable:
        n = n + 1
    return n

assert longueur("bonjour") == 7
assert longueur([1, 2, 3]) == 3
assert longueur(["salut", "toi"]) == 2

def appartient(iterable, elem):
    """ Iterable, Element -> bool
    Renvoie True si elem est l'un des éléments de l'itérable, False sinon """
    present = False
    for e in iterable:
        if e == elem:
            present = True
    return present

assert appartient([7, 8, 9], 9) == True
assert appartient([7, 8, 9], 5) == False
assert appartient("bonjour", "b") == True
assert appartient(["salut", "toi"], "t") == False

def nombre_occurrences(iterable, elem):
    """ Iterable, Element -> int
    Renvoie le nombre de fois qu'apparaît elem dans iter """
    n = ...
    for e in iterable:
        if ...:
            ...
    return ...

def plus_long_mot(mots):
    """ [str] -> int
    Renvoie la longueur du plus long mot parmis les mots """
    record = 0 # aucun mot n'a été étudié
    for ...: 
        if ...: 
            record = ...
    return ...

def prix_total(quantite, prix):
    """ [int], [int] -> int
    quantite et prix sont deux listes de même taille
    Renvoie le prix total que doit payer le client """
    p = 0
    for i in ...:
        p = p + ...
    return ...

def deux_suivants_egaux(lst):
    """ list -> bool
    Renvoie True si deux éléments consécutifs de la liste sont égaux, False sinon """
    pass

