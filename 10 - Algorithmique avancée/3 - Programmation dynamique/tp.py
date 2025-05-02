def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n- 1) + fibo(n - 2)
    
# la complexité de la fonction fibo est exponentielle

def fibomem(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return memo[n]
    else:
        inter1 = fibomem(n - 1, memo)
        inter2 = fibomem(n - 2, memo)
        memo[n] = inter1 + inter2
        return memo[n]
    
def fibodyn(n):
    T = [None for _ in range(n+1)]
    T[0], T[1] = 0, 1
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
    return T[n]
        
        
def nb_chemins(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return nb_chemins(n - 1, m) + nb_chemins(n, m - 1)
        
def nbc(n, m, memo):
    if (n, m) in memo:
        return memo[(n, m)]
    if n == 1 or m == 1:
        memo[(n, m)] = 1
        return 1
    else:
        inter1 = nbc(n - 1, m, memo)
        inter2 = nbc(n, m - 1, memo)
        memo[(n, m)] = inter1 + inter2
        return memo[(n, m)]
    
def nbc_dyn(n, m):
    T = [[None for j in range(m)] for i in range(n)]
    for i in range(n):
        T[i][0] = 1
    for j in range(m):
        T[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            T[i][j] = T[i - 1][j] + T[i][j - 1]
    return T[n - 1][m - 1]
          
systeme = [1, 4, 8, 10]

def rendu_monnaie_glouton(systeme, montant):
    nb_pieces = 0
    while montant > 0:
        plus_grande = systeme[0]
        for p in systeme:
            if p <= montant and p > plus_grande:
                plus_grande = p
        # on rend la pièce
        print("piece rendue : ", plus_grande)
        montant = montant - plus_grande
        nb_pieces = nb_pieces + 1
    return nb_pieces
        
def rendu_monnaie(systeme, montant):
    if montant == 0:
        return 0
    elif montant in systeme:
        return 1
    else:
        liste = []
        for p in systeme:
            if p <= montant:
                inter = rendu_monnaie(systeme, montant - p)
                liste.append(inter)
        return min(liste) + 1
 
# la complexité de l'algorithme est exponentielle
# rendu_monnaie(systeme, 42) ne termine pas en
# temps raisonnable
# glouton :
# + simplicité, rapidité
# - pas toujours optimal
# recursif :
# + optimal,
# - exponentiel, concept pas simple


# Pour mémoïser :
# 1. on ajoute un argument : la mémoire (dictionnaire)
# { montant: nb_pieces_mini }
# 2. la fonction commence par vérifier si les calculs
# n'ont pas déjà été effectués
# 3. avant de renvoyer quelque chose : on stocke la valeur
# calculée dans la mémoire
# 4. on renomme la fonction récursive (attention aux occurrences)
# On rajoute memo aux arguments d'appels de la fonction
# récursive
def rendu_monnaie2(systeme, montant, memo):
    if montant in memo:
        return memo[montant]
    if montant == 0:
        memo[0] = 0
        return 0
    elif montant in systeme:
        memo[montant] = 1
        return memo[montant]
    else:
        liste = []
        for p in systeme:
            if p <= montant:
                inter = rendu_monnaie2(systeme, montant - p, memo)
                liste.append(inter)
        memo[montant] = min(liste) + 1
        return memo[montant]

# cette fonction a meilleure complexité !!!!!
# cependant, on utilise de l'espace mémoire (on s'en fout)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        