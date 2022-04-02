
from classes.commun.enumerations import *



COFFRE = "Coffre"


    
    
# ---------------------------------------------------------------------------------------    
phase_du_jeu = ENUM_Phase.MENU
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
partie = None
menu = None 
clavier = None

interfaces = None
objets_interface = None

fenetre = None
evenements = None

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