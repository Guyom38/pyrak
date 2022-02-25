import pygame
from pygame.locals import *

import variables as VAR
import fonctions as FCT

class Chero(object):
    def __init__(self, nom, id):
        
        self.animationCycle = 0
        self.animationCpt = 0
        
        self.nom = nom
        self.id = id
        self.vie = 5
        self.mouvement = 4
        self.pouvoirs = [0,0]
        
        self.armes = [0,0,0]
        self.magies = [0,0,0]
        self.cle = False
        self.maudit = False

        self.x = VAR.posPieceCentrale[0]
        self.y = VAR.posPieceCentrale[1]

        self.deplaceX = 0
        self.deplaceY = 0
        self.deplaceVitesse = 1
        self.seDeplace = False
        self.direction = 0
      
    def deplacer(self, x, y):
        if self.mouvement < 1: return False
        self.mouvement = self.mouvement -1
        self.x, self.y = x, y
        

    def recentrer_camera(self):
        VAR.OffsetX = 0-(((self.x) * 9) * VAR.Zoom) + int((VAR.EcranX - VAR.v9) / 2)
        VAR.OffsetY = 0-(((self.y) * 9) * VAR.Zoom) + int((VAR.EcranY - VAR.v9) / 2)
        
    def afficher(self):
        t = VAR.heros.cpt % 3
        x = VAR.OffsetX + (((self.x * 9)+4) * VAR.Zoom) + self.deplaceX - 8
        y = VAR.OffsetY + (((self.y * 9)+4) * VAR.Zoom) + self.deplaceY - 8
        
        VAR.fenetre.blit(FCT.image_decoupe(VAR.perso, (self.id * 3) +t, 0, 32, 32), (x, y))
        #VAR.fenetre.blit(self.image, (VAR.OffsetX + ((xX * 9)  * VAR.Zoom), VAR.OffsetY + ((yY * 9) * VAR.Zoom), VAR.Zoom, VAR.Zoom))
        #pygame.draw.rect(VAR.fenetre, pygame.Color(0,255,0,255), (VAR.OffsetX + (((self.x * 9)+4) * VAR.Zoom) + self.deplaceX, VAR.OffsetY + (((self.y * 9)+4) * VAR.Zoom) + self.deplaceY, VAR.Zoom, VAR.Zoom))
