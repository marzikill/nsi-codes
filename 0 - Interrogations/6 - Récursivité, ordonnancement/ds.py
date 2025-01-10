class Maillon:
    """ Un maillon d'une liste chainée. """
    def __init__(self, v, s):
        """ int, Maillon -> None """
        self.valeur = v
        self.suivant = s

def creer_vide() -> Maillon: return None
def est_vide(m: Maillon) -> bool: return m is None
def est_singleton(m: Maillon) -> bool: return not est_vide(m) and est_vide(queue(m))
def ajoute(m: Maillon, e: int) -> Maillon: return Maillon(e, m)
def tete(m: Maillon) -> int: return m.valeur
def queue(m: Maillon) -> Maillon: return m.suivant
def affiche(m: Maillon) -> None:
    if est_vide(m):
        print('x')
    else:
        print(tete(m), end=' - ')
        affiche(queue(m))
def concatene(l1, l2):
    if est_vide(l1):
        return l2
    else:
        return ajoute(concatene(queue(l1), l2), tete(l1))
#+END_SRC