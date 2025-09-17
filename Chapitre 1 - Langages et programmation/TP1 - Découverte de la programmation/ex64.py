from turtle import *

def ligne(nbr_points):
    # le stylo doit être en position "up"
    # il faut utiliser "penup" avant l'appel de ligne
    for i in range(nbr_points):
        dot()
        forward(30)
       
# On trace une ligne et on se place au début de la suivante
penup()
ligne(7)
backward(7*30)
right(90)
forward(30)
left(90)

# On répète 4 fois supplémentaires les instructions précédentes
# C'est du control-c control-v
penup()
ligne(7)
backward(7*30)
right(90)
forward(30)
left(90)

penup()
ligne(7)
backward(7*30)
right(90)
forward(30)
left(90)

penup()
ligne(7)
backward(7*30)
right(90)
forward(30)
left(90)

penup()
ligne(7)
backward(7*30)
right(90)
forward(30)
left(90)

# On peut utiliser une boucle for
for i in range(5):
    penup()
    ligne(7)
    backward(7*30)
    right(90)
    forward(30)
    left(90)
          

done()