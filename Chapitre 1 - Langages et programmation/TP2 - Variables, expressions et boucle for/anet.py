from turtle import *
import random

def change_couleur():
    colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color((r, g, b))
    return (r,g,b)

change_couleur()
color("red")
write("hello")
