 
 
import pygame
from pygame.locals import *
import random
import math

import fonctions as FCT
import Classes.ui_transitions as UI

if 1 == 0:
    pygame.init()
    fenetre = pygame.display.set_mode((1280, 800), pygame.DOUBLEBUF, 32)

    pygame.display.set_caption("PyRAK vtest")
    clock = pygame.time.Clock()

    img = pygame.image.load("images\\mechants\\icones.png")

    j,k=0,0

    animation_cycle = pygame.time.get_ticks()
    arret_tirage_cycle = pygame.time.get_ticks()
    tirage_delais = 3000
    choix = random.randint(0, 8)
    tirage = True

    boucle_active = True
    while boucle_active:
        fenetre.fill((32,32,32,255))
        for event in pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                boucle_active = False
        
        # --- Tourbillons
        fenetre.blit(UI.image_tourbillon(fenetre, (640, 500), k % 358, (16,16,16), 20, 0 ),(0,0))
        fenetre.blit(UI.image_tourbillon(fenetre, (640, 500), -(k % 358), (40,40,40), 7, 20 ),(0,0))
        
        # --- Cadre
        pygame.draw.rect(fenetre, (0,0,0,255), (0, 390, 1280, 200), 0)
        pygame.draw.rect(fenetre, (16,16,16,255), (0, 400, 1280, 180), 0)
        
        # --- Liste des monstres
        for i in range(13):
            resultat = ((i+j) % 9)
            fenetre.blit(FCT.image_decoupe(img, resultat, 0, 100, 100), (i*100, 435))

        # --- Fleches en mouvements
        mouvement =  ((j%3) * 8)
        pygame.draw.polygon(fenetre, (0,0,0,255), ((600, 360 +mouvement), (700, 360 +((j%3) * 5)), (650, 450 +mouvement)))
        pygame.draw.polygon(fenetre, (16,16,16,255), ((620, 370 +mouvement), (680, 370 +((j%3) * 5)), (650, 430 +mouvement)))

        pygame.draw.polygon(fenetre, (0,0,0,255), ((600, 620 -mouvement), (700, 620 -mouvement), (650, 525 -mouvement)))
        pygame.draw.polygon(fenetre, (16,16,16,255), ((620, 610 -mouvement), (680, 610 -mouvement), (650, 545 -mouvement)))

        
        if tirage == True:
            if pygame.time.get_ticks() - animation_cycle > 150 :            # --- Tempo de l'animation
                j = j +1 
                animation_cycle = pygame.time.get_ticks()
            
            if pygame.time.get_ticks() - arret_tirage_cycle > tirage_delais:            # --- Arret de la roulette sur le monstre selectionné
                resultat = (((6+j) % 9) == choix)       # --- 6 = position de l'image selectionnée
                if resultat == True:
                    tirage = False
                
            
        pygame.display.update()
        clock.tick(25)

    pygame.quit() 