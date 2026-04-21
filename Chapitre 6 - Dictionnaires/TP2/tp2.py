likes = {'Bob': 102,
         'Ada': 201,
         'Charline': 103,
         'Daniel': 201}

def nb_likes(likes, nom):
    """ {str:int}, str -> int
    Renvoie le nombre de likes de nom """
    for k in likes:
        if k == nom:
            return likes[nom]
    return 0

def nb_likes(likes, nom):
    """ {str:int}, str -> int
    Renvoie le nombre de likes de nom """
    if nom in likes:
        return likes[nom]
    else:
        return 0

def ajoute_likes(likes, nom, l):
    """ {str: int}, str, int -> None
    Ajoute l au nombre de likes de nom """
    if nom in likes:
        likes[nom] = likes[nom] + l
    else:
        likes[nom] = l
        
def top_likes(likes):
    """ {str: int} -> str
    Renvoie le nom d'une personne possédant le plus de likes """
    nom = ''
    maxi = 0
    # À compléter : algorithme du maximum
    # cf cours sur les listes
    for prenom in likes:
        if likes[prenom] > maxi:
            maxi = likes[prenom]
            nom = prenom
    return nom
    
def top_likes_mieux(likes):
    """ {str: int} -> [str]
    Renvoie la liste des personnes possédant le plus de likes """
    noms = []
    maxi = 0
    for prenom in likes:
        if likes[prenom] > maxi:
            maxi = likes[prenom]
            noms = [prenom]
        elif likes[prenom] == maxi:
            noms.append(prenom)
    return noms


votes = ["Ali", "Bob", "Mél", "Ali", "Ali", "Mél"]

def compte_voix(votes):
    """ [str] -> {str: int}
    Renvoie le decompte des voix des votes """
    decompte = {}
    for nom in votes:
        if nom not in decompte:
            decompte[nom] = 1
        else:
            decompte[nom] = decompte[nom] + 1
    return decompte
    
    
def pourcentage(decompte, nom):
    """ {str: int}, str -> float
    Renvoie le pourcentage de votes obtenu par nom dans décompte """
    # À compléter
    
def resultat_second_tour(decompte):
    """ {str: int} -> str
    Renvoie le nom de la personne ayant obtenu le plus de votes """
    decompte[''] = 0
    meilleur = ''
    # À compléter
    
def deux_meilleurs(decompte):
    """ {str: int} -> {str: str}
    Renvoie un dictionnaire correspondant aux deux vote  majoritaires """
    decompte[''] = 0
    podium = {'1er': '', '2nd': ''}
    # À compléter
    
def resultat_premier_tour(decompte):
    """ {str: int} -> [str]
    Renvoie la ou les personnes gagnantes au premier tour """
