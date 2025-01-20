class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def creer_vide(): return None
def est_vide(a): return a is None
def est_feuille(a): return not est_vide(a) and est_vide(gauche(a)) and est_vide(droit(a))
def etiquette(a): return a.etiquette
def etiquette_str(a): return "•" if est_vide(a) else str(etiquette(a))
def gauche(a): return a.gauche
def droit(a): return a.droit
def Arbre(e, a1, a2): return Noeud(e, a1, a2)
