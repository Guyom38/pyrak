import pygame
from pygame.locals import *

import variables as VAR
import classes.commun.fonctions as FCT


class CMenu():
    def __init__(self):
        print("    + Initialisation module << Menu >>")

        self.menu_nom = ""
        self.menu_principal()
        
        self.dimX, self.dimY, self.esp = 300, 50, 6
        self.offX, self.offY = int((VAR.EcranX - self.dimX) / 2), VAR.EcranY - 100 - (len(self.MENU) * self.dimY + self.esp)
        self.fond_old = None
        
    def menu_principal(self):
        self.menu_nom = "PRINCIPAL"
        
        self.MENU = []
        self.MENU.append( (0, "Continuer") )
        self.MENU.append( (1, "Nouvelle partie") )
        self.MENU.append( (2, "Charger une partie") )
        #self.MENU.append( (9, "Enregistrer la partie") )
        self.MENU.append( (3, "Partie réseau") )
        self.MENU.append( (4, "Options") )
        self.MENU.append( (5, "Quitter") )
    
    def menu_noms_joueurs(self):
        self.menu_nom = "JOUEURS"
        
        self.MENU = []
        self.MENU.append( (-10, "JOUEUR 1") )
        self.MENU.append( (-11, "JOUEUR 1") )
        self.MENU.append( (-12, "JOUEUR 1") )
        self.MENU.append( (-13, "JOUEUR 1") )
        self.MENU.append( (-14, "JOUEUR 1") )
        
    def menu_partie_reseau(self):
        self.menu_nom = "RESEAU"
        
        self.MENU = []
        self.MENU.append( (6, "Créer une partie réseau") )
        self.MENU.append( (7, "Entrer un code de partie") )
        self.MENU.append( (8, "Retour") )

    def menu_multijoueur_entrer_code(self):
        self.menu_nom = "CODE"
        
        self.MENU = []
        self.MENU.append( (-1, "Entrez le code la partie") )
        self.MENU.append( (-2, "") )
        self.MENU.append( (8, "Retour") )
                
    def action_menu(self, id):
        if id == 5:
            VAR.boucle_principale = False
        elif id < -1:
            VAR.clavier.montrer()
        elif id == 0:
            VAR.phase_du_jeu = VAR.ENUM_Phase.DEPLACEMENT
        elif id == 1:
            VAR.partie.nouvelle_partie()
            VAR.phase_du_jeu = VAR.ENUM_Phase.DEPLACEMENT
        elif id == 2:
            VAR.partie.charger()
            VAR.phase_du_jeu = VAR.ENUM_Phase.DEPLACEMENT
            
        elif id == 3:
            self.menu_partie_reseau()
        elif id == 7:
            self.menu_multijoueur_entrer_code()
        elif id == 8:   
            VAR.clavier.cacher()
            
            if self.menu_nom == "PRINCIPAL":
                VAR.phase_du_jeu = VAR.ENUM_Phase.DEPLACEMENT
            else:
                self.menu_principal()
        elif id == 9:
            VAR.partie.enregistrer()
            
            
                    
    def afficher(self):
        self.afficher_fond_anime()
        VAR.fonts[20] = pygame.font.SysFont('arial', 20)
        y2 = 0
        
        # --- Cadre du menu
        fond_cadre = FCT.image_vide(self.dimX + (self.esp *2), (len(self.MENU) * ((self.dimY + self.esp)+1))+2)
        fond_cadre.fill((8,8,8,200))
        pygame.draw.rect(fond_cadre, (64,64,64,255), (0, 0, fond_cadre.get_width()-1, fond_cadre.get_height()-1), 2)
        VAR.fenetre.blit(fond_cadre, (self.offX - self.esp, self.offY - self.esp + y2))
        
        # --- Elements du menu   
        for id, txt_menu in self.MENU:
            x, y = self.offX, self.offY + y2 
            
            if id == -1:
                fond_bouton = (32,32,32,255)
            else:
                fond_bouton = (64,64,64,255)
                
            if id == -2:
                txt_menu = VAR.clavier.mot
            elif id < -2:
                pass
                
            # --- dessine fond de l'element
            fond_image = FCT.image_vide(self.dimX,self.dimY)
            fond_image.fill(fond_bouton)
            pygame.draw.rect(fond_image, (64,64,64,255), (0, 0, fond_image.get_width(), fond_image.get_height()), 2)
            VAR.fenetre.blit(fond_image, (x, y))
            
            # --- dessine le texte de l'element
            text_image =  VAR.fonts[20].render(txt_menu, True, (255,255,255,255)) 
            VAR.fenetre.blit(text_image, (x + int((self.dimX - text_image.get_width())/2), y + int((self.dimY - text_image.get_height())/2) ))
            
            # --- gere la selection
            if VAR.objets_interface.zone_clickable(x, y, self.dimX, self.dimY, 0) == VAR.ENUM_Clic.Clic:
                self.action_menu(id)
            
            # --- saut une ligne
            y2 += self.dimY + self.esp
        

    def afficher_fond_anime(self):
        if self.fond_old == None:
            self.fond_old = FCT.image_vide(VAR.EcranX, VAR.EcranY)
            self.fond_old.blit(VAR.fenetre, (0,0))
        
        VAR.fenetre.blit(self.fond_old, (0, 0))
        
        for y in range(0, VAR.EcranY, 4):
            pygame.draw.line(VAR.fenetre, (64,64,64,100), (0, y), (VAR.EcranX, y) ,2)
                
        
        
    
    