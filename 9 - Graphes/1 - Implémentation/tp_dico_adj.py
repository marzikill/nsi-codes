class Graphe:
    """ Un graphe représenté par une matrice d'adjacence.
    Les sommets sont les nombres 0, 1, ..., n - 1. """
    def __init__(self):
        self.adj = dict()
    
    def sommets(self):
        return list(self.adj.keys())
    
    def ajouter_arc(self, source, destination):
        self.adj[source].append(destination)
        
    def est_voisin(self, source, destination):
        # self.adj[source] : tous les voisins de source
        # for v in self.adj[source]:
        for v in self.voisins(source):
            if v == destination:
                return True
        return False

    def voisins(self, sommet):
        return self.adj[sommet]
    
    def liste_arcs(self):
        l = []
        for sommet in self.sommets():
            for destination in self.voisins(sommet):
                l.append((sommet, destination))
        return l

    def ordre(self):
        return len(self.sommets())
        
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
        
    def ajouter_sommet(self, s):
        self.adj[s] = []
        
    def supprimer_arc(self, source, destination):
        vs = self.adj[source]
        for i in range(len(vs)):
            if vs[i] == destination:
                vs.pop(i)
                # attention : on modifie la liste
                # vs alors qu'on est en train
                # d'itérer dessus : c'est en
                # général une très mauvaise idée
                return
    
    def supprimer_sommet(self, source):
        ...

        
# si l = [1, 2]
# >>> " - ".join([str(e) for e in l])
# 1 - 2
            
                
        
g1 = Graphe()
g1.ajouter_sommet('A')
g1.ajouter_sommet('B')
g1.ajouter_sommet('C')
g1.ajouter_sommet('D')
g1.ajouter_sommet('E')
g1.ajouter_sommet('F')
g1.ajouter_arc('A', 'B')
g1.ajouter_arc('A', 'C')
g1.ajouter_arc('A', 'D')
g1.ajouter_arc('B', 'D')
g1.ajouter_arc('C', 'A')
g1.ajouter_arc('C', 'D')
g1.ajouter_arc('D', 'E')
g1.ajouter_arc('E', 'F')
g1.ajouter_arc('F', 'E')

for s, l in g1.adj.items():
    print(f"{s} -> {l}")
