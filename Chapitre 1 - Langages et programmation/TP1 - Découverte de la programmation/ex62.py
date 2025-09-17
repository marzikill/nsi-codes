from turtle import *

def escalier(hauteur_marche, nbr_marches):
    for i in range(nbr_marches):
        left(90)
        forward(hauteur_marche)
        right(90)
        forward(hauteur_marche)
        
escalier(20, 5)