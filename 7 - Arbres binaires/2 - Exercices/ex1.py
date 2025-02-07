def f(x):
    if x <= 1:
        print("*")
    else:
        f(x - 1) # appel récursif
        print("*"*x)
        f(x - 1) # appel récursif
        
def g(x):
    if x <= 1:
        print("*")
    else:
        g(x - 1)
        g(x - 2)
        print("*"*x)
    
f(4)