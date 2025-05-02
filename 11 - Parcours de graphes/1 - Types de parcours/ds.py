class Pile:
    def __init__(self, max_elt = float('inf')):
        self.contenu = []
        self.max_elt = max_elt
        self.log_list = []

    def __repr__(self):
        return "[" + ", ".join(b.__repr__() for b in self.contenu) + "] (Sommet pile)" 

    def __len__(self):
        return len(self.contenu)

    def log(self):
        print("\n".join(self.log_list))

    def affiche(self):
        print(self)

    def est_vide(self):
        return self.contenu == []

    def est_pleine(self):
        return self.max_elt == len(self)

    def empiler(self, c):
        self.log_list.append(f"Empile {c}")
        if self.est_pleine():
            raise IndexError("Capacité maximale de la pile atteinte")
        self.contenu.append(c)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Impossible de dépiler : la pile est vide.")
        c = self.contenu.pop()
        self.log_list.append(f"Dépile {c}")
        return c

class File:
    def __init__(self, max_elt = float('inf')):
        self.contenu = []
        self.max_elt = max_elt
        self.log_list = []

    def __repr__(self):
        return "(Début file) [" + ", ".join(b.__repr__() for b in self.contenu) + "]"

    def __len__(self):
        return len(self.contenu)

    def log(self):
        print("\n".join(self.log_list))

    def affiche(self):
        print(self)

    def est_vide(self):
        return self.contenu == []

    def est_pleine(self):
        return len(self) == self.max_elt 

    def enfiler(self, b):
        self.log_list.append(f"Enfile {b}")
        if self.est_pleine():
            raise IndexError("Capacité maximale de la file atteinte")
        self.contenu.append(b)

    def defiler(self):
        if self.est_vide():
            raise IndexError("Impossible de défiler : la file est vide.")
        c = self.contenu.pop(0)
        self.log_list.append(f"Défile {c}")
        return c

class Graphe:
    """ Un graphe représenté par un dictionnaire d'adjacence. """
    def __init__(self):
        self.adj = dict()

    def ajouter_sommet(self, s):
        """ Graphe, str -> Nonetype
        Ajoute le sommet s au graphe self """
        # self.adj.setdefault(source, [])
        if s not in self.adj:
            self.adj[s] = []

    def ajouter_arc(self, source, destination):
        """ Graphe, str, str -> Nonetype
        Ajoute l'arc source -> destination au graphe self """
        self.adj[source].append(destination)

    def est_voisin(self, source, destination):
        """ Graphe, str, str -> bool
        Détermine si source et destination sont voisins """
        for v in self.adj[source]:
            if v == destination:
                return True
        return False
    
    def sommets(self):
        """ Graphe -> [str]
        Renvoie la liste des sommets du graphe self """
        return sorted(list(self.adj.keys()))
    
    def voisins(self, s):
        """ Graphe, stsr -> [str]
        Renvoie la liste des voisins de sommet """
        return sorted(self.adj[s])
    
    def liste_arcs(self):
        """ Graphe -> [(str, str)]
        Renvoie la liste des arcs du graphe """
        arcs = []
        for u in self.sommets():
            for v in self.adj[u]:
                arcs.append((u, v))
        return arcs
    
    def supprimer_arc(self, source, destination):
        """ Graphe, int, int -> Nonetype
        Supprime le ou les arcs source -> destination """
        for i, v in enumerate(self.adj[source]):
            if v == destination:
                self.adj[source].pop(i)
            
    def supprimer_sommet(self, sommet):
        """ Graphe, str -> Nonetype
        Supprime le sommet i du graphe. """
        for s in self.sommets():
            self.supprimer_arc(s, sommet)
        self.adj.pop(sommet)
    
    def ordre(self):
        """ Graphe -> int
        Renvoie l'ordre du graphe  """
        return len(self.adj)
    
    def taille(self):
        """ Graphe -> int
        Renvoie la taille du graphe """
        return len(self.liste_arcs())
    
    def decrire(self):
        """ Graphe -> Nonetype
        Affiche une description du graphe self """
        print(f"Graphe d'ordre {self.ordre()} et de taille {self.taille()}")
        for s in self.sommets():
            print(f"Sommet {s} -> {' '.join(str(i) for i in self.voisins(s))}")
