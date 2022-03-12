import json
import variables as VAR
from variables import *

from Classes.tuile import *
from Classes.jeton import *


class CPartie():
    def __init__(self):
        print("    + Initialisation module << Partie >>")


    def enregistrer(self):
        sauvegarde = {}
        
        # --- Preparation a la serialisation
        data_tuiles = []
        for tuile in VAR.tuiles.pioche:
            data_tuiles.append( (tuile.acces, tuile.piece, tuile.fontaine, tuile.teleport) )
        sauvegarde["tuiles"] = (VAR.tuiles.piochePosition,data_tuiles)
        
        # --- Preparation des jetons
        data_jetons = []
        for mechant in VAR.jetons.pioche:
            data_jetons.append( (mechant.id, mechant.force, mechant.nom, mechant.recompense) )
        sauvegarde["jetons"] = (VAR.jetons.piochePosition, data_jetons)
        
        data_terrain = []
        for y in range(0, VAR.PlateauY):
            for x in range(0, VAR.PlateauX):
                if VAR.terrain[x][y] == 0:
                    cellule = 0
                else:
                    acces = VAR.terrain[x][y].acces
                    piece = VAR.terrain[x][y].piece
                    fontaine = VAR.terrain[x][y].fontaine
                    teleport = VAR.terrain[x][y].teleport
                    if VAR.terrain[x][y].jeton != None:
                        jeton = (VAR.terrain[x][y].jeton.id, VAR.terrain[x][y].jeton.nom, VAR.terrain[x][y].jeton.force, VAR.terrain[x][y].jeton.recompense)
                    else:
                        jeton = None
                        
                    recompense = VAR.terrain[x][y].recompense
                    cellule = (acces, piece, fontaine, teleport, jeton, recompense)
                data_terrain.append( cellule )
        sauvegarde["terrain"] = (VAR.PlateauX, VAR.PlateauY, data_terrain)
        
        
        
        # --- Enregistrement des données
        with open("data_file.json", "w") as write_file:
            json.dump(sauvegarde, write_file)











    def charger(self):
        with open("data_file.json", "r") as read_file:
            sauvegarde = json.load(read_file)
            
            self.reinitialisation_tuiles(sauvegarde['tuiles'])
            self.reinitialisation_jetons(sauvegarde['jetons'])
            self.reinitialisation_terrain(sauvegarde['terrain'])
            
            VAR.joueur_en_cours = VAR.heros.liste[0]
            VAR.joueur_en_cours.recentrer_camera()
            VAR.camera.centrer_sur_joueur()
            
    def reinitialisation_tuiles(self, donnees):
        pos_tuiles, data_tuiles = donnees
        
        VAR.tuiles.pioche = []
        VAR.tuiles.piochePosition = pos_tuiles
        
        for acces, piece, fontaine, teleport in data_tuiles:
            VAR.tuiles.pioche.append( CTuile( acces, piece, fontaine, teleport))
        
    
    def reinitialisation_jetons(self, donnees):
        pos_jetons, data_jetons = donnees
    
        VAR.jetons.pioche = []
        VAR.jetons.piochePosition = pos_jetons
        
        for id, force, nom, recompense in data_jetons:
            VAR.jetons.pioche.append( CJeton( id, VAR.mechants.liste[id]) )    
            
    def reinitialisation_terrain(self, donnees):
        VAR.PlateauX, VAR.PlateauY, data_terrain = donnees
        VAR.terrain = FCT.GenereMat2D(VAR.PlateauX, VAR.PlateauY, 0)  
        
        x = 0
        y = 0
        for cellule in data_terrain:
            if cellule != 0:
               acces, piece, fontaine, teleport, jeton, recompense = cellule
               VAR.terrain[x][y] = CTuile(acces, piece, fontaine, teleport, x, y)
               VAR.terrain[x][y].jeton = jeton
               VAR.terrain[x][y].recompense = recompense
               VAR.terrain[x][y].generer()
               
            x += 1
            if x > VAR.PlateauX -1:
                y +=1
                x = 0
        