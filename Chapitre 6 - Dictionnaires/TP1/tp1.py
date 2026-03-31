votes = ["oui", "non", "oui", "oui", "oui", "non"]

def compte_voix(votes):
    """ [str] -> {str:int} """
    res = {"oui":0, "non":0}
    for v in votes:
        if v == "oui":
            res["oui"] += 1
        elif v == "non":
            res["non"] += 1
    return res

def resultat(votes):
    compte = compte_voix(votes)
    if compte["oui"] > compte["non"]:
        pourcentage = round(compte["oui"]/len(votes)*100, 2)
        return "Le oui l'emporte avec " + str(pourcentage) + "% de votes"
    elif compte["oui"] < compte["non"]:
        pourcentage = round(compte["non"]/len(votes)*100, 2)
        return "Le non l'emporte avec " + str(pourcentage) + "% de votes"
    else:
        return "Les deux avis sont à égalité"
    
naissances  = {"Alvyne":3, "Boubakar":8, "Clément":1, "Emilie":8}

def anniversaire(naissances, prenom):
    return naissances[prenom]
    
def anniversaires_du_mois(naissances, mois):
    prenoms = []
    for p in naissances:
        if naissances[p] == mois:
            prenoms.append(p)
    return prenoms    

assert anniversaires_du_mois(naissances, 8) ==  ["Boubakar", "Emilie"]
        
animaux = [
    {'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 5},
    {'nom': 'Tom', 'espece': 'chat', 'age': 7, 'enclos': 4},
    {'nom': 'Belle', 'espece': 'chien', 'age': 6, 'enclos': 3},
    {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}
]

def animaux_refuge(animaux):
    noms = []
    for a in animaux:
        noms.append(a["nom"])
    return noms

def animaux_enclos(animaux, numero):
    """ animaux : liste de dictionnaires"""
    noms = []
    for a in animaux:
        # a : dictionnaire
        if numero == a["enclos"]:
            noms.append(a["nom"])
    return noms

def informations(animaux, nom):
    for a in animaux:
        if a["nom"] == nom:
            return a
    return None
    
    
    
    
    
    