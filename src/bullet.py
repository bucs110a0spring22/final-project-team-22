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
    """
    the update method makes the bullet travle in a straight line across the screen going horizontally
    Arg: None
    return: none
    """
    if self.rect.x < 960:
      self.rect.x += 1
      
  def fired(self, x, y):
    """
    Fired method moves the bullet object onto the given coordinates
    Arg: x(int), y(int) each represents x and y coordinate of the bullet's destiny
    return: none
    """
    self.rect.x = x
    self.rect.y = y
