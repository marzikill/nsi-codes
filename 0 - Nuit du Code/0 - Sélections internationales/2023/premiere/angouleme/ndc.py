# Nuit du c0de 2023

import pyxel as pxl
import random

WINDOW_WIDTH = 192
WINDOW_HEIGHT = 128

class Player():
    def __init__(self,x,y,team):
        
        self.team = team #blue or red
        
        if self.team == "blue":
            self.x = 25
        elif self.team == "red":
            self.x = WINDOW_WIDTH - 3 - 6 - 25
        
        self.y = WINDOW_HEIGHT//2 
        
        self.w = 6
        self.h = 16
        
        self.u = 0
        self.v = 0
        
        self.velocity = 1
        
        self.score = 0
        self.state = 0
        
        if self.team == "blue":
            self.orientation_left = False
        elif self.team == "red":
            self.orientation_left = True
        
        self.boost = False
        self.boost_wait_time = 90 #frames
        self.boost_duration = 120 #frames
        self.boost_last_use = 100000 #frames
        ## controls
        if self.team == "red":
            self.ctrl_left = pxl.KEY_LEFT
            self.ctrl_right = pxl.KEY_RIGHT
            self.ctrl_up = pxl.KEY_UP
            self.ctrl_down = pxl.KEY_DOWN
            self.ctrl_competence = pxl.KEY_SPACE
        if self.team == "blue":
            self.ctrl_left = pxl.KEY_Q
            self.ctrl_right = pxl.KEY_D
            self.ctrl_up = pxl.KEY_Z
            self.ctrl_down = pxl.KEY_S
            self.ctrl_competence = pxl.KEY_W
    
    def controls(self):
        if pxl.btn(self.ctrl_left) and self.x > 3:
            self.orientation_left = True
            self.x -= self.velocity
            
        if pxl.btn(self.ctrl_right) and self.x + self.w < WINDOW_WIDTH - 3:
            self.orientation_left = False
            self.x += self.velocity
            
        if pxl.btn(self.ctrl_up) and self.y > 8:
            self.y -= self.velocity
            
        if pxl.btn(self.ctrl_down) and self.y + self.h < WINDOW_HEIGHT - 8:
            self.y += self.velocity
    
    def orientation(self):
        if self.orientation_left == True:
            if self.team == "blue":
                self.u = 8
            elif self.team == "red":
                self.u = 24
        else:
            if self.team == "blue":
                self.u = 0
            elif self.team == "red":
                self.u = 16
            
    
    def grow(self):
        
        if self.team == "blue": 
            if self.score >= 0:
                self.u = 0
                self.v = 10
                self.w = 7
                self.h = 15
            if self.score >= 4:
                self.u = 0 
                self.v = 26
                self.w = 7
                self.h = 15   
            if self.score >= 8:
                self.u = 0 
                self.v = 42
                self.w = 8
                self.h = 15
            if self.score >= 12:
                self.u = 0 
                self.v = 58
                self.w = 8
                self.h = 15
            if self.score >= 16:
                self.u = 0 
                self.v = 73
                self.w = 8
                self.h = 15
            if self.score >= 20:
                self.u = 0 
                self.v = 89
                self.w = 8
                self.h = 15
            if self.score >= 24:
                self.u = 0 
                self.v = 104
                self.w = 8
                self.h = 16
            if self.score > 24:
                self.u = 0
                self.v = 232
                self.w = 16
                self.h = 16
        
        if self.team == "red":
            if self.score >= 0:
                self.u = 16
                self.v = 10
                self.w = 7
                self.h = 15
            if self.score >= 4:
                self.u = 16 
                self.v = 26
                self.w = 7
                self.h = 15   
            if self.score >= 8:
                self.u = 16 
                self.v = 42
                self.w = 8
                self.h = 15
            if self.score >= 12:
                self.u = 16 
                self.v = 58
                self.w = 8
                self.h = 15
            if self.score >= 16:
                self.u = 16 
                self.v = 73
                self.w = 8
                self.h = 15
            if self.score >= 20:
                self.u = 16 
                self.v = 89
                self.w = 8
                self.h = 15
            if self.score >= 24:
                self.u = 16 
                self.v = 104
                self.w = 8
                self.h = 16
            if self.score > 24:
                self.u = 16
                self.v = 232
                self.w = 16
                self.h = 16
            
    def isBoost(self):
        if pxl.btn(self.ctrl_competence) and self.boost == False:
            self.velocity = 2
        else:
            self.velocity = 1


    def update(self):
        self.controls()
        self.isBoost()
        self.grow()
        self.orientation()
    
    def draw(self):
        pxl.blt(self.x, self.y,0,self.u,self.v,self.w,self.h,0)

class Food():
    def __init__(self):
        
        self.seed = random.randint(0,4)
        self.lu = [41,32,40,42,32]
        self.lv = [17,2,8,0,11]
        self.lw = [6,8,8,6,8]
        self.lh = [7,6,8,8,5]
        
        self.w = self.lw[self.seed]
        self.h = self.lh[self.seed]
        
        self.x = random.randint(3,WINDOW_WIDTH - self.w - 3)
        self.y = random.randint(16,WINDOW_HEIGHT - self.h - 8)
        

        
        self.u = self.lu[self.seed]
        self.v = self.lv[self.seed]
        
    def reset(self):
        self.x = random.randint(3,WINDOW_WIDTH - self.w - 3)
        self.y = random.randint(16,WINDOW_HEIGHT - self.h - 8)
        self.seed = random.randint(0,4)
        
    
    def update(self):
        pass
    
    def draw(self):
        pxl.blt(self.x,self.y,0,self.u,self.v,self.w,self.h,0)

class Game():
    def __init__(self):
        
        pxl.init(192,128, "BEAT EAT")
        pxl.load("theme.pyxres")
        
        self.player1 = Player(0,0,"blue")
        self.player2 = Player(15,15,"red")
        self.moove = True
        self.nb_food = 7
        self.foods = []
        self.generateFood()
        
        pxl.run(self.draw,self.update)
        
    def generateFood(self):
        for i in range(self.nb_food):
            self.foods.append(Food())
            
    def isEat(self):
        for f in self.foods:
            if self.player1.x + self.player1.w > f.x and self.player1.x < f.x + f.w and self.player1.y + self.player1.h > f.y and self.player1.y < f.y + f.h:
            
                self.player1.score += 1
                f.reset()
            
            if self.player2.x + self.player2.w > f.x and self.player2.x < f.x + f.w and self.player2.y + self.player2.h > f.y and self.player2.y < f.y + f.h:
            
                self.player2.score += 1
                f.reset()
            
                
    def update(self):
        if self.moove == True:
            self.player1.update()
            self.player2.update()
            for f in self.foods:
                f.update()
            self.isEat()
    
    def draw(self):
        pxl.cls(0)
        pxl.bltm(0,0,0,0,0,WINDOW_WIDTH,WINDOW_HEIGHT)
        for f in self.foods:
            f.draw()
        
        self.player1.draw()
        self.player2.draw()
        
        pxl.text(5,WINDOW_HEIGHT//2,str(self.player1.score),1)
        pxl.text(WINDOW_WIDTH-10,WINDOW_HEIGHT//2,str(self.player2.score),8)
        
        if self.player1.score > 24:
            self.moove = False
            pxl.cls(6)
            self.player1.u = 0
            self.player1.v = 232
            self.player1.w = 16
            self.player1.h = 16
            self.player1.draw()
            pxl.text(WINDOW_WIDTH//2,WINDOW_HEIGHT//2,"BLUE WIN",7)
        if self.player2.score > 24:
            self.moove = False
            pxl.cls(8)
            self.player2.u = 16
            self.player2.v = 232
            self.player2.w = 16
            self.player2.h = 16
            self.player2.draw()
            pxl.text(WINDOW_WIDTH//2,WINDOW_HEIGHT//2,"RED WIN",7)
        
Game()