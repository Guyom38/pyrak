import fonctions as FCT
class CMechant():
    def __init__(self, moteur, nom, force, tirage, image, icone, recompense, specialite):
        self.moteur = moteur
        
        self.nom = nom
        self.force = force
        
        self.image = image
        self.masque = FCT.Generer_Mask_Image(image)
        
        self.icone = icone
        
        self.recompense = recompense
        self.specialite = specialite
        
        self.tirage = tirage
        
        
        