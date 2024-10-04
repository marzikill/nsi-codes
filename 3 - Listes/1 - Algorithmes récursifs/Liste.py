class Liste:
    def __init__(self, c, n):
        assert isinstance(c, int), f"Les éléments d'une Liste sont de type int"
        assert isinstance(n, Liste) or n is None, f"La queue d'une Liste doit être une Liste"
        self.c = c
        self.n = n

def creer_vide() -> Liste: return None
def est_vide(l: Liste) -> bool: return l is None
def ajoute(l: Liste, e: int) -> Liste: return Liste(e, l)
def tete(l: Liste) -> int: return l.c
def queue(l: Liste) -> Liste: return l.n
def affiche(l: Liste) -> None: print("x") if est_vide(l) else (print(tete(l), end = " - "), affiche(queue(l)))
def element(l: Liste, i: int) -> int: return tete(l) if i == 0 else element(queue(l), i - 1)
