class Maillon:
    def __init__(self, v, n):
        self.valeur = v
        self.suivant = n

class Pile:
    """Une pile d'entiers"""
    def __init__(self):
        """ Pile -> Nonetype """
        self.sommet = None

    def est_vide(self):
        """ Pile -> bool
        Détermine si la pile est vide """
        return self.sommet is None
    
    def empiler(self, v):
        """ Pile, int -> Nonetype
        Empile la valeur v au sommet de la pile self """
        m = Maillon(v, self.sommet)
        self.sommet = m
    
    def depiler(self):
        """ Pile -> int
        Renvoie l'élément présent au sommet de la pile self, en le supprimant de la pile """
        if self.est_vide():
            raise IndexError("Impossible de dépiler : la pile est vide")
        else:
            valeur_e = self.sommet
            self.sommet = self.sommet.suivant
            return valeur_e.valeur
    
    def __str__(self):
        """ Pile -> str
        Construit la chaîne de caractère représentant la pile self """
        # s='[Sommet]'
        s = ["[Sommet]"]
        maillon_courant=self.sommet
        while maillon_courant != None:
            # s=s+f' {maillon_courant.valeur}'
            s.append(f' {maillon_courant.valeur}')
            maillon_courant=maillon_courant.suivant
        return "".join(s)

class File:
    """Une file d'entiers"""
    def __init__(self):
        """File -> Nonetype"""
        self.debut = None
        self.fin = None

    def est_vide(self):
        """ File -> bool
        Détermine si la file self est vide """
        return self.debut is None and self.fin is None
    
    def enfiler(self, v):
        """ File, int -> Nonetype
        Ajoute l'élément v à la file self """
        if self.est_vide():
            m = Maillon(v,None)
            self.debut = m
            self.fin = m
        else:
            nouveau = Maillon(v,None)
            maillon_courant = self.debut
            self.fin.suivant = nouveau
            self.fin = nouveau
        
    def defiler(self):
        """ File -> int
        Renvoie le premier élément de la file en le supprimant de celle-ci """
        if self.est_vide():
            raise IndexError("la file est vide")
        valeur=self.debut.valeur
        self.debut=self.debut.suivant
        if self.debut is None:
            self.fin = None
        return valeur

    def examine(self):
        if self.est_vide():
            raise IndexError("la file est vide")
        return self.debut.valeur
        
    
    def __str__(self):
        """ self -> str
        Construit la chaîne de caractères représentant la file self """
        s = ["[début]"]
        maillon_courant=self.debut
        while maillon_courant != None:
            # s=s+f' {maillon_courant.valeur}'
            s.append(f' {maillon_courant.valeur}')
            maillon_courant=maillon_courant.suivant
        s.append(" [fin]")
        return "".join(s)

class PileBornee:
    def __init__(self, maxi):
        self.pile = Pile()
        self.capacite = maxi
        self.taille = 0
        
    def est_vide(self):
        return self.pile.est_vide()
        # if self.taille == 0:
        #    return True
        # return False
        
    def est_pleine(self):
        """ PileBornee -> bool """
        return self.capacite == self.taille
    
    def empiler(self, v):
        """ PileBornee, int -> bool """
        if self.est_pleine():
            raise IndexError('la pile est pleine')
        else:
            self.pile.empiler(v)
            self.taille += 1
                    
    
    def depiler(self):
        """ PileBornee -> int """
        if self.est_vide():
            raise IndexError('On ne peut pas depiler')
        else:
            # valeur = self.pile.sommet.valeur
            self.taille -= 1
            return self.pile.depiler()
    
    def __str__(self):
        return self.pile.__str__()
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
