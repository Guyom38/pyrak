import random
from variables import ENUM_Jeton, ENUM_Objets
from Classes.jeton import *

class CJetons():
    def __init__(self, moteur):
        print("    + Initialisation module << Jetons >>")
        
        self.moteur = moteur
        self.pioche = [] 
        self.jetonSelect = None
         
    def charger(self):
        for i in range(12): self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_RAT) )
        for i in range(5):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SQUELETTE) )
        for i in range(8):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SQUELETTE_CLE) )
        for i in range(3):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SQUELETTE_ROI) )
        for i in range(2):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_SPECTRE) )
        for i in range(4):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_ARAIGNE) )
        for i in range(1):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_DRAGON) )
        for i in range(8):  self.pioche.append( CJeton(self.moteur, ENUM_Jeton.MONSTRE_MOMMIE) )
        for i in range(12): self.pioche.append( CJeton(self.moteur, ENUM_Jeton.COFFRE) )
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
            return (3, 9,  "Squelette - spadassin", ENUM_Objets.EPEE)
        elif id == ENUM_Jeton.MONSTRE_SQUELETTE_ROI: 
            return (4, 10, "Roi des squelette", ENUM_Objets.HACHE)
        elif id == ENUM_Jeton.MONSTRE_SQUELETTE_CLE: 
            return (2, 8,  "Squelette - gardien des clés", ENUM_Objets.CLE)
        elif id == ENUM_Jeton.MONSTRE_MOMMIE: 
            return (1, 7,  "Momie", ENUM_Objets.MAGIE_EPEE)
        elif id == ENUM_Jeton.MONSTRE_ARAIGNE: 
            return (6, 8,  "Araignée géante", ENUM_Objets.MAGIE_VIE)
        elif id == ENUM_Jeton.MONSTRE_SPECTRE: 
            return (5, 12, "Mort", ENUM_Objets.COFFRE)
        elif id == ENUM_Jeton.MONSTRE_RAT: 
            return (0, 5,  "Rat", ENUM_Objets.COUTEAUX)
        elif id == ENUM_Jeton.MONSTRE_DRAGON: 
            return (7, 15, "Dragon", ENUM_Objets.SUPER_COFFRE)
        elif id == ENUM_Jeton.COFFRE: 
            return (-1, 0,  "Coffre", ENUM_Objets.COFFRE)