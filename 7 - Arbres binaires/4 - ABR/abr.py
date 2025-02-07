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