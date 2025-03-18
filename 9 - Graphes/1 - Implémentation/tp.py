class Graphe:
    """ Un graphe représenté par une matrice d'adjacence.
    Les sommets sont les nombres 0, 1, ..., n - 1. """
    def __init__(self, n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]
    
    def sommets(self):
        s = []
        for i in range(self.n):
            s.append(i)
        return s
    
    def ajouter_arc(self, source, destination):
        self.adj[source][destination] = True
        
    def est_voisin(self, source, destination):
        return self.adj[source][destination]
#         if self.adj[source][destination] == True:
#             return True
#         return False

    def voisins(self, sommet):
        l = []
        # for i in range(len(self.adj)):
        for destination in self.sommets():
            if self.est_voisin(sommet, destination):
                l.append(destination)
        return l
    
    def liste_arcs(self):
        arcs = []
        for sommet in self.sommets():
            for destination in self.sommets():
                if self.est_voisin(sommet, destination):
                    arcs.append((sommet, destination))
        return arcs
#         arcs = []
#         for i in range(self.n):
#             for j in range(self.n):
#                 if self.adj[i][j]:
#                     arcs.append((i, j))
#         return arcs

    def ordre(self):
        return len(self.sommets())
        # return self.n

    def taille(self):
        return len(self.liste_arcs())
    
    def decrire(self):
        s = f"Graphe d'ordre {self.ordre()} et de taille {self.taille()}\n"
        for sommet in self.sommets():
            s += f"Sommet {sommet} -> "
            for dest in self.voisins(sommet):
                s += f"{dest} "
            s += "\n"
        print(s)
        
    def ajouter_sommet(self):
        self.n += 1
        for i in range(len(self.adj)):
            self.adj[i].append(False)
        derniere_ligne = [False]*self.n
        self.adj.append(derniere_ligne)
        
    def supprimer_arc(self, source, destination):
        self.adj[source][destination] = False
        
# si l = [1, 2]
# >>> " - ".join([str(e) for e in l])
# 1 - 2
            
                
        
g1 = Graphe(4)
g1.ajouter_arc(1, 3)
g1.ajouter_arc(0, 1)
g1.ajouter_arc(0, 3)
g1.ajouter_arc(3, 2)
g1.ajouter_arc(2, 1)

for row in g1.adj:
    print(row)