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
def liste2str(m: Maillon) -> str: return f"{tete(m)} - {liste2str(queue(m))}" if not est_vide(m) else "x"
def affiche(m: Maillon) -> None: print(liste2str(m))


# Listes exemples
l1 = ajoute(ajoute(ajoute(ajoute(creer_vide(), 9), 8), 6), 1)
l2 = ajoute(ajoute(ajoute(ajoute(creer_vide(), 5), 1), 6), 3)
l3 = ajoute(ajoute(ajoute(creer_vide(), 9), 7), 1)
l4 = ajoute(ajoute(ajoute(creer_vide(), 8), 3), 2)
