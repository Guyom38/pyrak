import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

import outils

from Classes.ui_barre_lateral import *
from Classes.ui_objets_interface import *


class CInterfaces():
    def __init__(self, moteur):
        print("    + Initialisation module << Interface >>")
        
        self.moteur = moteur
        self.menu = CBarre_Laterale(moteur)
        
        
    def afficher_cadre_heros(self):
        largInterf = 200
        
        scX, scY = pygame.display.get_surface().get_size()
        pX = scX - largInterf
        pY = 0

        pygame.Surface.fill(VAR.fenetre, pygame.Color(64,64,64,32), (pX, pY, largInterf, scY))

    def afficher(self):

        self.afficher_cadre_joueur()
        hauteur = self.menu.afficher_liste_joueurs()
        self.menu.afficher_liste_actions_joueur(hauteur)
        
        if VAR.image_interface is None:
            VAR.image_interface  = VAR.objets.cadre(0,0, VAR.EcranX, VAR.EcranY)        
        VAR.fenetre.blit(VAR.image_interface, (0, 0))


    def afficher_cadre_joueur(self):
        largeur_cadre = 330
        x, taille_ico1, taille_ico2 = 20, 50, 64
        
        if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT:
            img = pygame.image.load(VAR.joueur_en_cours.avatar).convert_alpha()
            x, taille_ico1, taille_ico2 = img.get_width(), 50, 50
            largeur_cadre = 500
            
        
        # --- Barre decors
        pygame.draw.rect(VAR.fenetre, pygame.Color(33,105,33,255), (0, VAR.EcranY - 106, (largeur_cadre-50), 6), 0)
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (0, VAR.EcranY - 50, VAR.EcranX, 50), 0)
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (0, VAR.EcranY - 60, VAR.EcranX, 5), 0)

        # --- Items
        for i in range(2):
            xP, yP =  (largeur_cadre+30) + (i*(taille_ico1+8)), VAR.EcranY - (taille_ico1+26)

            ico = None
            if VAR.joueur_en_cours.armes[i] != None:
                if VAR.joueur_en_cours.armes[i] == ENUM_Objets.COUTEAUX: 
                    ico = VAR.IMG[str(ENUM_Objets.COUTEAUX)]
                elif VAR.joueur_en_cours.armes[i] == ENUM_Objets.HACHE: 
                    ico = VAR.IMG[str(ENUM_Objets.HACHE)]
                elif VAR.joueur_en_cours.armes[i] == ENUM_Objets.MASSE: 
                    ico = VAR.IMG[str(ENUM_Objets.MASSE)]
            
            if ico != None:
                VAR.fenetre.blit(ico, (xP, yP))
            else:
                pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (xP, yP, taille_ico1, taille_ico1), 0)
                
            pygame.draw.rect(VAR.fenetre, pygame.Color(76,54,44,255), (xP, yP, taille_ico1, taille_ico1), 4)
        
        # --- 1 Item clé
        xP, yP =  (largeur_cadre+30) + (2*(taille_ico1+8)), VAR.EcranY - (taille_ico1+26)
        if VAR.joueur_en_cours.cle == True:
            ico = VAR.IMG[str(ENUM_Objets.CLE)]
            VAR.fenetre.blit(ico, (xP, yP))
        else:
            pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (xP, yP, taille_ico1, taille_ico1), 0)
        pygame.draw.rect(VAR.fenetre, pygame.Color(76,54,44,255), (xP, yP, taille_ico1, taille_ico1), 4)    
        
        # --- 3 Items de magie FORCE ET VIE
        for i in range(3):
            xP, yP = (largeur_cadre+38) + (3*(taille_ico1+8)) + (i*(taille_ico2+8)), VAR.EcranY - (taille_ico2+26)
            
            # --- Image de la magie
            ico = None
            if VAR.joueur_en_cours.magies[i] != None:
                if VAR.joueur_en_cours.magies[i] == ENUM_Objets.MAGIE_EPEE: 
                    ico = VAR.IMG[str(ENUM_Objets.MAGIE_EPEE)]
                elif VAR.joueur_en_cours.magies[i] == ENUM_Objets.MAGIE_VIE: 
                    ico = VAR.IMG[str(ENUM_Objets.MAGIE_VIE)]
            
            # --- Bouton de la magie
            if ico != None:
                if VAR.phase_du_jeu == ENUM_Phase.COMBAT:
                    ico = pygame.transform.scale(ico, (taille_ico2, taille_ico2))
                    ico.set_alpha(128) 
                if VAR.objets.afficher_bouton_image(xP, yP, ico) == ENUM_Clic.Clic:
                    print("oo")   
            else:
                pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (xP, yP, taille_ico2, taille_ico2), 0)
                
            pygame.draw.rect(VAR.fenetre, pygame.Color(76,54,44,255), (xP, yP, taille_ico2, taille_ico2), 4)
            
        # --- Cadre
        f = [(0, VAR.EcranY - 100), (0, VAR.EcranY), (largeur_cadre, VAR.EcranY), (largeur_cadre - 50, VAR.EcranY - 100)]
        pygame.draw.polygon(VAR.fenetre, pygame.Color(117,94,74,255), f, 0)
        pygame.draw.polygon(VAR.fenetre, pygame.Color(76 ,54,44,255), f, 4)

        if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT:
            VAR.fenetre.blit(img, (0, VAR.EcranY - img.get_height() + 30))
        
        # --- Pseudo
        FCT.texte(VAR.fenetre, VAR.joueur_en_cours.nom, x + 20, VAR.EcranY - 95, 30,  (0,0,0))
        FCT.texte(VAR.fenetre, VAR.joueur_en_cours.nom, x + 22, VAR.EcranY - 93, 30,  (255,255,255))

        # --- Vie et Energie
        for i in range(VAR.joueur_en_cours.vie):
            VAR.fenetre.blit(VAR.IMG["coeur"],(x + (i * 24) + 20, VAR.EcranY - 60))
        for i in range(VAR.joueur_en_cours.mouvement):
            VAR.fenetre.blit(VAR.IMG["energie"],(x + ((5+i) * 24) + 30, VAR.EcranY -60))   
    
  
            
            



    