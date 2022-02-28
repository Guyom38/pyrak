import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

class Chero(object):
    def __init__(self, nom, id):
        
        self.animationCycle = 0
        self.animationCpt = 0
        
        self.nom = nom
        self.id = id
        self.vie = 5
        self.mouvement = 4
        self.pouvoirs = [None, None]
        
        self.armes = ["ARME+1", None]
        self.magies = ["MAGIE_VIE", None, None]
        self.cle = True
        self.maudit = False

        self.x = VAR.posPieceCentrale[0]
        self.y = VAR.posPieceCentrale[1]
        self.xOld = self.x
        self.yOld = self.y

        self.deplaceX = 0
        self.deplaceY = 0
        self.deplaceVitesse = 8
        self.seDeplace = False
        self.direction = VAR.BAS

        if id == 1: self.avatar = "Images\\persos\\perso_argentus.png"
        elif id == 2: self.avatar = "Images\\persos\\perso_horan.png"
        elif id == 3: self.avatar = "Images\\persos\\perso_lord.png"
        elif id == 4: self.avatar = "Images\\persos\\perso_taia.png"
        elif id == 5: self.avatar = "Images\\persos\\perso_victorius.png"
        elif id == 6: self.avatar = "Images\\persos\\perso_voleuse.png"
        elif id == 7: self.avatar = "Images\\persos\\perso_chevaliere.png"
        elif id == 8: self.avatar = "Images\\persos\\perso1.png"
        elif id == 9: self.avatar = "Images\\persos\\perso5.png"
        
        self.ordre_images = (1,3,2,0)
        #self.masque = FCT.Generer_Mask_Image(image)
        
    def se_prend_un_coup(self):
        print( self.nom + " perd une vie !")
        self.vie = self.vie -1

    def demi_tour(self):
        self.deplacer(self.xOld, self.yOld)

    def deplacer(self, x, y):
        if self.mouvement < 1: return False
        self.xOld, self.yOld = self.x, self.y           # --- enregistre le chemin précédent

        self.seDeplace = True
        if self.x > x: self.direction = VAR.GAUCHE
        if self.x < x: self.direction = VAR.DROITE
        if self.y > y: self.direction = VAR.HAUT
        if self.y < y: self.direction = VAR.BAS
        
    def gestion_deplacement(self):
        if self.direction == VAR.GAUCHE:
            self.deplaceX -= self.deplaceVitesse
            VAR.OffsetX += self.deplaceVitesse
        elif self.direction == VAR.HAUT:
            self.deplaceY -= self.deplaceVitesse
            VAR.OffsetY += self.deplaceVitesse
        elif self.direction == VAR.DROITE:
            self.deplaceX += self.deplaceVitesse
            VAR.OffsetX -= self.deplaceVitesse   
        elif self.direction == VAR.BAS:
            self.deplaceY += self.deplaceVitesse
            VAR.OffsetY -= self.deplaceVitesse
                       
        if self.deplaceX >= VAR.v9: 
            self.seDeplace = False   
            self.x += 1 
        elif self.deplaceX <= -VAR.v9: 
            self.seDeplace = False   
            self.x -= 1 
        if self.deplaceY >= VAR.v9: 
            self.seDeplace = False   
            self.y += 1 
        elif self.deplaceY <= -VAR.v9: 
            self.seDeplace = False   
            self.y -= 1 
        
        # --- Deplacement terminé
        if self.seDeplace == False:
            self.deplaceX, self.deplaceY = 0, 0
            self.mouvement -= 1
            self.recentrer_camera()    
            
            # --- Si c'est une piece et pas la piece de depart, en avant pour un combat.
            que_fait_on = VAR.terrain[self.x][self.y].faut_il_tirer_un_jeton()
            if que_fait_on != -1:
                VAR.phase_du_jeu = ENUM_Phase.TRANSITION
                if que_fait_on == 1: 
                    VAR.phase_du_jeu_suivant = ENUM_Phase.TIRAGE   
                elif que_fait_on == 0:
                    VAR.phase_du_jeu_suivant = ENUM_Phase.COMBAT   
            
            
    def recentrer_camera(self):
        VAR.OffsetX = -(((self.x) * 9) * VAR.Zoom) + int((VAR.EcranX - VAR.v9) / 2)
        VAR.OffsetY = -(((self.y) * 9) * VAR.Zoom) + int((VAR.EcranY - VAR.v9) / 2)
        
    def afficher(self):
        t = VAR.heros.cpt % 3
        x = VAR.OffsetX + (((self.x * 9)+4) * VAR.Zoom) + self.deplaceX - 8
        y = VAR.OffsetY + (((self.y * 9)+4) * VAR.Zoom) + self.deplaceY - 20
        
        if self == VAR.joueur_en_cours:
            pygame.draw.circle(VAR.fenetre, pygame.Color(255,0,0,255), (x+16, y+24), 16+t, 3)
        
        VAR.fenetre.blit(FCT.image_decoupe(VAR.perso, (self.id * 3) +t, self.ordre_images[self.direction], 32, 32), (x, y))
        FCT.texte(VAR.fenetre, self.nom, x, y-16, 10, pygame.Color(0,0,0,255))
        FCT.texte(VAR.fenetre, self.nom, x+2, y-14, 10, pygame.Color(255,255,255,255))
