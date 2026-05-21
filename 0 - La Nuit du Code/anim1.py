import pyxel

pyxel.init(128, 128, title="Exemple 1", fps=15)

COULEURS = list(range(16)) # [0, 1, 2, ..., 15]

def update():
    """ Met à jour la logique du programme """
    # for i in range(len(COULEURS)):
    #     if COULEURS[i] < 15:
    #         COULEURS[i] += 1
    #     else:
    #         COULEURS[i] = 0

def draw():
    """ Affichage à l'écran """
    # Dessine 16 rectangles verticaux avec des couleurs différentes
    for i in range(16):
        pyxel.rect(i * 8, 0, 10, 128, COULEURS[i])


# Lancement de la boucle principale de Pyxel
pyxel.run(update, draw)
