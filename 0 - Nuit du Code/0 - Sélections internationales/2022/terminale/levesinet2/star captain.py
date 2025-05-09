"""
Utilisez les flèches pour vous déplacer, espace pour tirer
Les astéroïdes en fond ne sont pas des obstacles.
Vous avez 20 munitions, une fois que vous les avez toutes utilisées, elles se rechargent en une seconde.
Vous avez 6 points de vie, les ennemis font des dégâts allant de 1 à 6 lorsqu'ils vous touchent ou vous tirent dessus.
Les ennemis arrivent par série de 10, suivis d'un boss, avec une difficulté progressive. Il y a deux types d'ennemis
différents par niveau.
Après les boss 1 et 3, vous recevez une amélioration de la puissance de tir.
Vous gagnez après avoir vaincu le 5e boss.
"""


import pyxel as px
import random

def temps(frames):
    s=frames/30
    min=s//60
    s-=min
    return f"{int(min):02}:{int(s):02}"

class Ennemi:

    def __init__(self, tile_x, tile_y, h, w, x, y, pv, jeu):
        self.x = x
        self.y = y
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.h = h
        self.w = w
        self.existe = True
        self.etat = 0
        self.pv = pv
        self.tirs_liste = []
        self.jeu = jeu

    def creer_tir(self, type):
        self.tirs_liste.append([self.x+(self.w-2)/2, self.y+0.7*self.h, type])

    def update_tirs(self, vitesse):
        for tir in self.tirs_liste:
            tir[1] += vitesse


class Ennemi1(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(24, 8, 8, 8, x, y, 1, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(60) == 0:
            self.creer_tir(0)
        self.update_tirs(5)
        self.y += 0.25
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Ennemi2(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(32, 8, 8, 8, x, y, 2, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(60) == 0:
            self.creer_tir(1)
        self.update_tirs(5)
        self.y += 0.25
        if self.y > 128 or self.pv <= 0:
            self.existe = False


class Ennemi3(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(40, 8, 8, 8, x, y, 2, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(60) == 0:
            self.creer_tir(3)
        self.update_tirs(2)
        self.y += 0.1
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Ennemi4(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(48, 8, 8, 8, x, y, 3, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(60) == 0:
            self.creer_tir(3)
        self.update_tirs(3)
        self.y += 0.25
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Ennemi5(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(56, 8, 8, 8, x, y, 1, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(30) == 0:
            self.creer_tir(0)
        self.update_tirs(5)
        self.y += 0.4
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Ennemi6(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(64, 8, 8, 8, x, y, 6, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(60) == 0:
            self.creer_tir(2)
        self.update_tirs(5)
        self.y += 0.2
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Ennemi7(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(72, 8, 8, 8, x, y, 4, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(30) == 0:
            self.creer_tir(0)
        self.update_tirs(5)
        self.y += 0.15
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Ennemi8(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(80, 8, 8, 8, x, y, 7, jeu)

    def update(self):
        if px.frame_count % 20 >= 10:
            self.etat = 1
        else:
            self.etat = 0
        if random.randrange(90) == 0:
            self.creer_tir(4)
        self.update_tirs(2)
        self.y += 0.15
        if self.y > 128 or self.pv <= 0:
            self.existe = False

class Boss1(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(24, 24, 16, 16, x, y, 20, jeu)

    def update(self):
        
        if self.x+4<self.jeu.x:
            self.x+=0.5
        elif self.x+4>self.jeu.x:
            self.x-=0.5
        if random.randrange(60) == 0:
            self.creer_tir(2)
        self.update_tirs(3)
        if self.pv <= 0:
            self.existe = False
            self.jeu.niveau+=1
            self.jeu.boss=False

class Boss2(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(40, 24, 24, 16, x, y, 40, jeu)

    def update(self):
        
        if self.x+4<self.jeu.x:
            self.x+=0.5
        elif self.x+4>self.jeu.x:
            self.x-=0.5
        if random.randrange(40) == 0:
            self.creer_tir(5)
        self.update_tirs(2)
            

        if self.pv <= 0:
            self.existe = False
            self.jeu.boss=False

class Boss3(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(56, 24, 24, 16, x, y, 40, jeu)

    def update(self):
        
        if self.x+4<self.jeu.x:
            self.x+=0.5
        elif self.x+4>self.jeu.x:
            self.x-=0.5
        if random.randrange(60) == 0:
            self.creer_tir(4)
        self.update_tirs(5)
            

        if self.pv <= 0:
            self.existe = False
            self.jeu.niveau+=1
            self.jeu.boss=False

class Boss4(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(72, 24, 16, 16, x, y, 60, jeu)

    def update(self):
        
        if self.x+4<self.jeu.x:
            self.x+=0.5
        elif self.x+4>self.jeu.x:
            self.x-=0.5
        if random.randrange(20) == 0:
            self.creer_tir(1)
        self.update_tirs(5)
            

        if self.pv <= 0:
            self.existe = False
            self.jeu.boss=False

class Boss5(Ennemi):
    def __init__(self, x, y, jeu):
        super().__init__(40, 48, 24, 32, x, y, 100, jeu)

    def update(self):
        
        if self.x+12<self.jeu.x:
            self.x+=0.5
        elif self.x+12>self.jeu.x:
            self.x-=0.5
        if random.randrange(30) == 0:
            self.creer_tir(5)
        self.update_tirs(3)
            

        if self.pv <= 0:
            self.existe = False
            self.jeu.game_over=True
            self.jeu.game_over_text="Congratulations !!!"
            self.jeu.final_time = temps(px.frame_count)




class Jeu:

    def __init__(self):
        px.init(128, 128, "Star Captain")
        px.load("2.pyxres")
        self.x = 64
        self.y = 112
        self.dir = 0
        self.dernier_tir = 0
        self.tirs_liste = []
        self.munitions = 20
        self.munitions_epuisees = 0
        self.ennemis_liste = []
        self.phases=[[[Ennemi1, Ennemi2], 10, 2, Boss1], [[Ennemi3, Ennemi4], 10, 2, Boss2], [[Ennemi5, Ennemi6], 10, 2, Boss3], [[Ennemi7, Ennemi8], 10, 2, Boss4],[[],0,2,Boss5]]
        self.phase=self.phases.pop(0)
        self.scroll_y = 0
        self.liste_explosions = []
        self.pv = 6
        self.final_time = 0
        self.game_over = False
        self.score = 0
        self.niveau = 1
        self.game_over_text = "GAME OVER"
        self.boss=False
        px.run(self.update, self.draw)

    def mvt(self):
        if px.btn(px.KEY_LEFT) and self.x > 0:
            self.x -= 1
            self.dir = 1
        elif px.btn(px.KEY_RIGHT) and self.x < 120:
            self.x += 1
            self.dir = 2
        else:
            self.dir = 0
        if px.btn(px.KEY_UP) and self.y > 24:
            self.y -= 1
        if px.btn(px.KEY_DOWN) and self.y < 112:
            self.y += 1

    def creer_tir(self):
        if px.frame_count-self.dernier_tir >= 4 and self.munitions:
            self.dernier_tir = px.frame_count
            self.tirs_liste.append([self.x, self.y])
            self.munitions -= 1
            if self.munitions == 0:
                self.munitions_epuisees = px.frame_count

    def avancer_tir(self):
        for tir in self.tirs_liste:
            tir[1] -= 5

    def creer_ennemi(self, ennemi):
        self.ennemis_liste.append(ennemi(random.randint(0, 120), 24, self))

    def update(self):
        if self.game_over:
            return
        self.scroll_y = (self.scroll_y+1) % 1024
        self.mvt()
        if px.btn(px.KEY_SPACE):
            self.creer_tir()
        self.avancer_tir()
        if self.munitions == 0 and (px.frame_count-self.munitions_epuisees) % 30 == 29:
            self.munitions = 20
        if not self.boss:
            if self.phase[1]==0:
                if not self.ennemis_liste:
                    self.boss=True
                    self.creer_ennemi(self.phase[3])
                    if self.phases: self.phase=self.phases.pop(0)
            elif px.frame_count % (30*self.phase[2]) == 0:
                self.creer_ennemi(random.choice(self.phase[0]))
                self.phase[1]-=1
        self.verifier_collisions_tirs()
        self.verifier_collisions_joueur()
        for ennemi in self.ennemis_liste:
            if not ennemi.existe:
                self.ennemis_liste.remove(ennemi)
            else:
                ennemi.update()
        if self.pv <= 0 and not self.liste_explosions:
            self.game_over = True
            self.final_time=temps(px.frame_count)

    def verifier_collisions_tirs(self):
        for ennemi in self.ennemis_liste:
            for tir in self.tirs_liste:
                if -8 < tir[0]-ennemi.x < ennemi.w and -8 < ennemi.y-tir[1] < ennemi.h:
                    ennemi.pv -= self.niveau
                    self.score+=10
                    if ennemi.pv <= 0:
                        self.score+=10
                        self.liste_explosions.append(
                            [ennemi.x, ennemi.y, 1, 0])
                    self.tirs_liste.remove(tir)

    def verifier_collisions_joueur(self):
        for ennemi in self.ennemis_liste:
            if -8 < ennemi.x-self.x < ennemi.w and -8 < ennemi.y-self.y < ennemi.h:
                self.pv -= ennemi.pv
                self.liste_explosions.append([ennemi.x, ennemi.y, 1, 0])
                ennemi.existe = 0
                print(self.pv)
                if self.pv <= 0:
                    self.liste_explosions.append([self.x, self.y, 0, 0])
            for tir in ennemi.tirs_liste:
                if -8 < self.x-(tir[0]+3) < 2 and -2 < self.y-(tir[1]+3) < 8:
                    self.pv -= tir[2]+1
                    ennemi.tirs_liste.remove(tir)
                    if self.pv <= 0:
                        self.liste_explosions.append([self.x, self.y, 0, 0])

    def draw(self):
        px.cls(0)
        if self.game_over:
            px.text(35, 64, f"{self.game_over_text}\nSCORE: {self.score}\nTIME:{self.final_time}", 7)
            return
        etat = px.frame_count % 3
        px.bltm(0, self.scroll_y, 0, 0, 128, 128, 8*128)
        px.bltm(0, self.scroll_y-1024-128, 0, 0, 0, 128, 8*128)
        px.blt(self.x, self.y, 0, 8*self.dir, 8, 8, 8, 0)
        px.blt(self.x, self.y+8, 0, 8*etat, 16, 8, 8, 0)
        for tir in self.tirs_liste:
            px.blt(tir[0], tir[1], 0, 0, 24+(self.niveau-1)*8, 8, 8, 0)

        for ennemi in self.ennemis_liste:
            px.blt(ennemi.x, ennemi.y, 0, ennemi.tile_x,
                   ennemi.tile_y+ennemi.etat*8, ennemi.w, ennemi.h, 0)
            for tir in ennemi.tirs_liste:
                px.blt(tir[0], tir[1], 0, 8+8*(tir[2] %
                       2), 48+8*(tir[2]//2), 8, 8, 0)

        for explosion in self.liste_explosions:
            px.blt(explosion[0], explosion[1], 0, 8+8 *
                   explosion[2], 24+8*explosion[3], 8, 8, 0)
            explosion[3] += 1
            if explosion[3] > 2:
                self.liste_explosions.remove(explosion)
        px.blt(0, 0, 0, 0, 104, 128, 24)
        px.text(42, 9, "HP", 7)
        px.line(51, 10, 51, 12, 14)
        px.line(52, 9, 51+2*self.pv, 9, 14)
        px.rect(52, 10, self.pv*2, 3, 8)
        px.line(52, 13, 51+2*self.pv, 13, 14)
        px.line(52+2*self.pv, 10, 52+2*self.pv, 12, 14)
        px.blt(66, 7, 0, 0,8*(self.niveau-1)+ 24, 8, 8)
        px.text(73, 9, f"x{self.munitions}", 7)
        px.text(98, 9, str(self.score), 7)
        px.text(10, 10, temps(px.frame_count), 7)


jeu=Jeu()
