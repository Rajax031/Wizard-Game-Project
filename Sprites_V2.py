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
  def __int__(self, game):
    pg.sprite.Sprite.__int__(self)
    self.game = game
    # for the following line of code, in the parentheses, use values for x, y, width, and height, which are from spritesheets
    self.image = self.game.spritesheet.get_image(x, y, width, height)
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH / 2, HEIGHT / 2)
    self.pos = vec(WIDTH / 2, HEIGHT /2)
    self.vel = vec(0, 0)
    self.acc = vec(0, 0)
 
 class Platform(pg.sprite.Sprite):
 
