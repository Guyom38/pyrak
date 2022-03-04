import pygame
from pygame.locals import *

import variables as VAR
import fonctions as FCT

class CNotification():
    def __init__(self, joueur, icone, texte):
        self.joueur = joueur
        self.icone = icone
        self.texte = texte

        self.cycle = pygame.time.get_ticks()
        self.dessiner()

    def dessiner(self):
        self.image = pygame.Surface((VAR.notif_largeur, VAR.notif_hauteur),pygame.SRCALPHA,32)  
        pygame.draw.rect(self.image, (32,32,32,200), (0,0, VAR.notif_largeur, VAR.notif_hauteur), 0)
        FCT.texte(self.image, self.texte, 8, 2, 20, (255, 255, 255, 255) )
        pygame.draw.rect(self.image, (64,64,64,200), (0,0, VAR.notif_largeur, VAR.notif_hauteur), 2)
          


        
