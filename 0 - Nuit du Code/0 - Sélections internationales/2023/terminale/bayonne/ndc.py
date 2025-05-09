import pyxel as p

CST_TRANSPARENT = 5
CST_FPS = 60
CST_FRAME = 1/CST_FPS

CST_TERRAIN_SIZE = 255

class vec:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def dot(self, k):
        return vec(self.x * k, self.y * k)
    
    def sub(self, o):
        return vec(self.x - o.x, self.y - o.y)
    
    def add(self, o):
        return vec(self.x + o.x, self.y + o.y)
    
    def mul(self, o):
        return vec(self.x * o.x, self.y * o.y)
    
    def length(self):
        return p.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        return self.dot(1/self.length())
        
    def point_to(self, target):
        return target.sub(self).normalize()

vec_left = vec(-1, 0)
vec_right = vec(1, 0)
vec_up = vec(0, -1)
vec_down = vec(0, 1)

class rect:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = int(x), int(y), int(w), int(h)
        self.o_x, self.o_y = self.x, self.y
    
    def offset(self, v):
        self.x = self.o_x + int(v.x)
        self.y = self.o_y + int(v.y)

    def collision(self, o):
        return self.x < o.x + o.w and \
            self.x + self.w > o.x and \
            self.y < o.y + o.h and \
            self.y + self.h > o.y
    
    def copy(self):
        return rect(self.x, self.y, self.w, self.h)

null_rect = rect(0,0,0,0)

S_player = ((120,21,8,9), rect(0, 4, 8, 4))

S_pine_tree = ((69,89,10,11), null_rect)
S_big_tree = ((80,89,9,11), null_rect)
S_little_tree = ((95,90,4,9), null_rect)
S_grass1 = ((81,106,7,4), null_rect)
S_grass2 = ((90,106,9,3), null_rect)
S_grass3 = ((90,106,3,3), null_rect)


S_spider = ((119,63,9,9), rect(0, 4, 8, 4))
S_snake = ((129,64,8,8), rect(0, 4, 8, 4))
S_zombie = ((140,64,7,9), rect(0, 4, 8, 4))
S_skeleton = ((150,64,7,9), rect(0, 4, 8, 4))

S_heart = ((139,10,10,10), null_rect)
S_half_heart = ((149,11,10,10), null_rect)

S_wall_up = ((29,9,11,11), rect(0, 8, 11, 3))
S_wall_side = ((0,20,2,9), rect(0,0,2,9))
S_wall_upLeft = ((0,10,8,10), rect(0, 7, 8, 3))
S_wall_downLeft = ((0,29,10,11), rect(0, 2, 7, 8))
S_wall_upRight = ((50,9,10,11), rect(0, 8, 8, 3))
S_wall_downRight = ((49,29,11,11), rect(2, 2, 7, 8))

S_chest = ((30,101,9,9), null_rect)


p.init(128, 128, "NDC 2023", fps=CST_FPS)
p.load("5.pyxres")

class entity:
    def __init__(self, pos, base_speed, base_attack, base_life, sprite_info):
        self.pos = pos
        self.base_speed = float(base_speed)
        self.base_attack = float(base_attack)
        self.life = self.base_life = float(base_life)
        self.u, self.v, self.w, self.h = sprite_info[0]
        self.flip = False
        self.r = sprite_info[1].copy()
        self.r.offset(pos)
        
        self.base_timer = 0.5
        self.rem_timer = 0
        
    
    def ouch(self, damage):
        if self.rem_timer > 0:
            return
        self.rem_timer = self.base_timer
        print("aie ", damage)
        self.life -= damage
        if self.life <= 0:
            self.die()
    
    def move(self, dir):
        next_pos = self.pos.add(dir.dot(self.base_speed))
        
        if next_pos.x < 0 or next_pos.x > CST_TERRAIN_SIZE or next_pos.y < 0 or next_pos.y > CST_TERRAIN_SIZE:
            return
        
        self.r.offset(next_pos)
        
        for elem in colliders:
            if elem != self and self.r.collision(elem.r):
                if type(elem) == player and type(self) == enemy or type(self) == player and type(elem) == enemy:
                    continue
                self.r.offset(self.pos)
                return
        
        self.pos = next_pos
    
    def draw(self):
        self.w = -abs(self.w) if self.flip else abs(self.w)
        self.w = -abs(self.h) if self.flip else abs(self.h)
        p.blt(self.pos.x, self.pos.y, 0, self.u, self.v, self.w, self.h, CST_TRANSPARENT)
    
    def update(self):
        pass
    
    def die(self):
        pass
    
class slash:
    def __init__(self, pos, direction, damage):
        self.pos = pos
        self.box = rect(pos.x,pos.y,4,10)
        self.live_time = 10
        self.r = null_rect
        self.damage = damage
        self.direction = direction
        
            
    def update(self):
        self.live_time -=1
        if self.live_time <= 0:
            remove_top(self)
            return
        
        if self.direction.x > 0:
            self.pos = global_player.pos.add(vec(-3,0))
        elif self.direction.x < 0:
            self.pos = global_player.pos.add(vec(11,0))
        self.box.x, self.box.y = self.pos.x, self.pos.y
        
        for elem in entities:
            if elem != global_player and elem.r.collision(self.box):
                elem.ouch(self.damage)
                
    def draw(self):
        p.rect(self.pos.x,self.pos.y,4,10,7)

class Object:
    def __init__(self, pos, sprite_info):
        self.pos = pos
        self.u, self.v,self.w,self.h = sprite_info[0]
        self.r = sprite_info[1].copy()
        self.r.offset(pos)
        
    def draw(self):
        p.blt(self.pos.x, self.pos.y, 0, self.u, self.v, self.w, self.h, CST_TRANSPARENT)

drawables = []
entities = []
colliders = []
tops = []

def _sort_(elem):
    return elem.pos.y
    
def y_sort():
    drawables.sort(key=_sort_)

def add_entity(e):
    entities.append(e)
    drawables.append(e)
    if e.r != null_rect:
        colliders.append(e)

def add_object(o):
    drawables.append(o)
    if o.r != null_rect:
        colliders.append(o)

def add_top(t):
    entities.append(t)
    tops.append(t)
        

def remove_entity(e):
    entities.remove(e)
    drawables.remove(e)
    if e in colliders:
        colliders.remove(e)

def remove_top(t):
    entities.remove(t)
    tops.remove(t)

def update():
    global difficulty
    if quit:
        if p.btn(p.KEY_T):
            p.quit()
        if p.btn(p.KEY_R):
            difficulty=0
            restart(False)
    for elem in entities:
        elem.update()
    
    for elem in colliders:
        elem.r.offset(elem.pos)

cam_x, cam_y = 0,0
def draw():
    if quit:
        p.cls(0)
        p.camera(0,0)
        p.text(40, 40, "vous etes morts !! \n t pour quitter \n r pour recommencer", 7)
        return
    
    p.cls(5)
    y_sort()
    for elem in drawables:
        elem.draw()
    
    for elem in tops:
        elem.draw()
    
    """
    for elem in colliders:
        r = elem.r
        p.rect(r.x, r.y, r.w, r.h, 8)
    """
    
    p.text(3+cam_x,3+cam_y,"vie : "+str(round(global_player.life, 1)),7)
    p.text(3+cam_x,120+cam_y,"difficulte : "+str(round(difficulty)),7)
    
class player(entity):
    def __init__(self, pos, base_speed, base_attack, base_life):
        super().__init__(pos, base_speed, base_attack, base_life, S_player)
    
    def update(self):
        global cam_x, cam_y
        
        self.rem_timer -= CST_FRAME
        
        cam_x = self.pos.x - 64
        cam_y = self.pos.y - 64
        if cam_x < 0:
            cam_x = 0
        elif cam_x > CST_TERRAIN_SIZE - 128:
            cam_x = CST_TERRAIN_SIZE - 128
        if cam_y < 0:
            cam_y = 0
        elif cam_y > CST_TERRAIN_SIZE - 128:
            cam_y = CST_TERRAIN_SIZE - 128
            
        p.camera(cam_x, cam_y)
        
        for elem in entities:
            if type(elem) == enemy and elem.r.collision(self.r):
                self.ouch(elem.base_attack)
                break
                
        dir = vec(0,0)
        if p.btn(p.KEY_Q):
            dir.x -= 1
            self.flip = True
        if p.btn(p.KEY_D):
            dir.x += 1
            self.flip = False
        if p.btn(p.KEY_Z):
            dir.y -= 1
        if p.btn(p.KEY_S):
            dir.y += 1
        if p.btnp(p.KEY_J):
            self.slash = slash(self.pos, vec(1,0) if self.flip else vec(-1,0), self.base_attack)
            add_top(self.slash)
        
        self.move(dir.normalize())
    
    def die(self):
        end()
        
class enemy(entity):
    def __init__(self, pos, base_speed, base_attack, base_life, sprite_info):
        super().__init__(pos, base_speed, base_attack, base_life, sprite_info)
    
    def update(self):
        self.rem_timer -= CST_FRAME
        if global_player.pos.sub(self.pos).length() < 64:
            self.move(self.pos.point_to(global_player.pos))
        
    def ouch(self, damage):
        sl = global_player.slash
        self.pos.x += 12 * -p.sgn(sl.direction.x)
        print(self.life)
        super().ouch(damage)
    
    def die(self):
        remove_entity(self)

class chest:
    def __init__(self, pos):
        self.pos = pos
        self.box = rect(pos.x,pos.y,4,10)
        self.r = null_rect
        self.u, self.v, self.w, self.h = S_chest[0]
            
    def update(self):
        if global_player.r.collision(self.box):
            restart()
    
    def draw(self):
        p.blt(self.pos.x, self.pos.y, 0, self.u, self.v, self.w, self.h, CST_TRANSPARENT)
    

def create_map():
    terrain = [S_pine_tree, S_big_tree, S_little_tree,S_grass1,S_grass2,S_grass3]
    
    for i in range(p.rndi(100,140)):
        drawables.append(Object(vec(p.rndi(0,CST_TERRAIN_SIZE),p.rndi(0,CST_TERRAIN_SIZE)), terrain[p.rndi(0, len(terrain)-1)]))
        
    structure_pos = vec(p.rndi(0,CST_TERRAIN_SIZE - 32),p.rndi(0,CST_TERRAIN_SIZE - 32))
    add_object(Object(structure_pos.add(vec(0,1)), S_wall_upLeft))
    add_object(Object(structure_pos.add(vec(8,0)), S_wall_up))
    add_object(Object(structure_pos.add(vec(16,0)), S_wall_up))
    add_object(Object(structure_pos.add(vec(24,0)), S_wall_upRight))
    add_object(Object(structure_pos.add(vec(0,11)), S_wall_side))
    add_object(Object(structure_pos.add(vec(32,11)), S_wall_side))
    add_object(Object(structure_pos.add(vec(23,20)), S_wall_downRight))
    add_object(Object(structure_pos.add(vec(0,20)), S_wall_downLeft))
    
    add_top(chest(structure_pos.add(vec(13,9))))
        
def spawn_enemies(difficulty):
    enemies = [S_spider,S_snake,S_zombie,S_skeleton]
    for i in range(12 + difficulty * 4):
        add_entity(enemy(vec(p.rndi(10,245),p.rndi(10,245)), 0.3 + difficulty * 0.3, 0.7 + difficulty * 0.7,4 + difficulty * 1.5,enemies[p.rndi(0, len(enemies)-1)]))

def spawn_player(difficulty):
    global global_player
    global_player = player(vec(5,5), 0.5 + difficulty * 0.5, 0.8 + difficulty * 0.8, 10)
    add_entity(global_player)

difficulty = 0
def restart(d=True):
    global global_player, difficulty, drawables, entities, colliders, tops, quit
    quit = False
    life = global_player.life
    if d:
        difficulty+=1
    else:
        life = 10
    drawables = []
    entities = []
    colliders = []
    tops = []
    create_map()
    spawn_enemies(difficulty)
    spawn_player(difficulty)
    global_player.life += life

quit = False
def end():
    global quit
    quit = True

global_player = None
spawn_player(1)
create_map()
spawn_enemies(1)

p.run(update, draw)