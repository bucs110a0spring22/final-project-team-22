import pygame

class Player(pygame.sprite.Sprite):
  
  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(filename).convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.step = 5
    
  def move_up(self):
    """
    When this method is called, the player object will move up by self.step(int) 
    arg:none
    return:none
    """
    self.rect.y -= self.step
  def move_down(self):
    """
    When this method is called, the player object will down by self.step(int) 
    arg:none
    return:none
    """
    self.rect.y += self.step
  def move_left(self):
    """
    When this method is called, the player object will move left by self.step(int) 
    arg:none
    return:none
    """
    self.rect.x -= self.step
  def move_right(self):
    """
    When this method is called, the player object will move right by self.step(int) 
    arg:none
    return:none
    """
    self.rect.x += self.step
    