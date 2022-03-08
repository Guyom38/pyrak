import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

import random
import math

class CCombat():
    def __init__(self):
        print("    + Initialisation module << Combats >>")
        
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
        self.message_fin_de_combat = ""

        self.mode_magie = False
        self.magies_selectionnees = [None, None, None]

    def lancer_les_des(self):
        self.combat_termine = False
        self.de1 = random.randint(0,5)
        self.de2 = random.randint(0,5)

        
    def afficher(self):
        x, y, w, h = 128, 128, VAR.EcranX - 254, VAR.EcranY - 256
        img_clignotte = (VAR.combat.combat_termine == False or (self.cpt % 2 == 1))
        
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
        img_hero = FCT.iif(img_clignotte == True and self.calcul_qui_gagne() == -1, VAR.joueur_en_cours.masque, VAR.joueur_en_cours.image)
        tmp = pygame.transform.scale(img_hero, (img_hero.get_width(), img_hero.get_height() + t))
        xP1, yP1 = x+32, y+h-tmp.get_height()-32
        
        if self.de1 != -1 and self.de2 != -1:
            points_attaques = self.calcul_attaque()
            FCT.texte(VAR.fenetre, str(points_attaques), xP1+img_hero.get_width()-30, yP1 - 70, 120)
            
            
        VAR.fenetre.blit(tmp, (xP1, yP1))
        
        # ---------------------------------------------------------------------
        # --- dessin du mechant
        t = int(5 * math.cos (self.cpt))
        img2 = FCT.iif(img_clignotte == True and self.calcul_qui_gagne() == 1, VAR.mechants.liste[self.jeton.id].masque, VAR.mechants.liste[self.jeton.id].image)
 
        tmp = pygame.transform.flip(pygame.transform.scale(img2, (img2.get_width(), img2.get_height() + t)), True, False) 
        xP2, yP2 = x+w-tmp.get_width()-32, y+h-tmp.get_height()-32
        
        FCT.texte(VAR.fenetre, str(self.jeton.force), xP2-30, yP2 - 70, 120)
        VAR.fenetre.blit(tmp, (xP2, yP2))
        
        # ---------------------------------------------------------------------
        # --- dessin des dés
        self.animation_des_des()
        
        x = x+img_hero.get_width()
        if self.de1 != -1 and self.de2 != -1:
            for des, id, xD, yD in ((self.de1, 1, 12, 216), (self.de2, 2, 52, 186)):
                dd = FCT.image_decoupe(VAR.des, des, id, 85, 85)
                VAR.fenetre.blit(dd, (x+xD, y+h-yD))
              


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
    
    
    def calcul_qui_gagne(self):
        if VAR.combat.combat_termine == False: return -2
        
        if self.calcul_attaque() > self.jeton.force:
            return 1
        elif self.calcul_attaque() == self.jeton.force:
            return 0
        elif self.calcul_attaque() < self.jeton.force:
            return -1
            

    def gestion_combat(self):
        if VAR.combat.combat_termine == True:
            
            if self.resultat_cycle == 0:                      # --- Applique une seule fois le resultat du combat
                resultat = self.calcul_qui_gagne()
                if resultat == 1:
                    x, y = VAR.joueur_en_cours.x, VAR.joueur_en_cours.y
                    VAR.terrain[x][y].recompense = VAR.terrain[x][y].jeton.recompense
                    VAR.terrain[x][y].jeton = None
                    self.message_fin_de_combat = "remporte le combat"
                    VAR.joueur_en_cours.gestion_reaction_sur_place()
                    
                elif resultat == 0:
                    self.message_fin_de_combat = "repart brodouille"
                    VAR.joueur_en_cours.demi_tour()

                elif resultat == -1:
                    self.message_fin_de_combat = "perd un point de vie"
                    VAR.joueur_en_cours.se_prend_un_coup()
                    VAR.joueur_en_cours.demi_tour()
                
                self.resultat_cycle = pygame.time.get_ticks()
            
            # --- Pause de 3s avant de revenir au jeu
            if pygame.time.get_ticks() - self.resultat_cycle > 2000:      
                VAR.phase_du_jeu = ENUM_Phase.TRANSITION
                VAR.phase_du_jeu_suivant = ENUM_Phase.DEPLACEMENT
                VAR.notifications.ajouter(VAR.joueur_en_cours, "COMBAT", VAR.joueur_en_cours.nom + " " + self.message_fin_de_combat)


        
    
    
    