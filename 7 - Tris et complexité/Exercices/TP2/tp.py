def est_trie(tab):
    """ [int] -> bool
    Renvoie True si tab est trié par ordre croissant, False sinon """
    pass


def genere_tableau(n, x_min, x_max):
    """ int, int, int -> [int]
    Renvoie un tableau d'entiers tirés au hasard parmi [x_min, x_max] """
    pass


def echange(tab, i, j):
    """ [int], int, int -> None
    Échange les éléments d'indice i et j dans tab """
    pass


def tri_insertion(tab):
    """ [int] -> None
    Trie le tableau en place. """
    # Si le tableau est vide il n'y a rien à faire.
    if len(tab) == 0:
        return
    zone_triee = 0
    # Tant qu'il y a des éléments à trier dans le tableau
    while ...:
        pos_nouveau = zone_triee
        nouveau_elem = tab[zone_triee]
        # On échange le nouvel élément avec
        # l'élément du tableau qui se trouve
        # à sa gauche tant que cela est nécessaire 
        while ...:
            echange(tab, ..., ...)
            pos_nouveau = ... # on met à jour la position du nouvel élément
        # Il y a un élément de plus dans la zone triée
        zone_triee = ...


def tri_bulles(tab):
    """ [int] -> None
    Trie le tableau en place.  """
    if len(tab) == 0:
        return
    for passage in range(...):
        for i in range(...):
            # si deux éléments consécutifs ne sont
            # pas bien ordonnés, on échange leur position
            if ...:
                echange(...)

def maximum_parmi(tab, i):
    """ [int], int -> int
    Renvoie l'indice du maximum parmi les n-i+1 premiers éléments de tab """
    pass

def tri_selection(tab):
    """ [int] -> None """
    for i in range(...):
        i_maxi = ...
        echange(...)

