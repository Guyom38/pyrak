import Classes.ui_transitions as TRANSITION
import variables as VAR
from variables import *


class CPhase:
    def __init__(self, moteur):
        self.moteur = moteur
    
    def gestion_des_phases_de_jeu(self):
        if VAR.phase_du_jeu == ENUM_Phase.TRANSITION: 
            TRANSITION.transition_glisser(False)
                
            if VAR.phase_du_jeu_suivant == ENUM_Phase.TIRAGE:
                x, y = VAR.joueur_en_cours.x, VAR.joueur_en_cours.y
                
                if VAR.terrain[x][y].jeton == None:                         # --- Si aucun jeton, piece decouverte, alors tirage
                    print("kkkk")
                    jeton_mechant = VAR.jetons.piocher()
                    VAR.terrain[x][y].jeton = jeton_mechant
                    VAR.mechants.afficher_tirage_monstre(jeton_mechant.id)
                    VAR.combat.jeton = jeton_mechant
                                    
                if VAR.terrain[x][y].jeton.id != ENUM_Jeton.COFFRE:               # --- Lance le combat
                    VAR.combat.preparer_combat()
                    VAR.phase_du_jeu_suivant = ENUM_Phase.COMBAT
                
                else:                                                   # --- Coffre donc on repart sur le plateau
                    VAR.phase_du_jeu = ENUM_Phase.DEPLACEMENT
                
            elif VAR.phase_du_jeu_suivant == ENUM_Phase.COMBAT:
                VAR.phase_du_jeu = ENUM_Phase.COMBAT

            elif VAR.phase_du_jeu_suivant == ENUM_Phase.DEPLACEMENT:
                VAR.phase_du_jeu = ENUM_Phase.DEPLACEMENT
                    
        elif VAR.phase_du_jeu == ENUM_Phase.COMBAT:
            self.moteur.charger_musique("COMBAT")

            VAR.combat.gestion_combat()
            VAR.combat.afficher()