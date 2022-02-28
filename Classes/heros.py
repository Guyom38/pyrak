import pygame
from pygame.locals import *

from Classes.hero import *

import variables as VAR
import fonctions as FCT


class Cheros():
    def __init__(self, moteur):
        print("    + Initialisation module << Heros >>")
        
        self.liste = []
        self.joueur_liste_position = 0
        self.moteur = moteur
        
        self.cpt_cycle = 0
        self.cpt = 0

    def charger(self):
        self.liste.append( Chero("Argentus", 1))
        self.liste.append( Chero("Horan", 2))    
        self.liste.append( Chero("Lord Xanros", 3))
        #self.liste.append( Chero("Taia", 4))
        #self.liste.append( Chero("Victorius", 5))
        #self.liste.append( Chero("Aderyn", 6))

    def gestion_deplacement_joueur(self):
        if VAR.joueur_en_cours.seDeplace == True: 
            VAR.joueur_en_cours.gestion_deplacement()
        
        elif VAR.joueur_en_cours.mouvement == 0: 
            self.joueur_suivant()
            

    def afficher_sur_zone(self, x, y): 
        for hero in self.liste:
            if hero.x == x and hero.y == y:
                hero.afficher()
                
    def afficher(self):
        if pygame.time.get_ticks() - self.cpt_cycle > 150:
            self.cpt = self.cpt + 1
            self.cpt_cycle = pygame.time.get_ticks() 
                
        for x in range(len(VAR.terrain)):
            for y in range(len(VAR.terrain[x])):
                xP, yP = VAR.OffsetX + ((x * VAR.Zoom) * 9), (VAR.OffsetY + (y * VAR.Zoom) * 9)
                if FCT.SurEcran(xP, yP, VAR.v9, VAR.v9) == True:
                    VAR.heros.afficher_sur_zone(x, y)


    def joueur_suivant(self):
        if self.joueur_liste_position < len(self.liste) -1:
            self.joueur_liste_position = self.joueur_liste_position +1
        else:
            self.joueur_liste_position = 0

        VAR.joueur_en_cours = self.liste[self.joueur_liste_position]
        VAR.joueur_en_cours.mouvement = 4
        VAR.joueur_en_cours.recentrer_camera()


