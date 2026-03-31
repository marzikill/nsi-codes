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
    
    return None

def top_likes(likes):
    """ {str: int} -> str
    Renvoie le nom d'une personne possédant le plus de likes """
    nom = ''
    maxi = 0
    # À compléter : algorithme du maximum
    # cf cours sur les listes
    
def top_likes_mieux(likes):
    """ {str: int} -> [str]
    Renvoie la liste des personnes possédant le plus de likes """
    noms = []
    maxi = 0
    # À compléter
