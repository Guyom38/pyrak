import pygame
from pygame.locals import *

from Classes.notification import *
from variables import ENUM_Phase

class CNotifications():

    def __init__(self):
        print("    + Initialisation module << Notifications >>")
        self.liste = []
        self.bandeau = None
         
    def afficher(self):
        self.afficher_liste_notifications()
        
        if VAR.phase_du_jeu == ENUM_Phase.BANDEAU:  
            if self.bandeau == None: 
                self.initialiser_bandeau("")
            if self.bandeau.animation_etape != CNotification.TERMINE:
                self.bandeau.afficher()

    def ajouter(self, joueur, icone, texte):
        self.liste.append ( CNotification(joueur, icone, texte, False) )
    
    def initialiser_bandeau(self, txt):
        self.bandeau = CNotification("", "", txt, True)

        
    def nb_notifications(self):
        return len(self.liste)
       
    def afficher_liste_notifications(self):
        y = VAR.EcranY - ((VAR.notif_hauteur + 4) * 6) - 50

        for notification in self.liste:
            notification.afficher(y)
            y+= (VAR.notif_hauteur + 4)

            if notification.animation_etape == CNotification.TERMINE:
                self.liste.remove(notification)

    



        
