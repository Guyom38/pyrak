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



    
    
class ENUM_Jeton(Enum):
    MONSTRE_RAT = 0
    MONSTRE_MOMMIE = 1
    MONSTRE_SQUELETTE = 2
    MONSTRE_SQUELETTE_CLE = 3
    MONSTRE_SQUELETTE_ROI = 4
    MONSTRE_SPECTRE = 5
    MONSTRE_ARAIGNE = 6
    MONSTRE_DRAGON = 7
    COFFRE = 8

class ENUM_Actions(Enum):
    DECOUVRIR = 0
    ACCESSIBLE = 1
    PAUSE = 2
    HACHE = 3
    PRENDRE = 4
    BOTTE = 5
    COMBATTRE = 6
    OUVRIR = 7
    DEVERROUILLER = 8
    PIOCHER = 9
    
class ENUM_Objets(Enum):
    CLE = 0
    COFFRE = 1
    COUTEAUX = 2
    HACHE = 3
    PIEGE = 4
    MASSE = 5
    MAGIE_VIE = 6
    MAGIE_EPEE = 7
    EPEE = 8
    SUPER_COFFRE = 9

class ENUM_Phase(Enum):
    DEPLACEMENT = 0
    COMBAT = 1
    TRANSITION = 2
    TIRAGE = 3
    

# ---------------------------------------------------------------------------------------    
phase_du_jeu = ENUM_Phase.DEPLACEMENT
phase_du_jeu_suivant = ENUM_Phase.DEPLACEMENT

EcranX = 1024
EcranY = 768

PlateauX, PlateauY = 20, 20

Zoom = 16
v2 = (2 * Zoom)
v4 = (4 * Zoom)
v5 = (5 * Zoom)
v7 = (7 * Zoom)
v9 = (9 * Zoom)    


Taille = 16

OffsetX = Taille
OffsetY = Taille

nombreImageSeconde=25

bord = 50

cycle = 0

fps_cycle = 0
fps_cpt = 0
fps = 0

cpt = 0
cpt_cycle = 0
cpt_fps = 15
clock = None

joueur_en_cours = None

tuiles = None
plateau = None
interfaces = None
heros = None
combat = None
objets = None
jetons = None
phase = None
ressources = None

fenetre = None
clock = None
boucle_principale = True

texture = None
icones = None
icones2 = None
perso = None
mechants = None

icones_mechants = None

image_fond = None
image_zone = [], []
terrain = None

fonts = {}
image_interface = None

posPieceCentrale = (0,0)

IMG = {}
SONS = {}
MUSICS = {}




img0 = None
img1 = None
img2 = None
des = None

TRANSPARENCE = 16777215

