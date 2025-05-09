'''
Bienvenue dans notre documentation de notre jeu TokyoFight
le but du jeu est de survivre le plus longtemps dans tokyo la nuit,l'environnement est peuplé d'enemmis des ninjas ainsi que des rats
on va pouvoir se deplacer avec les touches Q à gauche et D à droite ou les fleches du claviers
on pourra sauter avec espace
on pourra sortir une épée afin de pouvoir tué les enemmis avec E
le but est d'avoir le score le plus haut vous avez 3 vies bonne chance
'''

import pyxel
import random
pyxel.init(128,128,title="Nuit du c0de 2022")
pyxel.load("tokyores.pyxres")
perx=90
pery=90
xanc=0
soly=100
energie=0
sens="d"
elist=[]
frappe=False
score=0
vies=3

               

def mouvement(x,y):
    global energie,sens
    if pyxel.btn(pyxel.KEY_RIGHT)or pyxel.btn(pyxel.KEY_D) :
        if (x < 120) :
            x+= 3
            sens="d"
    if pyxel.btn(pyxel.KEY_LEFT)or pyxel.btn(pyxel.KEY_Q):
        if (x > 0) :
            x -= 3
            sens="g"
    if pyxel.btn(pyxel.KEY_SPACE):
        if (y == soly) :
            energie=9
    return x,y
def creer_enemie():
    global elist,score
    d= 40 -score//50
    if (pyxel.frame_count% d == 0)and(random.randint(0,1)==1):
        typeen=random.randint(0,1)
        if typeen==0:
            elist.append([128,100,0])
        else:
            elist.append([0,101,1])
def mouv_enemie():
    global elist
    for en in elist:
        if en[2]==1:
            en[0]+=1+(score//1200)
        else:
            en[0]-=1+(score//1500)
def frapper():
    global frappe,coups
    if pyxel.btn(pyxel.KEY_E):
        frappe=True
        for en in elist:
            if sens=="d":
                if (en[1] in [i for i in range(pery,pery+8)]) and (en[0]in [i for i in range(perx,perx+16)]):
                        elist.remove(en)
                           
            else:
                if (en[1] in [i for i in range(pery,pery+8)]) and (perx in [i for i in range(en[0],en[0]+16)]):
                      elist.remove(en)
    else:
        frappe=False
def collision():
    global elist,vies
    for en in elist:
        if (en[1] in [i for i in range(pery,pery+8)]) and ((en[0]in [i for i in range(perx,perx+8)])or(perx in [i for i in range(en[0],en[0]+8)])):
            elist.remove(en)
            vies-=1
def gravite():
    global energie,perx,pery
    if pery<soly or energie>0:
        if energie<0:
            if pery-energie//2>soly:
                pery=soly
                energie=0
        pery-=energie//2
        if energie>-5:
            energie-=1
def update():
    global perx,pery,xanc,score
    score+=1
    gravite()
    collision()
    creer_enemie()
    mouv_enemie()
    frapper()
    xanc=perx
    perx,pery= mouvement(perx,pery)
def draw():
    global perx, pery,sens,frappe
    pyxel.cls(0)

    if vies>0:    
        pyxel.blt(0,108,1,0,0,128,20)
        pyxel.blt(0,0,1,0,20,128,108)
        pyxel.text(45,0,"Score: "+str(score),7)
        for i in range(vies):
            pyxel.blt(i*8+i,120,0,0,32,8,8,0)
        if sens == "d":
            if not(frappe):
                if pery<100:
                    if energie>0:
                        pyxel.blt(perx,pery,0,16,0,8,8,0)
                    else:
                        pyxel.blt(perx,pery,0,16,8,8,8,0)
            if frappe:
                pyxel.blt(perx,pery,0,33,0,13,8,0)
            elif pery==100:
                if xanc!=perx:
                    pyxel.blt(perx,pery,0,8,0,8,8,0)
                else:
                    pyxel.blt(perx,pery,0,0,0,8,8,0)
        
        if sens=="g":
            if not(frappe):
                if pery<100:
                    if energie>0:
                        pyxel.blt(perx,pery,0,24,0,8,8,0)
                    else:
                        pyxel.blt(perx,pery,0,24,8,8,8,0)
            if frappe:
                pyxel.blt(perx-6,pery,0,33,8,13,8,0)
            elif pery==100:
                if xanc!=perx:
                    pyxel.blt(perx,pery,0,8,8,8,8,0)
                else:
                    pyxel.blt(perx,pery,0,0,8,8,8,0)
        for en in elist:
            if en[2]==0:
                pyxel.blt(en[0],en[1],0,0,24,8,8,0)
            else:
                pyxel.blt(en[0],en[1],0,16,17,11,9,0)
    else:
        pyxel.text(50,60,"GAME OVER",8)
pyxel.run(update,draw)
