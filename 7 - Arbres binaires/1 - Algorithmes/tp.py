from ds import Arbre, creer_vide, est_vide, gauche, droit, etiquette

a0 = Arbre(5, None, None)
a1 = Arbre(-2, None, None)
a2 = Arbre(1, a0, a1)
a3 = Arbre(1,
    Arbre(4,
        None,
        Arbre(3, None, None)),
    Arbre(5,
        Arbre(2,
            Arbre(12, None, None),
            Arbre(9, None, None)),
        Arbre(8,
            Arbre(12, None, None),
    None)))
a4 = Arbre(9,
           Arbre(7, None, None),
           None)
a5 = Arbre(8,
           None,
           Arbre(5, None, None))
a6 = Arbre(1,
           Arbre(2, None, None),
           Arbre(3, None, None))
a7 = Arbre(12,
           a6,
           Arbre(4,
                 a4,
                 a5))

def est_feuille(a):
    """ Arbre -> bool
    Détermine si a est constitué d'un seul élément """
    return est_vide(gauche(a)) and est_vide(droit(a))

def taille(a):
    """ Arbre -> int
    Renvoie le nombre de nœuds de a """
    if est_vide(a):
        return 0
    else:
        return 1 + taille(gauche(a)) + taille(droit(a))

def somme(a):
    """ Arbre -> int
    Renvoie la somme des éléments de l'arbre a """
    if est_vide(a):
        return 0
    else:
        return somme(gauche(a)) + somme(droit(a)) + etiquette(a) 
        

def nb_niveaux(a):
    """ Arbre -> int
    Renvoie le nombre de niveaux de l'arbre """
    if est_vide(a):
        return 0
    else:
        return 1 + max(nb_niveaux(gauche(a)), nb_niveaux(droit(a)))
        
def affiche_infixe(a):
    """ Arbre -> Nonetype
    Affiche l'arbre a de manière infixe """
    if est_vide(a):
        pass
    else:
        #print("(", end = '')
        affiche_infixe(gauche(a))
        affiche_infixe(droit(a))
        print(etiquette(a), end = ' ')
        #print(")", end='')

def rechercher(a, e):
    """ Arbre, int -> bool
    Renvoie True ssi e est une des étiquettes de a """
    if est_vide(a):
        return False
    else:
        if etiquette(a) == e:
            return True
        else:
            return rechercher(gauche(a), e) or rechercher(droit(a), e)

def maximum(a):
    """ Arbre -> int
    Renvoie la plus grande étiquette de a """
    if est_feuille(a):
        return etiquette(a)
    elif est_vide(gauche(a)):
        return max(etiquette(a), maximum(droit(a)))
    elif est_vide(droit(a)):
        return max(etiquette(a), maximum(gauche(a)))
    else:
        m1 = maximum(gauche(a))
        m2 = maximum(droit(a))
        return max(m1, m2, etiquette(a))
        
    # à retenir : quand on doit écrire une fonction
    # dont le cas de base est est_feuille(a) il faut nécessairement
    # rajouter les cas
    # - est_vide(gauche(a)):
    # - est_vide(droit(a)):

# À finir pour lundi : affiche_infixe, rechercher, maximum

def est_egal(a1, a2):
    """ Arbre, Arbre -> bool
    Détermine si les arbres a1 et a2 sont identiques """
    if est_vide(a1) and est_vide(a2):
        return True
    # cas de base inutile 
    elif est_vide(a1) ^ est_vide(a2):
        # ^ : XOR
        return False
    else:
        sag_egaux = est_egal(gauche(a1), gauche(a2))
        sad_egaux = est_egal(droit(a1), droit(a2))
        return etiquette(a1) == etiquette(a2) and sag_egaux and sad_egaux

def est_egalf(a1, a2):
    """ Arbre, Arbre -> bool
    Renvoie True si et seulement si les arbres a1 et a2 sont faiblement égaux """
    pass

def contenu(a, d):
    """ Arbre, dict -> None
    Ajoute à d le contenu de a """
    if est_vide(a):
        return None
    else:
        if etiquette(a) in d:
            d[etiquette(a)] += 1
        else:
            d[etiquette(a)] = 1
        contenu(gauche(a), d)
        contenu(droit(a), d)
        return None
       

def est_dico_inclu(d1, d2):
    """ dict, dict -> bool
    Toutes les clés de d1 sont présentes dans d2 et
    sont associées à la même valeur.
    d1 est 'inclus' dans d2 """
    for k in d1:
        if k not in d2 or d1[k] != d2[k]:
            return False
    return True

def est_dico_egal(d1, d2):
    return est_dico_inclu(d1, d2) and est_dico_inclu(d2, d1)

def est_egalc(a1, a2):
    d1 = dict()
    contenu(a1, d1)
    d2 = dict()
    contenu(a2, d2)
    return est_dico_egal(d1, d2)
    













def est_egalc(a1, a2):
    """ Arbre, Arbre -> bool
    Renvoie True ssi les arbres a1 et a2 ont le même contenu """
    pass
