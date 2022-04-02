import pygame
from pygame.locals import *

import classes.commun.fonctions as FCT
import variables as VAR


class CJeton(object):
    def __init__(self, id, monstre):
        
        self.id = id
        self.x, self.y = 0, 0

        self.force = monstre.force
        self.nom = monstre.nom
        self.recompense = monstre.recompense

        self.image = FCT.image_decoupe(VAR.icones_mechants, id , 0, 100, 100, VAR.v5, VAR.v5)
