import random
from variables import ENUM_Jeton
from Classes.jeton import *

from Classes.mechants import *
from Classes.mechant import *

class CJetons():
    def __init__(self, moteur):
        print("    + Initialisation module << Jetons >>")
        
        self.moteur = moteur
        self.pioche = [] 
        self.jetonSelect = None
         
    def charger(self):
        for i, monstre in VAR.mechants.liste.items():
            for j in range(0, monstre.quantite):
                self.pioche.append( CJeton(self.moteur, i, monstre) )
        #for i in range(12): self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_RAT) )
        #for i in range(5):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SQUELETTE) )
        #for i in range(8):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SQUELETTE_CLE) )
        #for i in range(3):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SQUELETTE_ROI) )
        #for i in range(2):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SPECTRE) )
        #for i in range(4):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_ARAIGNE) )
        #for i in range(1):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_DRAGON) )
        #for i in range(8):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_MOMMIE) )
        #for i in range(12): self.pioche.append( CJeton(self.moteur, ENUM_Jeton.COFFRE) )
        random.shuffle(self.pioche)

# //
# // ---   
    def piocher(self):
        if len(self.pioche) > 0:
            self.jetonSelect = self.pioche[0]
            self.pioche.remove(self.pioche[0])   
            return self.jetonSelect 
        return None
       
    def afficher(self):
        pass
    
    def charger_proprietes(self, id):
        if id == ENUM_Jeton.MONSTRE_SQUELETTE: 
            return (3, 9,  "Squelette - spadassin", "ARME+2")
        elif id == ENUM_Jeton.MONSTRE_SQUELETTE_ROI: 
            return (4, 10, "Roi des squelette", "ARME+3")
        elif id == ENUM_Jeton.MONSTRE_SQUELETTE_CLE: 
            return (2, 8,  "Squelette - gardien des clés", "CLE")
        elif id == ENUM_Jeton.MONSTRE_MOMMIE: 
            return (1, 7,  "Momie", "MAGIE_FORCE")
        elif id == ENUM_Jeton.MONSTRE_ARAIGNE: 
            return (6, 8,  "Araignée géante", "MAGIE_VIE")
        elif id == ENUM_Jeton.MONSTRE_SPECTRE: 
            return (5, 12, "Mort", "COFFRE_OUVERT")
        elif id == ENUM_Jeton.MONSTRE_RAT: 
            return (0, 5,  "Rat", "ARME+1")
        elif id == ENUM_Jeton.MONSTRE_DRAGON: 
            return (7, 15, "Dragon", "SUPER_COFFRE")
        elif id == ENUM_Jeton.COFFRE: 
            return (-1, 0,  "Coffre", "COFFRE")