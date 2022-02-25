 
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

from ressources import *

import Classes.ui_transitions as TRANSITION

 
import variables as VAR
from variables import *

import fonctions as FCT
import Classes.ui_transitions

class CMoteur:
    def __init__(self):
        print("+ Initialisation module << Moteur >>")

        VAR.ressources = CRessources(self)    
        VAR.heros = Cheros(self)
        VAR.tuiles = CTuiles(self)
        VAR.plateau = CPlateau(self)
        VAR.interfaces = CInterfaces(self)
        VAR.objets = CObjets_Interface(self)
        VAR.combat = CCombat(self)
        VAR.jetons = CJetons(self)
        VAR.mechants = CMechants(self)
        VAR.phase = CPhase(self)

        VAR.boucle_principale = True

    def demarre(self):
        pygame.init()
        pygame.mixer.init()

        VAR.fenetre = pygame.display.set_mode((VAR.EcranX, VAR.EcranY), pygame.DOUBLEBUF, 32)
        pygame.display.set_caption("PyRAK v0.01")
        
        VAR.ressources.chargement()
        self.boucle()

   
        

        
    def gestion_clavier_souris(self):
        self.mouseG, self.mouseM, self.mouseD = pygame.mouse.get_pressed()
        self.mX, self.mY = pygame.mouse.get_pos()
            
        for event in pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                VAR.boucle_principale = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.souris = pygame.mouse.get_pressed()
                    
            if event.type == KEYDOWN:  
                if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT:
                    if event.key == 270 and VAR.Zoom < 64: FCT.zoom(True)
                    if event.key == 269 and VAR.Zoom > 5: FCT.zoom(False)
                        
                    
                    if event.key == K_LEFT: VAR.OffsetX = VAR.OffsetX + VAR.Taille
                    if event.key == K_RIGHT: VAR.OffsetX = VAR.OffsetX - VAR.Taille
                    if event.key == K_UP: VAR.OffsetY = VAR.OffsetY + VAR.Taille
                    if event.key == K_DOWN: VAR.OffsetY = VAR.OffsetY - VAR.Taille
                    
                    if VAR.OffsetX > VAR.v9: VAR.OffsetX = VAR.v9
                    if VAR.OffsetY > VAR.v9: VAR.OffsetY = VAR.v9
    
    def charger_musique(self, musique):
        pygame.mixer.music.load("Audios\\" + VAR.MUSICS[musique])
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
        
    def boucle(self):
        

        self.gestion_rythme(0)
        self.charger_musique("JEU1")
        
        
        while VAR.boucle_principale:
                 
            self.gestion_clavier_souris()
            #VAR.plateau.gestion_deplacement_plateau()
            VAR.heros.gestion_deplacement_joueur()
            
            VAR.plateau.fond()
            VAR.plateau.afficher()
            VAR.interfaces.afficher()

            VAR.phase.gestion_des_phases_de_jeu()
           
                    
            
            
            # ---------------------------------

            # ---------------------------------  
            FCT.texte(VAR.fenetre, "FPS : " + str(VAR.fps), 32, 20, 10)
            FCT.texte(VAR.fenetre, "ZOOM : " + str(VAR.Zoom), 32, 30, 10)
            FCT.texte(VAR.fenetre, "PIOCHE : " + str(len(VAR.tuiles.pioche)), 32, 40, 10)

            pygame.display.update()
            self.gestion_rythme(1)

        pygame.quit() 
        
 
        
        
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


                 
    