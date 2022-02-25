import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT


class CBarre_Laterale():
    def __init__(self, moteur):
        print("    + Initialisation module << Barre laterale >>")
        self.moteur = moteur
        
    def afficher_liste_joueurs(self):
        hauteur, largeur = (len(VAR.heros.liste) * 50) + 50, 150
           
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (VAR.EcranX-50, 0, 50, VAR.EcranY), 0)
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (VAR.EcranX-60, 0, 5, VAR.EcranY-60), 0)

        f = [(VAR.EcranX - largeur, 0), (VAR.EcranX, 0), (VAR.EcranX, hauteur), (VAR.EcranX - largeur, hauteur - 50)]
        pygame.draw.polygon(VAR.fenetre, pygame.Color(117,94,74,255), f, 0)
        pygame.draw.polygon(VAR.fenetre, pygame.Color(76 ,54,44,255), f, 4)   

        for i in range(len(VAR.heros.liste)):
            x, y, d, t =  (VAR.EcranX - largeur + 8) , (i * 38) + 30, 32, 0
            
            if VAR.joueur_en_cours == VAR.heros.liste[i]: 
                d, t = 150, VAR.heros.cpt % 3
                
            pygame.draw.rect(VAR.fenetre, pygame.Color(50,30,20,255), (x, y, d, 32), 0)
            pygame.draw.rect(VAR.fenetre, pygame.Color(76,54,44,255), (x, y, d, 32), 4)
            
            if VAR.objets.afficher_bouton_image(x, y, FCT.image_decoupe(VAR.perso, (VAR.heros.liste[i].id * 3) +t , 0, 32, 32)) == ENUM_Clic.Clic:
                VAR.heros.liste[i].recentrer_camera()
                
            VAR.fenetre.blit(FCT.image_decoupe(VAR.perso, (VAR.heros.liste[i].id * 3) +t , 0, 32, 32), (x, y))
            FCT.texte(VAR.fenetre, VAR.heros.liste[i].nom, x + 50, y+4, 10)
            for j in range(VAR.heros.liste[i].vie):
                VAR.fenetre.blit(VAR.IMG["mini_coeur"],(x +(j *10) + 50, y+14, 16, 16), (0,0,VAR.IMG["mini_coeur"].get_width(),VAR.IMG["mini_coeur"].get_height()))        

        return hauteur


        
    def afficher_liste_actions_joueur(self, hauteur):
        wIco, hIco = 63, 66
        xP, yP = VAR.EcranX-94, hauteur + 50

        # ------------------------------------------------------------
        # - MENU ACTIONS JOUEURS
        # ------------------------------------------------------------
        if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT and VAR.joueur_en_cours.seDeplace == False:
            for ico in (ENUM_Actions.PIOCHER, ENUM_Actions.PRENDRE, ENUM_Actions.PAUSE):
                
                if ico == ENUM_Actions.PIOCHER and VAR.plateau.nombre_de_zones_libres() > 0:                                       # --- PIOCHE disponible si un acces est visible
                    if VAR.objets.afficher_bouton_image(xP, yP, VAR.IMG[str(ico)]) == ENUM_Clic.Clic: 
                        VAR.tuiles.piocher()
                    yP = (yP +(hIco + 8))
                
                elif ico == ENUM_Actions.PAUSE and VAR.tuiles.tuileSelect == None:                                               # --- PAUSE disponible si aucune pioche n'a été tirée
                    if VAR.objets.afficher_bouton_image(xP, yP, VAR.IMG(str(ico))) == ENUM_Clic.Clic: 
                        VAR.heros.joueur_suivant()
                    yP = (yP +(hIco + 8))
                
                elif ico == ENUM_Actions.PRENDRE and VAR.terrain[VAR.joueur_en_cours.x][VAR.joueur_en_cours.y].recompense != None:                                                                                  # --- PRENDRE objet par terre
                    if VAR.objets.afficher_bouton_image(xP, yP, VAR.IMG(str(ico))) == ENUM_Clic.Clic:
                         print("kkkk")
                    yP = (yP +(hIco + 8))
                    
        elif VAR.phase_du_jeu == ENUM_Phase.COMBAT:
            if VAR.combat.lance_de_des == False and VAR.combat.combat_termine == False:
                if VAR.objets.afficher_bouton_image(xP, yP, FCT.icone(6)) == ENUM_Clic.Clic: 
                    VAR.combat.nombre_lances = 0
                    VAR.combat.lance_de_des = True
            
