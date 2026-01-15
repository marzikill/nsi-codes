from PIL import Image
from random import randint

img = Image.open("baboon.png")
largeur, hauteur = img.size
# L'instruction suivante crée une nouvelle Image en mode RGB
# et qui posséde les mêmes dimensions que img
img2 = Image.new("RGB", img.size)

for y in range(hauteur): #parcours des lignes
    for x in range(largeur): #parcours des colonnes d'une ligne
        pixel = img.getpixel((x, y))
        img2.putpixel((x, y),(pixel[0], 0, pixel[2]))

img2.show()