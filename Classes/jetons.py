import random
 
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
 
        random.shuffle(self.pioche)

# //
# // ---   
    def piocher(self):
        if len(self.pioche) > 0:
            self.jetonSelect = self.pioche[0]
            self.pioche.remove(self.pioche[0])   
            return self.jetonSelect 
        return None
