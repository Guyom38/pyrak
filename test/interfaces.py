import pygame
from pygame.locals import *

import variables as VAR
import outils

class CInterfaces():
    def __init__(self, moteur):
        self.moteur = moteur
        
    def afficher_cadre_heros(self):
        largInterf = 200
        
        scX, scY = pygame.display.get_surface().get_size()
        pX = scX - largInterf
        pY = 0

        pygame.Surface.fill(VAR.fenetre, pygame.Color(64,64,64,32), (pX, pY, largInterf, scY))

    def afficher(self):
        if VAR.image_interface is None:
            VAR.image_interface  = self.cadre(0,0, VAR.EcranX, VAR.EcranY)
            
            
        VAR.fenetre.blit(VAR.image_interface, (0, 0))
        
    def cadre(self, x, y, dimX, dimY):
        tmp = pygame.Surface((dimX, dimY),pygame.SRCALPHA,32)
        maxL, maxH = int(dimX / VAR.Taille), int(dimY / VAR.Taille)

        tX, tY = outils.correspondance("AM")
        for i in range(1, maxL -1):
            tmp.blit(VAR.texture, (i * VAR.Taille,0), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
            tmp.blit(VAR.texture, (i * VAR.Taille, (int(dimY / VAR.Taille)-1) * VAR.Taille), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
        
        tX, tY = outils.correspondance("4M")
        for i in range(1, maxH -1):
            tmp.blit(VAR.texture, (0, i * VAR.Taille), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
            tmp.blit(VAR.texture, ((int(dimX/ VAR.Taille)-1) * VAR.Taille, i * VAR.Taille), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))

        tX, tY = outils.correspondance("1L")
        tmp.blit(VAR.texture, (0,0), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
        tX, tY = outils.correspondance("2L")
        tmp.blit(VAR.texture, ((maxL-1) * VAR.Taille, 0), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
        tX, tY = outils.correspondance("8M")
        tmp.blit(VAR.texture, (0,(maxH-1)* VAR.Taille), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
        tX, tY = outils.correspondance("9M")
        tmp.blit(VAR.texture, ((maxL-1)* VAR.Taille,(maxH-1)* VAR.Taille), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
        
        return tmp