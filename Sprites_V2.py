#Updated version of sprites.py
#Spritesheet variable is in settings.py but we can use it here also


#INSERT SPRITESHEET FILE HERE, PNG FILE
Spritesheet = ""

import pygame as pg
from settings import *
vec = pg.math.Vector2

class Spritesheet:
#Loads file 
  def __init__(self, filename):
    self.spritesheet = pygame.image.load(filename).convert()
    
  #This gets the position of the sprite from the spritesheet
  def get_image(self, x, y, width, height):
    image = pygame.Surface((width, height))
    image.blit(self.spritesheet, (0,0), (x,y, width, height))
    return image
    
 class Player(pg.sprite.Sprite):
 
 
 class Platform(pg.sprite.Sprite):
 
