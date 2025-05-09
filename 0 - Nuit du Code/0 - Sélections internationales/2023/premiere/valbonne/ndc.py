import pyxel
import math
pyxel.init(128,128,"NDC 2023",fps=60)
pyxel.load("theme.pyxres")
pyxel.bltm(0,0,0,0,0,16,16)
"""" Variables """
isPlaying = 0
driveMode = False
drag = 0.01
missile_list = []
tankHitCoolDown = 0

class Tank:
    def __init__(self,controls_zqsd:bool,pos_x:float,pos_y:float,direction:int,hp:int,mass:float,acceleration:int,traction:int,max_speed:float):
        """Creates a tank"""
        self.controls_zqsd = controls_zqsd

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lenght = 16
        self.speed_x = 0
        self.speed_y = 0
        self.direction = direction

        self.missile_cooldown = 0

        self.hp = hp
        self.mass = mass
        self.acceleration = acceleration
        self.traction = traction

    def move(self):
        """moves the tank"""
        if driveMode :
            if self.controls_zqsd : 
                if pyxel.btn(pyxel.KEY_Z):
                    
                    self.speed_x += math.cos(self.direction*math.pi/4)*self.acceleration
                    self.speed_y += math.sin(self.direction*math.pi/4)*self.acceleration
                if pyxel.btn(pyxel.KEY_S):
                    self.speed_x -= math.cos(self.direction*math.pi/4)*self.acceleration
                    self.speed_y -= math.sin(self.direction*math.pi/4)*self.acceleration
                if pyxel.btnp(pyxel.KEY_Q):
                    self.direction -= 1
                if pyxel.btnp(pyxel.KEY_D):
                    self.direction += 1
                if abs(self.direction) == 8:
                    self.direction = 0
                if self.direction < 0:
                    self.direction += 8
            else:
                if pyxel.btn(pyxel.KEY_KP_8):
                    self.speed_x += math.cos(self.direction*math.pi/4)*self.acceleration
                    self.speed_y += math.sin(self.direction*math.pi/4)*self.acceleration
                if pyxel.btn(pyxel.KEY_KP_2):
                    self.speed_x -= math.cos(self.direction*math.pi/4)*self.acceleration
                    self.speed_y -= math.sin(self.direction*math.pi/4)*self.acceleration
                
                if pyxel.btnp(pyxel.KEY_KP_4):
                    self.direction -= 1
                if pyxel.btnp(pyxel.KEY_KP_6):
                    self.direction += 1
                if abs(self.direction) == 8:
                    self.direction = 0
                if self.direction < 0:
                    self.direction += 8
        else :
            if self.controls_zqsd : 
                if pyxel.btn(pyxel.KEY_Z): 
                    self.speed_y -= self.acceleration
                if pyxel.btn(pyxel.KEY_S):
                    self.speed_y += self.acceleration
                if pyxel.btn(pyxel.KEY_Q):
                    self.speed_x -= self.acceleration
                if pyxel.btn(pyxel.KEY_D):
                    self.speed_x += self.acceleration
                if pyxel.btn(pyxel.KEY_E): 
                    self.speed_y -= self.acceleration
                    self.speed_x += self.acceleration
                if pyxel.btn(pyxel.KEY_A): 
                    self.speed_y -= self.acceleration
                    self.speed_x -= self.acceleration
                if pyxel.btn(pyxel.KEY_W): 
                    self.speed_y += self.acceleration
                    self.speed_x -= self.acceleration
                if pyxel.btn(pyxel.KEY_C): 
                    self.speed_y += self.acceleration
                    self.speed_x += self.acceleration

                if pyxel.btn(pyxel.KEY_Z): 
                        self.direction = 6
                if pyxel.btn(pyxel.KEY_E) or pyxel.btn(pyxel.KEY_Z) and pyxel.btn(pyxel.KEY_D): 
                    self.direction = 7
                if pyxel.btn(pyxel.KEY_A)or pyxel.btn(pyxel.KEY_Z) and pyxel.btn(pyxel.KEY_Q) : 
                    self.direction = 5
                if pyxel.btn(pyxel.KEY_S):
                    self.direction = 2
                if pyxel.btn(pyxel.KEY_C)or pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_D): 
                    self.direction = 1
                if pyxel.btn(pyxel.KEY_W)or pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_Q): 
                    self.direction = 3
                if pyxel.btn(pyxel.KEY_Q):
                    self.direction = 4
                if pyxel.btn(pyxel.KEY_D):
                    self.direction = 0
            
            else:
                if pyxel.btn(pyxel.KEY_KP_8): 
                    self.speed_y -= self.acceleration
                if pyxel.btn(pyxel.KEY_KP_5):
                    self.speed_y += self.acceleration
                if pyxel.btn(pyxel.KEY_KP_4):
                    self.speed_x -= self.acceleration
                if pyxel.btn(pyxel.KEY_KP_6):
                    self.speed_x += self.acceleration
                if pyxel.btn(pyxel.KEY_KP_9)or pyxel.btn(pyxel.KEY_KP_6) and pyxel.btn(pyxel.KEY_KP_8): 
                    self.speed_y -= self.acceleration
                    self.speed_x += self.acceleration
                if pyxel.btn(pyxel.KEY_KP_7)or pyxel.btn(pyxel.KEY_KP_4) and pyxel.btn(pyxel.KEY_KP_8): 
                    self.speed_y -= self.acceleration
                    self.speed_x -= self.acceleration
                if pyxel.btn(pyxel.KEY_KP_1)or pyxel.btn(pyxel.KEY_KP_4) and pyxel.btn(pyxel.KEY_KP_2): 
                    self.speed_y += self.acceleration
                    self.speed_x -= self.acceleration
                if pyxel.btn(pyxel.KEY_KP_3)or pyxel.btn(pyxel.KEY_KP_6) and pyxel.btn(pyxel.KEY_KP_2): 
                    self.speed_y += self.acceleration
                    self.speed_x += self.acceleration

                if pyxel.btn(pyxel.KEY_KP_8): 
                        self.direction = 6
                if pyxel.btn(pyxel.KEY_KP_9): 
                    self.direction = 7
                if pyxel.btn(pyxel.KEY_KP_7) : 
                    self.direction = 5
                if pyxel.btn(pyxel.KEY_KP_5):
                    self.direction = 2
                if pyxel.btn(pyxel.KEY_KP_3): 
                    self.direction = 1
                if pyxel.btn(pyxel.KEY_KP_1): 
                    self.direction = 3
                if pyxel.btn(pyxel.KEY_KP_4):
                    self.direction = 4
                if pyxel.btn(pyxel.KEY_KP_6):
                    self.direction = 0

        if self.speed_x > 0:
            self.speed_x -= drag
        elif self.speed_x < 0:
            self.speed_x += drag
        if self.speed_y > 0:
            self.speed_y -= drag
        elif self.speed_y < 0:
            self.speed_y += drag
        if abs(self.speed_x) < drag:
            self.speed_x = 0
        if abs(self.speed_y) < drag:
            self.speed_y = 0
            
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.controls_zqsd:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.shoot()
        else:
            if pyxel.btnp(pyxel.KEY_KP_0):
                self.shoot()
        self.missile_cooldown -= 1
        
    def shoot(self):
        """WIP"""
        global missile_list
        if self.missile_cooldown <= 0:
            if self.direction == 0 or self.direction == 4:
                missile_list.append(Missile(self.pos_x+8,self.pos_y+8,0.5,self.direction,self.controls_zqsd))
            elif self.direction == 2 or self.direction == 6:
                missile_list.append(Missile(self.pos_x+8,self.pos_y+8,0.5,self.direction,self.controls_zqsd))
            else:
                missile_list.append(Missile(self.pos_x+8,self.pos_y+8,0.5,self.direction,self.controls_zqsd))
            self.missile_cooldown = 30

    def draw(self):
        """Valentin stuff"""
        if self.controls_zqsd:
            if self.direction == 0:
                pyxel.blt(self.pos_x,self.pos_y,0,16,0,16,16,0) #si le tank va vers la droite
            elif self.direction == 1:
                """"bas droite"""
                pyxel.blt(self.pos_x,self.pos_y,0,32,0,-16,-16,0)
            elif self.direction == 2:
                """bas"""
                pyxel.blt(self.pos_x,self.pos_y,0,0,0,16,-16,0)
            elif self.direction == 3:
                """bas gauche"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,32,0,16,-16,0)#marche
            elif self.direction == 4:
                """gauche"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,16,0,-16,16,0)
            elif self.direction == 5:
                """gauche haut"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,32,0,16,16,0)
            elif self.direction == 6:
                """haut"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,0,0,16,16,0)
            elif self.direction == 7:
                """droite haut"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,32,0,-16,16,0)
        else:
            if self.direction == 0:
                pyxel.blt(self.pos_x,self.pos_y,0,16,16,16,16,0) #si le tank va vers la droite
            elif self.direction == 1:
                """"bas droite"""
                pyxel.blt(self.pos_x,self.pos_y,0,32,16,-16,-16,0)
            elif self.direction == 2:
                """bas"""
                pyxel.blt(self.pos_x,self.pos_y,0,0,16,16,-16,0)
            elif self.direction == 3:
                """bas gauche"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,32,16,16,-16,0)#marche
            elif self.direction == 4:
                """gauche"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,16,16,-16,16,0)
            elif self.direction == 5:
                """gauche haut"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,32,16,16,16,0)
            elif self.direction == 6:
                """haut"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,0,16,16,16,0)
            elif self.direction == 7:
                """droite haut"""""""""
                pyxel.blt(self.pos_x,self.pos_y,0,32,16,-16,16,0)
            
    def damage(self,direction):
        self.hp -= 1
        if direction ==0:
            self.speed_x += self.mass
        elif direction == 1:
            self.speed_x += self.mass
            self.speed_y += self.mass
        elif direction == 2:
            self.speed_y += self.mass
        elif direction == 3:
            self.speed_x -= self.mass
            self.speed_y += self.mass
        elif direction == 4:
            self.speed_x -= self.mass
        elif direction == 5:
            self.speed_x -= self.mass
            self.speed_y -= self.mass
        elif direction == 6:
            self.speed_y -= self.mass
        elif direction == 7:
            self.speed_x += self.mass

        
    def fall(self):
        global isPlaying
        if self.pos_x+8 < 4 or self.pos_x+8 >124 or self.pos_y+8 < 4 or self.pos_y+8 >124 or self.hp <=0:
            if self.controls_zqsd :
                pyxel.text(40,60,"Player 2 wins",8)
            else:
                pyxel.text(40,60,"Player 1 wins",3)
            isPlaying = 2

    """ def collide(self):
        global tankHitCoolDown
        if not self.controls_zqsd and pyxel.pget(self.pos_x,self.pos_y) == 11 :
            if tankHitCoolDown <=0:
                player1.damage(self.direction)
                player2.damage(self.direction)
                tankHitCoolDown = 60
        if self.controls_zqsd and pyxel.pget(self.pos_x,self.pos_y) == 14:
            if tankHitCoolDown <=0:
                player1.damage(self.direction)
                player2.damage(self.direction)
                tankHitCoolDown = 60"""

class Missile:
    def __init__(self,pos_x:float,pos_y:float,speed:float,direction:int,greenTeam:bool):
        """Creates a Missile"""
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = math.cos(direction*math.pi/4)*speed
        self.speed_y = math.sin(direction*math.pi/4)*speed
        self.direction = direction
        self.greenTeam = greenTeam
        self.delete = False
        self.explosionCount = 0
        self.isColliding = bool

    def collide(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        
        #print(self.greenTeam,pyxel.pget(self.pos_x,self.pos_y))
        if not self.greenTeam and pyxel.pget(self.pos_x,self.pos_y) == 11 :
            self.isColliding = True
            player1.damage(self.direction)
            self.delete = True
        elif self.greenTeam and pyxel.pget(self.pos_x,self.pos_y) == 14 :
            self.isColliding = True
            player2.damage(self.direction)
            self.delete = True
            """"""""""""
        if not -10<self.pos_x<140 and not -10<self.pos_y<140:
            self.delete = True
        

    def draw(self):
        if self.direction == 0:
            pyxel.blt(self.pos_x,self.pos_y,0,0,52,7,1,0) 
        elif self.direction == 1:
            """"bas droite"""
            pyxel.blt(self.pos_x,self.pos_y,0,16,48,8,-8,0)
        elif self.direction == 2:
            """bas"""
            pyxel.blt(self.pos_x,self.pos_y,0,12,49,1,-7,0)
        elif self.direction == 3:
            """bas gauche"""""""""
            pyxel.blt(self.pos_x,self.pos_y,0,16,48,-8,-8,0)
        elif self.direction == 4:
            """gauche"""""""""
            pyxel.blt(self.pos_x,self.pos_y,0,0,52,-7,1,0)
        elif self.direction == 5:
            """gauche haut"""""""""
            pyxel.blt(self.pos_x,self.pos_y,0,16,48,8,-8,0)
        elif self.direction == 6:
            """haut"""""""""
            pyxel.blt(self.pos_x,self.pos_y,0,12,49,1,7,0)
        elif self.direction == 7:
            """droite haut"""""""""
            pyxel.blt(self.pos_x,self.pos_y,0,16,48,8,8,0)
        if self.isColliding == True:
            print("colliding")
            self.explosionCount += 1
            if self.explosionCount <= 20:
                pyxel.circ(self.pos_x,self.pos_y,4,10)
            elif self.explosionCount <= 35:
                pyxel.circ(self.pos_x,self.pos_y,6,9)
            elif self.explosionCount <= 45:
                pyxel.circb(self.pos_x,self.pos_y,8,8)
        if self.explosionCount == 60:
            self.explosionCount = 0
            self.isColliding = False
    
pyxel.load("theme.pyxres")
    
player1 = Tank(True,8,8,0,10,0.7,0.03,0.1,5)
player2 = Tank(False,104,104,4,10,0.7,0.03,0.1,5)

def update():
    """"The update thing"""
    global isPlaying
    global missile_list
    global tankHitCoolDown
    global player1
    global player2 
    global driveMode
    tankHitCoolDown -= 1
    if isPlaying == 1:
        player1.move()
        player2.move()
        for m in missile_list:
            m.collide()
        for m in missile_list:
            if m.delete:
                missile_list.remove(m)
        if (player1.pos_x+8-player2.pos_x-8)**2+(player1.pos_y+8-player2.pos_y-8)**2 < 36 and tankHitCoolDown < 0:
            player1.damage(player2.direction)
            player2.damage(player1.direction)
            tankHitCoolDown = 60
    elif isPlaying == 0:
        if 52<pyxel.mouse_x<76 and 70<pyxel.mouse_y<86 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            isPlaying = 1
        if 30<pyxel.mouse_x<76 and 50<pyxel.mouse_y<56 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if driveMode:
                driveMode = False
            else:
                driveMode = True
    if isPlaying == 2 and pyxel.btnp(pyxel.KEY_R):
        player1 = Tank(True,8,8,0,10,0.7,0.03,0.1,5)
        player2 = Tank(False,104,104,4,10,0.7,0.03,0.1,5)
        isPlaying = 0



def draw():
    """we drawin"""
    
    global isPlaying
    global missile_list
    global driveMode
    pyxel.cls(6)
    pyxel.bltm(0,0,0,0,0,128,128)
    if isPlaying == 0:
        """Draw the button"""
        pyxel.blt(52,70,0,32,48,24,16,0)
        pyxel.mouse(True)
        pyxel.text(40,20,'Tanks on ice',0)
        if driveMode:
            """the Samuel one"""""""""
            pyxel.blt(30,50,0,32,72,56,8)
        else:
            """the Nolhan one"""""""""
            pyxel.blt(44,50,0,32,64,40,8)
            
    if isPlaying == 1:#les barres de vie
        pyxel.blt(0,0,0,32,80,22,8)
        pyxel.rect(1,1,player1.hp*2,6,3)
        pyxel.blt(106,0,0,32,80,22,8)
        pyxel.rect(127-player2.hp*2,1,player2.hp*2,6,8)
    if isPlaying < 2:
        for m in missile_list:
            m.draw()
        player1.fall()
        player1.draw()
        player2.fall()
        player2.draw()
    else:
        player1.fall()
        player2.fall()
    if isPlaying > 0:
        pyxel.mouse(False)
    if isPlaying == 2:
        pyxel.text(30,100,'Press R to replay',0)
    

pyxel.playm(0,loop=True)
pyxel.run(update,draw)