import pygame

class Bullet(pygame.sprite.Sprite):
  
  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(filename).convert_alpha()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    
  def update(self):
    if self.rect.x < 960:
      self.rect.x += 1
      
  def fired(self, x, y):
    self.rect.x = x
    self.rect.y = y
