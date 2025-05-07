"""
KnockOut !
Jeu de combat et d'éjection sur plateforme
Joueur 1:
z : saut
q : se déplacer à gauche
d : se déplacer à droite
f : changer de capacités (passer de corps à corps à attaque à distance et inversement)
a : attaque rapide
e : attaque lourde # Non terminée

Joueur 2:
8 (numpad) : saut
4 (numpad) : se déplacer à gauche
6 (numpad) : se déplacer à droite
+ (numpad) : changer de capacités (passer de corps à corps à attaque à distance et inversement)
7 : attaque rapide
9 : attaque lourde # Non terminée

Pour gagner, il faut éjecter 3 fois son adversaire du terrain.
Plus on le tape, plus son adversaire prendra de dégâts et donc sera éjecté loin!
Lorsqu'un joueur n'a plus de vie, le jeu se ferme automatiquement
"""
import pyxel as pyx

YBPLATFORME = 11*4
YHPLATFORME = 9*4
XGPLATFORME = 2*4
XDPLATFORME = 13*4

class Personnage():
    def __init__(self, joueur: int):
        self.direction = 0
        self.joueur = joueur
        if joueur == 1: # Joueur à gauche
            self.x = 15
            self.mouvdroite = pyx.KEY_D
            self.mouvgauche = pyx.KEY_Q
            self.jump = pyx.KEY_Z
            self.atka = pyx.KEY_A
            self.atke = pyx.KEY_E
            self.direction = 1 # Regarde à droite
        elif joueur == 2: # Joueur à droite
            self.x = 47
            self.mouvdroite = pyx.KEY_KP_6
            self.mouvgauche = pyx.KEY_KP_4
            self.jump = pyx.KEY_KP_8
            self.atka = pyx.KEY_KP_7
            self.atke = pyx.KEY_KP_8
            self.direction = -1 # Regarde à gauche
        self.playerjump = 0
        self.y = 32
        self.ejectpercent = 0
        self.stocks = 3
        self.pulsionsaut = 0
        self.ejection = 0

    def update(self):
        # Appuis de touches
        if pyx.btn(self.mouvdroite) and (self.x+1 !=XGPLATFORME or not(YHPLATFORME<=self.y<=YBPLATFORME)): # À droite
            self.x+=1
            self.direction = 1
        if pyx.btn(self.mouvgauche) and (self.x+1 !=XDPLATFORME or not(YHPLATFORME<=self.y<=YBPLATFORME)): # À gauche
            self.x-=1
            self.direction = -1
        if pyx.btnp(self.jump)and self.playerjump<2: # Saut
            self.pulsionsaut = 6
            self.playerjump+=1
        if not(0<self.x<64) or not(0<self.y<64):
            # Mort du personnage
            self.stocks-=1
            self.ejectpercent=0
            if self.stocks == 0:
                pyx.quit()
            else:
                self.x = 32
                self.y = 32
                self.ejection = 0
        if pyx.btnp(self.atka):
            self.atk1(self.direction)
        if pyx.btnp(self.atke):
            self.atk2(self.direction)

        # Collisions
        if (
           self.y!=YHPLATFORME-0.5
                or self.x<XGPLATFORME
                or self.x>XDPLATFORME):
            if not(self.pulsionsaut): self.y+=0.5
            if self.playerjump != 2: self.playerjump = 1
        else:
            self.playerjump = 0

        # Sauts
        if self.pulsionsaut:
            if (self.y!=YBPLATFORME+0.5
                or self.x<XGPLATFORME 
                or self.x>XDPLATFORME):
                self.y-=1.5
                self.pulsionsaut -= 1
            else: self.pulsionsaut = 0

        # Ejection
        if self.ejection > 0 and (self.x+2 !=XGPLATFORME or not(YHPLATFORME<=self.y<=YBPLATFORME)):
            self.x+=2
            self.ejection-=2
            if self.ejection < 0: self.ejection = 0
        elif self.ejection <0 and (self.x-2 !=XDPLATFORME or not(YHPLATFORME<=self.y<=YBPLATFORME)):
            self.x-=2
            self.ejection+=2
            if self.ejection > 0: self.ejection = 0

    def atk1(self, direction):
        pass

    def atk2(self, direction):
        pass

    def draw(self):
        if self.joueur == 1:
            if not self.pulsionsaut:
                pyx.blt(self.x*2, self.y*2, 0, 24, 16, 8*self.direction, 8)
            else:
                pyx.blt(self.x*2, self.y*2, 0, 16, 24, 8*self.direction, 8)
        else:
            if not self.pulsionsaut:
                pyx.blt(self.x*2, self.y*2, 0, 32, 16, 8*self.direction, 8) 
            else:
                pyx.blt(self.x*2, self.y*2, 0, 24, 24, 8*self.direction, 8)


class Poing():
    def __init__(self, direction, x, y):
        self.x = x
        self.y = y
        self.direction = direction
        self.ttl = 15
        self.degats = 20
        self.puissance = 10

    def update(self):
        self.ttl -= 1

    def draw(self):
        if self.direction == 1:
            pyx.blt(self.x*2+6, self.y*2, 0, 40, 16, 8, 8)
        else:
            pyx.blt(self.x*2-6, self.y*2, 0, 16, 16, 8, 8)

class Waddle(Personnage):
    def __init__(self, joueur: int):
        super().__init__(joueur)
        self.sprite1 = (0,24) if joueur == 1 else (16,24)
        self.sprite2 = (8,24) if joueur == 1 else (24,24)
        self.props = []

    def atk1(self, direction):
        # Punch devant soi
        self.props.append(Poing(direction, self.x + self.direction, self.y))

    def atk2(self, direction):
        # Attaque chargée, qui fait plus ou moins avancer en fonction de la
        # charge.
        pass

    def update(self):
        super().update()
        for poing in enumerate(self.props):
            poing[1].update()
            if poing[1].ttl == 0:
                self.props.pop(poing[0])

    def draw(self):
        for poing in self.props:
            poing.draw()

        super().draw()

# Tirs de laser du Shooter
class Tir():
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
        self.degats = 15
        self.puissance = 3
    def update(self):
        # Faire bouger selon la direction
        self.x += self.direction
    def draw(self):
        pyx.blt(self.x*2, self.y*2, 0, 56,8,  8*self.direction, 8)

class Shooter(Personnage):
    def __init__(self, joueur: int):
        super().__init__(joueur)
        self.etat = 0  # 0 = Chibi, 1 = Grand, 2 = Max
        self.props = []
        self.tourne = 0 # 1, 2, 3 sont les étapes pendant qu'il tourne
        # 1 est un quart de tour, 2 deux quarts de tour, etc.
        # A 3, revient à 0.

    def update(self):
        super().update()
        if self.tourne: # Pendant l'attaque
            if self.tourne == 3:
                self.tourne = 0 # Fin de l'attaque
            else:
                self.tourne += 0.2
        for tir in enumerate(self.props):
            # Détruit le tir à la sortie de l'écran
            tir[1].update()
            if tir[1].x < 0 or tir[1].x > 64:
                self.props.pop(tir[0])

    def atk1(self, direction):
        # Tire dans la direction actuelle un rapide laser
        # Ajoute un tir dans la liste
        self.props.append(Tir(direction, self.x, self.y))

    def atk2(self, direction):
        # Tourne sur soi-même. Dure 15 frames
        if not(self.tourne):
            self.tourne = 0.2
        for tir in self.props:
            tir.update()

    def draw(self):
        # Doit dessiner le sprite avec sa position en fonction de la rotation de
        # self.tourne
        for tir in self.props:
            tir.draw()
        super().draw()


class App():
    def __init__(self):
        pyx.init(128, 128, title="KnockOut !")
        pyx.load('main.pyxres')
        # Touches pour changer de personnage
        self.change1 = pyx.KEY_F
        self.change2 = pyx.KEY_KP_PLUS
        self.char1 = Waddle(1)
        self.char2 = Shooter(2)
        pyx.run(self.update, self.draw)

    def update(self):
        # Collisions du joueur 1 sur le 2
        if isinstance(self.char1, Shooter):
            if self.char1.tourne and \
                    ((self.char2.x-self.char1.x)**2 + \
                    (self.char2.y-self.char1.y)**2) < 8:
                direction = -1 if (self.char2.x - self.char1.x) < 0 else 1
                self.char2.ejectpercent += 15
                self.char2.ejection = 4 * direction * \
                        (1 + self.char2.ejectpercent/100)
        for prop in enumerate(self.char1.props):
            if (-8 < prop[1].x-self.char2.x < 8) and \
                    (-8 < prop[1].y-self.char2.y < 8):
                self.char2.ejectpercent += prop[1].degats
                self.char2.ejection = prop[1].puissance * \
                        prop[1].direction * (1 + self.char2.ejectpercent/100)
        # Collisions du joueur 2 sur le 1
        if isinstance(self.char2, Shooter):
            if self.char2.tourne and \
                    ((self.char1.x-self.char2.x)**2 + \
                    (self.char1.y-self.char2.y)**2) < 8:
                direction = -1 if (self.char1.x - self.char2.x) < 0 else 1
                self.char1.ejectpercent += 15
                self.char1.ejection = 4 * direction * \
                        (1 + self.char1.ejectpercent/100)
        for prop in enumerate(self.char2.props):
            if (-8 < prop[1].x-self.char1.x < 8) and \
                    (-8 < prop[1].y-self.char1.y < 8):
                self.char1.ejectpercent += prop[1].degats
                self.char1.ejection = prop[1].puissance * \
                        prop[1].direction * (1 + self.char1.ejectpercent/100)
        # Changement de personnages
        if pyx.btnp(self.change1):
            if isinstance(self.char1, Waddle):
                self.char1 = Shooter(1)
            elif isinstance(self.char1, Shooter):
                self.char1 = Waddle(1)
        if pyx.btnp(self.change2):
            if isinstance(self.char2, Waddle):
                self.char2 = Shooter(2)
            elif isinstance(self.char2, Shooter):
                self.char2 = Waddle(2)

        self.char1.update()
        self.char2.update()

    def draw(self):
        pyx.bltm(0,0,0,0, 0, 128, 128)
        self.char1.draw()
        self.char2.draw()
        pyx.text(0,0,"player 1:" + str(self.char1.ejectpercent),3)
        pyx.text(0,10,"lives:"+str(self.char1.stocks),3)
        pyx.text(64,0,"player 2:" + str(self.char2.ejectpercent),3)
        pyx.text(64,10,"lives:"+str(self.char2.stocks),3)

App()
