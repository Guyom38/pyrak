from operator import truediv
import pygame
from pygame.locals import *

import variables as VAR
from variables import *

import fonctions as FCT
from Classes.ui_objets_interface import *

VAR.objets_interface = CObjets_Interface()

pygame.init()
VAR.fenetre = pygame.display.set_mode((VAR.EcranX, VAR.EcranY), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("PyRAK v0.04")
VAR.clock = pygame.time.Clock()
VAR.fonts[20] = pygame.font.SysFont('arial', 20) 

# --- Matrice des touches du clavier (code touche, (minuscule, majuscule), (dimension x, dimension y))
clavier = []
clavier.append( [(49, ("1","&"), (1,1)), (50, ("2","?"), (1,1)),  (51, ("3","#"), (1,1)), (52, ("4","@"), (1,1)), (53, ("5","?"), (1,1)), (54, ("6","-"),  (1,1)), (55, ("7","_"), (1,1)), (56, ("8","!"), (1,1)), (57, ("9","*"), (1,1)), (48, ("0",":"), (1,1)),  (8, ("RETOUR","RETOUR"), (2,1))] )
clavier.append( [(113, ("a","A"), (1,1)), (119, ("z","Z"), (1,1)),  (101, ("e","E"), (1,1)), (114, ("r","R"), (1,1)), (116, ("t","T"), (1,1)), (121, ("y","Y"),  (1,1)), (117, ("u","U"), (1,1)), (105, ("i","I"), (1,1)), (111, ("o","O"), (1,1)), (112, ("p","P"), (1,1)), (200, ("ENTRER","ENTRER"), (2,2))] )
clavier.append( [(97, ("q","Q"),  (1,1)), (115, ("s","S"), (1,1)),  (100, ("d","D"), (1,1)), (102, ("f","F"), (1,1)), (103, ("g","G"), (1,1)), (104, ("h","H"),  (1,1)), (106, ("j","J"), (1,1)), (107, ("k","K"),  (1,1)), (108, ("l","L"), (1,1)),  (59, ("m","M"), (1,1))]  )
clavier.append( [(304, ("MAJ","MAJ"), (2,1)), (122, ("w","W"), (1,1)), (120, ("x","X"), (1,1)), (99, ("c","C"), (1,1)),  (118, ("v","V"),  (1,1)), (98, ("b","B"), (1,1)),  (110, ("n","N"), (1,1)), (266, (".",","), (1,1)) , (32, ("ESPACE","ESPACE"), (3,1))                    ] )

mot, bloc_majuscule = "", False

boucle_principale = True   
while VAR.boucle_principale:

    offX, offY, dX, dY, esp = 100, 400, 70, 40, 4   
    x, y, touche_pressee = 0, 0, 0    

    VAR.fenetre.fill((128,128,128,255))
    pygame.draw.rect(VAR.fenetre, (32,32,32,255), (offX - esp, offY - esp, (dX*12) + (esp * 13), (dY*4) + (esp * 5)), 0 )
    pygame.draw.rect(VAR.fenetre, (8,8,8,255), (offX - esp, offY - esp, (dX*12) + (esp * 13), (dY*4) + (esp * 5)), 2 )    
    
    # --- Capture des evenements clavier et souris
    VAR.mouseG, VAR.mouseM, VAR.mouseD = pygame.mouse.get_pressed()
    VAR.mX, VAR.mY = pygame.mouse.get_pos()
        
    for event in pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: VAR.boucle_principale = False
            if event.type == KEYDOWN: 
                touche_pressee = event.key
                print(touche_pressee)
            
    # --- Detection de la touche MAJUSCULE
    touche_majuscule = (pygame.key.get_pressed()[304] == 1 or pygame.key.get_pressed()[303] == 1)
    if touche_majuscule == True: bloc_majuscule = False
    
    # --- Dessine le clavier
    for ligne_touches in clavier:      
        for touche in ligne_touches:          
            codeTouche, lettre, taille = touche
            tx, ty = taille
            toucheDimX, toucheDimY = (dX * tx) + (esp * (tx-1)), (dY * ty)+ (esp * (ty-1))
            lettre = FCT.iif(touche_majuscule == True or bloc_majuscule == True, lettre[1], lettre[0])
            
            # --- Gestion du clic souris sur la touche
            xT, yT = offX + x, offY + y    
            if VAR.objets_interface.zone_clickable(xT-2, yT-2, toucheDimX+3, toucheDimY+3, 0) == ENUM_Clic.Clic:
                touche_pressee = codeTouche
                if touche_pressee == 304:
                    bloc_majuscule = not bloc_majuscule
            
            # --- Gestion de l'action a entreprendre
            if touche_pressee == codeTouche:               
                if touche_pressee == 8:         # DEL
                    mot = mot[:(len(mot)-1)]
                elif touche_pressee == 200 :    # ENTRER
                    pass
                elif touche_pressee == 32 :      # ESPACE
                    mot += " "
                elif touche_pressee != 304:
                    mot += lettre
           
            # --- dessine touche
            if (codeTouche == 304 and (touche_majuscule == True or bloc_majuscule == True)) or touche_pressee == codeTouche:
                pygame.draw.rect(VAR.fenetre, (128,128,128,255), (xT, yT, toucheDimX, toucheDimY), 0 )
            else:
                pygame.draw.rect(VAR.fenetre, (64,64,64,255), (xT, yT, toucheDimX, toucheDimY), 0 )
                
            pygame.draw.rect(VAR.fenetre, (32,32,32,255), (xT+1, yT+1, toucheDimX-2, toucheDimY-2), 1 )
            image_text =  VAR.fonts[20].render(lettre, True, (255,255,255,255)) 
            VAR.fenetre.blit(image_text,  (xT + int((toucheDimX - image_text.get_width()) /2), yT  + int((toucheDimY - image_text.get_height()) /2)) )
            FCT.texte(VAR.fenetre, mot, offX, offY - 50, 20)
            
            # --- Colorie la selection
            
                
            x += ((dX + esp) * tx) 
        y += dY + esp
        x= 0
    
    pygame.display.update()
    VAR.clock.tick(VAR.nombreImageSeconde)
    
pygame.quit()
quit()
 