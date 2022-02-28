import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

import random
import math

class CCombat():
    def __init__(self, moteur):
        print("    + Initialisation module << Combats >>")
        
        self.moteur = moteur
        self.jeton = None
        self.preparer_combat()


    def preparer_combat(self):
        
        self.cpt_cycle = 0
        self.cpt = 0
        
        self.lance_de_des = False
        self.de1, self.de2 = -1, -1
        self.combat_termine = False

        self.de_cycle = 0
        self.resultat_cycle = 0
      
        self.nombre_lances = 0
        self.nombre_lances_max = 30
        


    def lancer_les_des(self):
        self.combat_termine = False
        self.de1 = random.randint(0,5)
        self.de2 = random.randint(0,5)

        
    def afficher(self):
        x, y, w, h = 128, 128, VAR.EcranX - 254, VAR.EcranY - 256
        
        # --- Rythme animation
        if pygame.time.get_ticks() - self.cpt_cycle > 150:
            self.cpt = self.cpt + 1
            self.cpt_cycle = pygame.time.get_ticks() 

        # --- Cadre
        VAR.fenetre.blit(pygame.transform.scale(VAR.img0, (w-16, h-16)), (x, y))
        
         # --- Barre titre
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (x, y, w, 50), 0)
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (x, y+55, w, 5), 0)
        
        txt = "Veuillez lancer les dés."
        FCT.texte(VAR.fenetre, txt, x+20, y+20, 20, pygame.Color(0,0,0,255))
        FCT.texte(VAR.fenetre, txt, x+20+2, y+20+2, 20, pygame.Color(255,255,255,255))
        
        # --- Cadre
        VAR.fenetre.blit(VAR.objets_interface.cadre(0, 0, w, h), (x, y))
        
        # ---------------------------------------------------------------------
        # --- dessin de joueur en cours
        t = int(3 * math.cos (self.cpt+3))
        tmp = pygame.transform.scale(VAR.img1, (VAR.img1.get_width(), VAR.img1.get_height() + t))
        xP1, yP1 = x+32, y+h-tmp.get_height()-32
        
        if self.de1 != -1 and self.de2 != -1:
            points_attaques = self.calcul_attaque()
            FCT.texte(VAR.fenetre, str(points_attaques), xP1+VAR.img1.get_width()-30, yP1 - 70, 120)
            
            
        VAR.fenetre.blit(tmp, (xP1, yP1))
        
        # ---------------------------------------------------------------------
        # --- dessin du mechant
        t = int(5 * math.cos (self.cpt))
        
        if VAR.combat.combat_termine == False or (self.cpt % 2 == 1):
            img2 = VAR.mechants.liste[self.jeton.id].image
        else:
            img2 = VAR.mechants.liste[self.jeton.id].masque
        
        tmp = pygame.transform.flip(pygame.transform.scale(img2, (img2.get_width(), img2.get_height() + t)), True, False) 
        xP2, yP2 = x+w-tmp.get_width()-32, y+h-tmp.get_height()-32
        
        FCT.texte(VAR.fenetre, str(self.jeton.force), xP2-30, yP2 - 70, 120)
        VAR.fenetre.blit(tmp, (xP2, yP2))
        
        # ---------------------------------------------------------------------
        # --- dessin des dés
        self.animation_des_des()
        
        x = x+VAR.img1.get_width()
        if self.de1 != -1 and self.de2 != -1:
            for des, id, xD, yD in ((self.de1, 1, 12, 286), (self.de2, 2, 52, 256)):
                dd = FCT.image_decoupe(VAR.des, des, id, 85, 85)
                VAR.fenetre.blit(dd, (x+xD, w-yD))


    def animation_des_des(self):
        if self.lance_de_des == True and (pygame.time.get_ticks() - self.de_cycle > 150):
            self.de_cycle = pygame.time.get_ticks()
            self.lancer_les_des()
            
            self.nombre_lances = self.nombre_lances +1
            if self.nombre_lances > self.nombre_lances_max: 
                self.lance_de_des = False
                self.combat_termine = True


    def calcul_attaque(self):
        bonus = 0
        for i in range(2):
            if VAR.joueur_en_cours.armes[i] != None:
                bonus = bonus + int(VAR.joueur_en_cours.armes[i].split("+")[1])
        return (self.de1+self.de2+2) +bonus  
        

    def gestion_combat(self):
        if VAR.combat.combat_termine == True:
            
            if self.resultat_cycle == 0:                      # --- Applique une seule fois le resultat du combat
                if self.calcul_attaque() > self.jeton.force:
                    x, y = VAR.joueur_en_cours.x, VAR.joueur_en_cours.y
                    VAR.terrain[x][y].recompense = VAR.terrain[x][y].jeton.recompense
                    VAR.terrain[x][y].jeton = None
                    print ("Gagné : " + str(VAR.terrain[x][y].recompense))
                
                elif self.calcul_attaque() == self.jeton.force:
                    print ("Exequo")
                    VAR.joueur_en_cours.demi_tour()

                elif self.calcul_attaque() < self.jeton.force:
                    print ("Perdu")
                    VAR.joueur_en_cours.se_prend_un_coup()
                    VAR.joueur_en_cours.demi_tour()
                
                self.resultat_cycle = pygame.time.get_ticks()
            
            # --- Pause de 3s avant de revenir au jeu
            if pygame.time.get_ticks() - self.resultat_cycle > 3000:      
                VAR.phase_du_jeu = ENUM_Phase.TRANSITION
                VAR.phase_du_jeu_suivant = ENUM_Phase.DEPLACEMENT


        
    
    
    