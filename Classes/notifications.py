import pygame
from pygame.locals import *

from Classes.notification import *

from variables import ENUM_Phase

class CNotifications():

    # --- Bandeau : Etape de l'animation
    NON_INITIALISE = 0
    INITIALISE = 1
    APPARITION = 2
    PAUSE = 3
    DISPARITION = 4
    TERMINE = 5

    def __init__(self):
        print("    + Initialisation module << Notifications >>")
        self.liste = []
     
        self.phases_de_jeu_apres = None
        self.bandeau_titre = ""

        self.animation_bandeau_cycle = 0
        self.animation_bandeau_y = VAR.EcranY - 100
        self.animation_bandeau_x = 0
        self.animation_etape = CNotifications.NON_INITIALISE
        self.animation_delais_pause = 1500

        self.couleur1 = pygame.Color(33,105,33,255)
        self.couleur2 = pygame.Color(105,74,64,255)
        self.couleur3 = pygame.Color(76,54,44,255)
        self.couleur4 = pygame.Color(64,64,64,32)
        self.couleur5 = pygame.Color(117,94,74,255)


    def ajouter(self, joueur, icone, texte):
        self.liste.append ( CNotification(joueur, icone, texte) )


    def nb_notifications(self):
        return len(self.liste)


    def afficher(self):
        x = VAR.EcranX - VAR.notif_largeur
        y = VAR.EcranY - ((VAR.notif_hauteur + 4) * 6) - 50

        for notification in self.liste:
            VAR.fenetre.blit(notification.image, (x, y))
            y+= (VAR.notif_hauteur + 4)

            if pygame.time.get_ticks() - notification.cycle > VAR.notif_duree:
                self.liste.remove(notification)


    def afficher_bandeau(self, txt=""):

        # --- Initialise le bandeau de titre
        if self.animation_etape == CNotifications.NON_INITIALISE or self.animation_etape == CNotifications.TERMINE:
            self.phases_de_jeu_apres = (VAR.phase_du_jeu, VAR.phase_du_jeu_suivant)
            VAR.phase_du_jeu = ENUM_Phase.BANDEAU
            self.bandeau_titre = txt

            self.animation_bandeau_cycle = pygame.time.get_ticks()
            self.animation_bandeau_x = VAR.EcranX
            self.animation_etape = CNotifications.APPARITION

        # --- Anime le bandeau de titre
        if self.animation_etape == CNotifications.APPARITION:
            if pygame.time.get_ticks() - self.animation_bandeau_cycle > 1:
                self.animation_bandeau_cycle = pygame.time.get_ticks()
                
                if self.animation_bandeau_x > 300:
                    self.animation_bandeau_x -= 64
                else:
                    self.animation_etape = CNotifications.PAUSE

        elif self.animation_etape == CNotifications.PAUSE:
            if pygame.time.get_ticks() - self.animation_bandeau_cycle > self.animation_delais_pause:
                self.animation_bandeau_cycle = pygame.time.get_ticks()
                self.animation_etape = CNotifications.DISPARITION
                    
        elif self.animation_etape == CNotifications.DISPARITION:
            if pygame.time.get_ticks() - self.animation_bandeau_cycle > 1:
                self.animation_bandeau_cycle = pygame.time.get_ticks()
                
                if self.animation_bandeau_x < VAR.EcranX:
                    self.animation_bandeau_x += 64
                else:
                   VAR.phase_du_jeu, VAR.phase_du_jeu_suivant = self.phases_de_jeu_apres
                   self.animation_etape = CNotifications.TERMINE

        if self.animation_etape != CNotifications.TERMINE:
            # --- Affiche le bandeau de titre
            pygame.draw.rect(VAR.fenetre, self.couleur2, (self.animation_bandeau_x, self.animation_bandeau_y -100, VAR.EcranX, 50), 0)
            pygame.draw.rect(VAR.fenetre, self.couleur2, (self.animation_bandeau_x, self.animation_bandeau_y -110, VAR.EcranX, 5), 0)
            pygame.draw.rect(VAR.fenetre, self.couleur3, (self.animation_bandeau_x, self.animation_bandeau_y -100, VAR.EcranX, 50), 2)
            pygame.draw.rect(VAR.fenetre, self.couleur3, (self.animation_bandeau_x, self.animation_bandeau_y -110, VAR.EcranX, 5), 2)
            FCT.texte(VAR.fenetre, self.bandeau_titre, self.animation_bandeau_x+30, self.animation_bandeau_y -150, 60 )



        
