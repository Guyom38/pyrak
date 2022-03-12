 
import pygame
from pygame.locals import *
from Classes.mechants import CMechants


from Classes.tuiles import *
from plateau import *
from Classes.ui_interfaces import *
from Classes.heros import *
from Classes.ui_combat import *
from Classes.jetons import *
from phase import *
from Classes.objets import *
from Classes.camera import *
from Classes.notifications import *
from Classes.ui_recompense import *
from Menu.clavier import *

from partie import *
from Menu.menu import *


from ressources import *

import Classes.ui_transitions as TRANSITION

 
import variables as VAR
from variables import *

import fonctions as FCT
import Classes.ui_transitions
import pickle

class CMoteur:
    def __init__(self):
        print("+ Initialisation module << Moteur >>")

        VAR.menu = CMenu()
        VAR.partie = CPartie()
        VAR.camera = CCamera()
        VAR.ressources = CRessources()    
        VAR.heros = Cheros()
        VAR.tuiles = CTuiles()
        VAR.plateau = CPlateau()
        VAR.interfaces = CInterfaces()
        VAR.objets_interface = CObjets_Interface()
        VAR.combat = CCombat()
        VAR.jetons = CJetons()
        VAR.mechants = CMechants()
        VAR.phase = CPhase()
        VAR.objets = CObjets()
        VAR.notifications = CNotifications()
        VAR.recompense = CRecompense()
        VAR.clavier = CClavier()
        
        VAR.boucle_principale = True


    def demarre(self):
        pygame.init()
        pygame.mixer.init()

        VAR.fenetre = pygame.display.set_mode((VAR.EcranX, VAR.EcranY), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("PyRAK v0.04")

        VAR.ressources.chargement()
        #VAR.partie.charger()
        
        VAR.camera.centrer_sur_joueur()
        VAR.notifications.initialiser_bandeau(VAR.joueur_en_cours.nom + ", a vous de jouer !")

        self.boucle()
    
        
    def boucle(self):
        
        self.gestion_rythme(0)

        while VAR.boucle_principale:
            VAR.evenements = pygame.event.get()
            self.gestion_souris()
            
            if VAR.phase_du_jeu == ENUM_Phase.MENU:
                VAR.menu.afficher()
                
            else:
                VAR.plateau.gestion_deplacement_plateau()
                VAR.heros.gestion_deplacement_joueur()
                VAR.camera.gestion()
                
                self.gestion_clavier()
                VAR.plateau.fond()
                
                VAR.phase.gestion_des_phases_de_jeu()
                VAR.interfaces.afficher()
                VAR.notifications.afficher()

            VAR.clavier.afficher()
            
            FCT.texte(VAR.fenetre, "FPS : " + str(VAR.fps), 32, 20, 10)
            FCT.texte(VAR.fenetre, "ZOOM : " + str(VAR.Zoom), 32, 30, 10)
            FCT.texte(VAR.fenetre, "PIOCHE : " + str(len(VAR.tuiles.pioche)), 32, 40, 10)

            pygame.display.update()
            self.gestion_rythme(1)

        VAR.partie.enregistrer()
        pygame.quit() 
        
        
        
    def gestion_souris(self):
        VAR.mouseG, VAR.mouseM, VAR.mouseD = pygame.mouse.get_pressed()
        VAR.mX, VAR.mY = pygame.mouse.get_pos()
        
        for event in VAR.evenements: #pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                VAR.boucle_principale = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                VAR.souris = pygame.mouse.get_pressed()
        
    def gestion_clavier(self):
            
        for event in VAR.evenements: #pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                VAR.boucle_principale = False
                    
            if event.type == KEYDOWN:  
                if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT:
                    if event.key == 270 and VAR.Zoom < 64: FCT.zoom(True)
                    if event.key == 269 and VAR.Zoom > 5: FCT.zoom(False)
                        
                    
                    if event.key == K_LEFT: VAR.OffsetX = VAR.OffsetX + VAR.v9
                    if event.key == K_RIGHT: VAR.OffsetX = VAR.OffsetX - VAR.v9
                    if event.key == K_UP: VAR.OffsetY = VAR.OffsetY + VAR.v9
                    if event.key == K_DOWN: VAR.OffsetY = VAR.OffsetY - VAR.v9
                    
                    if VAR.OffsetX > VAR.v9: VAR.OffsetX = VAR.v9
                    if VAR.OffsetY > VAR.v9: VAR.OffsetY = VAR.v9        
        
    def gestion_rythme(self, id):
        if id == 0:
            # --- Initialisation FPS
            VAR.cycle = pygame.time.get_ticks()
            VAR.fps_cycle = pygame.time.get_ticks()
            VAR.fps_cpt = 0
            VAR.fps = 0

            VAR.clock = pygame.time.Clock()

        else:
            # --- Calcul FPS
            VAR.fps_cpt = VAR.fps_cpt +1
            if pygame.time.get_ticks() - VAR.fps_cycle > 1000: 
                VAR.fps = VAR.fps_cpt
                VAR.fps_cpt = 0
                VAR.fps_cycle = pygame.time.get_ticks()

            # --- Tempo Animation
            if pygame.time.get_ticks() - VAR.cpt_cycle > 25:
                VAR.cpt = VAR.cpt + 1
                VAR.cpt_cycle = pygame.time.get_ticks() 
            
            # --- Limitation FPS
            VAR.clock.tick(VAR.nombreImageSeconde)


                 
    