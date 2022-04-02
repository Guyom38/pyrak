import pygame
from pygame.locals import *

from Classes.tuiles import *
import variables as VAR
from variables import *
import fonctions as FCT
import outils 
from Classes.class_bresenham import *

class CPlateau():

    def __init__(self):
        print("    + Initialisation module << Plateau >>")
        
        VAR.image_fond = None
        VAR.image_zone = [], []

        self.animation_cycle = 0    
        self.animation_cpt = 0
        self.animation_delais = 30
        
        self.mX, self.mY, self.mXOld, self.mYOld = 0,0,0,0
        self.teleport_destination = (-1, -1)
        
        self.creer_terrain()
    
    def creer_terrain(self):
        VAR.terrain = FCT.GenereMat2D(VAR.PlateauX, VAR.PlateauY, 0)  #[[0 for x in range(self.MAX_LARGEUR)] for i in range(self.MAX_HAUTEUR)]
            
    def fond(self):
        if VAR.image_fond is None:
            VAR.image_fond = pygame.Surface((VAR.EcranX, VAR.EcranY),pygame.SRCALPHA,32)
            tX, tY = outils.correspondance("BN")
            for y in range(1, int(VAR.EcranY / VAR.Taille)-1):
                for x in range(1, int(VAR.EcranX / VAR.Taille)-1):
                    VAR.image_fond.blit(VAR.texture, (x * VAR.Taille, y * VAR.Taille), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
        
        VAR.fenetre.blit(VAR.image_fond, (0, 0))

    def gestion_deplacement_plateau(self):
        if pygame.mouse.get_focused() == True: 
            if VAR.phase_du_jeu == VAR.ENUM_Phase.DEPLACEMENT:

                if pygame.mouse.get_pressed()[1] == 1:
                    
                    self.mXOld = self.mX
                    self.mYOld = self.mY
                    self.mX = VAR.mX
                    self.mY = VAR.mY

                    VAR.OffsetX = VAR.OffsetX - (self.mXOld - self.mX)
                    VAR.OffsetY = VAR.OffsetY - (self.mYOld - self.mY)
                   
                else:
                    self.mXOld = VAR.mX
                    self.mYOld = VAR.mY
                    self.mX = VAR.mX
                    self.mY = VAR.mY
    
    def afficher(self):
        
        VAR.tuiles.afficher()
        self.afficher_curseur()
        self.afficher_teleporteurs()
        VAR.heros.afficher()
        
        self.animation_cpt +=1

    def on_peut_construire(self):
        return (self.nombre_de_zones_libres() > 0)
    
    def nombre_de_zones_libres(self):
        return self.liste_voisins(True)
    
    def liste_voisins(self, compter = False):
        liste_voisins = []
        x, y = VAR.joueur_en_cours.x, VAR.joueur_en_cours.y
        est_affiche0, est_affiche1, est_affiche2, est_affiche3 = False, False, False, False
        
        if x-1 >= 0: 
            if VAR.terrain[x][y].acces[VAR.GAUCHE] == True: est_affiche0, est_libre0, est_limite0 = True, (VAR.terrain[x-1][y] == 0), False
        else: est_affiche0, est_libre0, est_limite0 = True, False, True
        if est_affiche0 == True : liste_voisins.append( (-1, 0, est_libre0, est_limite0) )
        
        if y-1 >= 0:
            if VAR.terrain[x][y].acces[VAR.HAUT] == True: est_affiche1, est_libre1, est_limite1 = True, (VAR.terrain[x][y-1] == 0), False
        else: est_affiche1, est_libre1, est_limite1 = True, False, True
        if est_affiche1 == True : liste_voisins.append( (0, -1, est_libre1, est_limite1) )
        
        if x+1 <= VAR.PlateauX: 
            if VAR.terrain[x][y].acces[VAR.DROITE] == True :  est_affiche2, est_libre2, est_limite2 = True, (VAR.terrain[x+1][y] == 0), False
        else: est_affiche2, est_libre2, est_limite2 = True, False, True
        if est_affiche2 == True : liste_voisins.append( (1, 0, est_libre2, est_limite2) )
        
        if y+1 <= VAR.PlateauY: 
            if VAR.terrain[x][y].acces[VAR.BAS] == True : est_affiche3, est_libre3, est_limite3 = True, (VAR.terrain[x][y+1] == 0), False
        else: est_affiche3, est_libre3, est_limite3 = True, False, True
        if est_affiche3 == True : liste_voisins.append( (0, 1, est_libre3, est_limite3) )
        
        
        if compter == True:                     # --- Compte et retourne les zones libres autour du joueur en cours
            compteur = 0
            for tmp, tmp, zone_libre, tmp in liste_voisins:
                if zone_libre == True: compteur += 1
            return compteur
        else:                                   # --- Retourne la liste des acces en indiquant si ils sont libres, hors limites
            return liste_voisins
    
    
    def afficher_teleporteurs(self):
        # --- Fleche de teleporteur
        if VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT and VAR.joueur_en_cours.peut_bouger() and VAR.tuiles.tuileSelect == None:   
            if VAR.terrain[VAR.joueur_en_cours.x][ VAR.joueur_en_cours.y].teleport == True and len(VAR.liste_teleports)>1:
                self.Animation_Teleporteurs()
                
        if VAR.phase_du_jeu == ENUM_Phase.TELEPORTER:
            VAR.joueur_en_cours.direction = (VAR.BAS, VAR.GAUCHE, VAR.HAUT, VAR.DROITE)[VAR.cpt % 3]
            if pygame.time.get_ticks() - self.animation_cycle > 1000 :
                if self.teleport_destination != (-1, -1):
                    
                    VAR.joueur_en_cours.x, VAR.joueur_en_cours.y = self.teleport_destination 
                    self.animation_cycle = pygame.time.get_ticks()
                    self.teleport_destination = (-1,-1)
                    VAR.joueur_en_cours.recentrer_camera()    
                    VAR.joueur_en_cours.mouvement -= 1
                    
                else:
                    VAR.joueur_en_cours.direction = VAR.BAS
                    VAR.phase_du_jeu = ENUM_Phase.DEPLACEMENT
                    VAR.notifications.ajouter(VAR.joueur_en_cours, "DEPLACEMENT", VAR.joueur_en_cours.nom + " s'est téléporté")

                
    def afficher_curseur(self):
        
        # --- Fleche de deplacement
        curseur = (-1, -1)
        for xD, yD, videOccupe, enDehors in self.liste_voisins():  #[(-1,0), (1,0), (0,-1), (0,1)]:
            x, y = VAR.joueur_en_cours.x + xD, VAR.joueur_en_cours.y + yD
            xP, yP = VAR.OffsetX + ((x * VAR.Zoom) * 9), (VAR.OffsetY + (y * VAR.Zoom) * 9)
            
            if FCT.SurEcran(xP, yP, VAR.v9, VAR.v9) == True:
                if enDehors == False:
                    if isinstance(VAR.terrain[x][y], CT.CTuile) == False:
                        if VAR.tuiles.joueur_a_deja_pioche() == True:
                            if VAR.mX >= xP and VAR.mX <= xP + VAR.v9 and VAR.mY >= yP and VAR.mY <= yP + VAR.v9:
                                VAR.tuiles.tuileSelect.generer()
                                VAR.tuiles.tuileSelect.afficher(x, y)
                                
                                if VAR.Zoom > 15:   
                                    if VAR.objets_interface.zone_clickable(xP, yP, VAR.v9, VAR.v9, 0) == ENUM_Clic.Clic:
                                        VAR.tuiles.placer(x, y, VAR.tuiles.tuileSelect, VAR.terrain[x-xD][y-yD], False)
                                        VAR.SONS["poser"].play()

                                    elif VAR.objets_interface.zone_clickable(xP, yP, VAR.v9, VAR.v9, 2) == ENUM_Clic.Clic:            
                                        VAR.tuiles.tuileSelect.tourner()
                                        VAR.SONS["rotation"].play()
                                        
                                curseur = (xP, yP)
                            elif VAR.Zoom > 15:                               # --- Mettre piece
                                VAR.plateau.Animation_Zone(xP, yP, 0)
                            ###    VAR.fenetre.blit(FCT.icone(0), (xP, yP, 63, 66))
                            
                    elif VAR.phase_du_jeu == ENUM_Phase.DEPLACEMENT and VAR.joueur_en_cours.peut_bouger():                               # --- Se déplacer 
                        if VAR.tuiles.verification_placement(VAR.terrain[x][y], x, y, VAR.terrain[x-xD][y-yD]) and VAR.Zoom > 15 and VAR.tuiles.tuileSelect == None:
                            self.Animation_Fleches(xP, yP, xD, yD)
                            #VAR.plateau.Animation_Curseur((xP, yP))      
                            

                            ###ico = FCT.iif(VAR.terrain[x][y].jeton == None or VAR.terrain[x][y].piece == False, 1, 6)
                            ###VAR.fenetre.blit(FCT.icone(ico), (xP, yP, 63, 66))
                            
                            if VAR.objets_interface.zone_clickable(xP, yP, VAR.v9, VAR.v9, 0) == ENUM_Clic.Clic:
                                VAR.joueur_en_cours.deplacer(x, y)
                
                # --- Dessine la zone en dehors
                else :
                    VAR.plateau.Animation_Zone(xP, yP, 1)

  
        if curseur != (-1, -1):
            VAR.plateau.Animation_Curseur(curseur)

    def Animation_Teleporteurs(self):
        xP, yP = outils.position(VAR.joueur_en_cours.x, VAR.joueur_en_cours.y, 4, 4) 
        trajets = []
        zd2 = int(VAR.Zoom / 2)
        for x2, y2 in VAR.liste_teleports:
            xT, yT = outils.position(x2, y2, 4, 4) 
            if xP != xT or yP != yT:
                tmp_liste = bresenham([xP+zd2, yP+zd2], [xT+zd2, yT+zd2]).path
                if (tmp_liste[0] == (xT+zd2, yT+zd2)): tmp_liste.reverse()
                trajets.append(tmp_liste)  

                if VAR.objets_interface.zone_clickable(xT-VAR.v4, yT-VAR.v4, VAR.v9, VAR.v9, 0) == ENUM_Clic.Clic:  
                    VAR.joueur_en_cours.recentrer_camera()
                    self.animation_cycle = pygame.time.get_ticks()
                    self.teleport_destination = (x2, y2)
                    VAR.phase_du_jeu = ENUM_Phase.TELEPORTER

        p = 0
        for tr in trajets:
            for pts in tr:
                if p %16 == (VAR.cpt %16): pygame.draw.rect(VAR.fenetre, (255,255,0,255), (pts[0]-4, pts[1]-4, 8, 8), 0)
                p += 1

              

    def Animation_Fleches(self, xP, yP, xD, yD):
        if VAR.joueur_en_cours.seDeplace == False:
            x1, y1 = xP-VAR.v4, yP+VAR.v4
            x2, y2 = xP-(xD * VAR.v9) + VAR.v4, yP-(yD * VAR.v9) + VAR.v4
            vv = (VAR.cpt % VAR.Zoom)*9
                                
            #                 x3
            #                 █
            #   x1------------x2 █
            #   █                   █x4
            #   x7------------x6 █
            #                 █
            #                 x5
                                
            # --- Dessine les fleches de deplacement
            figure, epais = None, 8
            off = int((VAR.Zoom - 8 ) /2)
            if xD == -1:            # --- GAUCHE
                t, figure = 1, ((x2, off+y2), (x2 - vv, off+y2), (x2 - vv, off+y2 - 4), (x2 - vv - epais, off+y2+(epais/2)), (x2 - vv, off+y2 + epais + 4), (x2 - vv, off+y2 + epais), (x2, off+y2+epais))
            elif xD == 1:           # --- DROITE
                x2 += VAR.Zoom
                t, figure = 2, ((x2, off+y2), (x2 + vv, off+y2), (x2 + vv, off+y2 - 4), (x2 + vv + epais, off+y2+(epais/2)), (x2 + vv, off+y2 + epais + 4), (x2 + vv, off+y2 + epais), (x2, off+y2+epais))
            elif yD == -1:          # --- HAUT
                t, figure = 3, ((off+x2, y2), (off+x2 , y2- vv), (off+x2 -4, y2 - vv), (off+x2 +(epais/2), y2- vv - epais), (off+x2 +epais+4, y2 - vv), (off+x2 +epais, y2 - vv), (off+x2+epais, y2))
            elif yD == 1:           # --- BAS
                y2 += VAR.Zoom
                t, figure = 4, ((off+x2, y2), (off+x2 , y2+ vv), (off+x2 -4, y2 + vv), (off+x2 +(epais/2), y2+ vv + epais), (off+x2 +epais+4, y2 + vv), (off+x2 + epais, y2 + vv), (off+x2+epais, y2))
                                    
            if figure != None :
                pygame.draw.polygon(VAR.fenetre, (255,255,0,128), figure, 0)
 
                                        
    def Animation_Curseur(self, curseur):
        xP, yP = curseur
        c = pygame.Color(255,0,0,255)
        f = VAR.fenetre
        t = 1+(VAR.cpt % 10)

        pygame.draw.line(f, c, (xP, yP), (xP + VAR.v2, yP), t)
        pygame.draw.line(f, c, (xP + VAR.v7, yP), (xP + VAR.v9, yP), t)
        pygame.draw.line(f, c, (xP, yP + VAR.v9), (xP + VAR.v2, yP + VAR.v9), t)
        pygame.draw.line(f, c, (xP + VAR.v7, yP + VAR.v9), (xP + VAR.v9, yP + VAR.v9), t)

        pygame.draw.line(f, c, (xP, yP), (xP, yP + VAR.v2), t)
        pygame.draw.line(f, c, (xP, yP + VAR.v7), (xP, yP + VAR.v9), t)
        pygame.draw.line(f, c, (xP + VAR.v9, yP), (xP + VAR.v9, yP + VAR.v2), t)
        pygame.draw.line(f, c, (xP + VAR.v9, yP + VAR.v7), (xP + VAR.v9, yP + VAR.v9), t)

    def Animation_Zone(self, xP, yP, id):
        if id == 0:
            c = pygame.Color(64,64,64,255)
        else:
            c = pygame.Color(128,0,0,255)
        
        if len(VAR.image_zone[id]) == 0:
            xP, yP = 0, 0

            for t in range(VAR.v2):
                VAR.image_zone[id].append(pygame.Surface((VAR.v9, VAR.v9),pygame.SRCALPHA,32))
                            
                formes = []
                for i in (-1, 1,3,5,7,9, 11, 13, 15, 17, 19, 21):
                    formes.append( [(xP+(VAR.Zoom*i)+t, yP),(xP+(VAR.Zoom*(i+1))+t, yP),(xP, yP+(VAR.Zoom*(i+1))+t), (xP, yP+(VAR.Zoom*i)+t)] )
                                    
                for z in formes:
                    pygame.draw.polygon(VAR.image_zone[id][t], c, z, 0)
                    pygame.draw.rect(VAR.image_zone[id][t], c, (xP, yP, VAR.v9, VAR.v9), 1)
        
        t = (VAR.cpt % ((VAR.v2)))  
        VAR.fenetre.blit(VAR.image_zone[id][t], (xP, yP))

    def appliquer_filtre_retro(self):
        for y in range( 0, VAR.EcranY, 4 ):
            pygame.draw.line(VAR.fenetre, pygame.Color(0,0,0,255), (0, y), (VAR.EcranX, y), 2)
            
  