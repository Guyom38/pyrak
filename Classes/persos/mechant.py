import classes.commun.fonctions as FCT
class CMechant():
    def __init__(self, nom, force, tirage, image, icone, recompense, specialite, quantite):
        
        self.nom = nom
        self.force = int(force)
        
        self.image = image
        self.masque = FCT.Generer_Mask_Image(image)
        
        self.icone = icone
        
        self.recompense = recompense.strip()    
        self.specialite = specialite
        
        self.tirage = tirage
        self.quantite : int = int(quantite)
        
        
        