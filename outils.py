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

def bresenham(x1,y1,x2, y2):
   liste = []
   
   m_new = 2 * (y2 - y1)
   slope_error_new = m_new - (x2 - x1)
 
   y=y1
   for x in range(x1,x2+1):
      liste.append((x, y))
     
      slope_error_new =slope_error_new + m_new
 
      if (slope_error_new >= 0):
         y=y+1
         slope_error_new =slope_error_new - 2 * (x2 - x1)
   
   return liste


