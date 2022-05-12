import pygame
import random
class Enemy(pygame.sprite.Sprite):

  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(filename).convert_alpha()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def update(self):

    move = random.randrange(0, 30)
    if move == 1:
      self.rect.x -= 3
  def wall(self):
    if self.rect.x <400:
      return True