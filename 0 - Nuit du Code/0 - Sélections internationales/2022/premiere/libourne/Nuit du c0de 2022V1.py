#Bienvenue dans Poulpy Wars, le but du jeu est de tuer 
#des monstres marins à l'aide d'un poulpe rose (tout mignon) 
#qui peut se déplacer et se tourner sur les côtés,
#vers le haut et le bas ainsi que sur ses diagonales.
#Des salves d'oursins agressifs arrivent à chaque nouveau 
#niveau. Ils peuvent arriver de tout les côtés. 
#Attention! Si un enemis vous touche , vous mourrez.
#Les enemis rebondissent sur les murs pour repartir
#à l'attaque.A chaque salve de monstres marins détruite, 
#Un nouveau niveau débute, plus dur jusqu'au bosse final.
#La touche E sert a quitter le jeu, la touche R sert à
#recommencer lorsque que l'on a perdu, la touche D pour
#tourner de 45 degrès dans le sens des aiguilles d'une montre,
#et Q pour le sens inverse. Enfin, les flèches servent à se déplacer.

#Bisous !
import pyxel
from random import * 
pyxel.init(128,128, title="Nuit du cOde 2022", fps=60)
pyxel.load("graphisme.pyxel.pyxres")
X_perso = 10
Y_perso = 100
Orientation_degres = 0
liste_tirs = []
Niveau = 0
liste_mechantsH = []
liste_mechantsG = []
nb_mechants = 5
Niv = 0
nb_vie = 1
liste_boss = []
                                                            #Fonction Du jeu
def bouger_personnage():
    global X_perso, Y_perso, Orientation_degres
    if pyxel.btn(pyxel.KEY_LEFT) and X_perso > 0:
        X_perso -= 1
        Orientation_degres = 270
    elif pyxel.btn(pyxel.KEY_RIGHT) and X_perso < 120:
        X_perso += 1
        Orientation_degres = 90
    elif pyxel.btn(pyxel.KEY_UP) and Y_perso > 0:
        Y_perso -= 1
        Orientation_degres = 0
    elif pyxel.btn(pyxel.KEY_DOWN) and Y_perso < 120:
        Y_perso += 1
        Orientation_degres = 180
    if pyxel.btnr(pyxel.KEY_D):
        if Orientation_degres == 360:
            Orientation_degres = 0
        else:
            Orientation_degres += 45
    if pyxel.btnr(pyxel.KEY_Q):
        if Orientation_degres == 0:
            Orientation_degres = 360
        else:
            Orientation_degres -= 45
            
            
def tirer_perso():
    global liste_tirs
    if pyxel.btnr(pyxel.KEY_SPACE):
        if Orientation_degres > 0 and Orientation_degres <= 45:
            liste_tirs.append([X_perso, Y_perso, [1,-1]])
        elif Orientation_degres >= 45 and Orientation_degres <= 90:
            liste_tirs.append([X_perso, Y_perso, [1,0]])
        elif Orientation_degres >= 90 and Orientation_degres <= 135:
            liste_tirs.append([X_perso, Y_perso, [1,1]])
        elif Orientation_degres >= 135 and Orientation_degres <= 180:
            liste_tirs.append([X_perso, Y_perso, [0,1]])
        elif Orientation_degres >= 180 and Orientation_degres <= 225:
            liste_tirs.append([X_perso, Y_perso, [-1,1]])
        elif Orientation_degres >= 225 and Orientation_degres <= 270:
            liste_tirs.append([X_perso, Y_perso, [-1,0]])
        elif Orientation_degres >= 270 and Orientation_degres <= 315:
            liste_tirs.append([X_perso, Y_perso, [-1,-1]])
        elif Orientation_degres >= 315 and Orientation_degres <= 360:
            liste_tirs.append([X_perso, Y_perso, [0,-1]])
        elif Orientation_degres == 0:
            liste_tirs.append([X_perso, Y_perso, [0,-1]])

            
def surprimer_tirs_perso():
    for tirs in liste_tirs:
        if tirs[0] >= 128 or tirs[0] < 0:
            liste_tirs.remove(tirs)
        elif tirs[1] >= 128 or tirs[1] < 0:
            liste_tirs.remove(tirs)

def creer_mechantsH():
    global nb_mechants
    niv0()
    niv1()
    niv2()
    niv3plus()
    boss()
    
    
    
    
def niv0():
    global nb_mechants
    if Niveau == 0:
        for i in range(nb_mechants):
            liste_mechantsH.append([randint(0,120),0 , 1])
        nb_mechants += 1
def niv1():
    global nb_mechants
    if Niveau == 1:
        for i in range(nb_mechants):
            liste_mechantsH.append([randint(0,120),0, 1])
        creer_mechantsB()
        nb_mechants -= 1
def niv2():
    global nb_mechants
    if Niveau == 2:
        for i in range(nb_mechants):
            liste_mechantsH.append([randint(0,120),0, 1])
        creer_mechantsB()
        creer_mechantsG()
        nb_mechants += 1
def niv3plus():
    global nb_mechants
    if Niveau >= 3 and Niveau < 10 or Niveau > 10:
        for i in range(nb_mechants):
            liste_mechantsH.append([randint(0,120),0, 1])
        creer_mechantsB()
        creer_mechantsG()
        creer_mechantsD()
        nb_mechants += 1
def boss():
    global nb_mechants
    if Niveau == 10 or Niveau > 11 and Niveau % 2 == 0:
        liste_boss.append([randint(0,88),0, 1 , 1, 100])
    
def nivREST():
    global nb_mechants
    if Niveau > 10:
        for i in range(nb_mechants):
            liste_mechantsH.append([randint(0,120),0, 1])
        creer_mechantsB()
        creer_mechantsG()
        creer_mechantsD()
        liste_boss.append([randint(0,88),0, 1 , 1, 100])
            

        
def creer_mechantsB():
    global nb_mechants
    for i in range(nb_mechants):
        liste_mechantsH.append([randint(0,120),120, -1])
        
def creer_mechantsG():
    global nb_mechants
    for i in range(nb_mechants):
        liste_mechantsG.append([0,randint(0,120), 1])
def creer_mechantsD():
    global nb_mechants
    for i in range(nb_mechants):
        liste_mechantsG.append([120,randint(0,120), -1])
def colision_perso_mechant():
    global nb_vie
    for mechant in liste_mechantsH:
        if mechant[0] <= X_perso+3 <= mechant[0]+8 and mechant[1] <= Y_perso+3 <= mechant[1]+8:
            liste_mechantsH.remove(mechant)
            nb_vie -= 1
    for mechant in liste_mechantsG:
        if mechant[0] <= X_perso+3 <= mechant[0]+8 and mechant[1] <= Y_perso+3 <= mechant[1]+8:
            liste_mechantsG.remove(mechant)
            nb_vie -= 1
    for mechant in liste_boss:
        if mechant[0] <= X_perso+3 <= mechant[0]+40 and mechant[1] <= Y_perso+3 <= mechant[1]+16:
            liste_boss.remove(mechant)
            nb_vie -= 1
    
    
def tuer_mechants():
    for tirs in liste_tirs:
        for mechant in liste_mechantsH:
            if mechant[0] <= tirs[0]+2  <= mechant[0]+8 and mechant[1] <= tirs[1] <= mechant[1]+8:
                liste_mechantsH.remove(mechant)
                liste_tirs.remove(tirs)
                break
    for tirs in liste_tirs:
        for mechant in liste_mechantsG:
            if mechant[0] <= tirs[0]+2 <= mechant[0]+8 and mechant[1] <= tirs[1] <= mechant[1]+8:
                liste_mechantsG.remove(mechant)
                liste_tirs.remove(tirs)
                break
    for mechant in liste_boss:
        for tirs in liste_tirs:
            if mechant[0] <= tirs[0]+2 <= mechant[0]+40 and mechant[1] <= tirs[1] <= mechant[1]+16:
                if mechant[4] == 0:
                    liste_boss.remove(mechant)
                    liste_tirs.remove(tirs)
                    
                    break
                else:
                    liste_tirs.remove(tirs)
                    mechant[4] -= 2
            
                                                            #Fonction Update
def update():
    global X_perso , Y_perso, Niv, Niveau , nb_vie
    if pyxel.btnr(pyxel.KEY_E):
        pyxel.quit()
    bouger_personnage()
    print(nb_vie)
    tirer_perso()
    for tirs in liste_tirs:
        tirs[0] += tirs[2][0]
        tirs[1] += tirs[2][1]
    surprimer_tirs_perso()
    creer_mechantsH()
    if len(liste_mechantsH ) != 0:
        Niveau = -1
    elif len(liste_mechantsG) != 0:
        Niveau = -1
    elif len(liste_boss) != 0:
        Niveau = -1
    else:
        Niv += 1
        Niveau = Niv
    for mechant in liste_mechantsH:
        value = randint(0,4)
        if value == 3:
            mechant[1] += 1 * mechant[2]
        if mechant[1] >= 120:
            mechant[2] = -1
        elif mechant[1] <=0:
            mechant[2] = 1
    for mechant in liste_mechantsG:
        value = randint(0,4)
        if value == 3:
            mechant[0] += 1 * mechant[2]
        if mechant[0] >= 120:
            mechant[2] = -1
        elif mechant[0] <=0:
            mechant[2] = 1
    for boss in liste_boss:
        boss[0] += 0.5 * boss[2]
        if boss[0] >= 88:
            boss[2] = -1
        elif boss[0] <=0:
            boss[2] = 1
        boss[1] += 0.5 * boss[3]
        if boss[1] >= 112:
            boss[3] = -1
        elif boss[1] <=0:
            boss[3] = 1
        
    colision_perso_mechant()
    tuer_mechants()
    

            
            
        

                                #Fonction Draw
def draw():
    global X_perso, Y_perso , nb_vie , X_perso , Y_perso , liste_mechantsH , liste_tirs , Niv , Niveau , liste_mechantsG
    pyxel.cls(0)
    if Orientation_degres > 0 and Orientation_degres <= 45:
        pyxel.blt(X_perso, Y_perso, 0, 16, 16, 8, 8 ,0)
    elif Orientation_degres >= 45 and Orientation_degres <= 90:
        pyxel.blt(X_perso, Y_perso, 0, 8, 16, 8, 8 ,0)
    elif Orientation_degres >= 90 and Orientation_degres <= 135:
        pyxel.blt(X_perso, Y_perso, 0, 16, 0, -8, 8 ,0)
    elif Orientation_degres >= 135 and Orientation_degres <= 180:
        pyxel.blt(X_perso, Y_perso, 0, 8, 0, 8, 8 ,0)
    elif Orientation_degres >= 180 and Orientation_degres <= 225:
        pyxel.blt(X_perso, Y_perso, 0, 16, 0, 8, 8 ,0)
    elif Orientation_degres >= 225 and Orientation_degres <= 270:
        pyxel.blt(X_perso, Y_perso, 0, 8, 8, 8, 8 ,0)
    elif Orientation_degres >= 270 and Orientation_degres <= 315:
        pyxel.blt(X_perso, Y_perso, 0, 16, 16, -8, 8 ,0)
    elif Orientation_degres >= 315 and Orientation_degres <= 360:
        pyxel.blt(X_perso, Y_perso, 0, 8, 24, 8, 8 ,0)
    elif Orientation_degres == 0:
        pyxel.blt(X_perso, Y_perso, 0, 8, 24, 8, 8 ,0)
        
    for tirs in liste_tirs:
        pyxel.blt(tirs[0]  + 3, tirs[1]+3, 0, 0, 8, 8, 8 ,0)
    pyxel.text(10,10, str(Niv), 10)
    for mechant in liste_mechantsH:
        pyxel.blt(mechant[0], mechant[1], 0 , 0, 16, 8, 8, 0)
        
    for mechant in liste_mechantsG:
        pyxel.blt(mechant[0], mechant[1], 0 , 0, 16, 8, 8, 0)
    for boss in liste_boss:
        pyxel.blt(boss[0], boss[1], 0 , 0, 104, 40, 16, 0)
    if nb_vie <= 0:
        pyxel.cls(0)
        pyxel.text(30, 64 , "Press R to restart", 2)
        if pyxel.btnr(pyxel.KEY_R):
            nb_vie += 1
            liste_mechantsH = []
            liste_mechantsG = []
            liste_tirs = []
            X_perso = 64
            Y_perso = 64
            Niv = 0
            Niveau = 0
    for boss in liste_boss:
        pyxel.text(60, 64 , str(boss[4]), 4)
    

pyxel.run(update, draw)