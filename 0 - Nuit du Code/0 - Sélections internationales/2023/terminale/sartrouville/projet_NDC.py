import pyxel

OBJ= {
    "murs": [(40,72), (48,72), (40,80), (48,80)]
}

class App:
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.x = 16
        self.y = 16
        self.level= 1
        pyxel.load ("5.pyxres")
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.deplacement()
        self.colli_mur()
        self.clef()
        
    def draw(self):
        pyxel.cls(1)
        if self.level==1:
            pyxel.bltm(0,0,0,0,0,128,128,5)
        if self.level==2:
            pyxel.bltm(0,0,0,128,0,128,128,5)
        if self.level==3:
            pyxel.bltm(0,0,0,256,0,128,128,5)
        pyxel.blt(self.x, self.y, 0, 144, 48,8,8,5)
        pyxel.rect(self.x+18,self.y-500,1000,1000,0)
        pyxel.rect(self.x-1010,self.y-500,1000,1000,0)
        pyxel.rect(self.x-500,self.y-1010,1000,1000,0)
        pyxel.rect(self.x-500,self.y+18,1000,1000,0)

    def debug(self):
        self.x=16
        self.y=16
        
    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
           # if self.x <= 119:
           self.x=self.x+1
        if pyxel.btn(pyxel.KEY_LEFT):
            #if self.x >= 1:
            self.x=self.x-1   
        if pyxel.btn(pyxel.KEY_DOWN):
            #if self.y <= 119:
            self.y=self.y+1  
        if pyxel.btn(pyxel.KEY_UP):
            #if self.y >= 1:
            self.y=self.y-1  
                

    def colli_mur(self):
        for j in range(8):
            if pyxel.btn(pyxel.KEY_RIGHT)== True and pyxel.pget(self.x + 7,self.y + j)==4:
                self.x=self.x-1
            if pyxel.btn(pyxel.KEY_LEFT)== True and pyxel.pget(self.x,self.y + j)==4:
                self.x=self.x+1
            elif pyxel.btn(pyxel.KEY_UP)== True and pyxel.pget(self.x + j,self.y)==0:
                self.y=self.y+1
            elif pyxel.btn(pyxel.KEY_DOWN)== True and pyxel.pget(self.x + j,self.y + 7)==9:
                self.y=self.y-1

        
    def clef(self):
        if self.y>=60  and self.y<=80 and self.level==1:
            if self.x>=110  and self.x<=113:
                self.level=2
                self.x=16
                self.y=108
                
        if self.y>=90  and self.y<=97 and self.level==2:
            if self.x>=96  and self.x<=108:
                self.level=3
                self.x=24
                self.y=64
        
App()