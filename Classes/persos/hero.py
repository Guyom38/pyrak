import pygame
from pygame.locals import *

import variables as VAR
import classes.commun.fonctions as FCT
import classes.commun.outils as outils

class Chero(object):
    def __init__(self, id, nom):

        
        #self.animationCycle = 0
        #self.animationCpt = 0
        
        self.nom = nom
        self.id = int(id)
        
        self.vie_max = 5
        self.vie = 5
        self.mouvement = 4
        self.pouvoirs = [None, None]
        
        self.armes = [None, None]
        self.magies = ["MAGIE_VIE", None, "MAGIE_VIE"]
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
        self.mort = False
        
        self.image = pygame.image.load("images\\heros\\" + id + ".png").convert_alpha()
        self.masque = FCT.Generer_Mask_Image(self.image)
        self.ordre_images = (1,3,2,0)
        self.image_offsetx, self.image_offsety = 8, 20

        
    def se_prend_un_coup(self):
        self.vie -= 1
        if self.vie == 0:
            self.mort = True
    

    def fait_un_demi_tour(self, force = False):
        self.deplacer(self.xOld, self.yOld, force)

    def peut_bouger(self):
        return (self.mouvement > 0)
    
    def deplacer(self, x, y, force = False):
        if self.peut_bouger() == False and force == False: 
            return False
        
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
            self.se_deplace()
            self.recentrer_camera()    
            self.gestion_reaction_sur_place()
            
    def se_repose(self):
        self.mouvement = 0
        
    def se_deplace(self):
        self.mouvement -=1
               
    def gestion_reaction_sur_place(self):
        nb_coffres = 0

        # --- Si c'est une piece et pas la piece de depart, en avant pour un combat.
        que_fait_on = VAR.terrain[self.x][self.y].faut_il_tirer_un_jeton()
        if que_fait_on == VAR.ENUM_Piece.TIRAGE_AU_SORT or que_fait_on == VAR.ENUM_Piece.COMBATTRE:
            VAR.phase_du_jeu = VAR.ENUM_Phase.TRANSITION
                
            if que_fait_on == VAR.ENUM_Piece.TIRAGE_AU_SORT: 
                VAR.phase_du_jeu_suivant = VAR.ENUM_Phase.TIRAGE   
            elif que_fait_on == VAR.ENUM_Piece.COMBATTRE:
                VAR.phase_du_jeu_suivant = VAR.ENUM_Phase.COMBAT   
            
        elif que_fait_on == VAR.ENUM_Piece.OBJET_A_RECUPERER :                                        # --- Objet a prendre ?
            if VAR.joueur_en_cours.cle == False:
                if VAR.terrain[self.x][self.y].recompense == "CLE":
                    VAR.joueur_en_cours.cle = True
                    VAR.terrain[self.x][self.y].recompense = None
                    VAR.terrain[self.x][self.y].pillier = True
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "Ramasse la clé")

                elif VAR.terrain[self.x][self.y].recompense == "COFFRE": 
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "N'a pas la clé !!")

                elif VAR.terrain[self.x][self.y].recompense == "COFFRE_OUVERT":
                    nb_coffres = 1
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "Récupére le coffre")
                
                elif VAR.terrain[self.x][self.y].recompense == "SUPER_COFFRE_OUVERT":
                    nb_coffres = 2
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "Récupére un super coffre")


            else:
                if VAR.terrain[self.x][self.y].recompense == "COFFRE":
                    nb_coffres = 1
                    VAR.joueur_en_cours.cle = False
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "OBJET", "Ouvre le coffre")

            if nb_coffres >0:
                VAR.terrain[self.x][self.y].recompense = None
                VAR.terrain[self.x][self.y].pillier = True
                VAR.phase_du_jeu = VAR.ENUM_Phase.RECOMPENSE
                VAR.joueur_en_cours.coffres += nb_coffres



    def recentrer_camera(self):
        #print("Recentrer camera")
        #VAR.camera.deplacer(self.x, self.y)
        VAR.OffsetX = -(((self.x) * 9) * VAR.Zoom) + int((VAR.EcranX - VAR.v9) / 2)
        VAR.OffsetY = -(((self.y) * 9) * VAR.Zoom) + int((VAR.EcranY - VAR.v9) / 2)
    
    
    def position_sur_ecran(self):
        decalage_milieu = 4
        x, y = outils.position(self.x, self.y, decalage_milieu, decalage_milieu)
        x += (self.deplaceX - self.image_offsetx)
        y += (self.deplaceY - self.image_offsety)
        return (x, y)
    
    
    def afficher(self):
        t = FCT.iif(self.mort, 0, VAR.heros.cpt % 3)        
        x, y = self.position_sur_ecran()
        
        if self == VAR.joueur_en_cours and not self.mort:
            pygame.draw.circle(VAR.fenetre, pygame.Color(255,0,0,255), (x+16, y+24), 16+t, 3)
        
        VAR.fenetre.blit(FCT.image_decoupe(VAR.perso, (self.id * 3) +t, self.ordre_images[self.direction], 32, 32), (x, y))
        FCT.texte(VAR.fenetre, self.nom, x, y-16, 10, pygame.Color(0,0,0,255))
        FCT.texte(VAR.fenetre, self.nom, x+2, y-14, 10, pygame.Color(255,255,255,255))
        
        if self.mort:
            i, liste = 0, outils.cercle_COS(x+16, y, 16)
            for cX, cY in liste:
                if (i % 40) == (VAR.cpt % 10)*4:
                    FCT.texte(VAR.fenetre, "z",  cX, cY, 10, (255,255,0,0))
                i+=1
