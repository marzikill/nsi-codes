import pyxel as p
from typing import List
from enum import Enum, unique
from random import randint


PLAYER_COUNT=4 # ICIIIIIIIIIIIIIIII
TIME_BEFORE_EXPLOSION=60
RANDOM_PATH=15

MapType = List[List[int]]


@unique
class Tiles(Enum):
    PATH = 0
    ROCK = 1
    WALL = 2

class Map():
    def __init__(self: 'Map'):
        self.tiles: MapType = []

        self.width = 15
        self.height = 13

        self.generate_blank_map()
        self.add_random_rock()

    def get(self: 'Map', x: int, y: int) -> Tiles | None:
        """
        Allows you to get a tiles

        :param x: int - The x coords of the point
        :param y: int - The y coords of the point
        
        :return Tiles | None - The tile value (or nothing if the coords are not in the tab)
        """
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return None
        
        return self.tiles[y][x]

    def generate_blank_map(self: 'Map') -> 'Map':
        """
        Allows you to generate a blank map for the game (just path and walls)

        :return 'Map'
        """

        self.tiles = []

        for y in range(self.height):
            line = []

            for x in range(self.width):
                if y % 2 == 0:
                    line.append(Tiles.PATH.value)
                else:
                    line.append(Tiles.PATH.value if x % 2 == 0 else Tiles.WALL.value)
                    
            self.tiles.append(line)
        
        return self
    
    def is_tile(self: 'Map', x: int, y: int, tile: Tiles) -> bool:
        """
        Allows you to know if the tile is the type asked for

        :param x: int - The x coords of the point
        :param y: int - The y coords of the point
        :param tile: Tiles - The tile type of the point we're looking for
        
        :return 'Map'
        """

        return self.tiles[y][x] == tile
    
    
    def set_tile(self: 'Map', x: int, y: int, tile: Tiles) -> 'Map':
        """
        Allows you to change the type of a tile
        
        :param x: int - The x coords of the point
        :param y: int - The y coords of the point
        :param tile: Tiles - The tile type of the point we've to replace by

        :return 'Map'
        """
        self.tiles[y][x] = tile

        return self
        
    
    def add_random_rock(self: 'Map') -> 'Map':
        """
        Allows you to generate randomly the rocks (10% of the map)

        :return 'Map'
        """


        width = self.width - 1
        height = self.height - 1
        
        # All the players coordonates (y, x)
        PLAYER_COORDS: MapType = [
            [0, 0],
            [0, 1],
            [1, 0],
            [0, width],
            [1, width],
            [0, width - 1],
            [height, 0],
            [height, 1],
            [height - 1, 0],
            [height, width],
            [height - 1, width],
            [height, width]
        ]

        for y in range(self.height):
            for x in range(self.width):
                if self.is_tile(x, y, Tiles.PATH.value) and [y, x] not in PLAYER_COORDS:
                    self.set_tile(x, y, Tiles.ROCK.value)
            
        for i in range(RANDOM_PATH):
            x = randint(0, width)
            y = randint(0, height)

            if self.is_tile(x, y, Tiles.ROCK.value):
                self.set_tile(x, y, Tiles.PATH.value)

        return self


class keyInput():
    def __init__(self, p_count) -> None:
        self.keynames = ["up", "left", "down", "right", "bomb"]
        self.keymap = []
        self.keys_dict = [[p.KEY_Z, p.KEY_Q, p.KEY_S, p.KEY_D,p.KEY_A],[p.KEY_Y,p.KEY_G,p.KEY_H,p.KEY_J,p.KEY_T],[p.KEY_O,p.KEY_K,p.KEY_L,p.KEY_M,p.KEY_I],[p.KEY_KP_8,p.KEY_KP_4,p.KEY_KP_5,p.KEY_KP_6,p.KEY_KP_7]]
        for i in range(p_count):
            self.keymap.append({})
            for j in range(len(self.keynames)):
                self.keymap[i][self.keynames[j]]=self.keys_dict[i][j]
            
        self.player_number = p_count
        self.players_input = []
        
    def get_input(self, key_name, player_id):
        key = self.keymap[player_id][key_name]

        return p.btnp(key)

        


class Game(): 
    def __init__(self: 'Game') -> None:
        self.player_count = PLAYER_COUNT

        self.bombs: List[Bomb] = []
        self.explosions: List[Explosion] = []
        
        self.counter = 0

        self.maze: Map = Map()

        # Generate the four players grid        
        self.players: List[Player] = []
        start_pos = [
                (0, 0),
                (self.maze.width - 1, self.maze.height - 1),
                (0, self.maze.height - 1),
                (self.maze.width - 1, 0)
            ]

        for i in range(self.player_count):
            player = Player(i, self)
            player.x = start_pos[i][0]
            player.y = start_pos[i][1]
            self.players.append(
                player
            )
        
        self.controls = keyInput(self.player_count)

        # Initialize the game
        p.init(128, 128, title="BombItKid", fps=30)

        # Load the pyxres file
        p.load("my_resource.pyxres")

        # Run the game
        p.playm(0,loop=True)
        p.run(self.update, self.draw)
        
    

    def update(self: 'Game') -> None:
        # reset the game
        if len(self.players) < 2:
            self.bombs: List[Bomb] = []
            self.explosions: List[Explosion] = []
            
            self.counter = 0

            self.maze: Map = self.maze.generate_blank_map()
            self.maze.add_random_rock()

            # Generate the four players grid        
            self.players: List[Player] = []

            start_pos = [
                    (0, 0),
                    (self.maze.width - 1, self.maze.height - 1),
                    (0, self.maze.height - 1),
                    (self.maze.width - 1, 0)
                ]

            for i in range(self.player_count):
                player = Player(i, self)
                player.x = start_pos[i][0]
                player.y = start_pos[i][1]
                self.players.append(
                    player
                )

            return

        for player in self.players:
            player.update()
        
        for bomb in self.bombs:
            is_destroyed = bomb.update(self)

            if is_destroyed:
                self.explose_bomb(bomb.power, bomb.x, bomb.y)
                self.bombs.remove(bomb)
                p.play(1,2)

        for explosion in self.explosions:
            ended = explosion.update()
            if ended and explosion in self.explosions:
                self.explosions.remove(explosion)

        if p.btnp(p.KEY_ESCAPE):
            p.quit()
        
        if self.counter < 600:
            self.counter +=1
        else:
            for player in self.players:
                if player.power < 5:
                    player.power+=1
            self.counter = 0
            

    def draw(self):
        p.cls(0)
        
        self.draw_maze()

        for player in self.players:
            player.draw()

        for bomb in self.bombs:
            bomb.draw()
        
        for explosion in self.explosions:
            explosion.draw()
            

    def draw_maze(self):
        for y in range(self.maze.height):
            for x in range(self.maze.width): 
                info = self.maze.get(x, y)

                p.blt((x * 8) + 4, y * 8, 0, info * 8, 24, 8, 8)

    def explose_bomb(self, power: int, x: int, y: int) -> None:
        """
        Calls when a bomb has to explose

        :param power: int - The power of the bomb
        :param x: int - The x coordonate of the bomb
        :param y: int - The y coordonate of the bomb
        :return None
        """
        BIT_MAP = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for neigh in BIT_MAP:
            for i in range(1, power + 1):
                tile_x = x + neigh[0] * i
                tile_y = y + neigh[1] * i

                # Get the neighbor tile
                tile = self.maze.get(tile_x, tile_y)

                if tile == Tiles.PATH.value or tile == Tiles.ROCK.value:
                    self.explosions.append(Explosion(tile_x,tile_y))

                # If the tile is a rock
                if tile == Tiles.ROCK.value:
                    # Change the tile to path
                    self.maze.set_tile(tile_x, tile_y, Tiles.PATH.value)
                    break

                # If the tile is a wall, we just stop the while, we don't have to continue the
                # power explosion
                if tile == Tiles.WALL.value:
                    break

                if tile == None:
                    break
                 


class Player():
    def __init__(self, id: int, game: Game):
        self.id: int = id # id on the player 0-3

        self.x: int = 0
        self.y: int = 0
        
        self.game: Game = game
        self.power = 1

        self.animation_duration = 5
        self.animations = [0, 0]
        self.directions = [0, 0]

    def update(self):
        dx = (self.game.controls.get_input("right", self.id) - self.game.controls.get_input("left", self.id))
        dy = (self.game.controls.get_input("down", self.id) - self.game.controls.get_input("up", self.id))

        for i in range(2):
            if self.animations[i] != 0:
                self.animations[i] -= 1


        if self.animations == [0, 0] and (0 <= self.x + dx < self.game.maze.width):
            if (0 <= self.y + dy < self.game.maze.height):
                bomb_in_front = False
                dcoors = (self.x + dx, self.y + dy)

                for bomb in self.game.bombs:
                    if bomb.x == dcoors[0] and bomb.y == dcoors[1]:
                        bomb_in_front = True

                if self.game.maze.tiles[self.y + dy][self.x] == Tiles.PATH.value and not bomb_in_front:
                    self.y += dy

                    if dy != 0:
                        self.animations[0] = self.animation_duration
                        self.directions[0] = dy

                if self.game.maze.tiles[self.y][self.x+dx] == Tiles.PATH.value and not bomb_in_front:
                    self.x += dx
                    
                    if dx != 0:
                        self.animations[1] = self.animation_duration
                        self.directions[1] = dx

        can_place_bomb = True
        for bomb in self.game.bombs:
            if bomb.player_id == self.id:
                can_place_bomb = False

        if self.game.controls.get_input("bomb", self.id) and can_place_bomb:
            self.game.bombs.append(Bomb(self.x, self.y, self.power, self.id))

        for explosion in self.game.explosions:
            if self.x == explosion.x and self.y == explosion.y and self in self.game.players:
                self.game.players.remove(self)

    def draw(self):
        p.blt(4 + (self.x - (self.animations[1] / self.animation_duration) * self.directions[1]) * 8, 
              (self.y - (self.animations[0] / self.animation_duration) * self.directions[0]) * 8, 
              0, 
              self.id * 8, 
              32, 
              8, 
              8, 
              p.COLOR_BLACK)

class Bomb():
    def __init__(self: 'Bomb', x: int, y: int, power: int, player_id: int) -> 'Bomb':
        self.x = x
        self.y = y
        self.power = power
        self.counter = TIME_BEFORE_EXPLOSION
        self.player_id = player_id
 
    
    def update(self, game: Game) -> bool:
        """
        Update the bomb counter and return True if the bilb should be destroy

        :return bool - Should the bomb be destroy
        """
        self.counter -= 1

        for explosion in game.explosions:
            if explosion.x == self.x and explosion.y == self.y and self in game.bombs:
                game.explose_bomb(self.power, self.x, self.y)
                game.bombs.remove(self)

        return self.counter == 0

    def draw(self):
        p.blt(4 + self.x * 8, self.y * 8, 0, 0, 40, 8, 8, p.COLOR_BLACK)

class Explosion():
    def __init__(self,x:int, y:int) -> None:
        self.duration=40
        self.x = x
        self.y = y

    def update(self):
        self.duration -= 1

        return self.duration == 0
    
    def draw(self):
        p.blt(4 + self.x * 8, self.y * 8, 0, 8, 40, 8, 8, p.COLOR_BLACK)
        
    def noise(self): 
        p.sound(2).speed = 60

        
Game()