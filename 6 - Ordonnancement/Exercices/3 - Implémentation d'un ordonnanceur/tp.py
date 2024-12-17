from ds import File

class Processus:
    """Représente un processus"""
    def __init__(self, pid, duree, arrivee):
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
        if self.arrivee <= t:
            self.duree_restante -= d
            
    def est_termine(self):
        """ Processus -> bool
        Détermine si le processus p a terminé son exécution """
        return self.duree_restante <= 0

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
        for i in range(q):
            self.table.append(p)
    
    def __repr__(self):
        """ self -> str
        Renvoie une chaine de caractère représentant le chronogramme self """
        return str(self.table)

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
        for i in range(len(p_list)):
            p = renvoie_et_supprime_premier(p_list)
            self.file_processus.enfiler(p)
    
    def exec_quantum(self):
        """ OrdonnanceurFIFO -> None
        Simule l'exécution d'un quantum """
        t = self.chrono.temps_ecoule()
        p = self.file_processus.examine()
        self.chrono.enregistrer(p, self.quantum)
        p.avancer(self.quantum, t)
        if p.est_termine():
            self.file_processus.defiler()
            
    def exec(self):
        """ OrdonnanceurFIFO -> Chronogramme
        Simule l'exécution des processus de la file et en renvoie le chronogramme """
        while not self.file_processus.est_vide():
            self.exec_quantum()

def renvoie_et_supprime_premier(p_list):
    """ [Processus] -> Processus
    Renvoie et supprime de p_list le processus dont l'attribut arrivee est le plus petit """
    mini = p_list[0].arrivee
    i_mini = 0
    for i in range(len(p_list)):
        if p_list[i].arrivee < p_list[i_mini].arrivee:
            i_mini = i
    return p_list.pop(i_mini)

# Il ne suffit pas de faire un parcours par valeur
# car il faut supprimer le processus dont le temps
# d'arrivée est le plus faible de p_list : pour ça
# on a besoin de son indice.
# def renvoie_et_supprime_premier(p_list):
#     court_tempo = p_list[0]
#     for process in p_list:
#         if process.arrivee <= court_tempo.arrivee :
#             court_tempo = process
#     return court_tempo

p1 = Processus(1, 10, 0)
p2 = Processus(2, 4, 3)
p3 = Processus(3, 8, 2)
p_list = [p1, p2, p3]

ordo = OrdonnanceurFIFO()
ordo.ajoute_processus(p_list)
print(ordo.file_processus)
ordo.exec()


















