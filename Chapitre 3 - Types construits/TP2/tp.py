# iter2 = [1, 2, 3]
# iter3 = (1, 2, 3)
# 
# def affiche(iter):
#     for e in iter
#         print(e)

# note = [16.5, 9.9, 6.4, 7.8, 11.7, 15.4]
# note[2] = 16.4 # enregistrer une modification
# Arrondir au demi point supérieur une note N
# N = 9.3
# if N%1 < 0.5:
#     N = N//1 + 0.5
# else:
#     N = N//1 + 1
# print(N)

def arrondir_notes(notes):
    """ [float] -> None
    Arrondi les notes au demi-point supérieur """
    # parcours par indice de notes :
    for i in range(len(notes)):
        N = notes[i]
        if N%1 < 0.5:
            notes[i] = N//1 + 0.5
        else:
            notes[i] = N//1 + 1
        # print(notes[i])
        
notes = [16.5, 9.9, 16.4, 7.8, 11.7, 15.4]
arrondir_notes(notes)
assert notes == [17.0, 10.0, 16.5, 8.0, 12.0, 15.5]

# notes = [10, 11, 12]
# notes = (10, 11, 12)

def applique_reduction(prix, reductions):
    """ [int], [int] -> None
    prix et reductions sont deux listes de même taille
    Modifie la liste prix en place pour leur appliquer la réduction
    correspondante """
    for i in range(len(prix)):
        p = prix[i]
        t = reductions[i]
        prix[i] = p*(1-t/100) // 1
    
reduction = [10, 5, 50]
prix = [100, 500, 50]

def inverse_reduction(reductions):
    """ [int] -> None
    Remplace chaque élément de la liste reductions par son pourcentage
    d'augmentation reciproque correspondant """
    for i in range(len(reductions)):
        # t = reductions[i]
        reductions[i] = (1/(1-reductions[i]/100) - 1)*100
        
def copie_independante(liste):
    n = len(liste) # ne sert à rien
    rep = [0 for i in range(len(liste))]
    for i in range(len(liste)):
        rep[i] = liste[i]
    return rep

# def copie_independante(liste):
#     rep = [e for e in liste]
#     return rep

a = [1, 2]
b = copie_independante(a)
print(id(a), id(b))
print(a, b)

def ajoute_fin(liste, e):
    n = len(liste)
    rep = [0 for i in range(n+1)] # rep est une liste de taille n + 1
    for i in range(n):
        rep[i] = liste[i]
    rep[n] = e # dernier indice : n = (n + 1) - 1
    return rep

def supprime_pos(liste, i):
    n = len(liste)
    rep = [0 for i in range(n-1)] # rep est une liste de taille n - 1
    for k in range(n):
        if k < i:
            rep[k] = liste[k]
        else:
            rep[k] = liste[k + 1]
    return rep
