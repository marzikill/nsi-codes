tab =  [[9,  23, 4, 9],
        [22, 16, 3, 0],
        [5,  6,  1, 8]]

def mystere(tab):
    """ [[int]] -> None """
    m, n = len(tab), len(tab[0])
    # m : nombre lignes
    # n : nombre de colonnes
    for i in range(m):
        for j in range(n):
            tab[i][j] = 2*tab[i][j]

def nombre_occurrences(tab, e):
    m, n = len(tab), len(tab[0])
    cpt = 0
    # m : nombre lignes
    # n : nombre de colonnes
    for i in range(m):
        for j in range(n):
            if tab[i][j] == e:
                cpt = cpt + 1
    return cpt
    
tab = [[3, 3, 3],
       [3, 2, 1],
       [0, 1, 2],
       [2, 1, 3]]

# pour e compris entre 0 et 4 (inclus)
for e in range(5):
    print(nombre_occurrences(tab, e), end = ' ')
# nb occ de 0 : 1
# nb occ de 1 : 3
# nb occ de 2 : 3
# nb occ de 3 : 5
# nb occ de 4 : 0

tab = [[3, 3, 3],
       [3, 2, 1],
       [0, 1, 2]]

# ex :
# - nombre_occurences_col(tab, j, e) : compte les occurrences de e dans la colonne j de tab
# - somme(tab) : renvoie la somme de tous les éléments présents dans tab

    
