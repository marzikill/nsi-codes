# Nuit du c0de 2023

import pyxel, random

pyxel.init(128, 128, title = "NDC 2023")
pyxel.load("2.pyxres")

niv = 0
victory, defeat, = False, False
player, ennemis_liste = 108, []
FRAME_REFRESH = random.randint(60,120)
FRAME_REFRESH_1 = 1
nb_ennemi, elim = 0, 0
tirs_liste = []

def reinitialiser():
     global niv, victory, defeat, player, ennemis_liste, tirs_liste, FRAME_REFRESH, FRAME_REFRESH_1, elim
     niv, victory, defeat = 0, False, False
     player, ennemis_liste, tirs_liste, elim = 108, [], [], 0
     FRAME_REFRESH, FRAME_REFRESH_1 = random.randint(60, 120), 1

def deplacement_joueur(player):
    if pyxel.btn(pyxel.KEY_UP):
        if player > 15:
            player -= 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if player < 108:
            player += 1
    return player
    
def ennemis_apparition(ennemis_liste):
    global nb_ennemi, victory
    if pyxel.frame_count % FRAME_REFRESH == 0:
        if nb_ennemi < 30:
            ennemis_liste.append([120,random.randint(20,108),2])
            nb_ennemi += 1
        if elim == 30:
            victory = True
    return ennemis_liste
    
def ennemis_deplacement(ennemis_liste):
    global defeat, elim
    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if tir[0]+3 >= ennemi[0] and tir[1] >= ennemi[1] and tir[1] <= ennemi[1]+8:
                ennemi[2] -= 1
                if ennemi[2] == 0:
                    ennemis_liste.remove(ennemi)#enlever ennemi de tableau
                    elim += 1
                tirs_liste.remove(tir)
        if pyxel.frame_count % FRAME_REFRESH_1 == 0:
            ennemi[0] -= 1
        if ennemi[0] == 20:
            defeat = True
    return ennemis_liste

def tirs_creation(tirs_liste):
    #Quand un tire apparait --> tir ajouté au tableau tirs_liste
    tirs_liste.append([14, player + 4])
    return tirs_liste

def tirs_deplacement(tirs_liste):
    for tir in tirs_liste:
        tir[0] += 1
        if tir[0] > 80:
            tirs_liste.remove(tir)
        #supprimer tir du tableau quand il quitte l'écran
    return tirs_liste
#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________
def update():
    global niv, player, ennemis_liste, tirs_liste
    if niv == 0:
        if pyxel.btnr(pyxel.KEY_RETURN):
            niv = 1
    elif victory == True or defeat == True:
        if pyxel.btnr(pyxel.KEY_RETURN):
            reinitialiser()
            
    if niv == 1:
        player = deplacement_joueur(player)
        ennemis_liste = ennemis_apparition(ennemis_liste)
        ennemis_liste = ennemis_deplacement(ennemis_liste)
        
        if pyxel.btnr(pyxel.KEY_SPACE):
            #Le tir est créé et ajouté au tableau
            tirs_liste = tirs_creation(tirs_liste)
            
        tirs_liste = tirs_deplacement(tirs_liste)
#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________
def draw():
    if niv == 0:
        pyxel.cls(9)
        pyxel.text(44, 28, "Welcome to", 7)
        pyxel.text(59, 46, "CLOMB", 7)
        pyxel.blt(47, 44, 0, 24, 24, 8, 8, 2)
        pyxel.rect(2, 60, 124, 1, 7)
        pyxel.text(48, 70, "Enter to", 7)
        pyxel.blt(56, 85, 0, 25, 32, 15, 8)
    elif niv == 1:
        pyxel.cls(1)

        #pyxel.rect(0,10,128,118,9)#zone joueur
        #pyxel.rect(0,10,20,118,15)#zone attaquants
        
        pyxel.blt(19, 14, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 24, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 34, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 44, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 54, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 64, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 74, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 84, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 94, 0, 9, 60, 1, 16, 0)
        pyxel.blt(19, 104, 0, 9, 60, 1, 16, 0)
        
        pyxel.blt(6, player, 0, 32, 16, 7, 8, 2)
        #pyxel.rect(6,player,8,8,13)
        
        pyxel.blt(2, 0, 0, 9, 60, 12, 16, 0)
        pyxel.blt(14, 0, 0, 12, 60, 12, 16, 0)
        pyxel.blt(26, 0, 0, 12, 60, 12, 16, 0)
        pyxel.blt(38, 0, 0, 12, 60, 12, 16, 0)
        pyxel.blt(50, 0, 0, 12, 60, 12, 16, 0)
        pyxel.blt(62, 0, 0, 12, 60, 12, 16, 0)
        pyxel.blt(74, 0, 0, 12, 60, 12, 16, 0)
        pyxel.blt(86, 0, 0, 9, 60, -12, 16, 0)
        pyxel.text(7,2,f"REMAINING ENNEMIES: {30-elim}",7)
        for ennemi in ennemis_liste:
            if ennemi[2] > 0:
                pyxel.blt(ennemi[0],ennemi[1], 0, 72, 16, -9, 8, 2)
            if ennemi[2] > 0:
                pyxel.blt(ennemi[0]-2,ennemi[1]-7, 0, 73, 57, 6, 6, 2) # vie 1
                if ennemi[2] > 1:
                    pyxel.blt(ennemi[0]+5,ennemi[1]-7, 0, 73, 57, 6, 6, 2) # vie 2

        for tir in tirs_liste:
            if tir[0] < 125:
                pyxel.rect(tir[0], tir[1], 3, 1, 10)
                
        pyxel.blt(0, 116, 0, 3, 9, 12, 16)
        pyxel.blt(12, 116, 0, 3, 9, 12, 16)
        pyxel.blt(24, 116, 0, 3, 9, 12, 16)
        pyxel.blt(36, 116, 0, 3, 9, 12, 16)
        pyxel.blt(48, 116, 0, 3, 9, 12, 16)
        pyxel.blt(50, 116, 0, 3, 9, 12, 16)
        pyxel.blt(62, 116, 0, 3, 9, 12, 16)
        pyxel.blt(74, 116, 0, 3, 9, 12, 16)
        pyxel.blt(86, 116, 0, 3, 9, 12, 16)
        pyxel.blt(98, 116, 0, 3, 9, 12, 16)
        pyxel.blt(110, 116, 0, 3, 9, 12, 16)
        pyxel.blt(122, 116, 0, 3, 9, 12, 16)
        
    if victory == True:
        pyxel.cls(11)
        pyxel.text(53, 43, "You won!", 7)
        pyxel.blt(41, 42, 0, 72, 8, 8, 8, 2)
        pyxel.text(32, 56, "Congrats! You've ", 7)
        pyxel.text(32, 63, "saved the village.", 7)
    elif defeat == True:
        pyxel.cls(2)
        pyxel.text(53, 43, "You lost!", 7)
        pyxel.blt(41, 43, 0, 64, 9, 8, 7)
        pyxel.text(32, 56, "BRUH! The village", 7)
        pyxel.text(32, 63, "has been destroyed.", 7)

pyxel.run(update, draw)