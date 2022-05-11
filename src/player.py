import pygame
class Player(pygame.sprite.Sprite):
  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image= pygame.image.load(filename).convert_alpha()
    self.image= pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.step=5
  def move_up(self):
      self.rect.y -= self.step
  def move_down(self):
      self.rect.y += self.step
  def move_left(self):
      self.rect.x -= self.step
  def move_right(self):
      self.rect.x += self.step
  def attack(self):
    pass