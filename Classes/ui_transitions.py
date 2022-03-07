  
import pygame
from pygame.locals import *


import variables as VAR
import fonctions as FCT
import outils

titre = ""
cercle = None

def transition_glisser(vertical): #1435
    i,j, largeur, cpt_cycle = 0, 1, 16, 0
    
    image_tmp = pygame.Surface((VAR.EcranX, VAR.EcranY),pygame.SRCALPHA,32)
    image_tmp.blit(VAR.fenetre, (0,0))

    boucle_transition = True
    while boucle_transition:
        if pygame.time.get_ticks() - cpt_cycle > 15:
            i = i + 16
            cpt_cycle = pygame.time.get_ticks() 
        
        if vertical:
            for ligne in range(int(VAR.EcranY/largeur)):
                j=FCT.iif(j == 1, -1, 1)
                VAR.fenetre.blit(image_tmp, (i * j , (ligne*largeur) ), (0, ligne*largeur, VAR.EcranX, largeur))
        else:
            for colonne in range(int(VAR.EcranX/largeur)):
                j=FCT.iif(j == 1, -1, 1)
                VAR.fenetre.blit(image_tmp, ( (colonne*largeur), i * j ), ( colonne*largeur, 0, largeur, VAR.EcranY))
                
        pygame.display.update()   
        if i > VAR.EcranX: 
            boucle_transition = False
            
            
def image_tourbillon(posCentre, rotation, couleur, largeur, offset):
    global cercle
    centreX, centreY = posCentre
    
    if cercle == None:
        cercle = outils.cercle_COS(centreX, centreY , VAR.EcranX)
        
    larg = int(360 / largeur)
    tmp_image = pygame.Surface((VAR.EcranX, VAR.EcranY), pygame.SRCALPHA)
    for j in range(0, larg):
        pos = (j * largeur) + rotation + offset
        i, i2 = outils.tour(pos), outils.tour(pos + (largeur-1))
        if j % 2 == 0:
            figure = (cercle[i], cercle[i2], (centreX, centreY ))
            pygame.draw.polygon(tmp_image, couleur, figure)
    return tmp_image



