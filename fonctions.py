from tkinter import Y
import pygame
from pygame.locals import *

import variables as VAR
import outils

def iif(condition, vrai, faux):
    if condition == True:
        return vrai
    else:
        return faux

def reset_clic(): VAR.cycle = pygame.time.get_ticks() 
def clic(bouton = -1, delais = -1):
    if delais == -1 and bouton == -1: 
        return False

    if pygame.time.get_ticks() > VAR.cycle + delais: 
        return True and pygame.mouse.get_pressed()[bouton] 

    return False
    
def zoom(grossir):
    if grossir == True: 
        VAR.Zoom = VAR.Zoom +4
    else:
        VAR.Zoom = VAR.Zoom -4
    
    VAR.joueur_en_cours.recentrer_camera()
        
    VAR.v2 = (2 * VAR.Zoom)
    VAR.v4 = (4 * VAR.Zoom)
    VAR.v5 = (5 * VAR.Zoom)
    VAR.v7 = (7 * VAR.Zoom)
    VAR.v9 = (9 * VAR.Zoom)  
    VAR.image_zone = [], []

    VAR.tuiles.reset_images_tuiles()
    
        
        
def texte(fenetre, txt, x, y, taille, color = (255,255,255)):
    text =  VAR.fonts[taille].render(txt, True, color) 
    VAR.fenetre.blit(text, (x, y))

def image(codeImg):
    tmp = pygame.Surface((VAR.Taille, VAR.Taille),pygame.SRCALPHA,32)
    tX, tY = outils.correspondance(codeImg)
    tmp.blit(VAR.texture, (0,0), (tX * VAR.Taille, tY * VAR.Taille, VAR.Taille, VAR.Taille))
                        
    # --- Colle le decors    
    tmp = pygame.transform.scale(tmp, (VAR.Zoom, VAR.Zoom))
    return tmp

def icone(codeImg):
    tmp = pygame.Surface((63, 66),pygame.SRCALPHA,32)
    tmp.blit(VAR.icones, (0,0), (codeImg * 63, 0, 63, 66))
                        
    # --- Colle le decors    
    tmp = pygame.transform.scale(tmp, (63, 66))
    return tmp

def image_decoupe(img, x, y, dimx, dimy, dimxZ = -1, dimyZ = -1):
    tmp = pygame.Surface((dimx, dimy),pygame.SRCALPHA,32)
    tmp.blit(img, (0,0), (int(x) * dimx, y * dimy, dimx, dimy))
                        
    # --- Colle le decors 
    if dimxZ != -1 and dimyZ != -1:   
        tmp = pygame.transform.scale(tmp, (dimxZ, dimyZ))
    return tmp

def SurEcran(xP, yP, xM, yM):
    return (xP >= -xM) and (xP < VAR.EcranX) and (yP >= -yM) and (yP < VAR.EcranY)

def GenereMat2D(xDim, yDim, valeurDefaut):
    return [[valeurDefaut for x in range(xDim)] for i in range(yDim)]

def Generer_Mask_Image(img):
    pixel_array = pygame.PixelArray(img.copy())
    for y in range(img.get_height()):
        for x in range(img.get_width()):
            if pixel_array[x][y] != VAR.TRANSPARENCE:
                pixel_array[x][y] = pygame.Color(255,255,255,255)
    img2 = pixel_array.make_surface()
    pixel_array.close()
    return img2
    
    