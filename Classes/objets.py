import pygame
from pygame.locals import *

import csv
import variables as VAR
import fonctions as FCT

from Classes.objet import *

class CObjets():
    def __init__(self, moteur):
        print("    + Initialisation module << Objets >>")
        self.moteur = moteur
        self.liste = {}

        self.image_icone_x, self.image_icone_y = 50, 50
        self.image_icones = None
        

    def charger(self):
        print("    + Chargement du fichier des objets : icones.png, infos.csv")

        with open('images\\objets\\infos.csv') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=';')
            for ligne in reader:
                if len(ligne) == 2:                                                     # --- il faut que la ligne comporte chaque colonne importante
                    numero, nom = ligne
                    if numero.__contains__("#") == False:  
                        nomf = nom.strip()                           # --- evite les lignes commentées
                        self.liste[nomf] = CObjet(numero, nomf)
                        print ("        + Objet << " + nomf + " >> ajouté.")