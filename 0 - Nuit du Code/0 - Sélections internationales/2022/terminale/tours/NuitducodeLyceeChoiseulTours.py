import pyxel
from random import randint
'''
le jeu est un smash bros like avec 2 personnage pouvant sauter et tirer avec chaque tir enlevant 1 hp a la personne adverse
Le joueur 1 se dirige avec fleche droite, fleche gauche, control et M
Le joueur 2 se dirige avec D, Q space , E

Auteur : Mathys, Rémy, Noël
Lycée Choiseul
Tours

'''
TRANSPARENT_COLOR = 2
 # couleur transparent = gris
TILE_FLOOR = (6, 5)
TILE_MUR=(5,0)
TILE_MUR_MOU=(5,8)
TILE_PLATEFORME=(1,0)

plateformes=[]
bullets=[]

class Coeur:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def update(self):
        pass
    def draw(self):
        pyxel.blt(self.x,self.y,0,32,64,16,16,2)

class Balle1:
    def __init__(self,x,y,vitesse,orientation):
        self.x=x
        self.y=y
        self.vitesse=vitesse
        self.timer=48
        self.orientation=orientation

    def update(self):
        self.x=self.x+self.vitesse*self.orientation
        self.timer-=1
    def draw(self):
        pyxel.blt(self.x,self.y,0,2,75,4,1,2)
    def timeout(self):
        if self.timer <= 0 :
            return True
        return False

class Plateforme:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def update(self):
        pass
    def draw(self):
        pyxel.bltm(self.x,self.y,0,32,96,24,8,2)







class Player1:
    def __init__(self):
        self.x=93
        self.y=10
        self.old_x=self.x
        self.old_y=self.y
        self.vitesse_animation=3
        self.nb_images_animation=2
        self.w_tile=8
        self.h_tile=8
        self.orientation_x=-1
        self.v_x=0
        self.v_y=0
        self.a_y=1
        self.vie = 3
        self.tempo=0

    def jump(self):
        self.y=self.y+1
        if self.collision_plateformes() :
            self.v_y = -6
        self.y=self.y-1


    def tire(self):
        new_tempo=pyxel.frame_count
        if new_tempo-self.tempo>10:
            self.tempo=new_tempo
            if self.orientation_x==-1:
                decalage=-1
            else:
                decalage=9
            balle=Balle1(self.x+decalage,self.y+4,5,self.orientation_x)
            bullets.append(balle)



    def collision_plateformes(self):
        for p in plateformes:
            #print(self.x, p.x,p.x+24, self.y+8, p.y,p.y+8)
            if self.x>p.x-8 and self.x<p.x + 24 and self.y+8>p.y and self.y+8<p.y+8:
                return True
        return False

    def collision_balles(self):
        drapeau = False
        for b in bullets:
            if pyxel.sqrt((self.x+4-b.x)**2 + (self.y+4-b.y)**2) <= 5 :
                bullets.remove(b)
                drapeau = True
        return drapeau



    def update(self):
        self.old_x=self.x
        self.old_y=self.y

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.v_x=1
            self.orientation_x=1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.v_x=-1
            self.orientation_x=-1
        if pyxel.btnr(pyxel.KEY_LEFT):
            self.v_x=0
        if pyxel.btnr(pyxel.KEY_RIGHT):
            self.v_x=0
        if pyxel.btn(pyxel.KEY_CTRL):
            self.jump()
        if pyxel.btnr(pyxel.KEY_M):
            self.tire()

        self.v_y=self.v_y+0.5
        self.x=self.x+self.v_x
        self.y=self.y+self.v_y
        if self.collision_balles() :
            self.vie = self.vie-1




        if self.collision_plateformes():
            self.y=self.old_y
            self.a_y=0
            self.v_y=0.5
        if self.x<0:
            self.x=self.old_x
        if self.x>pyxel.width-8:
            self.x=self.old_x

    def draw(self):
        numero_frame=pyxel.frame_count//self.vitesse_animation % self.nb_images_animation
        x_tile=numero_frame *8
        y_tile=16
        pyxel.blt(self.x, self.y, 0, x_tile, y_tile, self.orientation_x*self.w_tile, self.h_tile, TRANSPARENT_COLOR)


class Player2:
    def __init__(self):
        self.x=35
        self.y=10
        self.old_x=self.x
        self.old_y=self.y
        self.vitesse_animation=3
        self.nb_images_animation=2
        self.w_tile=8
        self.h_tile=8
        self.orientation_x=1
        self.v_x=0
        self.v_y=0
        self.a_y=1
        self.vie=3
        self.tempo=0

    def jump(self):
        self.y=self.y+1
        if self.collision_plateformes() :
            self.v_y = -6
        self.y=self.y-1

    def tire(self):
        new_tempo=pyxel.frame_count
        if new_tempo-self.tempo>10:
            self.tempo=new_tempo
            if self.orientation_x==-1:
                decalage=-5
            else:
                decalage=9
            balle=Balle1(self.x+decalage,self.y+4,5,self.orientation_x)
            bullets.append(balle)







    def collision_plateformes(self):
        for p in plateformes:
            if self.x>p.x and self.x<p.x + 25 and self.y+8>p.y and self.y+8<p.y+8:
                return True
        return False

    def collision_balles(self):
        for b in bullets:
            if pyxel.sqrt((self.x-b.x)**2 + (self.y-b.y)**2) <= 5 :
                bullets.remove(b)
                return True
        return False

    def update(self):
        self.old_x=self.x
        self.old_y=self.y

        if pyxel.btn(pyxel.KEY_D):
            self.v_x=1
            self.orientation_x=1
        if pyxel.btn(pyxel.KEY_Q):
            self.v_x=-1
            self.orientation_x=-1
        if pyxel.btnr(pyxel.KEY_Q):
            self.v_x=0
        if pyxel.btnr(pyxel.KEY_D):
            self.v_x=0
        if pyxel.btn(pyxel.KEY_SPACE):
            self.jump()
        if pyxel.btnr(pyxel.KEY_E):
            self.tire()

        self.v_y=self.v_y+0.5
        self.x=self.x+self.v_x
        self.y=self.y+self.v_y
        if self.collision_balles() :
            self.vie = self.vie-1


        if self.collision_plateformes():
            self.y=self.old_y
            self.a_y=0
            self.v_y=0.5
        if self.x<0:
            self.x=self.old_x
        if self.x>pyxel.width-8:
            self.x=self.old_x





    def draw(self):
        numero_frame=pyxel.frame_count//self.vitesse_animation % self.nb_images_animation
        x_tile=numero_frame *8
        y_tile=64
        pyxel.blt(self.x, self.y, 0, x_tile, y_tile, self.orientation_x*self.w_tile, self.h_tile, TRANSPARENT_COLOR)


class App:
    def __init__(self):
        global player1
        global plateformes
        pyxel.init(128, 128, title="tileset test")
        pyxel.load("5.pyxres")

        global player2
        global Balle1
        global coeur,coeur1,coeur2,coeur3,coeur4,coeur5

        coeur=Coeur(0,0)
        coeur1=Coeur(16,0)
        coeur2=Coeur(32,0)
        coeur3=Coeur(80,0)
        coeur4=Coeur(96,0)
        coeur5=Coeur(112,0)

        player1=Player1()
        player2=Player2()
        plateforme0= Plateforme(2*8,12*8)
        plateforme1= Plateforme(5*8,12*8)
        plateforme2= Plateforme(8*8,12*8)
        plateforme3= Plateforme(11*8,12*8)
        plateforme4= Plateforme(3*8,8*8)
        plateforme5= Plateforme(10*8,8*8)
        plateformes.append(plateforme0)
        plateformes.append(plateforme1)
        plateformes.append(plateforme2)
        plateformes.append(plateforme3)
        plateformes.append(plateforme4)
        plateformes.append(plateforme5)


        print("largeur fenetre =",pyxel.width)
        print("hauteur fenetre =",pyxel.height)
        print("largeur tilemap =",pyxel.tilemap(0).width)
        print("hauteur tilemap =",pyxel.tilemap(0).height)





        pyxel.run(self.update, self.draw)





    def update(self):
        for b in bullets:
            b.update()
            if b.timeout():
                bullets.remove(b)
        player1.update()
        player2.update()

    def draw(self):
        pyxel.cls(0)
        # couche 1
        pyxel.bltm(0, 0, 0,0, 128, 128, 128,2)



        for b in bullets:
            b.draw()
        for p in plateformes:
            p.draw()
        if player1.vie>0:
            player1.draw()
        if player2.vie>0:
            player2.draw()
        coeur.draw()
        coeur1.draw()
        coeur2.draw()
        coeur3.draw()
        coeur4.draw()
        coeur5.draw()
        if player2.vie == 3:
            pyxel.blt(0,0,0,32,64,16,16,2)
            pyxel.blt(16,0,0,32,64,16,16,2)
            pyxel.blt(32,0,0,32,64,16,16,2)

        elif player2.vie == 2:
            pyxel.blt(0,0,0,32,64,16,16,2)
            pyxel.blt(16,0,0,32,64,16,16,2)
            pyxel.blt(32,0,0,48,64,16,16,2)
        elif player2.vie == 1 :
            pyxel.blt(0,0,0,32,64,16,16,2)
            pyxel.blt(16,0,0,48,64,16,16,2)
            pyxel.blt(32,0,0,48,64,16,16,2)
        elif player2.vie <= 0:
            pyxel.blt(0,0,0,48,64,16,16,2)
            pyxel.blt(16,0,0,48,64,16,16,2)
            pyxel.blt(32,0,0,48,64,16,16,2)

            pyxel.blt(80,0,0,16,80,16,16,2)
            pyxel.blt(96,0,0,32,80,16,16,2)
            pyxel.blt(112,0,0,48,80,16,16,2)

            pyxel.blt(80,0,0,16,96,16,16,2)
            pyxel.blt(96,0,0,32,96,16,16,2)
            
            pyxel.text(40,90,"Joueur 1 GAGNE",randint(0,15))

        if player1.vie == 3:
            pyxel.blt(80,0,0,32,64,16,16,2)
            pyxel.blt(96,0,0,32,64,16,16,2)
            pyxel.blt(112,0,0,32,64,16,16,2)

        elif player1.vie == 2:
            pyxel.blt(80,0,0,32,64,16,16,2)
            pyxel.blt(96,0,0,32,64,16,16,2)
            pyxel.blt(112,0,0,48,64,16,16,2)
        elif player1.vie == 1 :
            pyxel.blt(80,0,0,32,64,16,16,2)
            pyxel.blt(96,0,0,48,64,16,16,2)
            pyxel.blt(112,0,0,48,64,16,16,2)


        elif player1.vie <=0:
            pyxel.blt(80,0,0,48,64,16,16,2)
            pyxel.blt(96,0,0,48,64,16,16,2)
            pyxel.blt(112,0,0,48,64,16,16,2)

            pyxel.blt(80,0,0,16,80,16,16,2)
            pyxel.blt(96,0,0,32,80,16,16,2)
            pyxel.blt(112,0,0,48,80,16,16,2)

            pyxel.blt(80,0,0,16,96,16,16,2)
            pyxel.blt(96,0,0,48,96,16,16,2)
            pyxel.text(40,90,"Joueur 2 GAGNE",randint(0,15))



App()