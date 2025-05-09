#MODULES
import pyxel, random

#INITIALISATION
pyxel.init(128, 128, title="NSD 2023")

#POSITION JOUEUR
poisson_x = 60
poisson_y = 60

#ARRIERE PLAN
bulle1_x = 50
bulle1_y = 50

fond1_x = 0
fond1_y = 112

pyxel.load('images.pyxres')
#EXPERIENCE
exp = 0
#COMPTEUR
compteur = 0
#LISTE ENNEMIS
ennemis_liste = []

#LISTE EXPLOSIONS
explosions_liste = []  

#DEPLACEMENTS JOUEUR
def poisson_deplacement(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120) :
            y = y + 2
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0) :
            y = y - 2
    if pyxel.btn(pyxel.KEY_A):
        pyxel.quit()
    return x, y

#ENNEMIS
def ennemis_creation(ennemis_liste):
    if (pyxel.frame_count % 10 == 0):
        ennemis_liste.append([0,random.randint(0, 120)])
    return ennemis_liste

#DEPLEMENT DES ENNEMIS VERS LA DROITE
def ennemis_deplacement(ennemis_liste):
    for ennemi in ennemis_liste:
        ennemi[0] += 2
        if  ennemi[0]>128:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


def poisson_suppression(exp):
    for ennemi in ennemis_liste:
        if compteur <= 60:
            if ennemi[0] <= poisson_x+8 and ennemi[1] <= poisson_y+8 and ennemi[0]+8 >= poisson_x and ennemi[1]+8 >= poisson_y:
                ennemis_liste.remove(ennemi)
                exp += 1
            # on ajoute l'explosion
                explosions_creation(poisson_x, poisson_y)
    return exp

#EXPLOSION
def explosions_creation(x, y):
    explosions_liste.append([x, y, 0])

#EXPLOSION
def explosions_animation():
    for explosion in explosions_liste:
        explosion[2] +=1
        if explosion[2] == 12:
            explosions_liste.remove(explosion)  
            
def temps(compteur):
    if pyxel.frame_count % 30 == 0:
        compteur += 1
    return compteur
    
def update():
    global poisson_x, poisson_y, ennemis_liste, exp, explosions_liste

    #POSITION POISSONS
    poisson_x, poisson_y = poisson_deplacement(poisson_x, poisson_y)

    #ENNEMIS
    ennemis_liste = ennemis_creation(ennemis_liste)

    #POSITION ENNEMIS
    ennemis_liste = ennemis_deplacement(ennemis_liste)

    # suppression du poisson et ennemi si contact
    exp = poisson_suppression(exp)

    # evolution de l'animation des explosions
    explosions_animation()   
    
    global compteur
    compteur = temps(compteur)
    
        
def draw():
    pyxel.cls(1)
    #pyxel.blt(bulle1_x, bulle1_y, 0, 9, 117, 1, 1)
    pyxel.blt(fond1_x, fond1_y, 0, 0, 168, 64, 64)
    pyxel.blt(fond1_x+64, fond1_y, 0, 0, 168, 64, 64)
    
    if compteur < 60:        
        pyxel.text(5,5, 'POINTS:'+ str(exp), 7)
        pyxel.text(90,5, 'TEMPS:'+ str(compteur) + 's', 7)

        if exp < 20:
            pyxel.blt(poisson_x, poisson_y, 0, 2, 69, 6, 3)
        elif  20 <= exp < 40:
            pyxel.blt(poisson_x, poisson_y, 0, 0, 74, 6, 6)
        elif  40 <= exp < 60:
            pyxel.blt(poisson_x, poisson_y, 0, 8, 74, 12, 6)
        elif  60 <= exp < 80:
            pyxel.blt(poisson_x, poisson_y, 0, 40, 64, 16, 16)
        elif  exp >= 80:
            pyxel.blt(poisson_x, poisson_y, 0, 56, 97, 32, 14)   
        
        
        for ennemi in ennemis_liste:
            if exp < 20:
                pyxel.blt(ennemi[0], ennemi[1], 0, 0, 71, 2, 1)
            elif  20 <= exp < 40:
                pyxel.blt(ennemi[0], ennemi[1], 0, 8, 69, 6, 3)
            elif  40 <= exp < 60:
                pyxel.blt(ennemi[0], ennemi[1], 0, 0, 90, 6, 6)
            elif  60 <= exp < 80:
                pyxel.blt(ennemi[0], ennemi[1], 0, 8, 82, 12, 6)
            elif  exp >= 80:
                pyxel.blt(ennemi[0], ennemi[1], 0, 24, 64, 16, 16)
            
        for explosion in explosions_liste:
            pyxel.circb(explosion[0]+4, explosion[1]+4, 2*(explosion[2]//4), 8+explosion[2]%3)            

    # sinon: GAME OVER
    if compteur >= 60:
        pyxel.text(20,40,'LA PARTIE EST TERMINEE !', 7)
        pyxel.text(20,60,'VOUS AVEZ FAIT ' + str(exp) + ' POINTS !', 7)
        
        
        '''pyxel.text(20,80,'APPUYEZ SUR ESPACE POUR RELANCER', 7)
    if pyxel.btn(pyxel.KEY_SPACE):
        pyxel.restart()'''
        

pyxel.run(update, draw)