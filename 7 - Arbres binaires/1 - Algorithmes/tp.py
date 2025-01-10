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
            Arbre(7, None, None),
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
    pass

def rechercher(a, e):
    """ Arbre, int -> bool
    Renvoie True ssi e est une des étiquettes de a """
    pass

def maximum(a):
    """ Arbre -> int
    Renvoie la plus grande étiquette de a """
    pass

# À finir pour lundi : affiche_infixe, rechercher, maximum

def est_egal(a1, a2):
    """ Arbre, Arbre -> bool
    Détermine si les arbres a1 et a2 sont identiques """
    pass

def est_egalf(a1, a2):
    """ Arbre, Arbre -> bool
    Renvoie True si et seulement si les arbres a1 et a2 sont faiblement égaux """
    pass

def contenu(a, d):
    """ Arbre, dict -> Nonetype
    Ajoute à d le contenu de a """
    pass

def est_dico_egal(d1, d2):
    """ dict, dict -> bool
    Détermine si les dictionnaires d1 et d2 sont égaux """
    pass

def est_egalc(a1, a2):
    """ Arbre, Arbre -> bool
    Renvoie True ssi les arbres a1 et a2 ont le même contenu """
    pass

