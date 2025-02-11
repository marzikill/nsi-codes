class Noeud:
    def __init__(self, v, g, d):
        self.etiquette = v
        self.gauche = g
        self.droit = d
    
class ArbreBinaire:
    def __init__(self, n = None):
        self.racine = n
        
    def est_vide(self):
        """ ArbreBinaire -> bool """
        return self.racine == None
    
    def etiquette(self):
        """ ArbreBinaire ->  int """
        return self.racine.etiquette
    
    def gauche(self):
        """ ArbreBinaire ->  ArbreBinaire """
        return self.racine.gauche
    
    def droit(self):
        """ ArbreBinaire -> ArbreBinaire """
        return self.racine.droit
    
    def est_feuille(self):
        """ ArbreBinaire -> bool """
        if self.est_vide():
            return False
        if self.droit().est_vide() and self.gauche().est_vide():
            return True
        return False
    
    def __str__(self):
        """ ArbreBinaire -> str """
        if self.est_vide():
            return ""
        else:
            s1 = self.gauche().__str__()
            s2 = self.droit().__str__()
            e = self.etiquette()
            return f"({s1}) {e} ({s2})"
        
    def ajouter_depuis_tableau(self, tab):
        """ ArbreBinaire, [int] -> None """
        file = [self]
        while not tab == []:
            a = file.pop(0)
            e = tab.pop(0)
            # Traitement
            if e is not None:
                a.racine = Noeud(e, ArbreBinaire(), ArbreBinaire())
                file.append(a.gauche())
                file.append(a.droit())
                
    def taille(self):
        """ ArbreBinaire -> int """
        if self.est_vide():
            return 0
        else:
            return 1 + self.gauche().taille() + self.droit().taille()
            
    def appartient(self, e):
        """ ArbreBinaire, int -> bool """
        if self.est_vide():
            return False
        elif self.etiquette() == e:
            return True
        else:
            return self.gauche().appartient(e) or self.droit().appartient(e)
        
    def inserer(self, e):
        """ ArbreBinaire, int -> None """
        if self.est_vide():
            self.racine = Noeud(e, ArbreBinaire(), ArbreBinaire())
        else:
            if self.gauche().taille() <= self.droit().taille():
                self.gauche().inserer(e)
            else:
                self.droit().inserer(e)

    
a_vide = ArbreBinaire()
feuille1 = ArbreBinaire(Noeud(1, ArbreBinaire(), ArbreBinaire()))
feuille2 = ArbreBinaire(Noeud(2, ArbreBinaire(), ArbreBinaire()))
a0 = ArbreBinaire(Noeud(3, feuille1, feuille2))
a1 = ArbreBinaire()
tab = [1, 2, None, None, 3, None, None]
a1.ajouter_depuis_tableau(tab)
a2 = ArbreBinaire()
a2.ajouter_depuis_tableau([3, 1, 4, None, 2])
a3 = ArbreBinaire()
a3.ajouter_depuis_tableau([3, 2, 4, 1])
a4 = ArbreBinaire()
a4.ajouter_depuis_tableau([3, 2, 4, None, 1])
a5 = ArbreBinaire()
a5.ajouter_depuis_tableau([3, 2, 6, 0, 4])
a6 = ArbreBinaire()
a6.ajouter_depuis_tableau([3, 1, 5, None, None, 2, 9])
a7 = ArbreBinaire()
for i in range(1, 8):
    a7.inserer(i)
    
class ABR:
    def __init__(self, n = None):
        self.racine = n
        
    def est_vide(self):
        """ ABR -> bool """
        return self.racine == None
    
    def etiquette(self):
        """ ABR ->  int """
        return self.racine.etiquette
    
    def gauche(self):
        """ ABR ->  ABR """
        return self.racine.gauche
    
    def droit(self):
        """ ABR -> ABR """
        return self.racine.droit
    
    def est_feuille(self):
        """ ABR -> bool """
        if self.est_vide():
            return False
        if self.droit().est_vide() and self.gauche().est_vide():
            return True
        return False
    
    def __str__(self):
        """ ABR -> str """
        if self.est_vide():
            return ""
        else:
            s1 = self.gauche().__str__()
            s2 = self.droit().__str__()
            e = self.etiquette()
            return f"({s1}) {e} ({s2})"
        
    def inserer(self, e):
        """ ABR, int -> None
        self est toujours un ABR après exécution de cette méthode """
        if self.est_vide():
            self.racine = Noeud(e, ABR(), ABR())
        else:
            if e < self.etiquette():
                self.gauche().inserer(e)
            else:
                self.droit().inserer(e)
    
    def appartient(self, e):
        """ ABR, int -> int"""
        if self.est_vide():
            return False
        elif e == self.etiquette():
            return True
        else:
            if e < self.etiquette():
                return self.gauche().appartient(e)
            else:
                return self.droit().appartient(e)
            
    def minimum(self):
        """ ABR -> int """
        if self.gauche().est_vide():
            return self.etiquette()
        return self.gauche().minimum()
        
a = ABR()
tab = [3, 6, 149, 7, 80, 4]
for e in tab:
    a.inserer(e)

a_test = ABR()
a_test.inserer(3)

def tableau_vers_abr(tab):
    """ tab -> ABR """
    a = ABR()
    for e in tab:
        a.inserer(e)
    return a
    
def stocke(a, l):
    """ ABR, [int] -> None """
    if a.est_vide():
        return 
    else:
        stocke(a.gauche(), l)
        l.append(a.etiquette())
        stocke(a.droit(), l)

def trie(tab):
    """ [int] -> [int] """
    a = tableau_vers_abr(tab)
    l = []
    stocke(a, l)
    return l
    
    