import pygame

class Wall(pygame.sprite.Sprite):
  
  def __init__(self, x,y):
    pygame.sprite.Sprite.__init__(self)
    self.rect = pygame.Rect((20, 50), (50, 2000))
    self.rect.x = x
    self.rect.y = y