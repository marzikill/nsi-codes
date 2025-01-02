def renvoie_et_supprime_premier(p_list):
    """ [Processus] -> Processus
    Renvoie et supprime de p_list le processus dont l'attribut arrivee est le plus petit """
    instant = p_list[0].arrivee
    indice = 0
    for i in range(len(p_list)):
        if p_list[i].arrivee < instant:
            instant = p_list[i].arrivee
            indice = i
    return p_list.pop(indice)

class Processus:
    """Représente un processus"""
    def __init__(self, pid, arrivee, duree):
        """Processus, int, int, int -> None"""
        self.pid = pid
        self.arrivee = arrivee
        # self.debut = -1
        # self.terminaison = -1
        self.duree = duree
        self.duree_restante = duree

    def __repr__(self):
        """ Processus -> str
        Renvoie une chaine de caractère représentant le processus self """
        return f"<P{self.pid}>"
    
    def avancer(self, d, t):
        """ Processus, int, int -> None
        Le processus (re)prend son exécution à la date t pour une durée d """
        assert t >= self.arrivee, "Impossible d'exécuter un processus inexistant"
        self.duree_restante -= d
    
    def est_termine(self):
        """ Processus -> bool
        Détermine si le processus p a terminé son exécution """
        return self.duree_restante <= 0
    
    def __init__(self, pid, arrivee, duree):
        """ Initialise un processus """
        self.pid = pid
        self.arrivee = arrivee
        self.debut = -1
        self.fin = -1
        self.duree = duree
        self.duree_restante = duree
    
    def avancer(self, d, t):
       """ Processus, int, int -> None
       Avancer un processus en mettant à jour les dates de début et de fin """
       if self.debut == -1:
          self.debut = t
       self.duree_restante -= d
       if self.est_termine():
          self.fin = d + t 
    
    def sejour(self):
        """ Renvoie le temps de séjour de self """
        if self.fin == -1:
            raise AttributeError("Le processus n'est pas terminé")
        return self.fin - self.arrivee
    
    def execution(self):
        """ Renvoie le temps d'exécution de self """
        return self.duree - self.duree_restante
    
    def attente(self):
        """ Renvoie le temps d'attente de self """
        if self.fin == -1:
            raise AttributeError("Le processus n'est pas terminé")
        return self.sejour() - self.execution()
    
    def latence(self):
        """ Renvoie le temps de latence de self """
        if self.debut == -1:
            raise AttributeError("Le processus n'a pas encore accédé au processeur")
        return self.debut - self.arrivee


p1 = Processus(1, 0, 10)
p2 = Processus(2, 3, 4)
p3 = Processus(3, 2, 8)

class Chronogramme:
    """Représente un chronogramme"""
    def __init__(self):
        """Chronogramme -> None"""
        self.table = []
        # self.t = 0

    def temps_ecoule(self):
        """ Chronogramme -> int
        Renvoie le nombre de cycles écoulés depuis l'instant initial """
        return len(self.table)
    
    def enregistrer(self, p, q):
        """ int, int -> None
        Enregistre l'information : le processus p est exécuté pendant q cycles """
        for _ in range(q):
            self.table.append(p)
    
    def __repr__(self):
        """ self -> str
        Renvoie une chaine de caractère représentant le chronogramme self """
        return " | ".join(str(p) for p in self.table)

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
        for _ in range(len(p_list)):
            premier = renvoie_et_supprime_premier(p_list)
            self.file_processus.enfiler(premier)
    
    def exec_quantum(self):
        """ OrdonnanceurFIFO -> None
        Simule l'exécution d'un quantum """
        tps = self.chrono.temps_ecoule()
        p = self.file_processus.examine()
        self.chrono.enregistrer(p, self.quantum)
        p.avancer(self.quantum, tps)
        if p.est_termine():
            self.file_processus.defiler()
    
    def exec(self):
        """ OrdonnanceurFIFO -> Chronogramme
        Simule l'exécution des processus de la file et en renvoie le chronogramme """
        while not self.file_processus.est_vide():
            self.exec_quantum()
        return self.chrono

