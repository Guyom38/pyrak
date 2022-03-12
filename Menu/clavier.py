import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT
from Classes.ui_objets_interface import *

class CClavier():
    def __init__(self):
        self.clavier = []
        self.clavier.append( [(49, ("1","&"), (1,1)), (50, ("2","?"), (1,1)),  (51, ("3","#"), (1,1)), (52, ("4","@"), (1,1)), (53, ("5","?"), (1,1)), (54, ("6","-"),  (1,1)), (55, ("7","_"), (1,1)), (56, ("8","!"), (1,1)), (57, ("9","*"), (1,1)), (48, ("0",":"), (1,1)),  (8, ("RETOUR","RETOUR"), (2,1))] )
        self.clavier.append( [(113, ("a","A"), (1,1)), (119, ("z","Z"), (1,1)),  (101, ("e","E"), (1,1)), (114, ("r","R"), (1,1)), (116, ("t","T"), (1,1)), (121, ("y","Y"),  (1,1)), (117, ("u","U"), (1,1)), (105, ("i","I"), (1,1)), (111, ("o","O"), (1,1)), (112, ("p","P"), (1,1)), (200, ("ENTRER","ENTRER"), (2,2))] )
        self.clavier.append( [(97, ("q","Q"),  (1,1)), (115, ("s","S"), (1,1)),  (100, ("d","D"), (1,1)), (102, ("f","F"), (1,1)), (103, ("g","G"), (1,1)), (104, ("h","H"),  (1,1)), (106, ("j","J"), (1,1)), (107, ("k","K"),  (1,1)), (108, ("l","L"), (1,1)),  (59, ("m","M"), (1,1))]  )
        self.clavier.append( [(304, ("MAJ","MAJ"), (2,1)), (122, ("w","W"), (1,1)), (120, ("x","X"), (1,1)), (99, ("c","C"), (1,1)),  (118, ("v","V"),  (1,1)), (98, ("b","B"), (1,1)),  (110, ("n","N"), (1,1)), (266, (".",","), (1,1)) , (32, ("ESPACE","ESPACE"), (3,1))                    ] )

        self.largeur = self.calcul_largeur_clavier()
        
        self.mot = ""
        self.bloc_majuscule = ""
        self.dX, self.dY, self.esp = 70, 40, 4   

        self.yRef = VAR.EcranY - (self.dY * len(self.clavier)) - (self.esp * (len(self.clavier)+1)) 
        self.y = VAR.EcranY
        
        self.visible = False
        self.apparait = False
        self.offX, self.offY = int( (VAR.EcranX - (self.dX*(self.largeur+1)) + (self.esp * (self.largeur+3)))/2 ), VAR.EcranY
        self.cycle = 0
        
    def calcul_largeur_clavier(self):
        largeur = 0
        for tmp, tmp, ij in self.clavier[0]:
            largeur += ij[0]
        return largeur
    
    def montrer(self):
        self.visible = True
        self.apparait = True
        self.offY = VAR.EcranY
        
    def cacher(self):
        self.apparait = False
        self.offY = self.yRef
    
    def gestion_apparition(self):
        if pygame.time.get_ticks() - self.cycle > 10: 
            if self.apparait == True:
                if self.offY > self.yRef:
                    self.offY -= 16
            else:
                if self.offY < VAR.EcranY:
                    self.offY += 16 
                else:
                    self.visible = False
            self.cycle = pygame.time.get_ticks()
                    
    def afficher(self):
        if self.visible == True:
            self.gestion_apparition()
                
            x, y, touche_pressee = 0, 0, 0   
            fond = FCT.image_vide(VAR.EcranX, (self.dY*4) + (self.esp * 7)+1)
            fond.fill((16,16,16,220))
            VAR.fenetre.blit(fond, (0, self.offY - (self.esp*2)))
            
            pygame.draw.rect(VAR.fenetre, (32,32,32,255), (self.offX - (self.esp*2), self.offY - (self.esp*2), (self.dX*self.largeur) + (self.esp * (self.largeur+3)), (self.dY*4) + (self.esp * 7)), 0 )
            pygame.draw.rect(VAR.fenetre, (8,8,8,255), (self.offX - (self.esp*2), self.offY - (self.esp*2), (self.dX*self.largeur) + (self.esp * (self.largeur+3)), (self.dY*4) + (self.esp * 7)), 2 )    
                
            for event in VAR.evenements: #pygame.event.get():        
                if event.type == KEYDOWN: 
                    touche_pressee = event.key
                    
            # --- Detection de la touche MAJUSCULE
            touche_majuscule = (pygame.key.get_pressed()[304] == 1 or pygame.key.get_pressed()[303] == 1)
            if touche_majuscule == True: self.bloc_majuscule = False
            
            # --- Dessine le clavier
            for ligne_touches in self.clavier:      
                for touche in ligne_touches:          
                    codeTouche, lettre, taille = touche
                    tx, ty = taille
                    toucheDimX, toucheDimY = (self.dX * tx) + (self.esp * (tx-1)), (self.dY * ty)+ (self.esp * (ty-1))
                    lettre = FCT.iif(touche_majuscule == True or self.bloc_majuscule == True, lettre[1], lettre[0])
                    
                    # --- Gestion du clic souris sur la touche
                    xT, yT = self.offX + x, self.offY + y    
                    if VAR.objets_interface.zone_clickable(xT-2, yT-2, toucheDimX+3, toucheDimY+3, 0) == ENUM_Clic.Clic:
                        touche_pressee = codeTouche
                        if touche_pressee == 304:
                            self.bloc_majuscule = not self.bloc_majuscule
                    
                    # --- Gestion de l'action a entreprendre
                    if touche_pressee == codeTouche:               
                        if touche_pressee == 8:         # DEL
                            self.mot = self.mot[:(len(self.mot)-1)]
                        elif touche_pressee == 200 :    # ENTRER
                            self.cacher()
                        elif touche_pressee == 32 :      # ESPACE
                            self.mot += " "
                        elif touche_pressee != 304:
                            self.mot += lettre
                
                    # --- dessine touche
                    if (codeTouche == 304 and (touche_majuscule == True or self.bloc_majuscule == True)) or touche_pressee == codeTouche:
                        pygame.draw.rect(VAR.fenetre, (128,128,128,255), (xT, yT, toucheDimX, toucheDimY), 0 )
                    else:
                        pygame.draw.rect(VAR.fenetre, (64,64,64,255), (xT, yT, toucheDimX, toucheDimY), 0 )
                        
                    pygame.draw.rect(VAR.fenetre, (32,32,32,255), (xT+1, yT+1, toucheDimX-2, toucheDimY-2), 1 )
                    image_text =  VAR.fonts[20].render(lettre, True, (255,255,255,255)) 
                    VAR.fenetre.blit(image_text,  (xT + int((toucheDimX - image_text.get_width()) /2), yT  + int((toucheDimY - image_text.get_height()) /2)) )
                    
                    # --- Colorie la selection
                    x += ((self.dX + self.esp) * tx) 
                y += self.dY + self.esp
                x= 0
