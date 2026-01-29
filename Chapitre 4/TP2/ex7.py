from PIL import Image
from random import randint

largeur, hauteur = 641, 429
img = Image.new("RGB", (641, 429))
VERT = (0, 122, 94)
ROUGE = (208, 20, 37)
JAUNE = (252, 208, 23)

for y in range(hauteur): #parcours des lignes
    for x in range(largeur): #parcours des colonnes d'une ligne
        if x < 214:
            img.putpixel((x,y), VERT)
        elif 214 <= x < 428:
            img.putpixel((x,y), ROUGE)
        else:
            img.putpixel((x,y), JAUNE)
        
img.show()