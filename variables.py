from enum import Enum

GAUCHE = 0
HAUT = 1
DROITE = 2
BAS = 3

COFFRE = "Coffre"

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
    
class ENUM_Piece(Enum):
    RIEN_FAIRE = -2
    OBJET_A_RECUPERER = -1
    COMBATTRE = 0
    TIRAGE_AU_SORT = 1
    
    
# ---------------------------------------------------------------------------------------    
phase_du_jeu = ENUM_Phase.DEPLACEMENT
phase_du_jeu_suivant = ENUM_Phase.DEPLACEMENT

animations = {}

EcranX = 1280
EcranY = 800

PlateauX, PlateauY = 20, 20

Zoom = 16
v2 = (2 * Zoom)
v3 = (3 * Zoom)
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
heros = None
combat = None
objets = None
jetons = None
phase = None
ressources = None
camera = None
notifications = None
recompense = None

interfaces = None
objets_interface = None

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
liste_teleports = []

fonts = {}

posPieceCentrale = (0,0)

IMG = {}
SONS = {}
MUSICS = {}




img0 = None
img1 = None
img2 = None
des = None

TRANSPARENCE = 16777215

# Notifications
notif_largeur, notif_hauteur = 350, 30
notif_duree = 10000

souris = 0
mouseG, mouseM, mouseD = 0, 0, 0
mX, mY = 0, 0

pos_minimum_dragon = 20