""""
Castle Battle by Oscar GUILLAUMOT & Louis BEAUCAMPS
---
Le jeu ce joue à 2. L'objectif est de détruire le chateau adverse, pour ce faire nous invoquons des soldats qui 
ont tous un cout et des statistiques différents.

Ce jeu utilise une monnaie par joueur. On peut gagner de ces pièces chaque seconde ou en tuant une unitée adverse.
Unités:
---
  nom  | prix  | stats
  
soldat |   50  | basique
géant  |  500  | bcp de vie mais lent
oiseau |  350  | rapide mais moins de vie
boss   | 1000  | surpuissant

Touches:
---
Vert: A-Z-E-S
Rouges: I-O-P-L

Rapel des touches et des unités en jeu.
"""





import pyxel as px


class Jeu:
    
    
    def __init__(self, h, l, titre):
        px.init(h, l, title = titre)
        
        self.isintro  = 0
        self.green_soldat = []
        self.red_soldat = []
        self.green_money = 50
        self.red_money = 50
        self.txtgreen = ["",False,px.frame_count]
        self.txtred = ["",False,px.frame_count]
        self.framecoin  = px.frame_count
        self.salary = 15
        self.hpred = 100
        self.hpgreen = 100
        self.gwin =1
        self.rwin =1
        self.degatchateaured = 0
        self.degatchateaugreen = 0
        
        px.load("1.pyxres")
        px.playm(0, True)
        px.run(self.update, self.draw)
        

    
    def intro(self):
        
        px.bltm(0,0,0,0,0,128,128)
        px.text(40,30,"castle battle", 8)
        px.text(55,40,"1vs1",3)
        px.text(43,60,"press space", px.frame_count % 12)
        
        if px.btnr(px.KEY_SPACE):
            self.isintro = 1
            self.green_money = 50
            self.red_money = 50
    
    
    def hp_chateau (self):
        
        """
        barre de vie
        """
        
        px.blt(0,16,0,32,64,round(self.hpgreen*0.16),16,2)
        px.blt(112,16,0,32,64,round(self.hpred*0.16),16,2)
    
    
    def gameover(self):
        
        if self.hpred <= 0:
            self.gwin = 0
        
        if self.hpgreen <= 0:
            self.rwin = 0


    def addmoney(self):
        
        if px.frame_count - self.framecoin >= 30:
            self.framecoin = px.frame_count
            self.green_money += self.salary
            self.red_money += self.salary
            self.salary = self.salary * 1.01


    def invocation(self):
        
        # vérifications des invocations du joueur vert
        if px.btnr(px.KEY_A) and self.green_money >= 50:
            self.green_money -= 50
            self.green_soldat.append(Soldat(16,58,1,1,1,2,1,10,30))
        
        # vérifications des invocations du joueur rouge
        if px.btnr(px.KEY_I) and self.red_money >= 50:
            self.red_money -= 50
            self.red_soldat.append(Soldat(112,58,1,-1,1,2,1,10,30))
        
        # vérifications des invocations du joueur vert
        if px.btnr(px.KEY_Z) and self.green_money >= 500:
            self.green_money -= 500
            self.green_soldat.append(Soldat(16,50,2,1,1,5,0.5,50,40))
        
        # vérifications des invocations du joueur rouge
        if px.btnr(px.KEY_O) and self.red_money >= 500:
            self.red_money -= 500
            self.red_soldat.append(Soldat(112,50,2,-1,1,5,0.5,50,40))
        
        # vérifications des invocations du joueur vert
        if px.btnr(px.KEY_E) and self.green_money >= 350:
            self.green_money -= 350
            self.green_soldat.append(Soldat(16,58,3,1,1,10,2,10,15))
        
        # vérifications des invocations du joueur rouge
        if px.btnr(px.KEY_P) and self.red_money >= 350:
            self.red_money -= 350
            self.red_soldat.append(Soldat(112,58,3,-1,1,10,2,10,15))
        
        # vérifications des invocations du joueur vert
        if px.btnr(px.KEY_S) and self.green_money >= 1000:
            self.green_money -= 1000
            self.green_soldat.append(Soldat(16,42,4,1,2,15,1,75,25))
        
        # vérifications des invocations du joueur rouge
        if px.btnr(px.KEY_L) and self.red_money >= 1000:
            self.red_money -= 1000
            self.red_soldat.append(Soldat(112,42,4,-1,2,15,1,75,25))


    def update(self):
        
        self.gameover()
        self.invocation()
        self.addmoney()
        green = []        
        self.degatchateaured = 0
        self.degatchateaugreen = 0
        
        for soldat in self.green_soldat:
            if soldat.hp > 0:
                green.append(soldat)
                soldat.update(self.red_soldat)
            else :
                if soldat.attackchateau:
                    self.degatchateaured += soldat.attack
                    px.play(3,10)
                else :
                    self.red_money += self.salary
                    self.txtred[0] = soldat.type*20
                    self.txtred[1] = True
                    self.txtred[2] = px.frame_count
        
        if px.frame_count-self.txtred[2] >= 10 :
            self.txtred[1] = False
            
        self.green_soldat = green
        red = []
        
        for soldat in self.red_soldat:
            if soldat.hp > 0:
                red.append(soldat)
                soldat.update(self.green_soldat)
            else :
                if soldat.attackchateau:
                    self.degatchateaugreen += soldat.attack
                    px.play(3,10)
                else :
                    self.green_money += self.salary                
                    self.green_money += self.salary
                    self.txtgreen[0] = soldat.type*20
                    self.txtgreen[1] = True
                    self.txtgreen[2] = px.frame_count
        
        if px.frame_count-self.txtgreen[2] >= 10 :
            self.txtgreen[1] = False
        self.red_soldat = red
        self.hpred -= self.degatchateaured
        self.hpgreen -= self.degatchateaugreen


    def draw(self):
        
        if self.isintro == 0:
            self.intro()
        
        elif self.gwin == 0:
            px.bltm(0,0,0,0,0,128,128)
            px.text(50,40,"GREEN WIN", 3)
        
        elif self.rwin == 0:
            px.bltm(0,0,0,0,0,128,128)
            px.text(50,40,"RED WIN", 8)
       
        else:
            px.bltm(0,0,1,0,0,128,128)
            px.blt(10,80,0,0,8,8,8,2)
            px.text(20,80,str(round(self.green_money)),0)
            px.blt(100,80,0,8,8,8,8,2)
            px.text(110,80,str(round(self.red_money)),0)
            px.blt(12,100,0,0,24,8,8,2)
            px.text(10,110,"A:50",3)
            px.blt(80,100,0,16,24,8,8,2)
            px.text(75,110,"I:50",8)
            px.blt(29,100,0,32,96, 8,16,2)
            px.text(27,120,"Z:500",3)
            px.blt(97,100,0,48,96, 8,16,2)
            px.text(90,120,"O:500",8)
            px.blt(45,100,0,32,88,8,8,2)
            px.text(40,110,"E:350",3)
            px.blt(115,100,0,48,88,8,8,2)
            px.text(107,110,"P:350",8)
            px.blt(80,80,0,16,120,8,8,2)
            px.text(75,90,"L:1000",8)
            px.blt(45,80,0,0,120,8,8,2)
            px.text(40,90,"S:1000",3)
            self.hp_chateau()
            
            for soldat in self.green_soldat:
                soldat.draw()
            
            for soldat in self.red_soldat:
                soldat.draw()
            
            if self.txtgreen[1] == True:
                px.text(10,10,str(self.txtgreen[0]),3)
                px.blt(18,9,0,0,8,8,8,2)
            
            if self.txtred[1] == True:
                px.text(118,10,str(self.txtred[0]),8)
                px.blt(108,9,0,8,8,8,8,2)




  
class Soldat :
    
    def __init__ (self, x, y, type, team, range, attack, vit, hp, vit_att):

        px.load("1.pyxres")
        self.x = x
        self.y = y
        self.type = type
        self.vit = vit
        self.skin = 0
        self.texte = False
        self.team = team
        self.hp = hp
        self.vit_att = vit_att
        self.range = range
        self.aie = 0
        self.attack = attack
        self.attackchateau = False
        self.attframe = px.frame_count
        
        if self.team == 1 :
            self.u = 0
        else:
            self.u = 16
        
        self.varframe = px.frame_count

    
    def update (self,enemies) :
        if self.testcombat(enemies) != False:
            self.combat(enemies)
        else:
            self.move()
    
    
    def draw (self) :
        
        if self.type == 1:
            px.blt(round(self.x), self.y, 0, self.u + (self.skin*8), 24, self.team*8, 8, 2)
        elif self.type == 2:
            px.blt(round(self.x), self.y, 0, 32 + self.u + (self.skin*8), 96, self.team*8, 16, 2)
        elif self.type == 3:
            px.blt(round(self.x), self.y, 0, 32 + self.u + (self.skin*8), 88, self.team*8, 8, 2)
        else:
            px.blt(round(self.x), self.y, 0, self.u + (self.skin*8), 120, self.team*8, 24, 2)
        if self.texte:
            px.text(self.x+2,self.y-8,str(self.aie),8)
    
    
    def fonskin(self):
        
        if px.frame_count-self.varframe >= 12:
            self.varframe = px.frame_count
            if self.skin == 0:
                self.skin = 1
            else :
                self.skin = 0
    
    
    def move (self):
        
        if ((self.x < 112 and self.team == 1) or (self.x > 16 and self.team == -1)):
            self.x += self.vit * self.team
            self.fonskin()
            return 0
        else:
            self.hp = 0
            self.attackchateau = True
            self.skin = 0
            
    def testcombat (self,enemies):
        
        for ennemie in enemies:
            if abs(ennemie.x - (self.x)) <= self.range+8 :
                return ennemie
            else:
                return False
        return False
    
    
    def combat (self, enemies):
        if px.frame_count-self.attframe >= self.vit_att:
            self.attframe = px.frame_count
            for ennemie in enemies:
                if ennemie.x - (self.x+8) <= self.range :
                    if self.type == 2:
                        print("aîe")
                    ennemie.degat(self.attack)
        elif px.frame_count-self.attframe <= 10 and self.aie != 0:
            self.texte = True
        else:
            self.texte = False
    
    def degat (self, hurt):
        self.hp-=hurt
        self.aie = hurt
        px.play(3,8)

Jeu(128, 128, "Nuit du c0de 2022")
