import pyxel
from random import*


####### Règles du jeu ###########

#### Jeu de plateforme, le but est d'atteindre la pièce à l'aide de la touche espace pour sauter et des touches directionnelles pour se déplacer horizontalement
###### Un scénario est présenter: le personnage doit récupérer toutes les pièces pour repartir chez lui



####################### INITIALISATION ########################

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Ara, et la conquête spatiale")


pyxel.load ("perso.pyxres")
pyxel.play(0, 0, 0, loop=True)
# position initiale du vaisseau
# (origine des positions : coin haut gauche)
perso_x = 6
perso_y = 90
plat_liste = []
x,y=0,100
for i in range(4):
    plat_liste.append([x,y])
    x = x + 30
    y=y-5
    
place_perso=True
saut=False
etape_saut=0

arrivee_x=105
arrivee_y=80

victoire=False

vies=3

niveau=0

pluie_liste=[]

restart=False

debut=False

scenario=True

mode_jeu=False

num_scenario=0

sens=[]
for k in range (4) :
    sens.append(1)
    

sens_a=1

######################### FONCTIONS ###########################

#### Mode jeu ####




def defaite (vies, perso_x, perso_y, pluie_liste) :
    
    for pluie in pluie_liste :
        if niveau>=2 :
            if ((perso_x+4)>=pluie[0]) and (perso_x-4<=pluie[0]) and ((perso_y+4)>=pluie[1]) and (perso_y<=pluie[1]) and vies>0 :
                pluie_liste.remove(pluie)
                vies-=1
    if perso_y>=128 and vies > 0 :
        vies-=1
        if niveau==3 :
            perso_x, perso_y = 6, 10
        else :
            perso_x, perso_y = 6, 90
    return vies, perso_x, perso_y, pluie_liste

def est_sur_plateforme (place_perso) :
    
    place_perso=False
    for plat in plat_liste :
        if (perso_x>=plat[0]) and (perso_x<=(plat[0]+20)) and (perso_y>=(plat[1]-8)) and (perso_y<=(plat[1])):
            place_perso=True
    return place_perso

def perso_deplacement(x):
    
    """déplacement avec les touches de directions"""
    if not restart :

        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x < 124) :
                x+=2
            
            
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x=x-2
                
    return x

def debut_saut (saut,etape_saut) :
    
    if not restart :
        if pyxel.btn(pyxel.KEY_SPACE):
            if place_perso :
                saut=True
                etape_saut=0
            
    return saut, etape_saut

def milieu_saut (saut, etape_saut, perso_y):
    
    if saut and etape_saut<10 :
        perso_y-=1
        etape_saut+=1
    elif etape_saut==10 :
        etape_saut=0
        saut=False
    return saut, etape_saut, perso_y

def descente (perso_y) :
    if not saut :
        if not place_perso :
            perso_y+=1
    return perso_y

def plateforme_deplacement (plat_liste) :
    k=0
    for plat in plat_liste :
        if sens[k]==1 :
            if plat[1]<110 :
                plat[1]+=1
            else :
                sens[k]=2
        if sens[k]==2 :
            if plat[1]>20 :
                plat[1]-=1
            else :
                sens[k]=1
        if k == 3:
            k=0
        else :
            k=k+1
    return plat_liste

def arivee_deplacement (arrivee_y, sens_a) :
    if sens_a==1 :
        if arrivee_y<105 :
            arrivee_y+=1
        else :
            sens_a=2
    if sens_a==2:
        if arrivee_y>15 :
            arrivee_y-=1
        else :
            sens_a=1
    return arrivee_y, sens_a

def perso_dep_niveau3 (perso_y):
    if place_perso :
        perso_y-=1
    return perso_y



def pluie_creation (pluie) :
    
    """création aléatoire des ennemis"""
    # pluie
    if not restart :
        if (pyxel.frame_count % 7 == 0) :
            x = randint (0,120)
            pluie_liste.append([x, 0])
    return pluie_liste

def pluie_deplacement(pluie_liste) :
    
    """déplacement de la pluie vers le haut et suppression s'ils sortent du cadre"""
    for pluie in pluie_liste :
        pluie[1] += 2
        if pluie [1]>128 :
                pluie_liste.remove(pluie)
    return pluie_liste
        
def prop_recommencer_jeu (restart):
    
    if vies==0 :
        restart=True
    return restart

def depart_a_zero (restart, debut) :

    if restart :
        if pyxel.btn(pyxel.KEY_R) :
            debut=True
            restart=False
    return restart, debut
            
def redepart_niveau1 (debut, vies, perso_x, perso_y) :
    
    if debut :
        vies=3
        if niveau == 3 :
            perso_x, perso_y=6, 10
        else :
            perso_x, perso_y=6, 90
        debut=False
    return debut, vies, perso_x, perso_y


##### Transition vers le scénario ######

def touche_arrivee (victoire, perso_x, perso_y) :
    if (perso_x>=arrivee_x) and (perso_x<=(arrivee_x+2)) and (perso_y>=arrivee_y-3) and (perso_y<=arrivee_y+5) :
        victoire=True
        perso_x, perso_y = 0,30
    return victoire, perso_x, perso_y

def transition_scenario (victoire, scenario, mode_jeu) :
    if victoire :
        mode_jeu=False
        scenario=True
        victoire=False
        
    return victoire, scenario, mode_jeu

### Mise en place du scénario ###

def texte_scenario (scenario, num_scenario, mode_jeu, niveau) :
    
    if pyxel.btn(pyxel.KEY_A) :
        scenario = False
        mode_jeu=True
        num_scenario+=1
        niveau+=1
    return scenario, num_scenario, mode_jeu, niveau

    
# =========================================================
# == UPDATE
# =========================================================

def update():
    """mise à jour des variables (30 fois par seconde)"""

    global perso_x, perso_y, saut, etape_saut, place_perso, victoire, vies, arrivee_x, arrivee_y, pluie_liste, restart, debut, scenario, num_scenario, mode_jeu, niveau, plat_liste, sens_a
    
    
    if mode_jeu :

        # mise à jour de la position du perso
        perso_y = descente(perso_y)
        perso_x = perso_deplacement(perso_x)
    
        # màj place_perso
        place_perso = est_sur_plateforme (place_perso)
        
        # màj saut
        saut,etape_saut=debut_saut (saut,etape_saut)
        saut,etape_saut,perso_y=milieu_saut (saut,etape_saut,perso_y)
        
        # victoire/defaite
        
        vies, perso_x, perso_y, pluie_liste=defaite(vies, perso_x, perso_y, pluie_liste)
        
        
        # mouvement plateforme
        if niveau>=3 :
            plat_liste=plateforme_deplacement(plat_liste)
            arrivee_y, sens_a=arivee_deplacement(arrivee_y, sens_a)
            perso_y=perso_dep_niveau3 (perso_y)
    
        
        # pluie
        if niveau>=2:
            pluie_liste=pluie_creation(pluie_liste)
            pluie_liste=pluie_deplacement(pluie_liste)
    
        # recommencer le jeu en cas de défaitee
        restart = prop_recommencer_jeu(restart)
        restart, debut = depart_a_zero (restart, debut)
        debut, vies, perso_x, perso_y = redepart_niveau1 (debut, vies, perso_x, perso_y)
        
        # transition scénario
        victoire, perso_x, perso_y =touche_arrivee(victoire, perso_x, perso_y)
        victoire, scenario, mode_jeu = transition_scenario (victoire, scenario, mode_jeu)
        
    if scenario :
    
        
        scenario, num_scenario, mode_jeu, niveau = texte_scenario (scenario, num_scenario, mode_jeu, niveau)
    
    
    


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    
    global perso_x, perso_y, saut, etape_saut, place_perso, victoire, vies, arrivee_x, arrivee_y, pluie_liste, restart, debut, scenario, num_scenario, mode_jeu, niveau, plat_liste

    # vide la fenetre
    pyxel.cls(0)
    
    if mode_jeu :
    
        

        # perso 
        pyxel.blt(perso_x, perso_y, 0, 0, 0, 8, 8)

        # plateformes
        for plat in plat_liste :
            pyxel.blt(plat[0], plat[1], 0, 0, 11, 20, 4)
    
        # arrivee
        pyxel.blt(arrivee_x, arrivee_y, 0, 17, 3, 20, 4, 0)
        
        # pluie
        for pluie in pluie_liste :
            pyxel.blt(pluie[0], pluie[1], 0, 8, 0, 8, 8, 0)
    
        # victoire/defaite
        if victoire :
            pyxel.text(46,54,'VICTOIRE', 7)
        if restart :
            # apparition restart en cas de défaite
            pyxel.text(46,54,'GAME OVER', 7)
            pyxel.text(20,64,'Press "r" to restart', 7)
        
        # vies
        pyxel.text(2,2,'Vies restantes:'+str(vies),5)
    
        # niveau
        pyxel.text(94,2,'Niveau:'+str(niveau),5)
    
    # affichage scenario
    if scenario :
        if num_scenario == 3 :
            pyxel.text(5, 14,"Apres avoir survecu a cette ",7)
            pyxel.text(5, 24,"grande tempete de meteorite et",7)
            pyxel.text(5, 34,"au tremblement de terre sur",7)
            pyxel.text(5, 44,"la planete Alturion, l'immense",7)
            pyxel.text(5, 54,"Ara parvint a quitter cette",7)
            pyxel.text(5, 64,"planete et retourna chez",7)
            pyxel.text(5, 74,"lui avec sa famille et ses",7)
            pyxel.text(5, 84,"amis. Tout cela est grace a",7)
            pyxel.text(5, 94,"vous, il vous sera ainsi",7)
            pyxel.text(5, 104,"eternellement reconnaissant",7)
            pyxel.text(5, 114,"et ne vous oubliera jamais !",7)
        if num_scenario == 2 :
            pyxel.text(5, 14,"En achevant ce niveau sous ",7)
            pyxel.text(5, 24,"cette tempete de meteorites",7)
            pyxel.text(5, 34,"Ara a obtenu deux",7)  
            pyxel.text(5, 44,"tiers des pieces de son",7)
            pyxel.text(5, 54,"vaisseau ! Ses chances de",7)
            pyxel.text(5, 64,"revoir sa famille ont",7)
            pyxel.text(5, 74,"considerablement augmente :",7)
            pyxel.text(5, 84,"plus qu'une piece avant la",7)
            pyxel.text(5, 94,"delivrance ! Seulement, les",7)
            pyxel.text(5, 104,"dangers sont encore grands...",7)

            pyxel.text(5, 114,"Press A",7)
        if num_scenario == 1 :
            pyxel.text(5, 14,"La premiere mission a ete un",7)
            pyxel.text(5, 24,"succes. Ara se dirige",7) 
            pyxel.text(5, 34,"dorenavant vers le deuxieme",7) 
            pyxel.text(5, 44,"lieu. Recuperer cette piece le",7) 
            pyxel.text(5, 54,"rapprochera grandement de la",7) 
            pyxel.text(5, 64,"liberte.",7)  

            pyxel.text(5, 74,"Press A",7)
        if num_scenario == 0 :
            pyxel.text(5,14,"Apres un long voyage a travers", 7)
            pyxel.text(5,24,"l'espace, le pilote spatial,", 7)
            pyxel.text(5,34,"Ara, s'est crashe sur une", 7)
            pyxel.text(5,44,'planete perdue, appelee', 7)
            pyxel.text(5,54,'Alturion. Ara reprend', 7)
            pyxel.text(5,64,'connaissance et se lance a la', 7)
            pyxel.text(5,74,'recherche de differentes pieces', 7)
            pyxel.text(5,84,'pour reparer son vaisseau et', 7) 
            pyxel.text(5,94,'enfin retourner chez lui...', 7)
            pyxel.text(55,114,'press A', 7)
    
        
    


###########################################################

pyxel.run(update, draw)