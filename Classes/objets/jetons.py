import random
 
import classes.objets.jeton as CJ

import classes.persos.mechants as CMS
import classes.persos.mechant as CM
import variables as VAR

class CJetons():
    def __init__(self):
        print("    + Initialisation module << Jetons >>")
         
    def charger(self):
        self.pioche = [] 
        self.piochePosition = 0
        self.jetonSelect = None
        
        for i, monstre in VAR.mechants.liste.items():
            for j in range(0, monstre.quantite):
                self.pioche.append( CJ.CJeton( i, monstre) )

        self.melanger()
        
        
    def melanger(self):
        random.shuffle(self.pioche)

# //
# // ---   
    def piocher(self):
        if len(self.pioche)-1 > self.piochePosition:
            self.jetonSelect = self.pioche[self.piochePosition]
            self.piochePosition += 1
            return self.jetonSelect 
        return None
