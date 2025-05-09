import pyxel
from random import randint

#Bienvenue dans BLOB STORY...

#Dans ce jeu, vous et votre adversaire incarnerez des BLOBs, créatures magiques de la forêt verte. Quel est l'objectif de ce jeu, nous direz-vous ? 
# #Manger la plus grande quantité de pommes afin de devenir le roi des BLOBs, le plus gros... 
# #Pour vous déplacer dans cet univers, 2 possibilités s'offrent à vous : déplacez-vous avec les touches flèches du clavier pour le BLOB bleu, ou avec les touches Z, Q, S et D pour le BLOB jaune.
#Attention, vous augmentez de taille après avoir mangé 4 pommes ! Cela vous ralentira cependant un peu, dans le but de laisser une chance à votre adversaire d'attraper les pommes suivantes également ! 
# #Vous pouvez augmenter de taille 3 fois au cours du jeu. Le premier joueur ayant mangé 16 pommes gagne donc la partie.
#Bon appétit et bonne Chance !
#Developped by Mouton Corp

#JOUEUR

class Joueur1():
    def __init__(self):
        self.x = 95
        self.y = 112
        self.p = 0
        self.u = 0
        self.c = 9
        self.w = 8
        self.h = 8
        self.vitesse = 3

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT,1,1) and self.x<112:
            self.x+=self.vitesse
        
        if pyxel.btnp(pyxel.KEY_LEFT,1,1) and self.x>8:
            self.x-=self.vitesse

        if pyxel.btnp(pyxel.KEY_UP,1,1) and self.y>8:
            self.y-=self.vitesse
        
        if pyxel.btnp(pyxel.KEY_DOWN,1,1) and self.y<112:
            self.y+=self.vitesse
    
    
    def draw(self):
        pyxel.blt(self.x, self.y,0,self.u,0, self.w,8, 0)
            

class Joueur2():
    def __init__(self):
        self.x = 30
        self.y = 112
        self.p = 0
        self.u = 0
        self.w = 8
        self.h = 8
        self.vitesse = 3

    def update(self):
        if pyxel.btnp(pyxel.KEY_D,1,1) and self.x<112:
            self.x+=self.vitesse
        if pyxel.btnp(pyxel.KEY_Q,1,1) and self.x>8:
            self.x-=self.vitesse
        if pyxel.btnp(pyxel.KEY_Z,1,1) and self.y>8:
            self.y-=self.vitesse
        if pyxel.btnp(pyxel.KEY_S,1,1) and self.y<112:
            self.y+=self.vitesse
    
    
    def draw(self):
        pyxel.blt(self.x, self.y,0,self.u,8, self.w, 8, 0)


#POMMMES
class Pomme():
    def __init__(self):
        self.x = 8
        self.y = 8

    def update(self):
        pass
    
    def draw(self):
        pyxel.blt(self.x, self.y,1,0,0, 8, 8, 0)


#FIN
class Fin():
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):

        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128)
        pyxel.text(40,15,"BLOB  STORY",12)
        pyxel.text(50,31,"BRAVO !",10)
        pyxel.text(30,45,"Le joueur avec 16 ",6)
        pyxel.text(37,55,"points gagne !",6)
        pyxel.text(15,80,"DEVELOPPED BY MOUTON CORP",6)


#MENU
class Menu:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.j1=Joueur1()
        self.j2=Joueur2()
        self.accueil = False

    def update(self):
        if self.accueil==False:
            self.x = (self.x + 1) % pyxel.width
            self.j1.update()
            self.j2.update()
        else:
            pass

    def draw(self):
        if self.accueil==False:
            pyxel.cls(0)
            pyxel.bltm(0,0,0,0,0,128,128)
            pyxel.text(40,15,"BLOB  STORY",12)
            pyxel.text(33,23,"Le premier a 16",12)
            if pyxel.frame_count%5 == 0:
                pyxel.text(30,31,">> PRESS SPACE <<",10)
            else:
                pyxel.text(30,31,">< PRESS SPACE ><",10)
            pyxel.text(20,79,"Player 2 : Z / Q / S / D",12)
            pyxel.text(5,70,"Player 1 : UP/DOWN/RIGHT/LEFT",12)
        else:
            pass


#APP
class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        pyxel.load("theme.pyxres")
        self.x = 0
        self.scorej1=0
        self.scorej2=0
        self.j1=Joueur1()
        self.j2=Joueur2()
        self.pom=Pomme()
        self.menu=Menu()
        self.fin=Fin()
        pyxel.run(self.update, self.draw)
    
    def collision(self): 
            #COLLISION AVEC LA POMME
        if abs(self.j1.x-self.pom.x)<self.j1.w-2 and abs(self.j1.y-self.pom.y)<self.j1.h-2:
            return 1
        if abs(self.j2.x-self.pom.x)<self.j2.w-2 and abs(self.j2.y-self.pom.y)<self.j2.h-2:
            return 0
            


    def update(self):
            #SI LE SCORE EST EGAL A 16 ALORS AFFICHE MENU DE FIN
        if self.scorej1 != 16 and self.scorej2 !=16:
            self.j1.update()
            self.j2.update()
            self.pom.update()
            self.menu.update()

            if pyxel.btnp(pyxel.KEY_SPACE,1,1):
                self.menu.accueil=True
                self.j1.u=16
                self.j2.u=16


                #RECUPERATION ET DEPLACEMENT DES POMMES
            if self.collision()==1:
                self.scorej1+=1
                self.pom.x,self.pom.y=randint(8,112),randint(8,112)
            if self.collision()==0:
                self.scorej2+=1
                self.pom.x,self.pom.y=randint(8,112),randint(8,112)

                #SCORE ET GROSSISSEMENT DES BLOB
            if self.scorej1==4:
                self.j1.u=8
                self.j1.vitesse=2
            if self.scorej1==8:
                self.j1.u=0
                self.j1.vitesse=1
            if self.scorej1==12:
                self.j1.u=32
                self.j1.w=16

            if self.scorej2==4:
                self.j2.u=8
                self.j2.vitesse=2
            if self.scorej2==8:
                self.j2.u=0
                self.j2.vitesse=1
            if self.scorej2==12:
                self.j2.u=32
                self.j2.w=16
            
            else:
                self.fin.update()
            

    def draw(self):
        if self.scorej1 != 16 and self.scorej2 !=16:
            pyxel.cls(0)
            pyxel.bltm(0,0,1,0,0,128,128)
            pyxel.text(2,2,str(self.scorej2),10)
            pyxel.text(120,2,str(self.scorej1),5)
            self.pom.draw()
            self.menu.draw()
            self.j1.draw()
            self.j2.draw()
        else:
            self.fin.draw()
            pyxel.text(2,2,str(self.scorej2),10)
            pyxel.text(120,2,str(self.scorej1),5)
        
        

App()