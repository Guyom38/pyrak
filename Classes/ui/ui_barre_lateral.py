import pygame
from pygame.locals import *

import variables as VAR
import classes.commun.fonctions as FCT


class CBarre_Laterale():
    def __init__(self):
        print("    + Initialisation module << Barre laterale >>")
        
    def afficher_menu(self):
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (VAR.EcranX-200, 0, 200, 50), 0)
        pygame.draw.rect(VAR.fenetre, pygame.Color(105,74,64,255), (VAR.EcranX-200, 0, 200, 50), 2)
        if VAR.objets_interface.afficher_bouton_image(VAR.EcranX-200, 16, VAR.IMG["mini_coeur"]) == VAR.ENUM_Clic.Clic: 
            VAR.phase_du_jeu = VAR.ENUM_Phase.MENU
            
            
    def afficher_liste_joueurs(self):
        hauteur, largeur = (len(VAR.heros.liste) * 50) + 60, 150
           
        pygame.draw.rect(VAR.fenetre, pygame.Color(80,50,30,255), (VAR.EcranX-50, 0, 50, VAR.EcranY), 0)
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
            
            if VAR.objets_interface.afficher_bouton_image(x, y, FCT.image_decoupe(VAR.perso, (VAR.heros.liste[i].id * 3) +t , 0, 32, 32)) == VAR.ENUM_Clic.Clic:
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
        
        for action in (VAR.ENUM_Actions.PIOCHER, VAR.ENUM_Actions.PRENDRE, VAR.ENUM_Actions.PAUSE, VAR.ENUM_Actions.COMBATTRE, VAR.ENUM_Actions.SE_BAIGNER):
            ico = action.value
            if VAR.phase_du_jeu == VAR.ENUM_Phase.DEPLACEMENT and VAR.joueur_en_cours.seDeplace == False:
                if action == VAR.ENUM_Actions.PIOCHER and VAR.plateau.on_peut_construire() == True and VAR.joueur_en_cours.peut_bouger() and VAR.tuiles.joueur_a_deja_pioche() == False:                                       # --- PIOCHE disponible si un acces est visible
                    if VAR.objets_interface.afficher_bouton_image(xP, yP, VAR.IMG[ico]) == VAR.ENUM_Clic.Clic: 
                        VAR.tuiles.piocher()
                    yP = (yP +(hIco + 8))
                
                elif action == VAR.ENUM_Actions.PAUSE and VAR.tuiles.tuileSelect == None and VAR.joueur_en_cours.peut_bouger() == False:       
                                                        # --- PAUSE disponible si aucune pioche n'a été tirée
                    if VAR.objets_interface.afficher_bouton_image(xP, yP, VAR.IMG[ico]) == VAR.ENUM_Clic.Clic: 
                        VAR.heros.joueur_suivant()
                    yP = (yP +(hIco + 8))
                
                elif action == VAR.ENUM_Actions.PRENDRE and VAR.terrain[VAR.joueur_en_cours.x][VAR.joueur_en_cours.y].recompense != None:                                                                                  # --- PRENDRE objet par terre
                    
                    cle = (VAR.terrain[VAR.joueur_en_cours.x][VAR.joueur_en_cours.y].recompense == "CLE")
                    coffre = (VAR.terrain[VAR.joueur_en_cours.x][VAR.joueur_en_cours.y].recompense == "COFFRE")
                    joueur_a_une_cle = VAR.joueur_en_cours.cle

                    if (coffre == False or joueur_a_une_cle == True) and cle == False:
                        if VAR.objets_interface.afficher_bouton_image(xP, yP, VAR.IMG[ico]) == VAR.ENUM_Clic.Clic:
                            VAR.phase_du_jeu = VAR.ENUM_Phase.INVENTAIRE
                        yP = (yP +(hIco + 8))
                        
                elif action == VAR.ENUM_Actions.SE_BAIGNER and VAR.tuiles.tuileSelect == None \
                    and VAR.terrain[VAR.joueur_en_cours.x][VAR.joueur_en_cours.y].fontaine == True and VAR.joueur_en_cours.vie < VAR.joueur_en_cours.vie_max:
                        
                    if VAR.objets_interface.afficher_bouton_image(xP, yP, VAR.IMG[ico]) == VAR.ENUM_Clic.Clic:
                            VAR.joueur_en_cours.vie = VAR.joueur_en_cours.vie_max
                            VAR.notifications.ajouter(VAR.joueur_en_cours, "", "Pète la forme !")
                            VAR.heros.joueur_suivant()
                    
            elif VAR.phase_du_jeu == VAR.ENUM_Phase.COMBAT:
                if VAR.combat.lance_de_des == False and VAR.combat.combat_termine == False:
                    if action == VAR.ENUM_Actions.COMBATTRE:
                        if VAR.objets_interface.afficher_bouton_image(xP, yP, VAR.IMG[ico]) == VAR.ENUM_Clic.Clic: 
                            VAR.combat.nombre_lances = 0
                            VAR.combat.lance_de_des = True
                        yP = (yP +(hIco + 8))
                    
                   

            
