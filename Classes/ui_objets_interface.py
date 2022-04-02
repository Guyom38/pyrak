import pygame
from pygame.locals import *

import variables as VAR
import fonctions as FCT
import outils
import Classes.class_bresenham as CB


class CObjets_Interface():
    def __init__(self):
        self.couleurTraces = pygame.Color(255,255,0,255)
    
    def zone_clickable(self, x, y, dimX, dimY, bouton):
        clic = VAR.ENUM_Clic.Rien
        if VAR.mX >= x and VAR.mX <= x + dimX and VAR.mY >= y and VAR.mY <= y + dimY:
            clic = VAR.ENUM_Clic.Survol
            if FCT.clic(bouton, 300) == True:
                clic = VAR.ENUM_Clic.Clic
                FCT.reset_clic()
            pygame.draw.rect(VAR.fenetre, pygame.Color(255,0,0,255), (x, y, dimX,dimY), (VAR.cpt % 6)+2)
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
    
    def tracer_pointilles_entre_joueur_et_inventaire(self, xP, yP, dimX, dimY):
        xT, yT = VAR.OffsetX + ((VAR.joueur_en_cours.x * 9)  * VAR.Zoom) + VAR.v2, VAR.OffsetY + ((VAR.joueur_en_cours.y * 9) * VAR.Zoom) + VAR.v2
        xM, yM = (xT -xP) /2, (yT -yP)  /2
        d2 = dimX / 2

        trajets = []
        trajets.append(CB.bresenham([xT+d2, yT+dimY], [xT+d2, yT+dimY-yM]).path)      #      |
        trajets.append(CB.bresenham([xT+d2, yT+dimY-yM], [xP+d2, yT+dimY-yM]).path)   #      -----
        trajets.append(CB.bresenham([xP+d2, yT+dimY-yM], [xP+d2, yP]).path)           #          |

        debut = (xP, yP, dimX, dimY)
        fin = (xT, yT, dimX, dimY)
        self.calculer_trajet_pointille(debut, fin, trajets)

    def calculer_trajet_pointille(self, debut, fin, trajets):
        p = 0
        for tr in trajets:
            for pts in tr:

                if p %8 == (VAR.cpt %8): pygame.draw.rect(VAR.fenetre, self.couleurTraces, (pts[0]-2, pts[1]-2, 4, 4), 0)
                p += 1
        
        pygame.draw.rect(VAR.fenetre, self.couleurTraces, debut, 4)
        pygame.draw.rect(VAR.fenetre, self.couleurTraces, fin, 4)
            