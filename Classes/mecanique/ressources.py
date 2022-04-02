import pygame
from pygame.locals import *

import variables as VAR
import classes.commun.fonctions as FCT


class CRessources:
    def __init__(self):
        print("    + Initialisation module << Ressources >>")


    def afficher(self, menu=False):
        titre_img = pygame.image.load("images\\titre.jpg")
        
        titre_txt = pygame.image.load("images\\titre.png").convert_alpha()  
        ratio = VAR.EcranX / titre_txt.get_width() * 0.60
        dimX = int(titre_txt.get_width() * ratio) 
        dimY = int(titre_txt.get_height() * ratio) 
        
        titre_img = pygame.transform.scale(titre_img, (VAR.EcranX, VAR.EcranY))
        titre_txt = pygame.transform.scale(titre_txt, (dimX, dimY))
        VAR.fenetre.blit(titre_img, (0,0))
        
        if menu == False:
            VAR.fenetre.blit(titre_txt, (int((VAR.EcranX - titre_txt.get_width())/2), int((VAR.EcranY - titre_txt.get_height())/2) ))
        else:
            VAR.fenetre.blit(titre_txt, (int((VAR.EcranX - titre_txt.get_width())/2), 100))
        pygame.display.update()
        
    def charger_musique(self, musique):
        pygame.mixer.music.load("audios\\" + VAR.MUSICS[musique])
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play()
            
    def barre_progression(self, valeur, max = 100):
        largeur_barre = int((VAR.EcranX / 3) * 2)
        hauteur_barre = 30

        longueur_barre = int(((largeur_barre) / max) * valeur)
        position_milieu = int((VAR.EcranX - largeur_barre) / 2)
        
        x, y = position_milieu, VAR.EcranY -40 - hauteur_barre
        pygame.draw.rect(VAR.fenetre, (0,0,0,255), (x, y,largeur_barre, hauteur_barre), 0)    # --- FOND
        pygame.draw.rect(VAR.fenetre, (255,255,0,255), (x, y,longueur_barre, hauteur_barre), 0)    # --- BARRE
        pygame.draw.rect(VAR.fenetre, (255,0,0,255), (x, y, largeur_barre, hauteur_barre), 2)    # --- CADRE
        pygame.display.flip()

    def chargement(self):
        self.afficher()
        print("\n+ Chargements des ressources")

        VAR.texture = pygame.image.load("images\\donjon.png").convert_alpha()   
        VAR.icones = pygame.image.load("images\\icones.png").convert_alpha()   
        VAR.icones_mechants = pygame.image.load("images\\mechants\\icones.png").convert_alpha()   
        self.barre_progression(10)

        VAR.perso = pygame.image.load("images\\EnemySpriteSheet1.png-par-Kazzador.png").convert_alpha()   
        
       
        # --- eau
        i = 0
        tmp = pygame.image.load("images\\eau2.png").convert_alpha()   
        for y in range(0, 4):
            for x in range(0, 8):
                VAR.IMG["eau" + str(i)] = FCT.image_decoupe(tmp, x, y, 48, 48 )
                i = i +1

        i = 0
        tmp = pygame.image.load("images\\passage2.png").convert_alpha()   
        for y in range(0, 3):
            for x in range(0, 8):
                VAR.IMG["passage" + str(i)] = FCT.image_decoupe(tmp, x, y, 48, 48 )
                i = i +1

        tmp = pygame.image.load("images\\icones2.png").convert_alpha()   
        VAR.IMG["coffre_ouvert"] = pygame.image.load("images\\objets\\coffre_ouvert.png").convert_alpha()   
        VAR.IMG["coeur"] = FCT.image_decoupe(tmp, 0, 0, 42, 42 )
        VAR.IMG["mini_coeur"] = FCT.image_decoupe(tmp, 0, 0, 42, 42, 16, 16 )
        VAR.IMG["mort"] = FCT.image_decoupe(tmp,  1, 0, 42, 42 )
        #VAR.IMG["cle"] = FCT.image_decoupe(tmp,  2, 0, 42, 42 )
        VAR.IMG["energie"] = FCT.image_decoupe(tmp,  3, 0, 42, 42 )
        self.barre_progression(20)

        for i, j in enumerate(VAR.ENUM_Actions):
            id = j.value
            VAR.IMG[id] = FCT.image_decoupe(pygame.image.load("images\\icones.png").convert_alpha(), id, 0, 63, 66 )
        self.barre_progression(30)  

        VAR.img0 = pygame.image.load("images\\1674_1057998444.png").convert_alpha()  
  
        VAR.img2 = pygame.transform.flip(pygame.image.load("images\\mechants\\00.png").convert_alpha(), True, False) 
        VAR.des = pygame.image.load("images\\des.png").convert_alpha()
        
        VAR.objets.image_icones = pygame.image.load("images\\objets\\icones.png").convert_alpha()

        VAR.SONS["rotation"] = pygame.mixer.Sound("audios\\2005.wav")
        VAR.SONS["poser"] = pygame.mixer.Sound("audios\\591.wav")

        VAR.MUSICS["JEU1"] = "Krzysztof_Kurkowski_-_A_forest_village_.mp3"
        VAR.MUSICS["JEU2"] = "Krzysztof_Kurkowski_-_A_walk_.mp3"
        VAR.MUSICS["COMBAT"] = "Krzysztof_Kurkowski_-_the_last_battle.mp3"
        self.barre_progression(40)
        
        VAR.mechants.charger()
        self.barre_progression(50)
        VAR.objets.charger()
        self.barre_progression(60)
        #VAR.tuiles.placer_piece_centrale()
        self.barre_progression(70)
        VAR.heros.charger()
        self.barre_progression(80)
        #VAR.jetons.charger()    
        
        

        for taille in (10,20,30,60,90,120,150):
            VAR.fonts[taille] = pygame.font.SysFont('arial', taille) 
            

        #VAR.notifications.ajouter("","","Bonjour et bienvenu !")
        #VAR.notifications.ajouter("","","Piocher une carte")
       # VAR.notifications.ajouter("","","dans le sac à droite.")
        #VAR.notifications.ajouter("","","A vous de jouer ...")

        self.barre_progression(100)
        self.afficher(True)
        #time.sleep(1)