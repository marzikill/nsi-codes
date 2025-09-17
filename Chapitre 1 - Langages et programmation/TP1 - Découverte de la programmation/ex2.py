from turtle import *

def carre(cote):
    for i in range(4):
        forward(cote)
        left(90)
        
for i in range(6):
    carre(70)
    left(60)