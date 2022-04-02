import pygame
from pygame.locals import *

import variables as VAR

import classes.ui.ui_transitions as CT
import classes.ui.notification as CN


class CRecompense():
    def __init__(self):
        print("    + Initialisation module << Recompense >>")
    
    def afficher(self):
        j, k = 0, 0

        animation_cycle = pygame.time.get_ticks()
        arret_tirage_cycle, tirage_delais, tirage = pygame.time.get_ticks(), 3000, True

        centreX, centreY = int(VAR.EcranX / 2), int(VAR.EcranY /2)
        centreCadreY = 200

        VAR.notifications.initialiser_bandeau(VAR.joueur_en_cours.nom + ", gagne un coffre !")

        boucle_active = True
        while boucle_active:
            VAR.fenetre.fill((0,165,200,255))
            
            for event in pygame.event.get():        
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    VAR.boucle_principale = False
                    boucle_active = False
            
            # --- Tourbillons
            VAR.fenetre.blit(CT.image_tourbillon((centreX, centreY), k % 358, (34,202,238), 20, 0 ),(0,0))
            
            #VAR.fenetre.blit(TRANSITION.image_tourbillon((centreX, centreY), -(k % 358), (40,40,40), 7, 20 ),(0,0))
            
            VAR.fenetre.blit(VAR.IMG["coffre_ouvert"], (centreX-100, centreY-100))

            VAR.notifications.afficher()
            
            if VAR.notifications.bandeau.animation_etape == CN.CNotification.TERMINE:
                VAR.phase_du_jeu = VAR.ENUM_Phase.DEPLACEMENT
                boucle_active = False

            k=k+1
            pygame.display.update()
            VAR.clock.tick(VAR.nombreImageSeconde)