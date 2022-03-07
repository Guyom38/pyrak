import pygame
from pygame.locals import *

from Classes.hero import *

import variables as VAR
import fonctions as FCT

import csv

class Cheros():
    def __init__(self):
        print("    + Initialisation module << Heros >>")
        
        self.liste = []
        self.liste_heros = {}
        self.joueur_liste_position = 0
        
        self.cpt_cycle = 0
        self.cpt = 0
        
    def charger(self):
        print("\n    + Chargement du fichier de heros : infos.csv")
        
        with open('images\\heros\\infos.csv') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=';')
            for ligne in reader:
                if len(ligne) == 4:                                                     # --- il faut que la ligne comporte chaque colonne importante
                    numero, nom, capacite1, capacite2 = ligne
                    if numero.__contains__("#") == False:                             # --- evite les lignes commentées
                        self.liste_heros[numero.strip()] = Chero(numero.strip(), nom.strip())
                        print ("        + Heros << " + nom + " >> ajouté.")
        

        self.liste.append(self.liste_heros["00"])
        self.liste.append(self.liste_heros["01"])
        self.liste.append(self.liste_heros["02"])
        

    def gestion_deplacement_joueur(self):
        if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT:
            if VAR.joueur_en_cours.seDeplace == True: 
                VAR.joueur_en_cours.gestion_deplacement()
            
            elif VAR.joueur_en_cours.mouvement == 0: 
                self.joueur_suivant()
            

    def afficher_sur_zone(self, x, y): 
        for hero in self.liste:
            if hero.x == x and hero.y == y:
                hero.afficher()
                
    def afficher(self):
        if pygame.time.get_ticks() - self.cpt_cycle > 150:
            self.cpt = self.cpt + 1
            self.cpt_cycle = pygame.time.get_ticks() 
                
        for x in range(len(VAR.terrain)):
            for y in range(len(VAR.terrain[x])):
                xP, yP = VAR.OffsetX + ((x * VAR.Zoom) * 9), (VAR.OffsetY + (y * VAR.Zoom) * 9)
                if FCT.SurEcran(xP, yP, VAR.v9, VAR.v9) == True:
                    VAR.heros.afficher_sur_zone(x, y)


    def joueur_suivant(self):
        VAR.notifications.afficher_bandeau(VAR.joueur_en_cours.nom + ", c'est a vous de jouer !")
        if self.joueur_liste_position < len(self.liste) -1:
            self.joueur_liste_position = self.joueur_liste_position +1
        else:
            self.joueur_liste_position = 0

        VAR.joueur_en_cours = self.liste[self.joueur_liste_position]
        VAR.joueur_en_cours.mouvement = 4
        VAR.joueur_en_cours.recentrer_camera()


