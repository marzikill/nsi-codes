from ds import creer_vide, est_vide, est_feuille, gauche, droit, etiquette, Arbre

a = Arbre("Kamel",
          Arbre("Kamel",
                Arbre("Joris", None, None),
                Arbre("Kamel", None, None)),
          Arbre("Carine",
                Arbre("Carine", None, None),
                Arbre("Abdou", None, None)))

def nb_joueurs(a):
    if est_feuille(a):
        return 1
    # ça marche UNIQUEMENT parce que les arbres sont parfaits
    # sinon il faudrait écrire :
    # elif est_vide(gauche(a)):
    # ...
    # elif est_vide(droit(a)):
    # ...
    return nb_joueurs(gauche(a)) + nb_joueurs(droit(a))


def nb_rounds(a):
    """ Arbre -> int
    Renvoie le nombre de rounds de la compétition a """
    if est_vide(a):
        return 0
    if est_feuille(a):
        return 0
    else:
        # ça marche UNIQUEMENT parce que les arbres sont parfaits
        # return nb_round(gauche(a)) + 1
        return max(nb_rounds(gauche(a)),nb_rounds(droit(a))) + 1

def occurrences(a, nom):
    """ Arbre, str -> int
    Renvoie le nombre d'occurrences de nom dans a """
    if est_vide(a):
        return 0
    else:
        if etiquette(a) == nom:
            return 1 + occurrences(gauche(a),nom) + occurrences(droit(a),nom)
        else:
            return  occurrences(gauche(a),nom) + occurrences(droit(a),nom)
        # return (etiquette(a) == nom) + occurrences(gauche(a),nom) + occurrences(droit(a),nom)

def nombre_matchs(a, nom):
    """ Arbre, str -> int
    Renvoie le nombre de matchs joués par le joueur nom dans la compétition d'arbre a """
    if etiquette(a) == nom:
        return occurrences(a, nom) - 1
    else:
        return occurrences(a, nom)

def liste_joueurs(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant participé à la compétition d'arbre a """
    if est_vide(a):
        return None
    elif est_feuille(a):
        return [etiquette(a)]
    else:
        return liste_joueurs(gauche(a)) + liste_joueurs(droit(a))
    
    
def niveau(a, i):
    """ Arbre, int -> [str]
    Renvoie la liste des étiquettes des nœuds de profondeur i de l'arbre a """
    if est_vide(a):
        return []
    elif i == 0:
        return [etiquette(a)]
    else:
        return niveau(gauche(a), i - 1) + niveau(droit(a), i - 1)

def vaincus_gagnant(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant joué un match contre le gagnant de la compétition d'arbre a """
    if est_feuille(a):
        return []
    # ça marche UNIQUEMENT parce que les arbres sont parfaits
    # sinon il faudrait écrire :
    # elif est_vide(gauche(a)):
    # ...
    # elif est_vide(droit(a)):
    # ...
    else:
        if etiquette(a) == etiquette(gauche(a)):
            return vaincus_gagnant(gauche(a)) + [etiquette(droit(a))] 
        else:
            return [etiquette(gauche(a))] + vaincus_gagnant(droit(a))
        
# Attention : l.pop(0) : réalise autant d'opération que
# la taille de la liste !
# l.pop() : temps constant (une seule opération)
# -> dû à l'implémentation du type list en python
# donc : pas terrible pour une file (on rappelle qu'on avait
# implémenté defiler en temps constant !).

def parcours_largeur(a):
    """ Arbre -> [str]
    Renvoie la liste des étiquettes des nœuds de l'arbre a, telle qu'obtenue à l'aide d'un parcours en largeur """
    file = [a]
    liste = []
    while not file == []:
        A = file.pop(0)
        # Traitement
        liste.append(etiquette(A))
        if not est_vide(gauche(A)): 
            file.append(gauche(A))
        if not est_vide(droit(A)):
            file.append(droit(A))
    return liste
        

def recherche_noeud(a, nom):
    """ Arbre, str -> Arbre
    Renvoie le sous-arbre de a dont la racine a pour étiquette nom et est de profondeur minimale dans a """
    pass

def joueurs_vaincus(a, nom):
    """ Arbre, str -> [str]
    Renvoie la liste des joueurs vaincus par nom dans la compétition d'arbre a """
    pass

# À finir pour vendredi !