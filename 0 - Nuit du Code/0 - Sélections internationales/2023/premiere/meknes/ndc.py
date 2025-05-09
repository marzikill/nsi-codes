import pyxel

# Définition des constantes
LARGEUR_ECRAN = 128
HAUTEUR_ECRAN = 128
LARGEUR_JOUEUR = 16
HAUTEUR_JOUEUR = 16
LARGEUR_PLATEFORME = 82
HAUTEUR_PLATEFORME = 10
REPULSION = 10
joueur_gagnant=0
orientation_j1=0
orientation_j2=1

#pyxel.sound(0).set("e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr", "p", "6", "vffn fnff vffs vfnn", 25,)


# Variables pour les joueurs
joueur1_x = 30
joueur1_y = 50
joueur1_couleur = 9
joueur1_saut = False
joueur1_vitesse_saut = 4
joueur1_vitesse_chute = 6

joueur2_x = 90
joueur2_y = 50
joueur2_couleur = 14
joueur2_saut = False
joueur2_vitesse_saut = 4
joueur2_vitesse_chute = 6

# Variables pour la plateforme
plateforme_x = 21
plateforme_y = 90

lancer = False
ecran_fini = False
pyxel.init(LARGEUR_ECRAN, HAUTEUR_ECRAN ,title="SUMO CLASH")
pyxel.load("ressources.pyxres")

pyxel.sound(1).set("a3","p", "6", "v", 25)
pyxel.sound(2).set("c2d2e2f2g2a2b2c3d3e3f3g3a3b3c4d4e4f4g4a4","p", "6", "v", 8)

def update():
    global joueur1_x, joueur1_y, joueur1_saut, joueur1_vitesse_saut, joueur1_vitesse_chute , ecran_fini, joueur_gagnant, orientation_j1
    global joueur2_x, joueur2_y, joueur2_saut, joueur2_vitesse_saut, joueur2_vitesse_chute, orientation_j2

    if lancer == False:
        pyxel.mouse(True)
    else :
        pyxel.mouse(False)


    # Gérer le mouvement horizontal du joueur 1    
    if pyxel.btn(pyxel.KEY_Q):
        joueur1_x -= 2    
        orientation_j1=1      
    if pyxel.btn(pyxel.KEY_D):
        joueur1_x += 2 
        orientation_j1=0
    if pyxel.btn(pyxel.KEY_Z):
        if not joueur1_saut:
            joueur1_saut = True
            joueur1_vitesse_saut = 3

    # Gérer le mouvement vertical du joueur 1 (saut et chute)
    if joueur1_saut:
        joueur1_y -= joueur1_vitesse_saut
        joueur1_vitesse_saut -= 0.15
        if joueur1_vitesse_saut < -4:
            joueur1_saut = False
            joueur1_vitesse_saut = 4
    else:
        joueur1_y += joueur1_vitesse_chute
        joueur1_vitesse_chute += 0.15
        
    # Gérer les collisions du joueur 1 avec la plateforme
    if joueur1_y + HAUTEUR_JOUEUR >= plateforme_y and joueur1_y + HAUTEUR_JOUEUR <= plateforme_y + HAUTEUR_PLATEFORME and \
            joueur1_x + LARGEUR_JOUEUR >= plateforme_x and joueur1_x <= plateforme_x + LARGEUR_PLATEFORME:
        joueur1_y = plateforme_y - HAUTEUR_JOUEUR
        joueur1_vitesse_chute = 0
        

    # Gérer le mouvement horizontal du joueur 2
    if pyxel.btn(pyxel.KEY_LEFT):
        joueur2_x -= 2
        orientation_j2=1
    if pyxel.btn(pyxel.KEY_RIGHT):
        joueur2_x += 2
        orientation_j2=0
    if pyxel.btn(pyxel.KEY_UP):
        if not joueur2_saut:
            joueur2_saut = True
            joueur2_vitesse_saut = 3

    # Gérer le mouvement vertical du joueur 2 (saut et chute)
    if joueur2_saut:
        joueur2_y -= joueur2_vitesse_saut
        joueur2_vitesse_saut -= 0.15
        if joueur2_vitesse_saut < -4:
            joueur2_saut = False
            joueur2_vitesse_saut = 4
    else:
        joueur2_y += joueur2_vitesse_chute
        joueur2_vitesse_chute += 0.15

    # Gérer les collisions du joueur 2 avec la plateforme
    if joueur2_y + HAUTEUR_JOUEUR >= plateforme_y and joueur2_y + HAUTEUR_JOUEUR <= plateforme_y + HAUTEUR_PLATEFORME and \
            joueur2_x + LARGEUR_JOUEUR >= plateforme_x and joueur2_x <= plateforme_x + LARGEUR_PLATEFORME:
        joueur2_y = plateforme_y - HAUTEUR_JOUEUR
        joueur2_vitesse_chute = 0

    # Pousser le joueur 2 si la touche S est enfoncée par le joueur 1
    if pyxel.btn(pyxel.KEY_DOWN):
        if orientation_j2==0:
            if joueur2_x - REPULSION <= joueur1_x <= joueur2_x + REPULSION and joueur2_y - REPULSION <= joueur1_y <= joueur2_y + REPULSION:
                joueur1_x += REPULSION
                pyxel.play(0, 1)
                

        else:
            if joueur2_x - REPULSION <= joueur1_x <= joueur2_x + REPULSION and joueur2_y - REPULSION <= joueur1_y <= joueur2_y + REPULSION:
                joueur1_x += -REPULSION
                pyxel.play(0, 1)

    # Pousser le joueur 1 si la touche flèche bas est enfoncée par le joueur 2
    if pyxel.btn(pyxel.KEY_S):
        if orientation_j1==0:
            if joueur1_x - REPULSION <= joueur2_x <= joueur1_x + REPULSION and joueur1_y - REPULSION <= joueur2_y <= joueur1_y + REPULSION:
                joueur2_x += REPULSION
                pyxel.play(0, 1)
        else:
            if joueur1_x - REPULSION <= joueur2_x <= joueur1_x + REPULSION and joueur1_y - REPULSION <= joueur2_y <= joueur1_y + REPULSION:
                joueur2_x += -REPULSION
                pyxel.play(0, 1)


     # Vérifier si les joueurs sont sortis de la fenêtre
    if joueur1_x < 0 or joueur1_x + LARGEUR_JOUEUR > LARGEUR_ECRAN or joueur1_y < 0 or joueur1_y + HAUTEUR_JOUEUR > HAUTEUR_ECRAN:
        joueur_gagnant=2
        joueur1_x = -100
        joueur1_y = -100
        ecran_fini = True
        pyxel.play(0, 2)
        ecran_fin()

    if joueur2_x < 0 or joueur2_x + LARGEUR_JOUEUR > LARGEUR_ECRAN or joueur2_y < 0 or joueur2_y + HAUTEUR_JOUEUR > HAUTEUR_ECRAN:
        joueur_gagnant=1
        joueur2_x = -100
        joueur2_y = -100
        ecran_fini = True
        pyxel.play(0, 2)
        ecran_fin()


def draw():
    global lancer , ecran_fini
    pyxel.cls(0)
    
    # Ecran d'accueil
    if lancer == False :
        pyxel.rect(0,0,128,128,7)
        pyxel.blt(45,55,2,0,0,39,39)
        pyxel.text(2, 104, "Appuyez sur D pour la documentation", 1)
        pyxel.text(10, 84, "Cliquez sur PLAY pour jouer", 1)
        ecran_debut()
        if pyxel.mouse_x  in range(45,85) and pyxel.mouse_y in range(55,70) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) == True:
            lancer = True
    else:
    
        # fond bleu
        pyxel.rect(0,0,128,128,6)
        # joueur 1
        if orientation_j1==0:
            pyxel.blt(joueur1_x, joueur1_y, 0, 0, 0, 16, 16 )
        else:
            pyxel.blt(joueur1_x, joueur1_y, 0, 0, 0, -16, 16 )
        # joueur 2
        if orientation_j2==0:
            pyxel.blt(joueur2_x, joueur2_y, 0, 16, 0, 16, 16)
        else:
            pyxel.blt(joueur2_x, joueur2_y, 0, 16, 0, -16, 16 )
        # plateform
        pyxel.blt(plateforme_x, plateforme_y, 0, 0, 16, 87, 87 )
        # lave
        pyxel.blt(0, 118, 1, 0, 0, 128, 128 )
    
    if ecran_fini == True :
        pyxel.rect(0,0,128,128,7)
        pyxel.text(12, 44, "Jeu fini", 1)
        pyxel.text(12, 64, "Appuyez sur R pour relancer", 1)
        pyxel.text(12, 84, "Gagnant: Joueur {}".format(joueur_gagnant), 1)




def ecran_fin():
    global ecran_fini, lien
    ecran_fini=True
    if pyxel.btn(pyxel.KEY_R):
        reset()

def ecran_debut():
    global lien
    if pyxel.btn(pyxel.KEY_D):
        webbrowser.open(lien)

def reset():
    global joueur1_x, joueur1_y, joueur1_saut, joueur1_vitesse_saut, joueur1_vitesse_chute, ecran_fini
    global joueur2_x, joueur2_y, joueur2_saut, joueur2_vitesse_saut, joueur2_vitesse_chute

    ecran_fini = False

    joueur1_x = 30
    joueur1_y = 50
    joueur1_saut = False
    joueur1_vitesse_saut = 4
    joueur1_vitesse_chute = 0

    joueur2_x = 90
    joueur2_y = 50
    joueur2_saut = False
    joueur2_vitesse_saut = 4
    joueur2_vitesse_chute = 0

    
#pxyel.play()
pyxel.run(update, draw)
