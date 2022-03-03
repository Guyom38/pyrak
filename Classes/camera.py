import pygame
from pygame.locals import *

import variables as VAR
from variables import *
import outils
from Classes.class_bresenham import *

class CCamera():
    def __init__(self, moteur):
        self.moteur = moteur

        self.x = 0
        self.y = 0

        self.seDeplace = False
        self.listeDeplacement = []

        self.cycle = pygame.time.get_ticks() 
        self.vitesseDeplacement = 50


    def centrer_sur_joueur(self):
        self.recentrer(VAR.joueur_en_cours.x, VAR.joueur_en_cours.y)

    # --- Forcer le centrage de la camera sur les coordonnées
    def recentrer(self, x, y):
        self.x, self.y = x, y
        VAR.OffsetX = -((self.x * 9) * VAR.Zoom) + int((VAR.EcranX - VAR.v9) / 2)
        VAR.OffsetY = -((self.y * 9) * VAR.Zoom) + int((VAR.EcranY - VAR.v9) / 2)

    # --- retourner la position d'une coordonnee 
    def ou_est_le_joueur_sur_lecran(self, x, y):
        xC = -((x * 9) * VAR.Zoom) + int((VAR.EcranX - VAR.v9) / 2)
        yC = -((y * 9) * VAR.Zoom) + int((VAR.EcranY - VAR.v9) / 2)
        return (xC, yC)

    
    def deplacer(self, x, y):
        self.listeDeplacement = bresenham([self.x, self.y], self.ou_est_le_joueur_sur_lecran(x,y)).path
        self.seDeplace = True


    def gestion(self):
        if self.seDeplace == True:
            if pygame.time.get_ticks() - self.cycle > self.vitesseDeplacement: 
                if len(self.listeDeplacement) > 0:
                    self.x, self.y = self.listeDeplacement[0]
                    self.listeDeplacement.remove(self.listeDeplacement[0])
                else:
                    self.seDeplace == False
                
                self.cycle = pygame.time.get_ticks()

