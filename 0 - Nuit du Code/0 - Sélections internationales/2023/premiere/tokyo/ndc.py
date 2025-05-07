# Nuit du c0de 2023

import pyxel as p
import random as r

p.init(128, 128)
p.load("4.pyxres")

player_y = 60
can_destroy = True

rectangles_width = []   # type = 1
rectangles_length = []   # type = 2
squares = []    # type = 3
speed = 1

level = 1
score = 0

p.playm(0)

def player_movement(y):
    if p.btn(p.KEY_DOWN) and y < 120:
        y += 1
    elif p.btn(p.KEY_UP) and y > 0:
        y -= 1
    
    return y

def player_powers(can_destroy):
    if p.frame_count % 90 == 0 and not(can_destroy):
        can_destroy = True
        
    if can_destroy:
        if p.btn(p.KEY_A):
            rectangles_width.clear()
            can_destroy = False
        elif p.btn(p.KEY_S):
            rectangles_length.clear()
            can_destroy = False
        elif p.btn(p.KEY_D):
            squares.clear()
            can_destroy = False
            
        return can_destroy
            
def player_hitbox():
    # Rectangle width
    for rectangle in rectangles_width:
        if player_y < rectangle[1] + 8 and player_y + 8 > rectangle[1] and rectangle[0] < 8:
            p.quit()
    
    # Rectangle length
    for rectangle in rectangles_length:
        if player_y < rectangle[1] + 16 and player_y + 8 > rectangle[1] and rectangle[0] < 8:
            p.quit()
            
    # Square
    for square in squares:
        if player_y < square[1] + 16 and player_y + 8 > square[1] and square[0] < 8:
            p.quit()

def rectangle_movement(rectangle):
    rectangle[0] -= speed
    return rectangle

def rectangle_spawn():
    # Pos y
    y = 1
    while not(y % 8 == 0):
        y = r.randint(0, 120)
    
    # What to spawn
    spawn_which = r.randint(1, 3)
    if spawn_which == 1:
        rectangles_width.append([128, y])
    elif spawn_which == 2:
        rectangles_length.append([128, y])
    elif spawn_which == 3:
        squares.append([128, y])

def rectangle_delete(rectangle, rectangle_type):
    if rectangle[0] <= -16:
        if rectangle_type == 1:
            rectangles_width.remove(rectangle)
        elif rectangle_type == 2:
            rectangles_length.remove(rectangle)
        elif rectangle_type == 3:
            squares.remove(rectangle)

def update():
    global player_y, can_destroy, speed, score, level
    
    #Player
    player_y = player_movement(player_y)
    
    player_hitbox()
    
    can_destroy = player_powers(can_destroy)
    
    # Rectangles_width
    for rectangle in rectangles_width:
        rectangle = rectangle_movement(rectangle)
        rectangle_delete(rectangle, 1)
    
    # Rectangles_length
    for rectangle in rectangles_length:
        rectangle = rectangle_movement(rectangle)
        rectangle_delete(rectangle, 2)
        
    # Squares
    for square in squares:
        square = rectangle_movement(square)
        rectangle_delete(square, 3)
    
    # Spawn
    if p.frame_count % 16 == 0:
        rectangle_spawn()
        rectangle_spawn()
        rectangle_spawn()
        rectangle_spawn()
        
    # Score
    if p.frame_count % 30 == 0:
        score += 1
        if score % 10 == 0:
            speed += .25
            level += 1
            p.playm(r.randint(0, 5))

def make_brick(x, y):
    p.blt(x, y, 0, 40, 40, 8, 8)
   
def draw():
    p.cls(5)
    
    # Player
    p.blt(0, player_y, 0, 0, 72, 8, 8)
    
    # Rectangle width
    for rectangle in rectangles_width:
        make_brick(rectangle[0], rectangle[1])
        make_brick(rectangle[0] + 8, rectangle[1])
    
    # Rectangle length
    for rectangle in rectangles_length:
        make_brick(rectangle[0], rectangle[1])
        make_brick(rectangle[0], rectangle[1] + 8)
    
    # Square
    for square in squares:
        make_brick(square[0], square[1])
        make_brick(square[0] + 8, square[1])
        make_brick(square[0], square[1] + 8)
        make_brick(square[0] + 8, square[1] + 8)
        
    # Score
    p.text(0, 0, "Score:" + str(score), 7)
    p.text(100, 0, "Level:" + str(level), 7)

p.run(update, draw)