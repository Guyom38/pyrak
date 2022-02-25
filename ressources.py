import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT

class CRessources:
    def __init__(self, moteur):
        print("    + Initialisation module << Ressources >>")
        self.moteur = moteur

    def chargement(self):
        print("\n+ Chargements des ressources")

        VAR.texture = pygame.image.load("Images\\donjon.png").convert_alpha()   
        VAR.icones = pygame.image.load("Images\\icones.png").convert_alpha()   
        VAR.icones_mechants = pygame.image.load("Images\\mechants\\icones.png").convert_alpha()   
        
        VAR.perso = pygame.image.load("Images\\EnemySpriteSheet1.png-par-Kazzador.png").convert_alpha()   
        
        tmp = pygame.image.load("Images\\icones2.png").convert_alpha()   
    
        VAR.IMG["coeur"] = FCT.image_decoupe(tmp, 0, 0, 42, 42 )
        VAR.IMG["mini_coeur"] = FCT.image_decoupe(tmp, 0, 0, 42, 42, 16, 16 )
        VAR.IMG["mort"] = FCT.image_decoupe(tmp,  1, 0, 42, 42 )
        #VAR.IMG["cle"] = FCT.image_decoupe(tmp,  2, 0, 42, 42 )
        VAR.IMG["energie"] = FCT.image_decoupe(tmp,  3, 0, 42, 42 )
       
        for id, e in enumerate(ENUM_Actions):
            VAR.IMG[str(e)] = FCT.image_decoupe(pygame.image.load("Images\\icones.png").convert_alpha(), int(e.value), 0, 63, 66 )
        
        for id, e in enumerate(ENUM_Objets):
            VAR.IMG[str(e)] = FCT.image_decoupe(pygame.image.load("Images\\icones3.png").convert_alpha(), int(e.value), 0, 50, 50 )
            
        #VAR.IMG["cle"] = FCT.image_decoupe(tmp, 0, 0, 50, 50 )
        #VAR.IMG["coffre"] = FCT.image_decoupe(tmp, 1, 0, 50, 50 )
        #VAR.IMG["couteaux"] = FCT.image_decoupe(tmp, 2, 0, 50, 50 )
        #VAR.IMG["hache"] = FCT.image_decoupe(tmp, 3, 0, 50, 50 )
        #VAR.IMG["piege"] = FCT.image_decoupe(tmp, 4, 0, 50, 50 )
        #VAR.IMG["masse"] = FCT.image_decoupe(tmp, 5, 0, 50, 50 )
        #VAR.IMG["vie"] = FCT.image_decoupe(tmp, 6, 0, 50, 50 )
        #VAR.IMG["epee"] = FCT.image_decoupe(tmp, 7, 0, 50, 50 )
        
        VAR.img0 = pygame.image.load("Images\\1674_1057998444.png").convert_alpha()  
        VAR.img1 = pygame.image.load("Images\\persos\\perso1.png").convert_alpha()    
        VAR.img2 = pygame.transform.flip(pygame.image.load("Images\\mechants\\00.png").convert_alpha(), True, False) 
        VAR.des = pygame.image.load("Images\\des.png").convert_alpha()
     
        VAR.SONS["rotation"] = pygame.mixer.Sound("Audios\\2005.wav")
        VAR.SONS["poser"] = pygame.mixer.Sound("Audios\\591.wav")

        VAR.MUSICS["JEU1"] = "Krzysztof_Kurkowski_-_A_forest_village_.mp3"
        VAR.MUSICS["JEU2"] = "Krzysztof_Kurkowski_-_A_walk_.mp3"
        VAR.MUSICS["COMBAT"] = "Krzysztof_Kurkowski_-_the_last_battle.mp3"

        
        VAR.mechants.charger()
        VAR.objets.charger()
        
        VAR.tuiles.placer_piece_centrale()
        
        VAR.heros.charger()
        VAR.jetons.charger()    
        
        VAR.joueur_en_cours = VAR.heros.liste[0]
        VAR.joueur_en_cours.recentrer_camera()

        for taille in (10,20,30,60,120,150):
            VAR.fonts[taille] = pygame.font.SysFont('arial', taille) 