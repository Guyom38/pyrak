import pygame
from pygame.locals import *

import variables as VAR
import classes.commun.fonctions as FCT

import classes.ui.ui_barre_lateral as CBL
import classes.ui.ui_objets_interface as COI


class CInterfaces():
    def __init__(self):
        print("    + Initialisation module << Interface >>")
        self.menu = CBL.CBarre_Laterale()
        
        # --- Dimensions
        self.largeur_cadre_joueur = 330

        # --- Couleurs
        self.couleur1 = pygame.Color(33,105,33,255)
        self.couleur2 = pygame.Color(105,74,64,255)
        self.couleur3 = pygame.Color(76,54,44,255)
        self.couleur4 = pygame.Color(64,64,64,32)
        self.couleur5 = pygame.Color(117,94,74,255)
        
        self.couleurNom = pygame.Color(255,255,255,255)

        self.imageCadreGlobal = None



    def afficher(self):

        self.afficher_cadre_joueur()
        self.menu.afficher_menu()
        hauteur = self.menu.afficher_liste_joueurs()
        self.menu.afficher_liste_actions_joueur(hauteur)
        self.afficher_cadre_global()
        
        

    def afficher_cadre_global(self):
        if self.imageCadreGlobal is None:
            self.imageCadreGlobal  = VAR.objets_interface.cadre(0,0, VAR.EcranX, VAR.EcranY)        
        VAR.fenetre.blit(self.imageCadreGlobal, (0, 0))


    def afficher_cadre_heros2(self):
        largInterf = 200
        scX, scY = pygame.display.get_surface().get_size()
        pX, pY = scX - largInterf, 0

        pygame.Surface.fill(VAR.fenetre, self.couleur4, (pX, pY, largInterf, scY))

    
    def afficher_cadre_joueur(self):
        phase_normale = ( VAR.phase_du_jeu in (VAR.ENUM_Phase.DEPLACEMENT, VAR.ENUM_Phase.INVENTAIRE, VAR.ENUM_Phase.BANDEAU) )

        xJ, yJ = VAR.joueur_en_cours.x, VAR.joueur_en_cours.y
        img = VAR.joueur_en_cours.image
        
        x, taille_ico_ref = FCT.iif(phase_normale == True, img.get_width(), 32), 50
        largeur_cadre = FCT.iif(phase_normale == True, 500, 300)

        # --- Barre decors
        pygame.draw.rect(VAR.fenetre, self.couleur1, (0, VAR.EcranY - 106, (largeur_cadre-50), 6), 0)         # Courbe1
        pygame.draw.rect(VAR.fenetre, self.couleur2, (0, VAR.EcranY - 50, VAR.EcranX, 50), 0)                 # Courbe2
        pygame.draw.rect(VAR.fenetre, self.couleur2, (0, VAR.EcranY - 60, VAR.EcranX, 5), 0)                  # Courbe3

        # --- Items
        xP, yP =  (largeur_cadre+30), VAR.EcranY - (taille_ico_ref+26)
        for posItem, typeItem in ((0,"ARME"), (1,"ARME"), (0,"CLE"), (0, ""), (0,"MAGIE"), (1,"MAGIE"), (2,"MAGIE")):
            taille_ico = taille_ico_ref

            # --- Recupere info sur l'objet du joueur
            nomObjet = None
            if typeItem == "ARME":
                if VAR.joueur_en_cours.armes[posItem] != None: nomObjet = VAR.joueur_en_cours.armes[posItem]
                
            elif typeItem == "CLE":
                if VAR.joueur_en_cours.cle == True: nomObjet = "CLE"
                
            elif typeItem == "MAGIE":
                if VAR.joueur_en_cours.magies[posItem] != None: 
                    nomObjet = VAR.joueur_en_cours.magies[posItem]
                    if VAR.phase_du_jeu == VAR.ENUM_Phase.COMBAT:
                        if VAR.objets_interface.zone_clickable(xP, yP, taille_ico, taille_ico, 0) == VAR.ENUM_Clic.Clic:
                            VAR.combat.magies_selectionnees[posItem] = VAR.joueur_en_cours.magies[posItem]  

            # --- Dessine l'objet trouvé
            if typeItem != "":
                if nomObjet != None:
                    ico = VAR.objets.liste[nomObjet].icone
                    VAR.fenetre.blit(ico, (xP, yP))
                else:
                    pygame.draw.rect(VAR.fenetre, self.couleur2, (xP, yP, taille_ico, taille_ico), 0)
                
                # --- Gestion du ramassage
                objetAPrendre = (VAR.phase_du_jeu == VAR.ENUM_Phase.INVENTAIRE and VAR.terrain[xJ][yJ].recompense != None)
                if objetAPrendre == True:
                    if typeItem != "CLE":
                        if VAR.terrain[xJ][yJ].recompense.__contains__(typeItem) == True:
                            VAR.objets_interface.tracer_pointilles_entre_joueur_et_inventaire(xP, yP, taille_ico, taille_ico)   
                            if VAR.objets_interface.zone_clickable(xP, yP, taille_ico, taille_ico, 0) == VAR.ENUM_Clic.Clic:
                                
                                if typeItem == "ARME":
                                    objet_du_joueur = VAR.joueur_en_cours.armes[posItem]
                                    VAR.joueur_en_cours.armes[posItem] = VAR.terrain[xJ][yJ].recompense
                                    VAR.terrain[xJ][yJ].recompense = objet_du_joueur
                                
                                elif typeItem == "MAGIE":
                                    objet_du_joueur = VAR.joueur_en_cours.magies[posItem]
                                    VAR.joueur_en_cours.magies[posItem] = VAR.terrain[xJ][yJ].recompense
                                    VAR.terrain[xJ][yJ].recompense = objet_du_joueur
                                    
                                VAR.terrain[xJ][yJ].pillier = (objet_du_joueur == None)                 # --- Si le joueur ne depose rien a la place, la piece est consideree pilliée
                                VAR.phase_du_jeu = VAR.ENUM_Phase.DEPLACEMENT
                                VAR.joueur_en_cours.mouvement = 0       

                pygame.draw.rect(VAR.fenetre, self.couleur3, (xP, yP, taille_ico, taille_ico), 4)   # --- Contour objet
                                 
                xP += taille_ico
            xP += 8
                
            # --- Cadre
            f = [(0, VAR.EcranY - 100), (0, VAR.EcranY), (largeur_cadre, VAR.EcranY), (largeur_cadre - 50, VAR.EcranY - 100)]
            pygame.draw.polygon(VAR.fenetre, self.couleur5, f, 0)
            pygame.draw.polygon(VAR.fenetre, self.couleur3, f, 4)

            if phase_normale == True:
                img = VAR.joueur_en_cours.image
                VAR.fenetre.blit(img, (0, VAR.EcranY - img.get_height() + 30))
            
            # --- Pseudo
            FCT.texte(VAR.fenetre, VAR.joueur_en_cours.nom, x + 20, VAR.EcranY - 95, 30,  (0,0,0))
            FCT.texte(VAR.fenetre, VAR.joueur_en_cours.nom, x + 22, VAR.EcranY - 93, 30, self.couleurNom)

            # --- Vie et Energie
            for i in range(VAR.joueur_en_cours.vie):
                VAR.fenetre.blit(VAR.IMG["coeur"],(x + (i * 24) , VAR.EcranY - 60))
            for i in range(VAR.joueur_en_cours.mouvement):
                VAR.fenetre.blit(VAR.IMG["energie"],(x + ((5+i) * 24) + 10, VAR.EcranY -60))  

  







    