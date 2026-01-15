from PIL import Image
from random import randint

largeur, hauteur = (512, 512)
# L'instruction suivante crée une nouvelle Image en mode RGB
# et qui posséde les mêmes dimensions que img
img2 = Image.new("RGB", (512, 512))

for y in range(hauteur): #parcours des lignes
    for x in range(largeur): #parcours des colonnes d'une ligne
        
        img2.putpixel((x, y),(randint(0, 255), randint(0, 255), randint(0, 255)))

img2.show()