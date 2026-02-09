from PIL import Image
from random import randint

mona = Image.open("mona_fond.png")
cri = Image.open("cri.jpg")
mona.show()
cri.show()
largeur, hauteur = mona.size
img = Image.new("RGB", mona.size)
VERT = (0, 255, 0)

for y in range(hauteur): #parcours des lignes
    for x in range(largeur): #parcours des colonnes d'une ligne
        pixel = mona.getpixel((x, y))
        if ...:
            img.putpixel(...)
        else:
            ...
            
img.show()