import pygame
from pygame.locals import *

import variables as VAR
import fonctions as FCT
import outils

class CObjets_Interface():
    def __init__(self, moteur):
        self.moteur = moteur
    
    def zone_clickable(self, xP, yP, dimX, dimY, bouton):
        clic = VAR.ENUM_Clic.Rien
        if self.moteur.mX >= xP and self.moteur.mX <= xP + dimX and self.moteur.mY >= yP and self.moteur.mY <= yP + dimY:
            clic = VAR.ENUM_Clic.Survol
            if FCT.clic(bouton, 300) == True:
                clic = VAR.ENUM_Clic.Clic
                FCT.reset_clic()
            pygame.draw.rect(VAR.fenetre, pygame.Color(255,0,0,255), (xP, yP, dimX,dimY), 8)
        return clic
        
    def afficher_bouton_image(self, xP, yP, image, bouton = 0):
        wIco, hIco = image.get_width(), image.get_height()
        clic = self.zone_clickable(xP, yP, wIco, hIco, bouton)
        VAR.fenetre.blit(image, (xP, yP, wIco, hIco))
        return clic
                
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