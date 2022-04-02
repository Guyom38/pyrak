import pygame
from pygame.locals import *
import random

import Classes.tuile as CT
import fonctions as FCT
import variables as VAR


class CTuiles():
    def __init__(self):
        print("    + Initialisation module << Tuiles >>")
       

    def joueur_a_deja_pioche(self):
        return (self.tuileSelect != None)
# //
# // ---   
    def charger(self):
        self.pioche = []
        self.piochePosition = 0
        self.tuileSelect = None
        
        #def __init__(acces, piece, fontaine, teleport, x = -1, y = -1):
        for i in range(20):  self.pioche.append( CT.CTuile( [True, True, False, False], False, True, False))
        for i in range(30):  self.pioche.append( CT.CTuile( [True, True, False, False], False, False, False))
        for i in range(13): self.pioche.append( CT.CTuile( [True, False, True, False], True, False, False))
        for i in range(13): self.pioche.append( CT.CTuile( [True, True, False, False], True, False, False))
        for i in range(14): self.pioche.append( CT.CTuile( [True, True, True, True], True, False, False))
        for i in range(10):  self.pioche.append( CT.CTuile( [True, True, True, False], False, False, False))
        for i in range(13): self.pioche.append( CT.CTuile( [True, True, True, False], True, False, False))
        for i in range(14):  self.pioche.append( CT.CTuile( [True, True, True, True], False, False, False))
        for i in range(20):  self.pioche.append( CT.CTuile( [True, False, True, False], False, False, True))
        for i in range(20):  self.pioche.append( CT.CTuile( [True, False, True, False], False, False, False))
        
        self.melanger()

    def melanger(self):
        random.shuffle(self.pioche)
        
# //
# // ---   
    def piocher(self):
        if len(self.pioche)-1 > self.piochePosition:
            self.tuileSelect = self.pioche[self.piochePosition]
            self.piochePosition += 1

# //
# // --- Force a redessiner chaque tuiles posés sur le plateau  
    def reset_images_tuiles(self):
        for x in range(len(VAR.terrain)):
            for y in range(len(VAR.terrain[x])):
                if isinstance(VAR.terrain[x][y], CT.CTuile) == True:
                    VAR.terrain[x][y].aMettreAjour = True
                    
        if self.tuileSelect != None:
            self.tuileSelect.aMettreAjour = True

# //
# // --- Affiche l'ensemble les tuiles posés sur le plateau
    def afficher(self):
        for x in range(len(VAR.terrain)):
            for y in range(len(VAR.terrain[x])):
                xP, yP = VAR.OffsetX + ((x * VAR.Zoom) * 9), (VAR.OffsetY + (y * VAR.Zoom) * 9)
                
                if FCT.SurEcran(xP, yP, VAR.v9, VAR.v9) == True:
                    if isinstance(VAR.terrain[x][y], CT.CTuile) == True:
                        # --- Pièces déjà posées
                        VAR.terrain[x][y].generer()
                        VAR.terrain[x][y].afficher()
                        VAR.tuiles.ferme_les_impasses(VAR.terrain[x][y])

# //
# // ---            
    def ferme_les_impasses(self, tu):
        x, y = tu.x, tu.y

        # --- Parcours les voisins des cotés
        for accesPiece, xDecalage, yDecalage, accesPieceACote in [(0, -1, 0, 2), (2, 1, 0, 0), (1, 0, -1, 3), (3, 0, 1, 1)]:
            blocage, mur = False, False
            
            xPieceACote, yPieceACote = x + xDecalage, y + yDecalage         # --- Coordonnées de la piece voisine
            acces = tu.acces[accesPiece]        # --- Il y a t-il un acces sur ce coté ?

            if acces == True:
                if isinstance(VAR.terrain[xPieceACote][yPieceACote], CT.CTuile) == True:              # --- Teste si il y a une zone voisine
                    accesVoisine = VAR.terrain[xPieceACote][yPieceACote].acces[accesPieceACote]
                    
                    if acces != accesVoisine: blocage, mur = True, True        # --- Pas de passage partagé
                else:
                    
                    if acces == True: blocage = True        # --- Pas de passage partagé

                if blocage == True:
                    hImg, vImg, d = ("GB", "GA") , "EA", 0
                    if tu.piece == True: hImg, vImg, d = ("FB", "FA") , "EB", 1

                    xP, yP, codeImg = 0, 0, ""
                    if accesPiece == VAR.GAUCHE: xP, yP, codeImg =  (0+d) * VAR.Zoom, VAR.v4, hImg[0]
                    if accesPiece == VAR.HAUT: xP, yP, codeImg =  VAR.v4, (0+d) * VAR.Zoom, vImg
                    if accesPiece == VAR.DROITE: xP, yP, codeImg =  (8-d) * VAR.Zoom, VAR.v4, hImg[0]
                    if accesPiece == VAR.BAS: xP, yP, codeImg =  VAR.v4, (8-d) * VAR.Zoom, vImg

                    if mur == True: codeImg = "7F"

                    tmp = FCT.image(codeImg)
                    VAR.fenetre.blit(tmp, (VAR.OffsetX + (x * VAR.v9) + xP, VAR.OffsetY + (y * VAR.v9) + yP, VAR.Zoom, VAR.Zoom))

                    # --- Ajoute le bout de porte qui manque
                    if (accesPiece == VAR.GAUCHE or accesPiece == VAR.DROITE) and mur == False: 
                        tmp = FCT.image(hImg[1])
                        VAR.fenetre.blit(tmp, (VAR.OffsetX + (x * VAR.v9) + xP, VAR.OffsetY + (y * VAR.v9) + yP - VAR.Zoom, VAR.Zoom, VAR.Zoom))

# //
# // ---
    def placer_piece_centrale(self):
        VAR.posPieceCentrale = int(VAR.PlateauX/2), int(VAR.PlateauY/2)
        piece_centrale = CT.CTuile( [True, True, True, True], True, True, False)
        
        self.placer(VAR.posPieceCentrale[0], VAR.posPieceCentrale[1], piece_centrale, None, True)

# //
# // --- tu : tuiles a poser
# // --- to : tuile d'origine    
    def placer(self, x, y, tu, to, premiere = False):
        if premiere == False and self.verification_placement(tu, x, y, to) == False: return False

        tu.x, tu.y = x, y
        tu.depart = premiere
        VAR.terrain[x][y] = tu
        
        if tu.teleport == True:
            VAR.liste_teleports.append((x, y))

        if premiere == False:
            VAR.joueur_en_cours.deplacer(x, y)
        self.tuileSelect = None

# //
# // --- Teste que la tuile est orienté pour créer une liason avec la tuile d'origine
    def verification_placement(self, tu, xPieceAPoser, yPieceAPoser, to):
        xD, yD = xPieceAPoser - to.x, yPieceAPoser - to.y
            
        if (xD, yD) == (1,0) and to.acces[VAR.DROITE] == tu.acces[VAR.GAUCHE]: return True
        if (xD, yD) == (0,1) and to.acces[VAR.BAS] == tu.acces[VAR.HAUT]: return True
        if (xD, yD) == (0,-1) and to.acces[VAR.HAUT] == tu.acces[VAR.BAS]: return True
        if (xD, yD) == (-1,0) and to.acces[VAR.GAUCHE] == tu.acces[VAR.DROITE]: return True

        return False
   