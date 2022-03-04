import pygame
from pygame.locals import *

from Classes.notification import *

class CNotifications():
   
    def __init__(self):
        print("    + Initialisation module << Notifications >>")
        self.liste = []
     

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


        