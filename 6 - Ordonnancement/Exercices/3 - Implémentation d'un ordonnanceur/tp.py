from ds import File

class Processus:
    """Représente un processus"""
    def __init__(self, pid, arrivee, duree):
        """Processus, int, int, int -> None"""
        self.pid = pid
        self.duree = duree
        self.arrivee = arrivee
        self.duree_restante = duree

    def __repr__(self):
        """ Processus -> str
        Renvoie une chaine de caractère représentant le processus self """
        return f"<P{self.pid}>"
    
    def avancer(self, d, t):
        """ Processus, int, int -> None
        Le processus (re)prend son exécution à la date t pour une durée d """
        pass
    
    def est_termine(self):
        """ Processus -> bool
        Détermine si le processus p a terminé son exécution """
        pass

    def sejour(self):
        """ Renvoie le temps de séjour de self """
        pass
    
    def execution(self):
        """ Renvoie le temps d'exécution de self """
        pass
    
    def attente(self):
        """ Renvoie le temps d'attente de self """
        pass
    
    def latence(self):
        """ Renvoie le temps de latence de self """
        pass

class Chronogramme:
    """Représente un chronogramme"""
    def __init__(self):
        """Chronogramme -> None"""
        self.table = []

    def temps_ecoule(self):
        """ Chronogramme -> int
        Renvoie le nombre de cycles écoulés depuis l'instant initial """
        return len(self.table)
    
    def enregistrer(self, p, q):
        """ int, int -> None
        Enregistre l'information : le processus p est exécuté pendant q cycles """
        pass
    
    def __repr__(self):
        """ self -> str
        Renvoie une chaine de caractère représentant le chronogramme self """
        pass

class OrdonnanceurFIFO:
    """Représente un ordonnanceur"""
    def __init__(self, q=1):
        """OrdonnanceurFIFO, int -> None"""
        self.chrono = Chronogramme()
        self.file_processus = File()
        self.quantum = q

    def ajoute_processus(self, p_list):
        """ OrdonnanceurFIFO, [Processus] -> None
        Ajoute à self.file_processus les processus de p_list par ordre d'arrivée """
        pass
    
    def exec_quantum(self):
        """ OrdonnanceurFIFO -> None
        Simule l'exécution d'un quantum """
        pass
    
    def exec(self):
        """ OrdonnanceurFIFO -> Chronogramme
        Simule l'exécution des processus de la file et en renvoie le chronogramme """
        pass

def renvoie_et_supprime_premier(p_list):
    """ [Processus] -> Processus
    Renvoie et supprime de p_list le processus dont l'attribut arrivee est le plus petit """
    pass

p1 = Processus(1, 10, 0)
p2 = Processus(2, 4, 3)
p3 = Processus(3, 8, 2)
ordo = OrdonnanceurFIFO()





















