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

def nombre_occurences_col(tab, j, e):
    n = len(tab[0]) # nb colonnes
    m = len(tab) # nb lignes
    cpt = 0
    for i in range(m): # on parcourt toutes les lignes
        if tab[i][j] == e:
            cpt = cpt + 1
    return cpt

# ex :
# - nombre_occurences_col(tab, j, e) : compte les occurrences de e dans la colonne j de tab
# - somme(tab) : renvoie la somme de tous les éléments présents dans tab

def somme(tab):
    s = 0
    n = len(tab[0]) # nb colonnes
    m = len(tab) # nb lignes
    for i in range(m):
        for j in range(n):
            s = s + tab[i][j]
    return s

def nombre_eleves(notes):
    """ [[str | int]] -> int
    Renvoie le nombre d'élèves de la classe """
    if notes == []:
        return -1
    return len(notes)

def nombre_notes(notes):
    """ [[str | int ]] -> int
    Renvoie le nombre d'évaluations passées par les élèves """
    return len(tab[0]) - 1

def nombre_absences_indice(notes, i):
    """ [[str | int]], int -> int
    Renvoie le nombre d'absences de l'élève d'indice i """
    # on compte le nombre de -1 dans la colonne
    # d'indice i du tableau
    

def nombre_absences(notes, eleve):
    """ [[str | int]], str -> int
    Renvoie le nombre d'absences de eleve """
    # on parcourt toutes les lignes
    # à la recherche de l'indice de la ligne dont le
    # premier élément est eleve

def moyenne_devoir(notes, n):
    """ [[str | int]], int -> int
    Renvoie la moyenne du devoir numero n """
    s = 0 # somme des notes des élèves
    nb = 0 # nombre d'élèves présents
    # on additionne toutes les notes des élèves
    # présents au devoir n et on compte le nombre
    # d'élèves présents.

def pire_devoir(notes):
    """ [[str | int]] -> int
    Renvoie le numéro du devoir dont la moyenne est la plus faible
    """
    pass
    

