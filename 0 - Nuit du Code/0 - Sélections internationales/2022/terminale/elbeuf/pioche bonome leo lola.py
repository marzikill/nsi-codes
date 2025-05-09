"""Notre jeu s'appelle pioche-bonome le but est de trouver la pièce derrière la
terre en minant en appuyant sur A, le personnage s'appelle tohnya et peut dire
hi en appuyant sur h et un coeur en appuyant sur L, il peut utiliser un jet pack
en restant appuyé sur espace. Lola Baffrey,Léo Carboni"""

import pyxel,random
class Jeu:
    def __init__(self):
        pyxel.init(128,128, title= "Nuit du c0de 2022")
        self.tohnya_x = 60
        self.tohnya_y = 28
        pyxel.load("bonome.pyxres")
        self.decor = [(0,0),(8,0),(0,8)]
        self.appui_miner = False
        self.aleatoire = (random.randint(0,128),random.randint(40,112))
        self.hauteur = self.tohnya_y
        self.cass =  []
        self.peut_bouger= [(i,j) for i in range(129) for j in range(29)]
        self.case_gagnante = [(self.aleatoire[0]+i-8,self.aleatoire[1]+j-8) for i in range(16)for j in range(16)]
        pyxel.playm(0,1,True)
        print(self.case_gagnante)
        print(self.aleatoire)
        self.gagner = False
        self.texte =""
        self.timer= 0
        pyxel.run(self.update, self.draw)
        
        
        
    def deplacement(self):
        if pyxel.btnp(pyxel.KEY_LEFT) and self.tohnya_x > 0 and (self.tohnya_x-8,self.tohnya_y) in self.peut_bouger:
 
            self.tohnya_x -= 8
        if pyxel.btnp(pyxel.KEY_RIGHT) and self.tohnya_x < 128 and (self.tohnya_x+8,self.tohnya_y) in self.peut_bouger:
            self.tohnya_x += 8
    def miner(self):
        if pyxel.btn(pyxel.KEY_A) and self.tohnya_y < 112:

            self.appui_miner = True
        else:
            self.appui_miner = False
    def sauter(self):
        if pyxel.btn(pyxel.KEY_SPACE) and self.tohnya_y > 0 and (self.tohnya_x,self.tohnya_y-8) in self.peut_bouger:
            self.tohnya_y -= 8
        else:
            if self.hauteur > self.tohnya_y :
                self.tohnya_y += 2
            if (self.tohnya_x,self.tohnya_y+8) in self.cass :
                self.tohnya_y += 8
    def casser(self):
        if pyxel.btnp(pyxel.KEY_A) and self.tohnya_y < 112:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.cass.append((self.tohnya_x+8,self.tohnya_y))
                self.peut_bouger.append((self.tohnya_x+8,self.tohnya_y))
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.cass.append((self.tohnya_x-8,self.tohnya_y))
                self.peut_bouger.append((self.tohnya_x-8,self.tohnya_y))
            else :
                self.cass.append((self.tohnya_x,self.tohnya_y+8))
                self.peut_bouger.append((self.tohnya_x,self.tohnya_y+8))
    def changer_gagner(self):
        if (self.tohnya_x,self.tohnya_y) in self.case_gagnante:
            self.gagner = True
    
    def texte_change(self):
        if (pyxel.frame_count % 60 == 0):
            self.texte = "fleches pour deplacer"
        if (pyxel.frame_count % 120 == 0):
            self.texte = "espace pour utiliser le jet pack"
        if (pyxel.frame_count % 180 == 0) :
            self.texte = "A pour miner et H et L surprise"

        
            
        
                
                
    def update(self):
        self.deplacement()
        self.miner()
        self.sauter()
        self.casser()
        self.changer_gagner()
        self.texte_change()
    def draw(self):
        pyxel.cls(0)
        #personnage
        if self.gagner == False:
            #minerai
            pyxel.blt(self.aleatoire[0],self.aleatoire[1],0,16,8,8,8,2)
            #decor
            for i in range(19):
                for h in range(8):
                    pyxel.blt(i*8,h*8,0,8,0,8,8)
        
            #nuage
            if (pyxel.frame_count % 10 == 0):   
                for i in range(4):
                        pyxel.blt(random.randint(0,128),random.randint(0,28),0,0,8,8,8)
            
            for i in range(19):
                pyxel.blt(i*8,36,0,8,8,8,8)
            #terre
            for i in range(19):
                for h in range(1,15):
                    pyxel.blt(i*8,36+h*8,0,8,32,8,8)
            pyxel.blt(4*8,5*8,0,8,16,8,8)
            pyxel.blt(5*8,12*8,0,8,16,8,8)
            pyxel.blt(7*8,5*8,0,8,16,8,8)
            pyxel.blt(8*8,8*8,0,8,16,8,8)
            pyxel.blt(9*8,6*8,0,8,16,8,8)
            pyxel.blt(14*8,10*8,0,8,16,8,8)
            pyxel.blt(1*8,8*8,0,8,16,8,8)
        
            #bloc cassés
            for bloc in self.cass:
                    pyxel.blt(bloc[0], bloc[1], 0, 0,24 , 8, 8)
            
        
            #animation bonome      
            if self.appui_miner :
                if (pyxel.frame_count % 15 == 0):
                    pyxel.play(0,9)
                    if pyxel.btn(pyxel.KEY_RIGHT):
                        pyxel.blt(self.tohnya_x,self.tohnya_y,0,24,32,8,8,7)
                    elif pyxel.btn(pyxel.KEY_LEFT):
                        pyxel.blt(self.tohnya_x,self.tohnya_y,0,24,32,-8,8,7)
                else:
                    if pyxel.btn(pyxel.KEY_LEFT):
                        pyxel.blt(self.tohnya_x,self.tohnya_y,0,24,24,-8,8,7)
                    else :    
                        pyxel.blt(self.tohnya_x,self.tohnya_y,0,24,24,8,8,7)
            else :
                #bonome
                if pyxel.btn(pyxel.KEY_RIGHT):
                    pyxel.blt(self.tohnya_x,self.tohnya_y,0,16,24,8,8,7)
                if pyxel.btn(pyxel.KEY_LEFT):
                    pyxel.blt(self.tohnya_x,self.tohnya_y,0,16,24,-8,8,7)
                else:
                    pyxel.blt(self.tohnya_x,self.tohnya_y,0,16,24,8,8,7)
            pyxel.text(0,0,self.texte,3)
            if pyxel.btn(pyxel.KEY_H) :
                pyxel.blt(self.tohnya_x,self.tohnya_y-8,0,24,16,8,8,11)
            if pyxel.btn(pyxel.KEY_L) :
                pyxel.blt(self.tohnya_x+8,self.tohnya_y-8,0,16,16,8,8,7)
            if (pyxel.frame_count % 30 == 0):
                self.timer +=1
            pyxel.text(120,100,str(self.timer)+"s",3)
            pyxel.blt(1*8,28,0,16,0,8,8,2)
            pyxel.blt(3*8,28,0,24,0,8,8,2)
            pyxel.blt(6*8,28,0,16,0,8,8,2)
            
            pyxel.blt(15*8,28,0,24,0,8,8,2)
            pyxel.blt(12*8,28,0,16,0,8,8,2)
        else :
            #ecran de fin
            pyxel.text(40,60,'Bravo bonome',7)
            pyxel.blt(self.aleatoire[0],self.aleatoire[1],0,16,8,8,8,2)
            pyxel.blt(self.tohnya_x,self.tohnya_y,0,16,24,8,8,7)
            pyxel.text(20,80,"vous avez fini en "+str(self.timer)+"s",7)
            
        
        

        
        
            
    

Jeu()
