import pygame
from pygame.locals import *

import variables as VAR
import classes.commun.fonctions as FCT
import classes.ui.ui_transitions as TRANSITION

import csv, math, random
import classes.persos.mechant as CM

class CMechants():
    def __init__(self):
        print("    + Initialisation module << Mechants >>")
        
        self.liste = {}
    
    
    def nb_mechants(self):
        return len(self.liste)   
     
     
    def charger(self):
        print("    + Chargement du fichier de mechants : infos.csv")
        
        with open('images\\mechants\\infos.csv') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=';')
            for ligne in reader:
                if len(ligne) == 7:                                                     # --- il faut que la ligne comporte chaque colonne importante
                    numero, nom, force, tirage, recompense, specialite, quantite = ligne
                    if numero.__contains__("#") == False:                             # --- evite les lignes commentées
                        tmp_image, tmp_icone = pygame.image.load("Images\\mechants\\" + numero + ".png").convert_alpha(), None
                        #tmp_image = FCT.Generer_Mask_Image(tmp_image)
                        
                        self.liste[numero] = CM.CMechant(nom.strip(), int(force), int(tirage), tmp_image, tmp_icone, recompense.strip(), specialite.strip(), int(quantite))
                        print ("        + " + quantite + "x Mechant << " + nom + " >> ajouté.")
        

    def piocher(self):
        return random.randint(0, VAR.mechants.nb_mechants())
    

    def afficher_tirage_monstre(self, choix):
        j, k = 0, 0

        animation_cycle = pygame.time.get_ticks()
        arret_tirage_cycle, tirage_delais, tirage = pygame.time.get_ticks(), 3000, True

        centreX, centreY = int(VAR.EcranX / 2), int(VAR.EcranY /2)+200
        centreCadreY = centreY-80

        boucle_active = True
        while boucle_active:
            VAR.fenetre.fill((32,32,32,255))
            
            for event in pygame.event.get():        
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    VAR.boucle_principale = False
                    boucle_active = False
            
            # --- Tourbillons
            VAR.fenetre.blit(TRANSITION.image_tourbillon((centreX, centreY), k % 358, (16,16,16), 20, 0 ),(0,0))
            VAR.fenetre.blit(TRANSITION.image_tourbillon((centreX, centreY), -(k % 358), (40,40,40), 7, 20 ),(0,0))
            
            # --- Cadre
            pygame.draw.rect(VAR.fenetre, (0,0,0,255), (0, centreCadreY-10, VAR.EcranX, 200), 0) #390
            pygame.draw.rect(VAR.fenetre, (16,16,16,255), (0, centreCadreY, VAR.EcranX, 180), 0) #400
            
            # --- Liste des monstres
            nbImages = int(VAR.EcranY / self.nb_mechants())
            for i in range(nbImages):
                resultat = ((i+j) % (self.nb_mechants()))
                VAR.fenetre.blit(FCT.image_decoupe(VAR.icones_mechants, resultat, 0, 100, 100), ((i*100)-30, centreCadreY +40)) #435

            # --- Fleches en mouvements
            c1, c2 = (32,32,0,255), (64,64,0,255)
            mouvement =  ((j%3) * 8)
            pygame.draw.polygon(VAR.fenetre, c1, ((centreX-50, centreCadreY - 40 +mouvement), (centreX+50, centreCadreY - 40  +mouvement), (centreX, centreCadreY + 50 +mouvement))) #360,360,450
            pygame.draw.polygon(VAR.fenetre, c2, ((centreX-30, centreCadreY - 30 +mouvement), (centreX+30, centreCadreY - 30  +mouvement), (centreX, centreCadreY + 30 +mouvement))) #370,370,430

            pygame.draw.polygon(VAR.fenetre, c1, ((centreX-50, centreCadreY + 230 -mouvement), (centreX+50, centreCadreY + 230 -mouvement), (centreX, centreCadreY + 135 -mouvement))) #620,620,525
            pygame.draw.polygon(VAR.fenetre, c2, ((centreX-30, centreCadreY + 220 -mouvement), (centreX+30, centreCadreY + 220 -mouvement), (centreX, centreCadreY + 155 -mouvement))) #610,610,545

            if tirage == True:
                if pygame.time.get_ticks() - animation_cycle > 100 :            # --- Tempo de l'animation
                    j = j +1 
                    animation_cycle = pygame.time.get_ticks()
                
                if pygame.time.get_ticks() - arret_tirage_cycle > tirage_delais:            # --- Arret de la roulette sur le monstre selectionné
                    resultat = (((int(nbImages/2)+j-2) % (self.nb_mechants())) == choix)       # --- 6 = position de l'image selectionnée
                    if resultat == True:
                        tirage, arret_tirage_cycle = False, pygame.time.get_ticks() 
            
            else:       # --- affichage du monstre
                t = int(3 * math.cos (k))
                id = FCT.iif(choix < 10, "0"+str(choix), str(choix))
                monstre = self.liste[id]
                tmp = pygame.transform.scale(monstre.image, (monstre.image.get_width(), monstre.image.get_height() + t))
                VAR.fenetre.blit(tmp, (centreX - (tmp.get_width() / 2), centreCadreY - tmp.get_height()))

                if pygame.time.get_ticks() - arret_tirage_cycle > tirage_delais:                # --- Delais supplémentaire pour quitter l'ecran
                    boucle_active = False
                    
            k=k+1    
            pygame.display.update()
            VAR.clock.tick(VAR.fps)