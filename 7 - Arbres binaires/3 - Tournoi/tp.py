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
    pass

def liste_joueurs(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant participé à la compétition d'arbre a """
    # if est_vide(a):
    #     return ....................................
    # elif est_feuille(a):
    #     return [..................................]
    # else:
    #     return ....................................

def niveau(a, i):
    """ Arbre, int -> [str]
    Renvoie la liste des étiquettes des nœuds de profondeur i de l'arbre a """
    pass

def vaincus_gagnant(a):
    """ Arbre -> [str]
    Renvoie la liste des joueurs ayant joué un match contre le gagnant de la compétition d'arbre a """
    pass

def parcours_largeur(a):
    """ Arbre -> [str]
    Renvoie la liste des étiquettes des nœuds de l'arbre a, telle qu'obtenue à l'aide d'un parcours en largeur """
    pass

def recherche_noeud(a, nom):
    """ Arbre, str -> Arbre
    Renvoie le sous-arbre de a dont la racine a pour étiquette nom et est de profondeur minimale dans a """
    pass

def joueurs_vaincus(a, nom):
    """ Arbre, str -> [str]
    Renvoie la liste des joueurs vaincus par nom dans la compétition d'arbre a """
    pass

