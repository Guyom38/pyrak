from enum import Enum

GAUCHE = 0
HAUT = 1
DROITE = 2
BAS = 3

class ENUM_Clic(Enum):
    Rien = -1
    Survol = 0
    Clic = 1

   
class ENUM_Pouvoirs(Enum):
    affinitite_magique = 0
    marche_astrale = 1
    
    double_attaque = 2
    reincarnation = 3
    
    sacrifice = 4
    substitution = 5
    
    attaque_par_derriere = 6
    marche_rampante = 7
    
    entrainement_au_combat = 8
    inarretable = 9
    
    premonition = 10
    risseuse_de_destin = 11


class ENUM_Actions(Enum):
    DECOUVRIR = 0
    ACCESSIBLE = 1
    PAUSE = 2
    HACHE = 3
    PRENDRE = 4
    MAGIE = 5
    COMBATTRE = 6
    OUVRIR = 7
    DEVERROUILLER = 8
    PIOCHER = 9
    SE_BAIGNER = 5
    
    
class ENUM_Phase(Enum):
    DEPLACEMENT = 0
    COMBAT = 1
    TRANSITION = 2
    TIRAGE = 3
    INVENTAIRE = 4
    BANDEAU = 5
    AU_SUIVANT = 6
    RECOMPENSE = 7
    TELEPORTER = 8
    MENU = 9
    
class ENUM_Piece(Enum):
    RIEN_FAIRE = -2
    OBJET_A_RECUPERER = -1
    COMBATTRE = 0
    TIRAGE_AU_SORT = 1