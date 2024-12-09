from ds import Pile, Chapeau, File, Bonhomme

def init_piles():
    c=Chapeau(1)
    c2=Chapeau(2)
    c3=Chapeau(3)
    c4=Chapeau(4)
    c5=Chapeau(5)
    p1 = Pile()
    p1.empiler(c)
    p1.empiler(c2)
    p1.empiler(c3)
    p1.empiler(c4)
    p1.empiler(c5)
    p2=Pile()
    p2.empiler(c2)
    p2.empiler(c)
    p2.empiler(c5)
    p2.empiler(c3)
    p2.empiler(c4)
    p3=Pile()
    p3.empiler(c4)
    p3.empiler(c5)
    p3.empiler(c)
    p3.empiler(c2)
    p3.empiler(c3)
    p4=Pile()
    p4.empiler(c5)
    p4.empiler(c4)
    p4.empiler(c3)
    p4.empiler(c2)
    p4.empiler(c)
    return p1,p2,p3,p4

def init_files():
    f1=File()
    f2=File()
    f3=File()
    f4=File()
    f1.enfiler(Bonhomme(1))
    f1.enfiler(Bonhomme(2))
    f1.enfiler(Bonhomme(3))
    f1.enfiler(Bonhomme(4))
    f1.enfiler(Bonhomme(5))
    
    f2.enfiler(Bonhomme(5))
    f2.enfiler(Bonhomme(4))
    f2.enfiler(Bonhomme(3))
    f2.enfiler(Bonhomme(2))
    f2.enfiler(Bonhomme(1))
    
    f3.enfiler(Bonhomme(4))
    f3.enfiler(Bonhomme(3))
    f3.enfiler(Bonhomme(5))
    f3.enfiler(Bonhomme(1))
    f3.enfiler(Bonhomme(2))
    
    f4.enfiler(Bonhomme(3))
    f4.enfiler(Bonhomme(2))
    f4.enfiler(Bonhomme(1))
    f4.enfiler(Bonhomme(5))
    f4.enfiler(Bonhomme(4))
    return f1, f2, f3, f4

p1, p2, p3, p4 = init_piles()
f1, f2, f3, f4 = init_files()


def compatibles(p, f):
    """ Pile, File -> Bool
    Détermine si les chapeaux sont associés aux bon bonshommes """
    while not p.est_vide():
        b = f.defiler()
        c = p.depiler()
        if not b.content(c):
            return False
    return True
    # ou bien return f.est_vide()
    
# Si on exécute : 
# >>> compatibles(p1, f1)
# False
# >>> compatibles(p1, f2)
# False
# 
# Mais si on exécute directement 
# >>> compatibles(p1, f2)
# True
# 
# Cela vient du fait que la fonction compatibles
# MODIFIE les piles et les files. On parle de donnée mutable.
        

def restaure_pile(p, p_aux):
    """ Pile, Pile -> None
    Restaure p à son état initial lorsque les dépilements successifs
    on été empilés dans p_aux. """
    while not p.est_vide():
        c = p.depiler()
        p_aux.empiler(c)
    while not p_aux.est_vide():
        c = p_aux.depiler()
        p.empiler(c)

def restaure_file(f, f_aux):
    """ File, File -> None
    Restaure f à son état initial lorsque les défilement successifs
    on été enfilés dans f_aux. """
    while not f.est_vide():
        b = f.defiler()
        f_aux.enfiler(b)
    while not f_aux.est_vide():
        b = f_aux.defiler()
        f.enfiler(b)
        

def compatibles_mieux(p, f):
    """ Pile, File -> Bool
    Détermine si les chapeaux sont associés aux bons bonshommes
    L'état de la pile p et la file f sera le même avant et après exécution """
    p_aux = Pile()
    f_aux = File()
    while not p.est_vide():
        b = f.defiler()
        c = p.depiler()
        f_aux.enfiler(b)
        p_aux.empiler(c)
        if not b.content(c):
            restaure_pile(p, p_aux)
            restaure_file(f, f_aux)
            return False
    restaure_pile(p, p_aux)
    restaure_file(f, f_aux)    
    return True
    # ou bien return f.est_vide()

p1, p2, p3, p4 = init_piles()
f1, f2, f3, f4 = init_files()

def solution():
    """ () -> [(int, int)]
    Renvoie la liste des associations pile i <-> file j """
    piles = init_piles()
    files = init_files()
    sol = []
    for i in range(len(piles)):
        for j in range(len(files)):
            p = piles[i]
            f = files[j]
            if compatibles_mieux(p, f):
                sol.append((i, j))
    return sol
    
# Question 5.
# 1. Ordre d'arrivée (premier au début) 7 8 9 10 3 2 1 5 4 6
# 2. 3 piles, de taille A: 4, B: 1, C: 2.
# 8 9 10 sont dans le même ordre qu'initialement : elles ne sont passées
# par aucune pile.
# 4 3 2 1 sont les premières billes (tombées dans la première pile) qui ont
# 5 est tombée dans la seconde pile
# 7 6 sont tombées dans la troisième pile.

def arrivee_rampe(profondeur):
    """ [int] -> [int]
    Détermine l'ordre d'arrivée des boules numérotées de 1 à 10 """
    rampe_lancement = File()
    for b in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        rampe_lancement.enfiler(b)
    piles = [Pile(max_elt = p) for p in profondeur] # liste de piles bornées, dans l'ordre du parcours.
    rampe_finale = File() # billes dans l'ordre d'arrivée
    numero_pile = 0 # indice de la pile à remplir
    
    # on remplit les piles dans l'ordre dans lequel elles sont positionnées
    # sur le parcours tant que cela est possible (c'est à dire tant que
    # la dernière pile du parcours n'est pas vide)
    # Si la pile que l'on cherche à remplir est pleine,
    # alors il faut commencer par changer le numéro de la pile à remplir. 
    # On empile une bille prise depuis la rampe de lancement sur la pile à remplir.
    while not piles[-1].est_pleine():
        if piles[numero_pile].est_pleine():
            numero_pile += 1
        b = rampe_lancement.defiler()
        piles[numero_pile].empiler(b)
        
    # Toutes les billes restantes roulent directement dans la rampe d'arrivée.
    while not rampe_lancement.est_vide():
        b = rampe_lancement.defiler()
        rampe_finale.enfiler(b)
  
    # On retire les ressorts dans l'ordre dans lesquels ils sont positionnés
    # sur le parcours. Les billes ressortent des trous et viennent s'accumuler
    # sur la rampe de lancement.
    for p in piles:
        while not p.est_vide():
            b = p.depiler()
            rampe_finale.enfiler(b)
    # Dans certains cas, cet algorithme peut ne pas produire le résultat
    # attendu, pourquoi ? Trouver un exemple qui produise un résultat incorrect.
    # Puis, corriger l'algorithme.

    return rampe_finale

