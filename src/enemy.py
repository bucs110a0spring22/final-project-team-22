import pygame
import random
# import random
class Enemy(pygame.sprite.Sprite):
  def __init__(self, x,y, filename):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(filename).convert_alpha()
    self.image= pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.step=1
  def update(self):
    accumulator=0
    if accumulator%2==0:
        if self.rect.y>0 and self.rect.y<400:
          self.rect.y+=self.step
        if self.rect.y==400:
          self.rect.y-=self.step

      
    
    """
    accumulator=0
    if accumulator%2==0:
      if self.rect.y<480:
        self.rect.y-=self.step
      else:
        accumulator+=1
    else:
      if self.rect.y>0:
        self.rect.y+=self.step
      else:
        accumulator+=1
    """
"""
  pygame.init()

  x, y = 200, 130

  screen = pygame.display.set_mode((400,300), 0, 32)
  pygame.display.set_caption("Game")
  sprite = pygame.image.load("assets/Enemy_jelly.png")

  screen.blit(sprite, (x-50,y-50))

  keys = pygame.key.get_pressed()
  if keys[pygame.image.load("assets/Enemy_jelly.png").K_a]: x -= 2
  if keys[pygame.image.load("assets/Enemy_jelly.png").K_d]: x += 2
  if keys[pygame.image.load("assets/Enemy_jelly.png").K_w]: x -= 2
  if keys[pygame.image.load("assets/Enemy_jelly.png").K_s]: x += 2
"""
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((400,300), 0, 32)
# pygame.display.set_caption("Game")
# x, y = 200, 130
# sprite = pygame.image.load("assets/Enemy_jelly.png")


# loop = True
# while loop:
#   # screen.fill(0,0,0)
#   # screen.blit(sprite, (x-50,y-50))
#   for event in pygame.event.get():
#     if event.type == QUIT:
#       loop = False

#   keys = pygame.key.get_pressed()
#   if keys[pygame.K_LEFT]: x -= 2
#   if keys[pygame.K_RIGHT]: x += 2
#   if keys[pygame.K_UP]: x -= 2
#   if keys[pygame.K_DOWN]: x += 2
#   pygame.display.flip()
#   clock.tick(60)

# pygame.quit()


# pygame.init()

# x, y = 200, 130

# screen = pygame.display.set_mode((400,300), 0, 32)
# pygame.display.set_caption("Game")
# sprite = pygame.image.load("assets/Enemy_jelly.png")

# screen.blit(sprite, (x-50,y-50))

# keys = pygame.key.get_pressed()
# if keys[pygame.image.load("assets/Enemy_jelly.png").K_a]: x -= 2
# if keys[pygame.image.load("assets/Enemy_jelly.png").K_d]: x += 2
# if keys[pygame.image.load("assets/Enemy_jelly.png").K_w]: x -= 2
# if keys[pygame.image.load("assets/Enemy_jelly.png").K_s]: x += 2

