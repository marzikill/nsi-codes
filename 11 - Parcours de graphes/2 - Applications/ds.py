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

class Ensemble:
    def __init__(self):
        """ Ensemble -> Nonetype """
        self.contenu = dict()

    def ajouter(self, elt):
        """ Ensemble, elt -> Nonetype """
        self.contenu[elt] = True

    def supprimer(self, elt):
        """ Ensemble, elt -> Nonetype """
        self.contenu.pop(elt)

    def __contains__(self, elt):
        """ Ensemble, elt -> bool """
        if self.contenu.get(elt):
            return True
        return False

def arcs_vers_graphe_o(arcs):
    """ [(Sommet, Sommet)] -> Graphe
    Sommet peut être de type int ou str
    Construit le graphe non orienté dont on donne la liste des arêtes. """
    g = Graphe()
    for (source, destination) in arcs:
        g.ajouter_sommet(source)
        g.ajouter_sommet(destination)
        g.ajouter_arc(source, destination)
    return g

def arcs_vers_graphe_no(arcs):
    """ [(Sommet, Sommet)] -> Graphe
    Sommet peut être de type int ou str
    Construit le graphe non orienté dont on donne la liste des arêtes. """
    g = Graphe()
    for (source, destination) in arcs:
        g.ajouter_sommet(source)
        g.ajouter_sommet(destination)
        g.ajouter_arc(source, destination)
        g.ajouter_arc(destination, source)
    return g


def parcours_profondeur(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en profondeur """
    vus = Ensemble()
    ordre_visites = []
    à_explorer = Pile()
    à_explorer.empiler(depart)
    while not à_explorer.est_vide():
        # définition du sommet courant 
        sommet = à_explorer.depiler()
        if sommet in vus:
            continue
        # opération de traitement
        vus.ajouter(sommet)
        ordre_visites.append(sommet)
        # ajout des voisins non visités
        for destination in reversed(G.voisins(sommet)):
            if not destination in vus:
                à_explorer.empiler(destination)
    return ordre_visites

def parcours_largeur(G, depart):
    """ Graphe, Sommet -> [Sommet]
    Parcours le graphe G depuis le sommet depart en largeur """
    vus = Ensemble()
    ordre_visites = []
    à_explorer = File()
    à_explorer.enfiler(depart)
    while not à_explorer.est_vide():
        # définition du sommet courant 
        sommet = à_explorer.defiler()
        if sommet in vus:
            continue
        # opération de traitement
        vus.ajouter(sommet)
        ordre_visites.append(sommet)
        # ajout des voisins non visités
        for destination in G.voisins(sommet):
            if not destination in vus:
                à_explorer.enfiler(destination)
    return ordre_visites

def oublie_orientation(G):
    """ Graphe -> Graphe
    Renvoie le graphe non orienté G' dans lequel on a "oublié"
    le sens des arcs de G """
    Gp = Graphe()
    for s in G.sommets():
        Gp.ajouter_sommet(s)
    for (source, destination) in G.liste_arcs():
        Gp.ajouter_arc(source, destination)
        Gp.ajouter_arc(destination, source)
    return Gp

g1 = arcs_vers_graphe_o([(0, 2), (1, 0), (1, 3),
                         (3, 2), (4, 5), (5, 6), (6, 4)])    
g2 = arcs_vers_graphe_no([(0, 1), (0, 5), (0, 8),
                          (1, 2), (2, 3), (3, 4), (3, 7),
                          (3, 8), (4, 5), (4, 7)])
g3 = arcs_vers_graphe_o([(1, 2), (4, 5), (4, 3), (5, 3)])
g3.ajouter_sommet(0)
g4 = arcs_vers_graphe_o([(0, 1), (1, 2), (2, 3), (2, 4),
                         (3, 5), (5, 4), (4, 1)])
