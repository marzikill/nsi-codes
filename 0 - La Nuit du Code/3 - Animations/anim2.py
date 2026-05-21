import pyxel

pyxel.init(128, 128, title="Exemple 2") # 30 fps par défaut

POSITION = {"x": 64, "y": 64}

def update_carre():
    if pyxel.btn(pyxel.KEY_LEFT):  
        POSITION['x'] -= 2 
    if pyxel.btn(pyxel.KEY_RIGHT):
        POSITION['x'] += 2
    if pyxel.btn(pyxel.KEY_UP):
        POSITION['y'] -= 2
    if pyxel.btn(pyxel.KEY_DOWN):
        POSITION['y'] += 2

def update():
    """ Met à jour la logique du programme """
    update_carre()

def draw():
    """ Affichage à l'écran """
    pyxel.rect(POSITION["x"], POSITION["y"], 8, 8, 3)

pyxel.run(update, draw)
