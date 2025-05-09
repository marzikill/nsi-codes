# Nuit du c0de 2023

import pyxel, random
pyxel.init(128, 128, title='NDC 2023')
pyxel.load('theme.pyxres')

#Variables Globales
time = 0
r_time = 0
x1 = 64
y1 = 86
d1 = 'droite'
saut1 = 0
x2 = 43
y2 = 86
saut2 = 0
d2 = 'gauche'
score1 = 0
score2 = 0
d_envi='droite'
t_envi=random.randint(150, 750)
Jeu=0
liste_ennemis = []
liste_ennemis_droite=[]
tir_liste1 = [[0,1]]
tir_liste_droite1 = [[0,1]]
tir_liste2 = [[0,1]]
tir_liste_droite2 = [[0,1]]
tir1=0
tir2=0
vie1=3
vie2=3

#Liste des fonctions
#Joueur1
def J1_mouvement(x, y, d, saut):
    if pyxel.btn(pyxel.KEY_D):
        if x<124:
            d = 'droite'
            x = x + 1
    if pyxel.btn(pyxel.KEY_Q):
        if x>1:
            d = 'gauche'
            x = x - 1
    if pyxel.btn(pyxel.KEY_Z):
        if saut == 0:
            y = y - 20
            saut = saut + 1
    return x, y, d, saut

#Joueur2
def J2_mouvement(x, y, d, saut):
    if pyxel.btn(pyxel.KEY_LEFT):
        if x>1:
            d = 'gauche'
            x = x - 1
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x<124:
            d = 'droite'
            x = x + 1
    if pyxel.btn(pyxel.KEY_UP):
        if saut == 0:
            y = y - 20
            saut = saut + 1
    return x, y, d, saut

#Tir
def creation_tir(tir_liste, x, y, d, tir_liste_droite, tir):
    if pyxel.btn(pyxel.KEY_F) and tir==0:
        if d=='droite':
            tir_liste_droite.append([x+8,y+4])
            tir+=1
        else:
            tir_liste.append([x,y+4])
            tir+=1
    return tir_liste, x, y, d, tir_liste_droite, tir

def creation_tir2(tir_liste, x, y, d, tir_liste_droite, tir):
    if pyxel.btn(pyxel.KEY_DOWN) and tir==0:
        if d=='droite':
            tir_liste_droite.append([x+8,y+4])
            tir+=1
        else:
            tir_liste.append([x,y+4])
            tir+=1
    return tir_liste, x, y, d, tir_liste_droite, tir

def supression_tir(tir_liste, tir_liste_droite):
    for tirs in tir_liste :
        tirs[0]-=1
        if tirs[0]>128:
            tir_liste.remove(tirs)
    for tirs2 in tir_liste_droite:
        tirs2[0]+=1
        if tirs2[0]<1:
            tir_liste_droite.remove(tirs2)
    return tir_liste, tir_liste_droite

#Ennemis
def creation_ennemi(liste_ennemis):
    if pyxel.frame_count%30 ==0 :
        ennemi_apparition = random.randint(0,2)
        if ennemi_apparition == 0:
            liste_ennemis.append([38,50])
    return liste_ennemis

def ennemi_supresion(liste_ennemis):
    for enemi in liste_ennemis:
        if enemi[0]>128:
            liste_ennemis.remove(enemi)
    return liste_ennemis

def creation_ennemi_droite(liste_ennemis_droite):
    if pyxel.frame_count%30 ==0 :
        ennemi_apparitiond = random.randint(0,2)
        if ennemi_apparitiond == 0:
            liste_ennemis_droite.append([88,50])
    return liste_ennemis_droite

def ennemi_supresion_droite(liste_ennemis_droite):
    for enemid in liste_ennemis_droite:
        if enemid[0]<5:
            liste_ennemis_droite.remove(enemid)
    return liste_ennemis_droite
    
#Collisions
def collision(tir_liste, tir_liste_droite, liste_ennemis, liste_ennemis_droite, score):
    for tir in tir_liste :
        for ennemi in liste_ennemis:
            if tir[0]> ennemi[0] and tir[0]< ennemi[0]+8 and tir[1]> ennemi[1] and tir[1]<ennemi[1]+8:
                tir_liste.remove(tir)
                liste_ennemis.remove(ennemi)
                score+=5
    for tir8 in tir_liste_droite :
        for ennemi8 in liste_ennemis_droite:
            if tir8[0]> ennemi8[0] and tir8[0]< ennemi8[0]+8 and tir8[1]> ennemi8[1] and tir8[1]<ennemi8[1]+8:
                tir_liste_droite.remove(tir8)
                liste_ennemis_droite.remove(ennemi8)
                score+=5
    return tir_liste, tir_liste_droite, liste_ennemis, liste_ennemis_droite, score

def collision2(liste_ennemis ,liste_ennemis_droite, x, y, vie):
    for ennemi4 in liste_ennemis :
        if ennemi4[0]>x and ennemi4[0]< x+8 and ennemi4[1]>y and ennemi4[1] < y+8 :
            liste_ennemis.remove(ennemi4)
            vie-=1
    for ennemi5 in liste_ennemis_droite :
        if ennemi5[0]>x and ennemi5[0]< x+8 and ennemi5[1]>y and ennemi5[1] < y+8 :
            liste_ennemis_droite.remove(ennemi5)
            vie-=1
    return liste_ennemis, liste_ennemis_droite, x, y, vie

#Général
def environnement(x, d_envi, y):
    if y==88:
        if d_envi=='droite':
            x+=0.5
        else:
            x-=0.5
    return x, d_envi, y
    
def chrono(time, r_time, score1, score2, d_envi, t_envi, tir1, tir2):
    time+=1
    t_envi-=1
    if tir1!=0:
        tir1+=1
    if tir2!=0:
        tir2+=1
    if time%30==0:
        r_time+=1
        time=0
        score1 +=1
        score2 +=1
    if t_envi==0:
        if d_envi=='droite':
            d_envi='gauche'
        else:
            d_envi='droite'
        t_envi=random.randint(150,750)
    if tir1>=30:
        tir1=0
    if tir2>=30:
        tir2=0
    return time, r_time, score1, score2, d_envi, t_envi, tir1, tir2

def gravite(y, x):
    if y<88:
        y+=2
    if y>=8 and x<20 :
        y+=2
    if y>=88 and x>108:
        y+=2
    if x>20 and y>=89 and x<108:
        y+=2
    return y, x
    
def cooldown(saut, tir):
    if saut!=0:
        saut += 1 
    if saut %30 == 0:
        saut = 0
    if tir!=0:
        tir+=1
    if tir%30==0:
        tir=0
    return saut, tir

def perdre(Jeu, y1, y2, vie1, vie2):
    if y1>=115 or y2>=115:
        Jeu=1
    if vie1==0:
        Jeu=1
    if vie2==0:
        Jeu=1
    return Jeu, y1, y2, vie1, vie2
    
def restart(time, r_time, y1, x1, saut1, d1, x2, y2, saut2, d2, score1, score2, d_envi, t_envi, Jeu, liste_ennemis, liste_ennemis_droite, tir_liste1, tir_liste2, tir_liste_droite1, tir_liste_droite2, tir1, tir2, vie1, vie2):
    if pyxel.btnr(pyxel.KEY_SPACE):
        time = 0
        r_time = 0
        x1 = 64
        y1 = 86
        d1 = 'droite'
        saut1 = 0
        x2 = 43
        y2 = 86
        saut2 = 0
        d2 = 'gauche'
        score1 = 0
        score2 = 0
        d_envi='droite'
        t_envi=random.randint(150, 750)
        Jeu=0
        liste_ennemis = []
        liste_ennemis_droite=[]
        tir_liste1 = [[0,1]]
        tir_liste_droite1 = [[0,1]]
        tir_liste2 = [[0,1]]
        tir_liste_droite2 = [[0,1]]
        tir1=0
        tir2=0
        vie1=3
        vie2=3
    return time, r_time, y1, x1, saut1, d1, x2, y2, saut2, d2, score1, score2, d_envi, t_envi, Jeu, liste_ennemis, liste_ennemis_droite, tir_liste1, tir_liste2, tir_liste_droite1, tir_liste_droite2, tir1, tir2, vie1, vie2

#Update
def update():
    
    global time, r_time, y1, x1, saut1, d1, x2, y2, saut2, d2, score1, score2, d_envi, t_envi, Jeu, liste_ennemis, liste_ennemis_droite, tir_liste1, tir_liste2, tir_liste_droite1, tir_liste_droite2, tir1, tir2, vie1, vie2
    
    if Jeu==0:
        #Générale
        time, r_time, score1, score2, d_envi, t_envi, tir1, tir2 = chrono(time, r_time, score1, score2, d_envi, t_envi, tir1, tir2)
        Jeu, y1, y2, vie1, vie2 = perdre(Jeu, y1, y2, vie1, vie2)
        
        #Joueur1
        y1, x1 = gravite(y1, x1)
        x1, y1, d1, saut1 = J1_mouvement(x1, y1, d1, saut1)
        saut1, tir1 = cooldown(saut1, tir1)
        x1, d_envi, y1 = environnement(x1, d_envi, y1)
        tir_liste1, x1, y1, d1, tir_liste_droite1, tir1 = creation_tir(tir_liste1, x1, y1, d1, tir_liste_droite1, tir1)
        tir_liste1, tir_liste_droite1 = supression_tir(tir_liste1, tir_liste_droite1)
        tir_liste1, tir_liste_droite1, liste_ennemis, liste_ennemis_droite, score1 = collision(tir_liste1, tir_liste_droite1, liste_ennemis, liste_ennemis_droite, score1)
        liste_ennemis ,liste_ennemis_droite ,x1, y1, vie1 =collision2(liste_ennemis ,liste_ennemis_droite   , x1, y1, vie1)
        
        #Joueur2
        y2, x2 = gravite(y2, x2)
        x2, y2, d2, saut2 = J2_mouvement(x2, y2, d2, saut2)
        saut2, tir2 = cooldown(saut2, tir2)
        x2, d_envi, y2 = environnement(x2, d_envi, y2)
        tir_liste2, x2, y2, d2, tir_liste_droite2, tir2 = creation_tir2(tir_liste2, x2, y2, d2, tir_liste_droite2, tir2)
        tir_liste2, tir_liste_droite2 = supression_tir(tir_liste2, tir_liste_droite2)
        tir_liste2, tir_liste_droite2, liste_ennemis, liste_ennemis_droite, score2 = collision(tir_liste2, tir_liste_droite2, liste_ennemis, liste_ennemis_droite, score2)
        liste_ennemis ,liste_ennemis_droite ,x2, y2, vie2 =collision2(liste_ennemis ,liste_ennemis_droite   , x2, y2, vie2 )
        
        #Ennemis
        liste_ennemis = creation_ennemi(liste_ennemis)
        liste_ennemis = ennemi_supresion(liste_ennemis)
        liste_ennemis_droite = creation_ennemi_droite(liste_ennemis_droite)
        liste_ennemis_droite = ennemi_supresion_droite(liste_ennemis_droite)
        for ennemis in liste_ennemis:
            ennemis[1], ennemis[0] = gravite(ennemis[1], ennemis[0])
            ennemis[0], d_envi, ennemis[1] = environnement(ennemis[0], d_envi, ennemis[1])
        for ennemis2 in liste_ennemis_droite:
            ennemis2[1], ennemis2[0] = gravite(ennemis2[1], ennemis2[0])
            ennemis2[0], d_envi, ennemis2[1] = environnement(ennemis2[0], d_envi, ennemis2[1])

    if Jeu==1:
        time, r_time, y1, x1, saut1, d1, x2, y2, saut2, d2, score1, score2, d_envi, t_envi, Jeu, liste_ennemis, liste_ennemis_droite, tir_liste1, tir_liste2, tir_liste_droite1, tir_liste_droite2, tir1, tir2, vie1, vie2 = restart(time, r_time, y1, x1, saut1, d1, x2, y2, saut2, d2, score1, score2, d_envi, t_envi, Jeu, liste_ennemis, liste_ennemis_droite, tir_liste1, tir_liste2, tir_liste_droite1, tir_liste_droite2, tir1, tir2, vie1, vie2)

#Draw
def draw():
    
    pyxel.cls(0)
    
    if Jeu==1:
        pyxel.bltm(0, 0, 1, 0, 0, 128, 128)
        if y1>=115 or vie1==0:
            pyxel.text(45, 30, 'Player 2 win', 10)
        if y2>=115 or vie2==0:
            pyxel.text(45, 30, 'Player 1 win', 10)
        pyxel.text(10, 64, 'Score P1 : '+str(score2), 7)
        pyxel.text(70, 64, 'Score P2 : '+str(score1), 7)
        pyxel.rect(64, 63, 2, 7, 8)
    
    if Jeu==0:
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        
        #Générale
        pyxel.rect(2, 2, 49, 8, 5)
        pyxel.text(3, 3, 'Temps : '+str(r_time), 7)
    
        #Joueur1
        if d1=='droite':
            pyxel.blt(x1, y1, 0, 0, 16, 8, 8, 10)
        else:
            pyxel.blt(x1, y1, 0, 8, 16, 8, 8, 10)
        
        for tir1 in tir_liste1 :
            pyxel.rect(tir1[0],tir1[1],4,1,10)
        for tir2 in tir_liste_droite1 :
            pyxel.rect(tir2[0],tir2[1],4,1,10)
        pyxel.rect(9, 29, 30, 7, 9)
        pyxel.text(10, 30, 'Vie : '+str(vie2), 7)
        
        #Joueur2
        if d2=='droite':
            pyxel.blt(x2, y2, 0, 0, 24, 8, 8, 10)
        else:
            pyxel.blt(x2, y2, 0, 8, 24, 8, 8, 10)
        
        for tir3 in tir_liste2 :
            pyxel.rect(tir3[0],tir3[1],4,1,10)
        for tir4 in tir_liste_droite2 :
            pyxel.rect(tir4[0],tir4[1],4,1,10)
        pyxel.rect(89, 29, 30, 7, 9)
        pyxel.text(90, 30, 'Vie : '+str(vie1), 7)
        
        #Ennemis
        for ennemi in liste_ennemis:
            pyxel.blt(ennemi[0],ennemi[1], 0, 0, 32, 8, 8, 10)
        for ennemi_droite in liste_ennemis_droite:
            pyxel.blt(ennemi_droite[0],ennemi_droite[1], 0, 8, 32, 8, 8, 10)

pyxel.run(update, draw)