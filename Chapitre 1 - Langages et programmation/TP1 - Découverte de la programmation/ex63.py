from turtle import *

def triangle(longueur):
    for i in range(3):
        forward(longueur)
        left(120)
        
def carre(longueur):
    for i in range(4):
        forward(longueur)
        left(90)

def pentagone(longueur):
    for i in range(5):
        forward(longueur)
        left(360/5)

def polygone(longueur, nbr_cotes):
    for i in range(nbr_cotes):
        forward(longueur)
        left(360/nbr_cotes)

# polygone(100, 3)
# polygone(100, 4)
# polygone(100, 5)
# polygone(100, 6)
# polygone(100, 7)

# Ou tout simplement : 
for i in range(3, 8):
    polygone(100, i)

done()