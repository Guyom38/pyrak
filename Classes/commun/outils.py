import math
import pygame
from pygame.locals import *
import variables as VAR

def correspondance(code):
        x, y = 0, 0
        
        if ord(code[0])>=48 and ord(code[0])<=57:
           x = ord(code[0])-48
        elif ord(code[0])>=65 and ord(code[0])<=90:
           x = ord(code[0])-65 +10
 
        if ord(code[1])>=48 and ord(code[1])<=57:
           y = ord(code[1])-48
        elif ord(code[1])>=65 and ord(code[1])<=90:
           y = ord(code[1])-65 +10     

        return x, y
     
def cercle_COS(x_centre, y_centre, rayon):
    tmp = []
    angle = 0
    for index in range(1, 360):
        angle = (index*math.pi/180)
        tmp.append( (x_centre + (rayon*math.cos(angle)), y_centre + (rayon*math.sin(angle))) )
    return tmp
 
def tour(x):
   return (x % 359)

# --- Retourne la position de la cellule sur l'ecran en pixel
def position(x, y, xOff = 0, yOff = 0):
   if (xOff, yOff) == (0, 0): return VAR.OffsetX + ((x * VAR.Zoom) * 9), (VAR.OffsetY + (y * VAR.Zoom) * 9) 
   return VAR.OffsetX + ((x * VAR.Zoom) * 9) + (xOff * VAR.Zoom), (VAR.OffsetY + (y * VAR.Zoom) * 9) + (yOff * VAR.Zoom)

