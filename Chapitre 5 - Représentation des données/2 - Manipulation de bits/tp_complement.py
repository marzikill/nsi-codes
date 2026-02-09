def combien_bits(n):
    """ int -> int
    n est un entier positif
    Renvoie le nombre de bits nécessaires à l'écriture en base 2 de n """
    # si n <= 1 alors il s'écrit sur 1 bit
    N = 1
    while n > 1:
        N = ...
        n = ...
    return ...

def base2(n):
    """ int -> [int]
    n est un entier positif
    Renvoie l'écriture en base 2 de n """
    N = combien_bits(n)
    bits = [-1 for i in range(N)]
    for i in range(...):
        n, b = n//2, n%2
        bits[...] = ...
    return ...

def base10(bits):
    """ [int] -> int """
    N = len(bits)
    puiss2 = 1
    n = 0
    for i in range(N-1, -1, -1):
        n = n + bits[i]*puiss2
        puiss2 = 2*puiss2
    return n

def inverser(bits):
    """ [int] -> [int]
    Inverse les bits de la liste """
    N = len(bits)
    inv = [0 for i in range(N)]
    # À compléter 
    return inv

def ajouter1(bits):
    """ [int] -> [int] """       
    N = len(bits)
    plusun = [b for b in bits]
    # À compléter 
    return plusun

def ecriture_base2(n, N):
    bits = base2(n)       
    taille = len(bits)
    return [0]*(N - taille) + bits

def complement_a_2(n, N):
    """ int, int -> [int]
    Renvoie l'écriture en complément à 2 de n sur N bits """
    pass

def base10_cp2(bits, N):
    if bits[0] == 0:
        return base10(bits) 
    return -2**N + base10(bits)

def somme(bits1, bits2):
    """ [int], [int] -> [int]
    bits1 et bits2 sont de même taille
    renvoie la somme chiffre à chiffre de bits1 avec bits2 en gérant les retenues """
    N = len(bits1)
    s = [...]
    retenue = ...
    for i in range(...):
        # À compléter
    return s

