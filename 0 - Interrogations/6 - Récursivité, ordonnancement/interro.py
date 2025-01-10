from ds import *

def repeter(a, n):
    if n == 0:
        return creer_vide()
    else:
        # n > 0
        inter = repeter(a, n - 1)
        return ajoute(inter, a)

def repliquer(l, n):
    if est_vide(l):
        return creer_vide()
    elif n == 0:
        return creer_vide()
    else:
        inter = repliquer(queue(l), n)
        debut = repeter(tete(l), n)
        return concatene(debut, inter)

def eliminer(l):
    if est_vide(l):
        return creer_vide()
    elif est_singleton(l):
        return l
    else:
        inter = eliminer(queue(l))
        if tete(l) == tete(queue(l)):
            return inter
        else:
            return ajoute(inter, tete(l))

# l = creer_vide()
# l = ajoute(l, 3)
# l = ajoute(l, 2)
# ...
l = ajoute(ajoute(ajoute(creer_vide(), 3), 2), 1)
l2 = concatene(repliquer(l, 2), repliquer(l, 3))
affiche(l)
affiche(l2)