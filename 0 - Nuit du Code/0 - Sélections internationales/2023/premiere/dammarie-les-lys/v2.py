import pyxel


WIDHT = 128
HAUTEUR = 128
LARGEUR = 128
G = 1
pyxel.init(128,128)
pyxel.load("theme.pyxres")
X=0
Y=1

FPS = 60


position_plateforme = (24,73)
taille_plateforme = (80,16)
surface_plateforme = (position_plateforme[X],position_plateforme[X]+taille_plateforme[X]
                      ,position_plateforme[Y],position_plateforme[Y]+taille_plateforme[Y])




menu = True

def hitbox(hit1,hit2,teste=False):
    if hit1[3] >= hit2[2] and hit1[2] <= hit2[3]:
        if teste:
            print("y")
        if hit1[1] >= hit2[0] and hit1[1] <= hit2[1] or hit1[X] <= hit2[1] and hit1[X] >= hit2[X]:
            return True
    return False



class Player:
    def __init__(self,x,y,height,widht,touche,touche2,u,v,px,py):
        self.default_x = x
        self.default_y = y
        self.x = self.default_x
        self.y = self.default_y
        self.h = height
        self.w = widht
        self.touche = touche
        self.touche2 = touche2
        self.force_chute = 0
        self.pourcent = 0
        self.projection = 0
        self.jump_dispo = 2
        self.attacking = False
        self.delay_attack = 0
        self.sens = 1
        self.v = v
        self.u = u
        self.projectile = []
        self.px = px
        self.py = py
        self.pv = 3
    
        
        
    def draw(self):
        pyxel.blt(self.x,self.y,0,self.u ,self.v,self.w* self.sens,self.h,colkey=0)
        for proj in self.projectile:
            pyxel.blt(proj[X],proj[Y],0,self.px,self.py,6*proj[3],3,colkey=0)
            proj[X] += 2 * proj[3]
            proj[2] -= 2
            if proj[2] < 0:
                self.projectile.pop()
    
    def move(self):
        if  pyxel.btn(self.touche[0]) or pyxel.btn(self.touche2[0]) :
            self.x -=2
            self.sens = -1
        if  pyxel.btn(self.touche[1]) or pyxel.btn(self.touche2[1]):
            self.x +=2
            self.sens = 1
        if  pyxel.btnp(self.touche[2]) or pyxel.btn(self.touche2[2]) and self.jump_dispo > 0:
            self.force_chute = -8
            self.jump_dispo -= 1
        if  pyxel.btnp(self.touche[3]) or pyxel.btn(self.touche2[3]):
            self.attack()
        if pyxel.btnp(self.touche[4]) or pyxel.btn(self.touche2[4]) and len(self.projectile)<1:
            self.projectile.append([self.x,self.y + 8,60,self.sens])
    
    def graviter(self):
        self.y += self.force_chute
        self.x += self.projection
        
            
        if not hitbox(self.hitbox_player(),surface_plateforme):
            self.force_chute += G
        
        else:
            self.force_chute = 0
            self.y = position_plateforme[Y] - self.h
            self.jump_dispo = 2
        
        
            
        
            
        if self.projection < 0:
            self.projection += G
        if self.projection > 0:
            self.projection -= G
        
    def respawn(self):
        if self.y > 200:
            self.y = self.default_y
            self.x = self.default_x
            self.force_chute = 0
            self.projection = 0
            self.pourcent = 0
            self.pv -= 1
            
    def degat(self,sens,deg):
        self.projection += (2 + self.pourcent//30 ) * sens
        self.force_chute -= (2 + self.pourcent//40 )
        self.pourcent += deg
    
    def attack(self):
        if not self.attacking:
            self.color = 3
            self.attacking = True
            self.delay_attack = FPS // 3
            self.w += 4
            self.v += 24
    
    def player_run(self):
        self.move()
        self.graviter()
        self.respawn()
        
        if self.delay_attack < 0 and self.attacking:
            self.w -= 4
            self.v -= 24
            self.attacking = False
        else:
            self.delay_attack -= 1
        
        
            
        
        
    def hitbox_player(self):
        return [self.x,self.x + self.w,self.y,self.y + self.h]
    def hitbox_projectile(self):
        hit = []
        for proj in self.projectile:
            hit.append([proj[X],6 + proj[X] ,proj[Y],proj[Y] + 3,proj[3]])
        return hit
        
        
        
player1 = Player(80,20,16,8,
                 [pyxel.KEY_LEFT,pyxel.KEY_RIGHT,pyxel.KEY_UP,pyxel.KEY_DOWN,pyxel.KEY_CTRL],
                 [pyxel.GAMEPAD1_BUTTON_DPAD_LEFT,pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT,pyxel.GAMEPAD1_BUTTON_B,pyxel.GAMEPAD1_BUTTON_A,pyxel.GAMEPAD1_BUTTON_X],
                 0,16,56,11)     
        
player2 = Player(40,20,16,8,[pyxel.KEY_Q,pyxel.KEY_D,pyxel.KEY_Z,pyxel.KEY_S,pyxel.KEY_A],
                 [pyxel.GAMEPAD2_BUTTON_DPAD_LEFT,pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT,pyxel.GAMEPAD2_BUTTON_B,pyxel.GAMEPAD2_BUTTON_A,pyxel.GAMEPAD2_BUTTON_X],
                 0,64,49,11)     




def combat():
    # vérifi si les joueur son en colition et s'attaque
    if hitbox(player1.hitbox_player(),player2.hitbox_player()):
        if player1.attacking:
            player2.degat(player1.sens,10)
            pyxel.play(0,2)
    if hitbox(player2.hitbox_player(),player1.hitbox_player()):
        if player2.attacking:
            player1.degat(player2.sens,10)
            pyxel.play(0,2)
    les_proj = player1.hitbox_projectile()
    for proj in les_proj:

        if hitbox(player2.hitbox_player(),proj,teste=True):

            player2.degat(proj[4],5)
            pyxel.play(0,3)
            player1.projectile.pop()
            
    les_proj = player2.hitbox_projectile()
    for proj in les_proj:
        if hitbox(player1.hitbox_player(),proj,teste=True):
            player1.degat(proj[4],5)
            pyxel.play(0,3)
            player2.projectile.pop()
    
def relancer():
    global menu
    pyxel.text(25,HAUTEUR//2, "Appuyer sur [ESPACE]",7)
    if pyxel.btnp(pyxel.KEY_SPACE):
            menu = False
            player1.pv = 3
            player2.pv = 3

def update():
    if pyxel.frame_count % 1 == 0:
        player1.player_run()
        player2.player_run()
        combat()
        

def draw():
    
    if not menu:
        if player1.pv <= 0:
            pyxel.cls(0)
            pyxel.text(25,HAUTEUR//3, "elepha win",7)
            relancer()
        elif player2.pv <= 0:
            pyxel.cls(0)
            pyxel.text(25,HAUTEUR//3, "robot win",7)
            relancer()
        else:
            pyxel.cls(0)
            pyxel.bltm(X,Y,0,0,0,128,128)
            player1.draw()
            player2.draw()
            pyxel.text(1/3*LARGEUR,116,str(player1.pourcent)+"%",3)
            pyxel.text(2/3*LARGEUR-12,116,str(player2.pourcent)+"%",8)

    else:
        relancer()
        
            



pyxel.run(update,draw)


