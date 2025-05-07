'''Bonjour et bienvenue sur EcoInvasion !
Tout d'abord le but du jeux est de récupérer les pieuvres
rose et laisser les oiseaux aller à la mer.
utilisez les flèches pour vous déplacer
Pour chaque oiseaux ramasser vous perdez 3 de score
Pour chaque extraterrestre détruit vous gagnez 1 !
à partir de 10 de score si vous laissez passer 
un oiseau dans la mer vous gagnez 1 et au contraire
si vous laissez passer une extraterrestre vous perdez 4.
( Si vous redescendez en dessous de 10 de score
ce mode se désactive ). 
La vitesse augmente de 20% tout les 10 de score.
BOSS : Tout les 15 de score il y'a 2 fois plus de monstres
 Pour une expérience plus immersive veuillez vous munir d'écouteurs.'''


import pyxel
from random import *
pyxel.init(128, 128, title="Nuit du c0de 2022")
obstacles_liste= []
perso_x = 0
perso_y = 50
pyxel.load("1.pyxres")
score=0
a=0
b=30



#==============================================================#
###########################initialisation######################
#==============================================================#

def update():
    global obstacles_liste,perso_x,perso_y,score,b
    obstacles_generation(obstacles_liste)
    obstacles_mouvement(obstacles_liste)
    obstacles_supression(obstacles_liste)
    perso_x, perso_y = perso_deplacement(perso_x, perso_y)
    if score==15:
        b=5
    
    
def draw():
    global score, perso_x, perso_y
    if score >= 0:
        pyxel.blt(0,0,0,0,64,128,128)
        ### dessins des obstacles ###
        for obstacle in obstacles_liste:
            # oiseau
            if obstacle[2] == 1:
                pyxel.blt(obstacle[0],obstacle[1],0,16,16,-8,8,0)
            # extraterrestre
            if obstacle[2] ==2:
                pyxel.blt(obstacle[0],obstacle[1],0,24,24,-8,8,2)
        
        pyxel.blt(perso_x, perso_y, 0,24,0,8,17,6)
        pyxel.text(1,1,'score : '+ str(score), 0)
    else:
        global a
        pyxel.cls(0)
        pyxel.stop(0)
        pyxel.stop(1)
        pyxel.text(50,64, 'GAME OVER', 7)
        pyxel.text(25,80, 'RESTART (press Y/N)', 7)
        
        if a ==0:
            pyxel.play(2,9,0, loop=False)
            a=1
        if pyxel.btn(pyxel.KEY_Y):
            perso_x = 5
            perso_y = 50
            score = 0
            pyxel.play(1,1,0,loop=True)
            
        if pyxel.btn(pyxel.KEY_N):
            pyxel.quit()
        

    

#==============================================================#
########################### FONCTIONS ##########################
#===============================================================
pyxel.play(1,1,0,loop=True)
'''creation des obstacles'''
def obstacles_generation(obstacles_liste):
        ###création d'obstacles###
        #pour que les obstacles soit généré toutes les secondes) 
        bon_ou_mauvais= randint(0,1)
        
        if (pyxel.frame_count % b ==0):
            coord=randint(0,120)
            oui_non = True
           
            if bon_ou_mauvais ==0:
                for element in obstacles_liste:
                    if element[1]-8< coord < element[1]+8:
                        oui_non = False
                        
                if oui_non ==True :
                    obstacles_liste.append([128,coord,1])
                   
            else:
                for element in obstacles_liste:
                    if element[1]-8< coord < element[1]+8:
                        oui_non = False
                if oui_non== True:
                    obstacles_liste.append([128,coord,2])
    
            

''' mouvement des obstacles '''
def obstacles_mouvement(obstacles_liste):
    for i in range(len(obstacles_liste)-1):
        obstacles_liste[i][0] -= 1

''' disparition des obstacles si ils sortent du cadre'''
def obstacles_supression(obstacles_liste):
    global score
    for obstacle in obstacles_liste:
        if obstacle[0] < 0 :
            if score >= 10: 
                if obstacle[2] == 2:
                    score= score - 4                    
                if obstacle[2] == 1:
                    score= score + 1
                    pyxel.play(0,4,0, loop=False)
                    

            obstacles_liste.remove(obstacle)
        if perso_x-8< obstacle[0]< perso_x+8 and perso_y-8< obstacle[1]< perso_y+16 :
            
            if obstacle[2] == 1:
                score= score - 3
                pyxel.play(0,4,0, loop=False)
            if obstacle[2] == 2:
                score= score + 1
                pyxel.play(0,3,0, loop=False)
            obstacles_liste.remove(obstacle)

'''mouvement du personnage'''
def perso_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x=x+3
     
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :         
            x=x-3

    if (x>=30):
        x=x-3
    if pyxel.btn(pyxel.KEY_DOWN):
        if(y < 120) :
            y=y+3

    if pyxel.btn(pyxel.KEY_UP):
         if(y > 0 ):
            y=y-3
    
    return x, y


    
  
#==============================================================#
########################### EXECUTION ##########################
#==============================================================#
pyxel.run(update, draw)
