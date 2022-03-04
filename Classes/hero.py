import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

class Chero(object):
    def __init__(self, moteur, id, nom):
        self.moteur = moteur
        
        self.animationCycle = 0
        self.animationCpt = 0
        
        self.nom = nom
        self.id = int(id)
        self.vie = 5
        self.mouvement = 4
        self.pouvoirs = [None, None]
        
        self.armes = [None, None]
        self.magies = [None, None, None]
        self.cle = False
        self.coffres = 0
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
        
        self.image = pygame.image.load("Images\\heros\\" + id + ".png").convert_alpha()
        self.masque = FCT.Generer_Mask_Image(self.image)
        self.ordre_images = (1,3,2,0)
        self.image_offsetx, self.image_offsety = 8, 20

        
    def se_prend_un_coup(self):
        print( self.nom + " perd une vie !")
        self.vie = self.vie -1


    def demi_tour(self, force = False):
        self.deplacer(self.xOld, self.yOld, force)


    def deplacer(self, x, y, force = False):
        if self.mouvement < 1 and force == False: return False
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
            self.gestion_reaction_sur_place()
            
            
    def gestion_reaction_sur_place(self):
        # --- Si c'est une piece et pas la piece de depart, en avant pour un combat.
        que_fait_on = VAR.terrain[self.x][self.y].faut_il_tirer_un_jeton()
        if que_fait_on == ENUM_Piece.TIRAGE_AU_SORT or que_fait_on == ENUM_Piece.COMBATTRE:
            VAR.phase_du_jeu = ENUM_Phase.TRANSITION
                
            if que_fait_on == ENUM_Piece.TIRAGE_AU_SORT: 
                VAR.phase_du_jeu_suivant = ENUM_Phase.TIRAGE   
            elif que_fait_on == ENUM_Piece.COMBATTRE:
                VAR.phase_du_jeu_suivant = ENUM_Phase.COMBAT   
            
        elif que_fait_on == ENUM_Piece.OBJET_A_RECUPERER :                                        # --- Objet a prendre ?
            if VAR.joueur_en_cours.cle == False:
                if VAR.terrain[self.x][self.y].recompense == "CLE":
                    VAR.joueur_en_cours.cle = True
                    VAR.terrain[self.x][self.y].recompense = None
                    VAR.terrain[self.x][self.y].pillier = True
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "Ramasse la clé")

                elif VAR.terrain[self.x][self.y].recompense == "COFFRE": 
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "N'a pas la clé !!")
            else:
                if VAR.terrain[self.x][self.y].recompense == "COFFRE":
                    VAR.joueur_en_cours.coffres += 1
                    VAR.joueur_en_cours.cle = False
                    VAR.terrain[self.x][self.y].recompense = None
                    VAR.terrain[self.x][self.y].pillier = True
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "Ouvre le coffre")
            
                
    def recentrer_camera(self):
        print("Recentrer camera")
        #VAR.camera.deplacer(self.x, self.y)
        VAR.OffsetX = -(((self.x) * 9) * VAR.Zoom) + int((VAR.EcranX - VAR.v9) / 2)
        VAR.OffsetY = -(((self.y) * 9) * VAR.Zoom) + int((VAR.EcranY - VAR.v9) / 2)
    
    
    def position_sur_ecran(self):
        decalage_milieu = 4
        x = VAR.OffsetX + (((self.x * 9)+decalage_milieu) * VAR.Zoom) + self.deplaceX - self.image_offsetx
        y = VAR.OffsetY + (((self.y * 9)+decalage_milieu) * VAR.Zoom) + self.deplaceY - self.image_offsety
        return (x, y)
    
    
    def afficher(self):
        t = VAR.heros.cpt % 3
        x, y = self.position_sur_ecran()
        
        if self == VAR.joueur_en_cours:
            pygame.draw.circle(VAR.fenetre, pygame.Color(255,0,0,255), (x+16, y+24), 16+t, 3)
        
        VAR.fenetre.blit(FCT.image_decoupe(VAR.perso, (self.id * 3) +t, self.ordre_images[self.direction], 32, 32), (x, y))
        FCT.texte(VAR.fenetre, self.nom, x, y-16, 10, pygame.Color(0,0,0,255))
        FCT.texte(VAR.fenetre, self.nom, x+2, y-14, 10, pygame.Color(255,255,255,255))
