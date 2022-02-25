import pygame
from pygame.locals import *

import variables as VAR
import fonctions as FCT


class CObjet():
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        
        self.icone = FCT.image_decoupe( VAR.objets.image_icones, int(id), 0, VAR.objets.image_icone_x, VAR.objets.image_icone_y )
