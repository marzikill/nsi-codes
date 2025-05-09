import pyxel

class Projectile:
    def __init__(self,x,y,cote,num,classe):
        self.pos_x=x
        self.pos_y=y
        self.cote=cote
        self.num=num-1
        self.classe=classe
        if self.classe=='base':
            self.num_attaque=1
        else :
            self.num_attaque=0




class Perso():
    def __init__(self,espece,numero):
        self.dessin_cord=[[0,0],[0,16],[0,32],[0,48]]
        self.pos_x=10+(numero-1)*50
        self.pos_y=80
        self.vie=200
        self.vie_max=200
        self.attaque=10
        self.dist=10
        self.vitesse=1
        self.classe=espece
        self.cd_loin=0
        self.cd_proche=0
        self.descente=False
        self.cote=1
        self.numero=numero
        
    def dessin(self):
        if self.classe=='base':
            for elem in self.dessin_cord:
                elem[0]=16
                
    def changement_stat(self):
        if self.classe=='mage':
            self.attaque=5
            self.vitesse=0.8
            self.dist=25
            
class Jeu():
    def __init__(self):
        self.frame=0
        self.fps=100
        self.demarre=False
        self.regles=False
        self.perso_choisi=False
        self.perso_cree=False
        self.liste_perso=[]
        self.j1_choix=1
        self.j2_choix=1
        self.case_y1=208
        self.case_y2=112
        self.J1=None
        self.J2=None
        self.liste_projectile=[]
               
        pyxel.init(128,128,title="NDC 2023",fps=self.fps)
        pyxel.load('theme.pyxres',True, True,False,False) 
        pyxel.run(self.update,self.draw)

        
 
    def demarrage(self):
        if 10<=pyxel.mouse_x<=42 and 100<=pyxel.mouse_y<=116 :
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
                self.demarre=True
                
    def regle_affichage(self):
        if 80<=pyxel.mouse_x<=122 and 100<=pyxel.mouse_y<=116 :
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)==True:
                self.regles=True    
    def choisir(self):
        if self.j1_choix==1 and self.j2_choix==1 :
            self.case_y1=208
            self.case_y2=112
        if  self.j1_choix==1 and self.j2_choix==2 :
            self.case_y1=144
            self.case_y2=176
        if  self.j1_choix==2 and self.j2_choix==1 :
            self.case_y1=176
            self.case_y2=144
        if  self.j1_choix==2 and self.j2_choix==2 :
            self.case_y1=112
            self.case_y2=208
        if self.J1==None:
            if pyxel.btn(pyxel.KEY_Q)==True:
                self.j1_choix=1
            if pyxel.btn(pyxel.KEY_D)==True:
                self.j1_choix=2
            if pyxel.btn(pyxel.KEY_E)==True:              
                self.J1=Perso(['mage','base'][self.j1_choix-1],1)       
        if self.J2==None:
            if pyxel.btn(pyxel.KEY_LEFT)==True:
                self.j2_choix=1
            if pyxel.btn(pyxel.KEY_RIGHT)==True:
                self.j2_choix=2
            if pyxel.btn(pyxel.KEY_RCTRL)==True:
                self.J2=Perso(['mage','base'][self.j2_choix-1],2)
        if self.J1!=None and self.J2!=None:
            self.liste_perso.append(self.J1)
            self.liste_perso.append(self.J2)
            self.perso_choisi=True
            
    def cooldown(self):
        for perso in self.liste_perso:
            if perso.cd_loin!=0:
                if self.frame%self.fps==0:
                    perso.cd_loin-=1                
            if perso.cd_proche!=0:
                if self.frame%self.fps/5==0:
                    perso.cd_proche-=0.2
                    
    def deplacement(self):
        #perso 1
        if pyxel.btn(pyxel.KEY_Q)==True and 0<self.liste_perso[0].pos_x:
            self.liste_perso[0].pos_x-=self.liste_perso[0].vitesse
        if pyxel.btn(pyxel.KEY_D)==True and self.liste_perso[0].pos_x<116:
            self.liste_perso[0].pos_x+=self.liste_perso[0].vitesse
        #perso 2
        if pyxel.btn(pyxel.KEY_LEFT)==True and 0<self.liste_perso[1].pos_x:
            self.liste_perso[1].pos_x-=self.liste_perso[1].vitesse
        if pyxel.btn(pyxel.KEY_RIGHT)==True and self.liste_perso[1].pos_x<116:
            self.liste_perso[1].pos_x+=self.liste_perso[1].vitesse
    
    def saut(self):
        #perso 1
        if self.liste_perso[0].descente==False:
            if pyxel.btn(pyxel.KEY_Z)==True:
                if self.liste_perso[0].pos_y>=60:
                    self.liste_perso[0].pos_y-=2
                else :
                    self.liste_perso[0].descente=True
            else :
                self.liste_perso[0].descente=True
        else :
            self.liste_perso[0].pos_y+=1
        #perso 2
        if self.liste_perso[1].descente==False:
            if pyxel.btn(pyxel.KEY_UP)==True:
                if self.liste_perso[1].pos_y>=60:
                    self.liste_perso[1].pos_y-=2
                else :
                    self.liste_perso[1].descente=True
            else :
                self.liste_perso[1].descente=True
        else :
            self.liste_perso[1].pos_y+=1
                
    def position(self):
        if self.liste_perso[0].pos_x<self.liste_perso[1].pos_x:
            self.liste_perso[0].cote=1
            self.liste_perso[1].cote=-1
        else :
            self.liste_perso[0].cote=-1
            self.liste_perso[1].cote=1
    
    def attaque_loin(self):
        if self.liste_perso[0].cd_loin==0 and pyxel.btn(pyxel.KEY_A)==True:
            if self.liste_perso[0].cote==1:
                self.liste_projectile.append(Projectile(self.liste_perso[0].pos_x+16,self.liste_perso[0].pos_y+4,1,self.liste_perso[0].numero,self.liste_perso[0].classe))
                self.liste_perso[0].cd_loin+=1
            else :
                self.liste_projectile.append(Projectile(self.liste_perso[0].pos_x,self.liste_perso[0].pos_y+4,-1,self.liste_perso[0].numero,self.liste_perso[0].classe))
                self.liste_perso[0].cd_loin+=1
        if self.liste_perso[1].cd_loin==0 and pyxel.btn(pyxel.KEY_RSHIFT)==True:
            if self.liste_perso[1].cote==1:
                self.liste_projectile.append(Projectile(self.liste_perso[1].pos_x+16,self.liste_perso[1].pos_y+4,1,self.liste_perso[1].numero,self.liste_perso[1].classe))
                self.liste_perso[1].cd_loin+=1
            if self.liste_perso[1].cote==-1:
                self.liste_projectile.append(Projectile(self.liste_perso[1].pos_x,self.liste_perso[1].pos_y+4,-1,self.liste_perso[1].numero,self.liste_perso[1].classe))
                self.liste_perso[1].cd_loin+=1
                
    def deplacement_projectile(self):
        for proj in self.liste_projectile:
            proj.pos_x+=1*proj.cote
            if proj.pos_x<=0 or proj.pos_x>=128:
                self.liste_projectile.remove(proj)
        
    
    def recevoir_attaque(self):
        for proj in self.liste_projectile:
            if proj.num==0:
                if proj.pos_x<=self.liste_perso[1].pos_x and proj.pos_x+5>=self.liste_perso[1].pos_x:
                    if self.liste_perso[1].pos_y+16>=proj.pos_y>=self.liste_perso[1].pos_y:
                        self.liste_projectile.remove(proj)
                        self.liste_perso[1].vie-=self.liste_perso[0].dist

            if proj.num==1:
                if proj.pos_x<=self.liste_perso[0].pos_x and proj.pos_x+5>=self.liste_perso[0].pos_x:
                    if self.liste_perso[0].pos_y+16>=proj.pos_y>=self.liste_perso[0].pos_y:
                        self.liste_projectile.remove(proj)
                        self.liste_perso[0].vie-=self.liste_perso[1].dist

                        
    def atq(self):

        if self.liste_perso[1].pos_x-20<=self.liste_perso[0].pos_x<=self.liste_perso[1].pos_x+20 or self.liste_perso[0].pos_x-20<=self.liste_perso[1].pos_x<=self.liste_perso[0].pos_x+20:
            if pyxel.btnp(pyxel.KEY_E)==True:
                self.liste_perso[1].vie-=self.liste_perso[0].attaque
            if pyxel.btnp(pyxel.KEY_RCTRL)==True:
                self.liste_perso[0].vie-=self.liste_perso[1].attaque
        
    def update(self):
        self.frame+=1
        if (self.demarre==False and self.regles==False) or (self.regles==True and self.demarre==False):
            self.demarrage()
            self.regle_affichage()
        elif self.perso_choisi==False:
            self.choisir()
        elif self.perso_choisi==True:
            for perso in self.liste_perso:
                perso.dessin()
                perso.changement_stat()
            self.cooldown()
            self.deplacement()
            for perso in self.liste_perso:
                if perso.pos_y>=100:
                    perso.descente=False
            self.saut()
            self.position()
            self.attaque_loin()
            self.deplacement_projectile()
            self.recevoir_attaque()
            self.atq()

        
        
    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(False)
        if self.demarre==False and self.regles==False:
            pyxel.bltm(3,0,0,0,0,128,128)
            pyxel.mouse(True)
            pyxel.blt(10,100,0,0,112,32,16,14)
            pyxel.blt(80,100,0,32,112,32,16,14)
        elif self.demarre==True:
            if self.perso_choisi==False:  
                #Mage
                pyxel.blt(10,20,0,64,self.case_y1,64,27,14)
                pyxel.blt(12,22,0,64,24,8,8,14)
                pyxel.blt(12,22,0,72,64,8,8,14)
                pyxel.text(22,22,'ATK:5',0)
                pyxel.text(22,28,'DIS:25',0)
                pyxel.text(22,34,'PV:200',0)
                pyxel.text(22,40,'VIT:90%',0)
                #Base
                pyxel.blt(70,20,0,64,self.case_y2,64,27,14)
                pyxel.blt(72,22,0,72,24,8,8,14)
                pyxel.blt(72,22,0,72,64,8,8,14)
                pyxel.text(82,22,'ATK:10',0)
                pyxel.text(82,28,'DIS:10',0)
                pyxel.text(82,34,'PV:200',0)
                pyxel.text(82,40,'VIT:100%',0)
                pyxel.text(10,100,'To chose the character',3)
                pyxel.text(10,110,'player 1 has to click "E"',3)
                pyxel.text(10,120,'and Player 2: "right Ctrl"',3)
            elif self.demarre==True and self.perso_choisi==True:
                
                pyxel.bltm(0,0,0,128,0,128,128)
                if self.liste_perso[0].vie>0:
                    if pyxel.btn(pyxel.KEY_E)==True:
                        self.liste_perso[0].dessin_cord[0][1]=32
                    elif pyxel.btn(pyxel.KEY_Z)==True or pyxel.btn(pyxel.KEY_S)==True:
                        self.liste_perso[0].dessin_cord[0][1]=48
                    else :
                        self.liste_perso[0].dessin_cord[0][1]=0
                    pyxel.blt(self.liste_perso[0].pos_x+2,self.liste_perso[0].pos_y-8,0,72,40,7,7,14)
                    pyxel.blt(self.liste_perso[0].pos_x,self.liste_perso[0].pos_y,0,self.liste_perso[0].dessin_cord[0][0],self.liste_perso[0].dessin_cord[0][1],16*self.liste_perso[0].cote,16,9)
                else:
                    pyxel.blt(40,50,0,144,72,48,16,14)
                    
                if self.liste_perso[1].vie>0:
                    if pyxel.btn(pyxel.KEY_RCTRL)==True or pyxel.btn(pyxel.KEY_RSHIFT)==True:
                        self.liste_perso[1].dessin_cord[0][1]=32
                    elif pyxel.btn(pyxel.KEY_UP)==True or pyxel.btn(pyxel.KEY_DOWN)==True:
                        self.liste_perso[1].dessin_cord[0][1]=48
                    else :
                        self.liste_perso[1].dessin_cord[0][1]=0
                    pyxel.blt(self.liste_perso[1].pos_x+2,self.liste_perso[1].pos_y-8,0,64,40,7,7,14)
                    pyxel.blt(self.liste_perso[1].pos_x,self.liste_perso[1].pos_y,0,self.liste_perso[1].dessin_cord[0][0],self.liste_perso[1].dessin_cord[0][1],16*self.liste_perso[1].cote,16,9)
                else:
                    pyxel.blt(40,50,0,96,72,48,16,14)
                
                pyxel.rect(1,1,48,18,13)
                pyxel.rect(78,1,48,18,13)
                pyxel.rect(2,2,(self.liste_perso[0].vie/self.liste_perso[0].vie_max)*46,16,11)
                pyxel.rect(79,2,(self.liste_perso[1].vie/self.liste_perso[1].vie_max)*46,16,11)
                
                pyxel.blt(self.liste_perso[0].pos_x+2,self.liste_perso[0].pos_y-8,0,72,40,7,7,14)
                pyxel.blt(self.liste_perso[1].pos_x+2,self.liste_perso[1].pos_y-8,0,64,40,7,7,14)

                for proj in self.liste_projectile:
                    pyxel.blt(proj.pos_x,proj.pos_y,0,0+8*proj.num_attaque,64,8*proj.cote,8,2)
                pyxel.rect(1,1,48,18,13)
                pyxel.rect(78,1,48,18,13)
                pyxel.rect(2,2,(self.liste_perso[0].vie/self.liste_perso[0].vie_max)*46,16,11)
                pyxel.rect(79,2,(self.liste_perso[1].vie/self.liste_perso[1].vie_max)*46,16,11)    
                               
        elif self.regles==True and self.demarre==False :
            pyxel.mouse(True)
            pyxel.cls(3)

            pyxel.text(1,8,'For Player 1 :',0)
            pyxel.text(1,14,'Q to go left',0)
            pyxel.text(1,26,'D to go right',0)
            pyxel.text(1,20,"Z to jump",0)
            pyxel.text(1,32,"S to sneak",0)
            pyxel.text(1,38,"E for melee attack",0)
            pyxel.text(1,44,"A for range attack",0)
            pyxel.text(1,54,'For Player 2 :',0)
            pyxel.text(1,60,'Left arrow to go left',0)
            pyxel.text(1,66,'Right arrow to go right',0)
            pyxel.text(1,72,"Up arrow to jump",0)
            pyxel.text(1,78,"Down arrow to sneak",0)
            pyxel.text(1,84,"Right control for melee attack",0)
            pyxel.text(1,90,"Right shift for range attack",0)
            pyxel.blt(10,106,0,0,112,32,16,14)

        
        
    
Jeu()
