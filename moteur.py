 
import pygame
from pygame.locals import *

import Classes.mechants as CMS
import Classes.tuiles as CTS
import plateau as CPL
import Classes.ui_interfaces as CUI
import Classes.heros as CHS
import Classes.ui_combat as CUC
import Classes.jetons as CJS
import phase as CPH
import Classes.objets as COS
import Classes.camera as CCA
import Classes.notifications as CNS
import Classes.ui_recompense as CRE
import Menu.clavier as CCL
import Classes.ui_transitions as CUT
import Classes.ui_objets_interface as CUO
import partie as CPA
import Menu.menu as CME
import ressources as CRS


 
import variables as VAR
import fonctions as FCT


class CMoteur:
    def __init__(self):
        print("+ Initialisation module << Moteur >>")

        VAR.menu = CME.CMenu()
        VAR.partie = CPA.CPartie()
        VAR.camera = CCA.CCamera()
        VAR.ressources = CRS.CRessources()    
        VAR.heros = CHS.Cheros()
        VAR.tuiles = CTS.CTuiles()
        VAR.plateau = CPL.CPlateau()
        VAR.interfaces = CUI.CInterfaces()
        VAR.objets_interface = CUO.CObjets_Interface()
        VAR.combat = CUC.CCombat()
        VAR.jetons = CJS.CJetons()
        VAR.mechants = CMS.CMechants()
        VAR.phase = CPH.CPhase()
        VAR.objets = COS.CObjets()
        VAR.notifications = CNS.CNotifications()
        VAR.recompense = CRE.CRecompense()
        VAR.clavier = CCL.CClavier()
        
        VAR.boucle_principale = True


    def demarre(self):
        pygame.init()
        pygame.mixer.init()

        VAR.fenetre = pygame.display.set_mode((VAR.EcranX, VAR.EcranY), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("PyRAK v0.04")

        VAR.ressources.chargement()
        #VAR.partie.charger()
        
        #VAR.camera.centrer_sur_joueur()
        #VAR.notifications.initialiser_bandeau(VAR.joueur_en_cours.nom + ", a vous de jouer !")

        self.boucle()
    
        
    def boucle(self):
        
        self.gestion_rythme(0)

        while VAR.boucle_principale:
            VAR.evenements = pygame.event.get()
            self.gestion_souris()
            
            if VAR.phase_du_jeu == VAR.ENUM_Phase.MENU:
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

            pygame.display.update()
            self.gestion_rythme(1)

        
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
                if VAR.phase_du_jeu == VAR.ENUM_Phase.DEPLACEMENT:
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


                 
    