# Nuit du c0de 2023

import pyxel
import random
import time

class Game:
    def __init__(self):
        pyxel.init(128,128, title='NDC 2023')
        pyxel.load('2.pyxres')
        pyxel.playm(0, loop=True)
        self.player = Player(self)
        
        self.timer = 30
        
        self.game_over = False
        
        
        self.game_objects = {'key' : (11,5), 'door' : (10,6), 'diamond' : (4,3)}
        self.solid_blocks = [(7,5), (2,5), (0,8), (0,7), (0,6), (0,5), (1,5),(3,5),(8,5),(9,5),(9,6),(10,5),(8,7)]
        self.current_level = 0
        self.all_levels = [Level(self,0,x,0,128,128) for x in range(0,256,16)]
        
        
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.player.update()
        if pyxel.frame_count % 30 == 0:
            self.timer -= 1
            if self.timer < 0:
                self.game_over = True
            
    
    def draw(self):
        if not self.game_over:
            pyxel.cls(4)
            self.all_levels[self.current_level].draw()
            self.player.draw()
            pyxel.text(0,0,'level : ' + str(self.current_level),7)
            pyxel.text(80,0,'timer : ' + str(self.timer),7)
        else:
            pyxel.text(42,50, 'GAME OVER', 7)
    
class Player:
    def __init__(self, game):
        self.game = game
        self.x = 8
        self.y = 112
        
        self.speed = 2
        self.sprites = [(0,24,16,8,8)]
        self.current_sprite = 0
        self.col_key = 2
        
        self.got_key = False
        
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move_right()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.move_left()
        if pyxel.btn(pyxel.KEY_DOWN):
            self.move_down()
        if pyxel.btn(pyxel.KEY_UP):
            self.move_up()
            
        self.check_key_collision()
        self.check_door_collision()
        self.check_diamond_collision()
    
    def draw(self):
        img, u, v, w, h = self.sprites[self.current_sprite]
        pyxel.blt(self.x, self.y, img, u, v, w, h,self.col_key)
        
        
    def move_up(self):
        self.y -= self.speed
        if self.check_collision():
            self.move_down()
            
    def move_down(self):
        self.y += self.speed
        if self.check_collision():
            self.move_up()
        
    def move_right(self):
        self.x += self.speed
        if self.check_collision():
            self.move_left()
        
    def move_left(self):
        self.x -= self.speed
        if self.check_collision():
            self.move_right()
        
    def check_collision(self):
        tile_x = (self.x + 4) // 8
        tile_y = (self.y + 4) // 8
        
        grid = self.game.all_levels[self.game.current_level]
        
        return grid.is_solid(tile_x, tile_y)
        
    def check_key_collision(self):
        tile_x = (self.x + 4) // 8
        tile_y = (self.y + 4) // 8
        grid = self.game.all_levels[self.game.current_level]
        if grid.get_tile(tile_x, tile_y) == self.game.game_objects['key']:
            grid.remove_tile(tile_x, tile_y)
            self.got_key = True
            
    def check_door_collision(self):
        tile_x = (self.x + 4) // 8
        tile_y = (self.y + 4) // 8
        grid = self.game.all_levels[self.game.current_level]
        if grid.get_tile(tile_x, tile_y) == self.game.game_objects['door'] and self.got_key:
            self.x = 8
            self.y = 112
            self.got_key = False
            self.game.current_level = (self.game.current_level + 1) % len(self.game.all_levels)
            self.game.timer = 30
            
            #self.game.current_level += 1
            #self.game.level_cleared()
            
    def check_diamond_collision(self):
        tile_x = (self.x + 4) // 8
        tile_y = (self.y + 4) // 8
        grid = self.game.all_levels[self.game.current_level]
        if grid.get_tile(tile_x, tile_y) == self.game.game_objects['diamond']:
            grid.remove_tile(tile_x, tile_y)
            
            #Rajouter du temps
            self.game.timer += 5
        
        
        
        
class Monster:
     def __init__(self):
         self.x = random.randint(50,127)
         self.y = random.randint(0 ,100)
            
    
class Level:
    def __init__(self,game, tm, u, v, w, h):
        self.game = game
        self.tm = tm
        self.u = u
        self.v = v 
        self.w = w
        self.h = h
        self.col_key = 2
        self.grid = [[pyxel.tilemap(tm).pget(i,j) for i in range(u, w + u)] for j in range(v, h)]
        
        

        
    def draw(self):
        pyxel.bltm(0,0, self.tm, self.u * 8,self.v * 8,self.w,self.h, self.col_key) # u est en pixels
        #pyxel.text(0,0,str(self.grid),7)
        
    def is_solid(self, i, j):
        """Renvoie True si la tuile de coordonnées (i,j) est solide """
        return self.grid[j][i] in self.game.solid_blocks
        
    def get_tile(self, i, j):
        """Renvoie la tuile aux coordonnées (i,j) """
        return self.grid[j][i]
        
    def remove_tile(self, i, j):
        """Efface la tuile de coordonnées (i,j) """
        self.grid[j][i] = (0,0)
        n = self.game.current_level
        pyxel.tilemap(self.tm).pset(i+n*16, j, (0,0))
        
    #def level_cleared(self):
        #Joue une musique 
       # pyxel.text(0, 50, 'Level cleared!!', 7)
    #   self.game.current_level = self.game.current_level + 1# % len(self.game.all_levels)
    #   self.game.player.x = 24
    #   self.game.player.y = 104
    #   self.game.player.got_key = False
    
Game()