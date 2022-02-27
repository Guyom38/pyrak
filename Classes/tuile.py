import pygame
from pygame.locals import *
import variables as VAR
from variables import *

import outils
import fonctions as FCT


class CTuile(object):
    def __init__(self, moteur, acces, piece, fontaine, teleport, x = -1, y = -1):
        self.moteur = moteur
        
        self.acces = acces
        self.piece = piece
        self.fontaine = fontaine
        self.teleport = teleport
        self.x = x
        self.y = y

        self.image = None
        self.aMettreAjour = True
        
        self.jeton = None
        self.recompense = None

        self.depart = False

    # -1 : Rien ne se passe
    #  0 : Reprise du combat
    #  1 : Tirage avant combat
    def faut_il_tirer_un_jeton(self):
        lance_combat = -1

        if self.piece == True and self.depart == False:
            lance_combat = 1
            
            if self.jeton != None:
                if self.jeton.nom == VAR.COFFRE: 
                    lance_combat = -1
                else:
                    lance_combat = 0
            if self.recompense != None: lance_combat = -1
            
        return lance_combat
                    

    def generer(self):
        if self.piece == True:
            self.generer_piece()
        else:
            self.generer_couloir()


    def generer_couloir(self):

        # --- Piece
        self.base = [["BN","BN","BN","BN","BN","BN","BN","BN","BN"],
                     ["BN","BN","BN","BN","BN","BN","BN","BN","BN"],
                     ["BN","BN","I1","G1","G1","G1","I0","BN","BN"],
                     ["BN","BN","F2","90","91","92","F0","BN","BN"],
                     ["BN","BN","F2","A0","00","A2","F0","BN","BN"],
                     ["BN","BN","F2","B0","B1","B2","F0","BN","BN"],
                     ["BN","BN","H1","E1","E1","E1","H0","BN","BN"],
                     ["BN","BN","BN","BN","BN","BN","BN","BN","BN"],
                     ["BN","BN","BN","BN","BN","BN","BN","BN","BN"]]

        # --- Passage à gauche
        if self.acces[VAR.GAUCHE] == True:
            self.base[0][3], self.base[1][3],self.base[2][3]                  = "F2", "F2", "F2"
            self.base[0][4], self.base[1][4],self.base[2][4], self.base[3][4] = "51", "61", "00", "00"
            self.base[0][5], self.base[1][5],self.base[2][5]                  = "F0", "F0", "F0"
            
        # --- Passage à haut
        if self.acces[VAR.HAUT] == True:
            self.base[3][0], self.base[4][0], self.base[5][0] = "G1", "51", "E1"
            self.base[3][1], self.base[4][1], self.base[5][1] = "G1", "52", "E1"
            self.base[3][2], self.base[4][2], self.base[5][2] = "G1", "00", "E1"
            self.base[4][3] = "00"

        # --- Passage à droite
        if self.acces[VAR.DROITE] == True:
            self.base[6][3], self.base[7][3], self.base[8][3]                  = "F2", "F2", "F2"
            self.base[5][4], self.base[6][4], self.base[7][4], self.base[8][4] = "00", "00", "41", "51"
            self.base[6][5], self.base[7][5], self.base[8][5]                  = "F0", "F0", "F0"   

        # --- Passage à bas
        if self.acces[VAR.BAS] == True:
            self.base[4][5] = "00"
            self.base[3][6], self.base[4][6], self.base[5][6] = "G1", "00", "E1"
            self.base[3][7], self.base[4][7], self.base[5][7] = "G1", "50", "E1"
            self.base[3][8], self.base[4][8], self.base[5][8] = "G1", "51", "E1"

        # --- Angle
        if self.acces[VAR.GAUCHE] == True: # GAUCHE
            if self.acces[VAR.HAUT] == True: # HAUT
                self.base[3][3] = "G2"
                self.base[2][2] = "BN"
            if self.acces[VAR.BAS] == True: # BAS
                self.base[3][5] = "G0"
                self.base[2][6] = "BN"

        if self.acces[VAR.DROITE] == True: # DROITE
            if self.acces[VAR.HAUT] == True:  # HAUT
                self.base[5][3] = "E2"
                self.base[6][2] = "BN"
            if self.acces[VAR.BAS] == True:  # BAS
                self.base[5][5] = "E0"
                self.base[6][6] = "BN"

        if self.acces != (True, True, True, True):
            if self.acces[VAR.GAUCHE] == False   and self.acces[VAR.BAS] == True      : self.base[3][6] = "G0"      
            if self.acces[VAR.GAUCHE] == False   and self.acces[VAR.HAUT] == True     : self.base[3][2] = "G2"     
            if self.acces[VAR.HAUT] == False     and self.acces[VAR.DROITE] == True   : self.base[6][3] = "E2"     
            if self.acces[VAR.HAUT] == True      and self.acces[VAR.DROITE] == False  : self.base[5][2] = "E2"  
            if self.acces[VAR.BAS] == True       and self.acces[VAR.DROITE] == False  : self.base[5][6] = "E0"  
            if self.acces[VAR.BAS] == False      and self.acces[VAR.DROITE] == True   : self.base[6][5] = "E0"  
            if self.acces[VAR.GAUCHE] == True    and self.acces[VAR.HAUT] == False    : self.base[2][3] = "G2"  
            if self.acces[VAR.GAUCHE] == True    and self.acces[VAR.BAS] == False     : self.base[2][5] = "G0"  

    def generer_piece(self):
        # --- Piece
        self.base = [["I1","G1","G1","G1","G1","G1","G1","G1","I0"],
                     ["F2","19","0A","0A","0A","0A","0A","1A","F0"],
                     ["F2","28","90","91","91","91","92","28","F0"],
                     ["F2","28","A0","00","00","00","A2","28","F0"],
                     ["F2","28","A0","00","00","00","A2","28","F0"],
                     ["F2","28","A0","00","00","00","A2","28","F0"],
                     ["F2","28","B0","B1","B1","B1","B2","28","F0"],
                     ["F2","29","0A","0A","0A","0A","0A","2A","F0"],
                     ["H1","E1","E1","E1","E1","E1","E1","E1","H0"]]
        
        # --- Passage à gauche
        if self.acces[VAR.GAUCHE] == True:
            self.base[0][3], self.base[1][3]                  = "G2", "1A"
            self.base[0][4], self.base[1][4], self.base[2][4] = "51", "61", "00"
            self.base[0][5], self.base[1][5]                  = "G0", "3B"   
            
        # --- Passage à haut
        if self.acces[VAR.HAUT] == True:
            self.base[3][0], self.base[4][0], self.base[5][0] = "G2", "51", "E2"
            self.base[3][1], self.base[4][1], self.base[5][1] = "38", "52", "18"
            self.base[4][2] = "00"

        # --- Passage à droite
        if self.acces[VAR.DROITE] == True:
            self.base[7][3], self.base[8][3]                  = "2A", "E2"
            self.base[6][4], self.base[7][4], self.base[8][4] = "00", "41", "51"
            self.base[7][5], self.base[8][5]                  = "1B", "E0"   
            
        # --- Passage à bas
        if self.acces[VAR.BAS] == True:
            self.base[4][6] = "00"
            self.base[3][7], self.base[4][7], self.base[5][7] = "38", "50", "18"
            self.base[3][8], self.base[4][8], self.base[5][8] = "G0", "51", "E0"


    def tourner(self):
        gauche, haut, droite, bas = self.acces
        self.acces = (bas, gauche, haut, droite)
        self.aMettreAjour = True
        self.generer()


    def afficher(self, xX = -1, yY = -1):
        if (xX, yY) == (-1, -1):
            xX, yY = self.x, self.y
        
        if self.image == None or self.aMettreAjour == True:
            self.image = pygame.Surface((VAR.v9, VAR.v9),pygame.SRCALPHA,32)    
            for y in range(9):
                for x in range(9):
                    tmp = FCT.image(self.base[x][y])
                    self.image.blit(tmp, (x * VAR.Zoom, y * VAR.Zoom), (0, 0, VAR.Zoom, VAR.Zoom))
            self.aMettreAjour = False
        
        xP, yP = VAR.OffsetX + ((xX * 9)  * VAR.Zoom), VAR.OffsetY + ((yY * 9) * VAR.Zoom)
        VAR.fenetre.blit(self.image, (xP, yP, VAR.Zoom, VAR.Zoom))
        
        # --- affichage du mechant
        if self.piece == True and VAR.Zoom > 15 :
            xP, yP = xP+VAR.v2, yP+VAR.v2
            
            if self.jeton != None:                                              # --- Dessin du monstre tiré
                VAR.fenetre.blit(self.jeton.image, (xP, yP))
                FCT.texte(VAR.fenetre, str(self.jeton.force), xP, yP, 60, pygame.Color(0,0,0,255))
                FCT.texte(VAR.fenetre, str(self.jeton.force), xP+2, yP+2, 60, pygame.Color(255,255,255,255))
        
            elif self.recompense != None :                                       # --- Dessin de la recompense a prendre
                VAR.fenetre.blit(VAR.objets.liste[self.recompense].icone, (xP, yP))


    
        
          
        
 
            
        
        
    