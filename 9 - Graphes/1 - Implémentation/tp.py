class Graphe:
    """ Un graphe représenté par une matrice d'adjacence.
    Les sommets sont les nombres 0, 1, ..., n - 1. """
    def __init__(self, n):
        self.n = n
        self.adj = [[False]*n for _ in range(n)]

    def sommets(self):
        """ Graphe -> [int]
        Renvoie la liste des sommets du graphe self """
        return [i for i in range(self.n)]

    def ajouter_arc(self, source, destination):
        """ Graphe, int, int -> None
        Ajoute l'arc source -> destination """
        self.adj[source][destination] = True

g1 = Graphe(4)
g1.ajouter_arc(1, 3)
