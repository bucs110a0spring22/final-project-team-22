import pygame
from src import player
class Bullet(pygame.sprite.Sprite):
  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image= pygame.image.load(filename).convert_alpha()
    self.image= pygame.transform.scale(self.image, (200, 200))
    self.rect= self.image.get_rect()
    self.rect.x= x
    self.rect.y= y
  def update(self):
    self.rect.x+=1
