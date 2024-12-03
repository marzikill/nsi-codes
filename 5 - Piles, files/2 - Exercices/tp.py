from ds import *

p = creer_pile_vide()
empiler(p, 12)
empiler(p, 14)
empiler(p, 8)
empiler(p, 7)
empiler(p, 19)
empiler(p, 22)

def sommet(p):
    p1 = depiler(p)
    empiler(p, p1)
    return p1

# accès au premier élément sans modifier la pile
# complexité en temps constant

f = creer_file_vide()
enfiler(f, 22)
enfiler(f, 19)
enfiler(f, 7)
enfiler(f, 8)
enfiler(f, 14)
enfiler(f, 12)

def tete(f):
    f_aux = creer_file_vide()
    b = defiler(f)
    enfiler(f_aux, b)
    while not est_file_vide(f):
        enfiler(f_aux, defiler(f))
    while not est_file_vide(f_aux):
        enfiler(f, defiler(f_aux))
    return b

# accès au premier élément sans modifier la pile
# complexite linéaire


def tamis(p):
    """ Pile -> Pile, Pile """
    p_pair, p_impair = creer_pile_vide(), creer_pile_vide()
    while not est_pile_vide(p):
        e = depiler(p)
        if e%2 != 0:
            empiler(p_impair, e)
        else:
            empiler(p_pair, e)
    return p_pair, p_impair
        
def maximum(p):
    """ Pile -> int """
    # initialisation incorrecte si que des nombres < 0
    # maxi = 0
    # Solution 1 (très bien)
    # maxi = depiler(p)
    # Solution 2 (sans dépilement)
    maxi = -float("inf") # valeur initiale plus petite que tous les entiers
    while not est_pile_vide(p):
        c = depiler(p)
        if c > maxi:
            maxi = c
    return maxi
    
def retourne(p):
    """ Pile -> None """
    f_aux = creer_file_vide()
    while not est_pile_vide(p):
        enfiler(f_aux, depiler(p))
    while not est_file_vide(f_aux):
        empiler(p, defiler(f_aux))
    # pas d'instruction return
    # la fonction est exécutée pour son effet de bord
    # on modifie la pile p en place
    
def retourne_mieux(p):
    p_aux = creer_pile_vide()
    while not est_pile_vide(p):
        empiler(p_aux, depiler(p))
    p = p_aux
# est_ce que c'est mieux ?

# Exercice 3
# Code naïf qui ne marche pas du tout
# def est_bien_parenthesee(p):
#     p_ouverte, p_ferme = 0, 0
#     for parenthese in p:
#         if parenthese == "(":
#             p_ouverte += 1
#         else:
#             p_ferme += 1
#     if p[-1] == ")" and p[0] == "(" and p_ouverte == p_ferme:
#         return True
#     return False

def est_bien_parenthesee(chaine):
    """ str -> bool """
    p = creer_pile_vide()
    for c in chaine:
        if c == "(":
            empiler(p, c)
        elif est_pile_vide(p):
            return False
        elif c == ")":
            depiler(p)
    return est_pile_vide(p)

# 3. 16 = 2**4 combinaisons possibles, donc
# pour une expression de taille n il y a 2**n.

# le code suivant : compte de 0 à 15 (16 possibilité) en base 2
# autrement dit on liste toutes les chaînes de caractères
# de taille n = 4 constituées uniquement de deux symboles
# n = 4
# for i in range(2**n):
#     print(int2strbin(i, n))

def expression(x, n):
    """ int, int -> str """
    binaire = int2strbin(x, n)
    # on remplace dans la chaîne binaire tous
    # les 0 par des ( et les 1 par des )
    chaine = ""
    for b in binaire:
        if b == "0":
            chaine += "("
        else:
            chaine += ")"
    return chaine

# On affiche toutes les expressions de taille 4
# avec des parenthèses ouvrantes et fermantes
# n = 4
# for i in range(2**n):
#     print(expression(i, n))

def liste_bien_parenthesee(n):
    """ int -> [str] """
    l = []
    for i in range(2**n):
        expr = expression(i, n)
        if est_bien_parenthesee(expr):
            l.append(expr)
    return l
#   # Avec une liste en compréhension
#     return [ expression(i, n) for i in range(2**n)
#              if est_bien_parenthesee(expression(i, n))] 

# Exercice 5

def tri_pile(A):
    B = creer_pile_vide()
    C = creer_pile_vide()
    while not est_pile_vide(A):
        if est_pile_vide(B):
            empiler(B, depiler(A))
        sA, sB = sommet(A), sommet(B)
        if sA < sB:
            empiler(B, depiler(A))
            while not est_pile_vide(C):
                empiler(B, depiler(C))
        else:
            empiler(C, depiler(B))
    # attention, cela vide la pile A
    return B
            
# Exercice 4

# 1.a. 5 6 / 4 + 3 * 2 +
# 1.b -13

e = "3 4 - 12 1 + *"

def decoupe(e):
    """ str -> File[str | int] """
    f = creer_file_vide()
    element_en_lecture = ''
    for c in e:
        if c in {'+', '-', '/', '*'}:
            enfiler(f, c)
            element_en_lecture = ''
        elif c == " " and not element_en_lecture == '':
            enfiler(f, int(element_en_lecture))
            element_en_lecture = ''
        else:
            element_en_lecture += c
    return f

# {'+', '-', '/', '*'} est un ensemble
# '1' in {'+', '-', '/', '*'}
# opération "in" en temps constant en la taille de l'ensemble

# ['+', '-', '/', '*'] est une liste
# '1' in ['+', '-', '/', '*']
# opération "in" en temps proportionnel en la taille de la liste

def evalue(f):
    """ File -> int """
    p = creer_pile_vide()
    while not est_file_vide(f):
        c = defiler(f)
        if c in {'+', '-', '/', '*'}:
            if not est_pile_vide(p):
                a = depiler(p)
            else:
                return None
            if not est_pile_vide(p):
                b = depiler(p)
            else:
                return None
            if c == '+':
                empiler(p, a + b)
            elif c == '*':
                empiler(p, a * b)
            elif c == '-':
                empiler(p, b - a)
            elif c == '/':
                empiler(p, b / a)
        else:
            empiler(p, c)
    if est_pile_vide(p):
        return None
    reponse = depiler(p)
    if not est_pile_vide(p):
        return None
    return reponse

def calculatrice_npi(chaine):
    f = decoupe(chaine)
    return evalue(f)
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















