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
    nb = 0
    for n in notes[i]:
        if n == -1:
            nb = nb + 1
    return nb

def nombre_absences(notes, eleve):
    """ [[str | int]], str -> int
    Renvoie le nombre d'absences de eleve """
    # on parcourt toutes les lignes
    # à la recherche de l'indice de la ligne dont le
    # premier élément est eleve
    # On renvoie -1 si eleve n'est pas dans la liste
    for i in range(nombre_eleves(notes)):
        if notes[i][0] == eleve:
            return nombre_absences_indice(notes, i)
    return -1

def est_representative(notes, i):
    nb_abs_maxi = int(1/3*nombre_notes(notes)) + 1
    return nombre_absences_indice(notes, i) < nb_abs_maxi

def convocation_rattrapage(notes):
    """ [[ str | int ]] -> [str]
    Renvoie la liste des élèves à convoquer au rattrapage """
    return [notes[i][0] for i in range(nombre_eleves(notes))
            if not est_representative(notes, i)]

def moyenne_devoir(notes, n):
    """ [[str | int]], int -> int
    Renvoie la moyenne du devoir numero n """
    s = 0 # somme des notes des élèves
    nb = 0 # nombre d'élèves présents
    # on additionne toutes les notes des élèves
    # présents au devoir n et on compte le nombre
    # d'élèves présents.
    s = 0
    nb_presents = 0
    for i in range(nombre_eleves(notes)):
        if notes[i][n] != -1:
            s = s + notes[i][n]
            nb_presents = nb_presents + 1
    return round(s/nb_presents, 2)

def pire_devoir(notes):
    """ [[str | int]] -> int
    Renvoie le numéro du devoir dont la moyenne est la plus faible
    """
    # il n'y a pas de pire devoir si il n'y a pas de notes
    if nombre_notes(notes) == 0:
        return -1
    n_mini = 1
    pire = moyenne_devoir(notes, 1)
    for n in range(1, nombre_notes(notes) + 1):
        if moyenne_devoir(notes, n) < pire:
            n_mini = n
            pire = moyenne_devoir(notes, n)
    return n_mini      

def moyennes(notes):
    """ [[str | int]] -> int
    Renvoie la moyenne des élèves de la classe """
    # on initialise le tableau des moyennes : il s'agit d'une liste 
    # dont tous les éléments sont des listes du type 
    # [prénom de l'élève, -1]
    # notes[i][0] correspond au prénom de l'élève d'indice i
    m = [[notes[i][0], -1] for i in range(nombre_eleves(notes))]
    joker = pire_devoir(notes)
    for i in range(nombre_eleves(notes)):
        nb_notes = 0
        s = 0
        for n in range(1, nombre_notes(notes) + 1):
            # On compte le devoir si l'élève est présent à
            # celui-ci et si ça n'est pas le pire devoir
            if notes[i][n] != -1 and n != joker:
                nb_notes += 1
                s += notes[i][n]
        # On ne compte les notes que si la moyenne est
        # représentative 
        if est_representative(notes, i):
            m[i][1] = round(s/nb_notes, 2)
    return m
    

