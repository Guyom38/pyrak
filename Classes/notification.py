import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

class CNotification():
    NON_INITIALISE = 0
    INITIALISE = 1
    APPARITION = 2
    PAUSE = 3
    DISPARITION = 4
    TERMINE = 5
    
    def __init__(self, joueur, icone, texte, bandeau):
        self.joueur = joueur
        self.icone = icone
        self.texte = texte

        self.cycle = pygame.time.get_ticks()
        self.phases_de_jeu_apres = None
       
        self.animation_cycle = 0
        self.animation_y = VAR.EcranY - 100
        self.animation_x = 0
        self.animation_etape = CNotification.NON_INITIALISE
        self.animation_delais_pause = 1000

        self.couleur1 = pygame.Color(33,105,33,255)
        self.couleur2 = pygame.Color(105,74,64,255)
        self.couleur3 = pygame.Color(76,54,44,255)
        self.couleur4 = pygame.Color(64,64,64,32)
        self.couleur5 = pygame.Color(117,94,74,255)
        
        self.bandeau = bandeau
        if self.bandeau:
            self.max_mouvement_x = 300
            self.pas_mouvement_x = 64
            self.animation_delais_pause = 1200

            self.phases_de_jeu_apres = (VAR.phase_du_jeu, VAR.phase_du_jeu_suivant)
            VAR.phase_du_jeu = ENUM_Phase.BANDEAU
                
        else:
            self.max_mouvement_x = EcranX - VAR.notif_largeur
            self.pas_mouvement_x = 16
            self.animation_delais_pause = 5000
      

    def dessiner_notification(self):
        self.image = pygame.Surface((VAR.notif_largeur, VAR.notif_hauteur),pygame.SRCALPHA,32)  
        pygame.draw.rect(self.image, (32,32,32,200), (0,0, VAR.notif_largeur, VAR.notif_hauteur), 0)
        FCT.texte(self.image, self.texte, 8, 2, 20, (255, 255, 255, 255) )
        pygame.draw.rect(self.image, (64,64,64,200), (0,0, VAR.notif_largeur, VAR.notif_hauteur), 2)
    
    def dessiner_bandeau(self):
        pygame.draw.rect(VAR.fenetre, self.couleur2, (self.animation_x, self.animation_y -100, VAR.EcranX, 50), 0)
        pygame.draw.rect(VAR.fenetre, self.couleur2, (self.animation_x, self.animation_y -110, VAR.EcranX, 5), 0)
        pygame.draw.rect(VAR.fenetre, self.couleur3, (self.animation_x, self.animation_y -100, VAR.EcranX, 50), 2)
        pygame.draw.rect(VAR.fenetre, self.couleur3, (self.animation_x, self.animation_y -110, VAR.EcranX, 5), 2)
        FCT.texte(VAR.fenetre, self.texte, self.animation_x+30, self.animation_y -150, 60 )

    
    def afficher(self, y = -1):
        
        if y != -1: self.animation_y = y
        
        # --- Initialise le bandeau de titre
        if self.animation_etape in (CNotification.NON_INITIALISE, CNotification.TERMINE):
            
           
                
            self.animation_cycle = pygame.time.get_ticks()
            self.animation_x = VAR.EcranX
            self.animation_etape = CNotification.APPARITION

        # --- Anime le bandeau de titre
        if self.animation_etape == CNotification.APPARITION:
            if pygame.time.get_ticks() - self.animation_cycle > 1:
                self.animation_cycle = pygame.time.get_ticks()
                
                if self.animation_x > self.max_mouvement_x:
                    self.animation_x -= self.pas_mouvement_x
                else:
                    self.animation_etape = CNotification.PAUSE

        elif self.animation_etape == CNotification.PAUSE:
            if pygame.time.get_ticks() - self.animation_cycle > self.animation_delais_pause:
                self.animation_cycle = pygame.time.get_ticks()
                self.animation_etape = CNotification.DISPARITION
                    
        elif self.animation_etape == CNotification.DISPARITION:
            if pygame.time.get_ticks() - self.animation_cycle > 1:
                self.animation_cycle = pygame.time.get_ticks()
                
                if self.animation_x < VAR.EcranX:
                    self.animation_x += self.pas_mouvement_x
                else:
                   if self.bandeau == True:
                       VAR.phase_du_jeu, VAR.phase_du_jeu_suivant = self.phases_de_jeu_apres
                   self.animation_etape = CNotification.TERMINE

        if self.animation_etape != CNotification.TERMINE:
            if self.bandeau == True:
                self.dessiner_bandeau()
            else:
                if self.bandeau == False: 
                    self.dessiner_notification()
                VAR.fenetre.blit(self.image, (self.animation_x, self.animation_y))
            


        
