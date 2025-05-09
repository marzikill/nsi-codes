import pyxel

liste_murs=((0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(0,4),(1,4),(2,4),(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(3,5),(4,5),(5,5),(0,7),(1,7),(2,7),(0,8))
liste_panneau=(('Bienvenue dans notre jeu !', 'Le but ? Atteindre la fin !', 'Simple non ?', 'H pour interagir et fermer'),
('Vous avez trouve la cle ?','Maintenant apprenons le saut','Appuyer sur la barre espace !'),
('ATTENTION !','un slime','il faudrait trouver un moyen','de passer'),
('Ah, excuser moi','apparement, ce slime','n etait pas si mechant'),
('Hmmmm','des plateformes volantes','bonne chance'),
('Ces sauts sont difficiles','il faut le faire','au dernier moment !'),
('Pas de message ici','non, definitivement pas'),
('Ne touche pas les piques !! ','ils pourrais faire mal'),
('Le grand saut','ahahah','ne te loupe pas'),
('Ouuuuuuuuh','celui ci est vraiment','pas evident'),
('Bienvenue dans notre jeu !', 'Le but ? Atteindre la fin !','euh... y a un soucis'),
('vous etes au milieu','du VIDE'),
('LE','NIVEAU','ULTIIIIME'),
('Bravo','vous avez atteint...'),
('La fin','mais...'),
("Vous n'aurez rien !",'Voilà comment on vous récompense !'))
#-------------------------------------------------------------------------------
# Joueur
#-------------------------------------------------------------------------------

class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")

        self.tuile_fixe=([0,72,8,8,5],[8,72,8,8,5])
        self.tuile_bouge=([0,88,8,8,5],[8,88,8,8,5])
        self.tuile_saut=[0,80,8,8,5]
        self.tuile_descend=[8,80,8,8,5]

        self.tuile_actu=0

        self.nb_morts=0

        self.x=10
        self.y=0

        self.en_mouvement=False
        self.en_saut=False
        self.descend=False
        self.saut=13

        self.cle=False
        self.anim_cle=False
        self.temps_cle=0
        self.porte=False
        self.pensee=False

        self.bonus_1=False
        self.bonus_2=False

        self.niveau=0
        self.nb_change=1

        self.menu=True
        self.menu_touches=False
        self.son=True

        self.p_actif=False

        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def deplacement(self):
        self.en_mouvement=False

        if pyxel.btn(pyxel.KEY_RIGHT) and not(self.is_wall(8,7)) and not(self.anim_cle) and 0<=self.x<=120:
            if self.bonus_1:
                self.x+=3
            else:
                self.x+=1

            self.tuile_fixe[0][2]=8
            self.tuile_fixe[1][2]=8

            self.tuile_bouge[0][2]=8
            self.tuile_bouge[1][2]=8

            self.tuile_saut[2]=8
            self.tuile_descend[2]=8

            if not(self.en_saut):
                self.en_mouvement=True

        elif pyxel.btn(pyxel.KEY_LEFT) and not(self.is_wall(0,7)) and not(self.anim_cle):
            if self.bonus_1:
                self.x-=3
            else:
                self.x-=1

            self.tuile_fixe[0][2]=-8
            self.tuile_fixe[1][2]=-8

            self.tuile_bouge[0][2]=-8
            self.tuile_bouge[1][2]=-8

            self.tuile_saut[2]=-8
            self.tuile_descend[2]=-8

            if not(self.en_saut):
                self.en_mouvement=True

    def sauter(self):
        if pyxel.btnp(pyxel.KEY_SPACE) and not(self.en_saut) and self.saut>0 and not(self.anim_cle):
            self.en_saut=True
            pyxel.playm(0)
        if self.en_saut and not(self.anim_cle):
            if self.saut>0:
                self.saut-=1
                for cx in range(9):
                    if not(self.is_wall(cx,-1)):
                        self.y-=1
                        break
            else:
                self.en_saut=False

    def gravite(self):
        if (not(self.is_wall(1,8)) or not(self.is_wall(7,8))) and not(self.en_saut) and not(self.anim_cle):
            if self.bonus_2==True:
                self.y+=1
                if (not(self.is_wall(1,8)) or not(self.is_wall(7,8))):
                    self.y+=1
            else:
                self.y+=1
            self.descend=True
        elif (self.is_wall(0,8) or self.is_wall(8,8)):
            self.saut=13
            self.descend=False

    def is_wall(self,x,y):
        return pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+x)//8),(self.y+y)//8) in liste_murs

    def echelle(self):
        if (pyxel.tilemap(0).pget(((self.x+(128*self.niveau))//8),(self.y+8)//8)==(9,2) or pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+8)//8),(self.y+8)//8)==(9,2) or pyxel.tilemap(0).pget(((self.x+(128*self.niveau))//8),(self.y)//8)==(9,2) or pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+8)//8),(self.y)//8)==(9,2)) and not(self.en_saut):
            if pyxel.btn(pyxel.KEY_UP):
                self.y-=2
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.y+=2

    def panneau(self):
        if not(self.p_actif):
            for cx in range(9):
                if pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+cx)//8),(self.y+4)//8)==(4,6) and pyxel.btnp(pyxel.KEY_H):
                    self.p_actif=True
                    break
        elif self.p_actif:
            nb=0
            pyxel.rect(4,84,120,36,0)
            pyxel.rectb(4,84,120,36,3)
            for texte in liste_panneau[self.niveau]:
                pyxel.text(6,86+(8*nb),liste_panneau[self.niveau][nb],7)
                nb+=1
            if pyxel.btnp(pyxel.KEY_H):
                self.p_actif=False

    def coffre(self):
        for cx in range(9):
            if pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+cx)//8),(self.y+4)//8)==(7,5) and pyxel.btnp(pyxel.KEY_H):
                self.cle=True
                self.anim_cle=True
                pyxel.playm(2)
                self.temps_cle=20
                break
        if self.anim_cle:
            if self.temps_cle>0:
                self.temps_cle-=1
            else:
                self.anim_cle=False

    def ouvrir_porte(self):
        if pyxel.btnp(pyxel.KEY_H) and self.pensee:
            self.pensee=False
        for cx in range(9):
            if pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+cx)//8),(self.y+4)//8)==(2,6) and pyxel.btnp(pyxel.KEY_H):
                if self.cle:
                    self.porte=True
                    self.cle=False
                    break
                else:
                    self.pensee=True

    def bonus_1_act(self):
        for cx in range(9):
            if pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+cx)//8),(self.y-1)//8)==(4,5):
                self.bonus_1=True

    def bonus_2_act(self):
        for cx in range(9):
            if pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+cx)//8),(self.y-1)//8)==(3,5):
                self.bonus_2=True

    def change_map(self):
        if self.porte:
            self.niveau+=1
            self.porte=False
            self.x=10
            self.y=55
            self.p_actif=False
            self.bonus_1=False
            self.bonus_2=False

    def mort(self):
        if self.y>128 or pyxel.tilemap(0).pget(((self.x+(128*self.niveau)))//8,(self.y+7)//8)==(6,6) or pyxel.tilemap(0).pget(((self.x+(128*self.niveau)+8))//8,(self.y+7)//8)==(6,6):
            self.niveau=0
            self.cle=False
            self.porte=False
            self.p_actif=False
            self.x=10
            self.y=55
            self.nb_morts+=1
            self.bonus_1=False
            self.bonus_2=False
            self.nb_change=1
            pyxel.playm(4)

#-------------------------------------------------------------------------------
# Menu
#-------------------------------------------------------------------------------

    def fonction_menu(self):
        pyxel.mouse(True)
        if self.son==True:
            pyxel.playm(3,1,True)
        if self.son==False:
            pyxel.stop()
        if 0<=pyxel.mouse_x<=128 and 0<=pyxel.mouse_y<=80 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.menu=False
            self.menu_touches=False
        elif 16<=pyxel.mouse_x<=56 and 96<=pyxel.mouse_y<=128 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.menu_touches:
                self.menu_touches=False
            else:
                self.menu_touches=True
        elif 72<=pyxel.mouse_x<=112 and 96<=pyxel.mouse_y<=128 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.son:
                self.son=False
            else:
                self.son=True

#-------------------------------------------------------------------------------
# Update
#-------------------------------------------------------------------------------
    def update(self):
        if self.menu:
            self.fonction_menu()
        else:
            pyxel.mouse(False)
            self.gravite()
            self.sauter()
            self.deplacement()
            self.echelle()
            self.coffre()
            self.ouvrir_porte()
            self.bonus_1_act()
            self.bonus_2_act()
            self.change_map()
            self.mort()
#-------------------------------------------------------------------------------
# Draw
#-------------------------------------------------------------------------------
    def change_tuile(self):
        if pyxel.frame_count%12==0:
            if self.tuile_actu>=1:
                self.tuile_actu=0
            else:
                self.tuile_actu+=1

    def draw(self):
        if self.menu:
            pyxel.bltm(0,0,0,0,128,128,128)
            if self.menu_touches:
                pyxel.rect(4,44,120,30,0)
                pyxel.rectb(4,44,120,30,3)
                pyxel.text(6,46,"Interagir : H",7)
                pyxel.text(6,56,"Sauter : Espace",7)
                pyxel.text(6,66,"Deplacement : Fleches",7)
        else:
            pyxel.bltm(0,0,0,128*self.niveau,0,128,128)
            self.change_tuile()
            if self.en_mouvement==False and not(self.en_saut) and not(self.descend) and not(self.anim_cle):
                pyxel.blt(self.x,self.y,0,self.tuile_fixe[self.tuile_actu][0],self.tuile_fixe[self.tuile_actu][1],self.tuile_fixe[self.tuile_actu][2],self.tuile_fixe[self.tuile_actu][3],self.tuile_fixe[self.tuile_actu][4])
            elif self.en_mouvement and not(self.en_saut) and not(self.descend) and not(self.anim_cle):
                pyxel.blt(self.x,self.y,0,self.tuile_bouge[self.tuile_actu][0],self.tuile_bouge[self.tuile_actu][1],self.tuile_bouge[self.tuile_actu][2],self.tuile_bouge[self.tuile_actu][3],self.tuile_bouge[self.tuile_actu][4])
            elif self.en_saut and not(self.anim_cle):
                pyxel.blt(self.x,self.y,0,self.tuile_saut[0],self.tuile_saut[1],self.tuile_saut[2],self.tuile_saut[3],self.tuile_saut[4])
            elif self.descend and not(self.anim_cle):
                pyxel.blt(self.x,self.y,0,self.tuile_descend[0],self.tuile_descend[1],self.tuile_descend[2],self.tuile_descend[3],self.tuile_descend[4])

            if self.cle:
                pyxel.blt(self.x,self.y-8,0,0,48,8,8,5)

            if self.pensee==True:
                pyxel.rect(4,101,120,13,0)
                pyxel.rectb(4,101,120,13,3)
                pyxel.text(6,105,"Mmmh une cle serait utile...",7)

        self.panneau()

        if self.anim_cle:
            pyxel.blt(self.x,self.y,0,24,80,8,8,5)

        #---
        pyxel.text(2,2,str(self.nb_morts), 8)

Jeu()