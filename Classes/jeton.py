import pygame
from pygame.locals import *

import fonctions as FCT
import variables as VAR
import outils


class CJeton(object):
    def __init__(self, moteur, id):
        self.moteur = moteur
        
        self.id = id
        self.x, self.y = 0, 0

        img_id, self.force, self.nom, self.recompense = VAR.jetons.charger_proprietes(id)
        self.image = FCT.image_decoupe(VAR.icones_mechants, img_id , 0, 100, 100, VAR.v5, VAR.v5)
        
    def afficher(self):
        pass
        
        
        