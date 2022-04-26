import pygame
class Bullet(pygame.sprite.Sprite):
  def __init__(self, position, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image= pygame.image.load(filename)
    self.rect= self.image.get_rect()
    self.rect.x= position[0]
    self.rect.y= position[1]

  def update(self):
    