def indice(caractere):
    "Renvoie l'indice de `caractere` qui doit être une majuscule"
    return ord(caractere) - ord('A')

def majuscule(i):
    """Renvoie la majuscule d'indice donnée
    majuscule(0) renvoie 'A'
    majuscule(25) renvoie 'Z'
    """
    return chr(ord('A') + i)

print(indice('Z'))
print(25 + 8)
print(33 % 26)
print(majuscule(7))

def cesar(message, decalage):
    resultat = ''
    for caractere in ...:
        if 'A' <= caractere <= ...:
            i = ...(caractere)
            i = (i + ...) ...
            resultat += ...(i)
        else:
            resultat += ...
    return ...

# Tests

assert cesar('HELLO WORLD!', 5) == 'MJQQT BTWQI!'
assert cesar('MJQQT BTWQI!', -5) == 'HELLO WORLD!'

assert cesar('BONJOUR LE MONDE !', 23) == 'YLKGLRO IB JLKAB !'
assert cesar('YLKGLRO IB JLKAB !', -23) == 'BONJOUR LE MONDE !'
