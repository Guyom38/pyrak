import pygame
from pygame.locals import *

import csv
import variables as VAR
import fonctions as FCT


class CObjet():
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        
        self.icone = FCT.image_decoupe( VAR.objets.image_icones, id, 0, VAR.objets.image_icone.x, VAR.objets.image_icone.y )

class CObjets():
    def __init__(self, moteur):
        print("    + Initialisation module << Objets >>")
        self.moteur = moteur
        self.liste = {}

        print("        + Chargement du fichier de textures << icones.png >>")
        self.image_icone_x, self.image_icone_y = 50, 50
        self.image_icones = pygame.image.load("images\\objets\\icones.png").convert_alpha()

    def charger(self):
        print("    + Chargement du fichier des objets : infos.csv")
        
        with open('images\\objets\\infos.csv') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=';')
            for ligne in reader:
                if len(ligne) == 2:                                                     # --- il faut que la ligne comporte chaque colonne importante
                    numero, nom = ligne
                    if numero.__contains__("#") == False:                             # --- evite les lignes commentées
                        self.liste[nom] = CObjet(numero, nom)
                        print ("        + Objet << " + nom + " >> ajouté.")