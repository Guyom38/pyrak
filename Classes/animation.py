import pygame
from pygame.locals import *

class CAnimation():
    def __init__(self, delais):
        self.delais = delais
        self.timer = pygame.time.get_ticks()
        self.cpt = 0
        
    def cycle(self):
        if pygame.time.get_ticks() - self.timer > self.delais:
            self.cpt += 1
            self.timer = pygame.time.get_ticks()
            return True
            
        return False
    
    def position(self, modulo):
        return self.cpt % modulo