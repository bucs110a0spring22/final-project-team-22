import pygame,sys,random
#import sys
#import random
from src import bullet
from src import enemy
from src import player
class Controller:
  def __init__(self, width=640, height=480):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.fill((250, 250, 250))  # set the background to white
    self.clock=pygame.time.Clock()
    pygame.font.init()
    pygame.key.set_repeat(1, 50)
    self.enemies = pygame.sprite.Group()
    self.bullets=pygame.sprite.Group()
    number_of_enemies=3
    for i in range(number_of_enemies):
      self.enemies.add(enemy.Enemy(width/2,height/2,"assets/Enemy_jelly.png"))
    self.player=player.Player(50,height/2,"assets/Player.png")
    self.bullet=bullet.Bullet(-10,-10,"assets/Bullet_drawing.png")
    #self.bullets.add(bullet.Bullet(-10,-10,"assets/Bullet_drawing.png"))
    self.all_sprites=pygame.sprite.Group((self.player),tuple(self.enemies), tuple(self.bullets))
    self.gamestate="RUNNING"
  def mainloop(self):
    while True:
      if self.gamestate=="RUNNING":
        self.gameloop()
  def gameloop(self):
    while self.gamestate=="RUNNING":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if(event.key == pygame.K_w):
              self.player.move_up()
          elif(event.key == pygame.K_s):
              self.player.move_down()
          elif(event.key == pygame.K_a):
              self.player.move_left()
          elif(event.key == pygame.K_d):
              self.player.move_right()
          elif(event.key == pygame.K_SPACE):
            self.bullet.fired(self.player.rect.x,self.player.rect.y)
      self.enemies.update()
      self.bullets.update()
      self.screen.blit(self.background, (0, 0))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()