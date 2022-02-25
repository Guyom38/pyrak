import pygame
from pygame.locals import *
import random

from tuile import *
import fonctions as FCT

class CTuiles():
    def __init__(self, moteur):
        self.moteur = moteur

        self.pioche = []
        
        self.charger()
        self.piocher()

# //
# // ---   
    def charger(self):
        for i in range(12):  self.pioche.append( CTuile(self.moteur, [True, True, False, False], False, True, False))
        for i in range(14):  self.pioche.append( CTuile(self.moteur, [True, True, False, False], False, False, False))
        for i in range(13): self.pioche.append( CTuile(self.moteur, [True, False, True, False], True, False, False))
        for i in range(13): self.pioche.append( CTuile(self.moteur, [True, True, False, False], True, False, False))
        for i in range(14): self.pioche.append( CTuile(self.moteur, [True, True, True, True], True, False, False))
        for i in range(5):  self.pioche.append( CTuile(self.moteur, [True, True, True, False], False, False, False))
        for i in range(13): self.pioche.append( CTuile(self.moteur, [True, True, True, False], True, False, False))
        for i in range(7):  self.pioche.append( CTuile(self.moteur, [True, True, True, True], False, False, False))
        for i in range(4):  self.pioche.append( CTuile(self.moteur, [True, False, True, False], False, False, True))
        for i in range(4):  self.pioche.append( CTuile(self.moteur, [True, False, True, False], False, False, False))

        random.shuffle(self.pioche)

# //
# // ---   
    def piocher(self):
        if len(self.pioche) > 0:
            self.tuileSelect = self.pioche[0]
            self.pioche.remove(self.pioche[0])

# //
# // --- Force a redessiner chaque tuiles posés sur le plateau  
    def reset_images_tuiles(self):
        for x in range(len(VAR.terrain)):
            for y in range(len(VAR.terrain[x])):
                if isinstance(VAR.terrain[x][y], CTuile) == True:
                    VAR.terrain[x][y].aMettreAjour = True
                    
        self.tuileSelect.aMettreAjour = True

# //
# // --- Affiche l'ensemble les tuiles posés sur le plateau
    def afficher(self):
        for x in range(len(VAR.terrain)):
            for y in range(len(VAR.terrain[x])):
                xP, yP = VAR.OffsetX + ((x * VAR.Zoom) * 9), (VAR.OffsetY + (y * VAR.Zoom) * 9)
                if FCT.SurEcran(xP, yP, VAR.v9, VAR.v9) == True:
                
                    if isinstance(VAR.terrain[x][y], CTuile) == True:
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
                if isinstance(VAR.terrain[xPieceACote][yPieceACote], CTuile) == True:              # --- Teste si il y a une zone voisine
                    accesVoisine = VAR.terrain[xPieceACote][yPieceACote].acces[accesPieceACote]
                    
                    if acces != accesVoisine: blocage, mur = True, True        # --- Pas de passage partagé
                else:
                    
                    if acces == True: blocage = True        # --- Pas de passage partagé

                if blocage == True:
                    hImg, vImg, d = ("GB", "GA") , "EA", 0
                    if tu.piece == True: hImg, vImg, d = ("FB", "FA") , "EB", 1

                    xP, yP, codeImg = 0, 0, ""
                    if accesPiece == 0: xP, yP, codeImg =  (0+d) * VAR.Zoom, 4 * VAR.Zoom, hImg[0]
                    if accesPiece == 1: xP, yP, codeImg =  4 * VAR.Zoom, (0+d) * VAR.Zoom, vImg
                    if accesPiece == 2: xP, yP, codeImg =  (8-d) * VAR.Zoom, 4 * VAR.Zoom, hImg[0]
                    if accesPiece == 3: xP, yP, codeImg =  4 * VAR.Zoom, (8-d) * VAR.Zoom, vImg

                    if mur == True: codeImg = "7F"

                    tmp = FCT.image(codeImg)
                    VAR.fenetre.blit(tmp, (VAR.OffsetX + (x * VAR.v9) + xP, VAR.OffsetY + (y * VAR.v9) + yP, VAR.Zoom, VAR.Zoom))

                    # --- Ajoute le bout de porte qui manque
                    if (accesPiece == 0 or accesPiece == 2) and mur == False: 
                        tmp = FCT.image(hImg[1])
                        VAR.fenetre.blit(tmp, (VAR.OffsetX + (x * VAR.v9) + xP, VAR.OffsetY + (y * VAR.v9) + yP - VAR.Zoom, VAR.Zoom, VAR.Zoom))

# //
# // ---
    def placer_piece_centrale(self):
        VAR.posPieceCentrale = 2, 3 #int(self.MAX_LARGEUR/2), int(self.MAX_HAUTEUR/2)
        self.placer(VAR.posPieceCentrale[0], VAR.posPieceCentrale[1], CTuile(self.moteur, [True, True, True, True], True, True, False), None, True)

# //
# // --- tu : tuiles a poser
# // --- to : tuile d'origine    
    def placer(self, x, y, tu, to, premiere = False):
        if premiere == False and self.verification_placement(tu, x, y, to) == False: return False
        
        tu.x, tu.y = x, y
        VAR.terrain[x][y] = tu
    
        if premiere == False:
            VAR.joueur_en_cours.deplacer(x, y)
        VAR.tuiles.piocher()

# //
# // --- Teste que la tuile est orienté pour créer une liason avec la tuile d'origine
    def verification_placement(self, tu, xPieceAPoser, yPieceAPoser, to):
        xD, yD = xPieceAPoser - to.x, yPieceAPoser - to.y
            
        if (xD, yD) == (1,0) and to.acces[2] == tu.acces[0]: return True
        if (xD, yD) == (0,1) and to.acces[3] == tu.acces[1]: return True
        if (xD, yD) == (0,-1) and to.acces[1] == tu.acces[3]: return True
        if (xD, yD) == (-1,0) and to.acces[0] == tu.acces[2]: return True

        return False
   