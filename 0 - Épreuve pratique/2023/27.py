def separe(tab):
    gauche = 0
    droite = len(tab)-1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche +=1
        else :
            tab[gauche], tab[droite] = tab[droite],tab[gauche]
            droite -= 1
    return tab



def recherche_min(tab):
    min = tab[0]
    for elm in tab:
        if elm < min:
            min = elm
    return min
