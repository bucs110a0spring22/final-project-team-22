import pygame,sys,random
#import sys
#import random
from src import bullet
from src import enemy
from src import player
class Controller:

  def __init__(self, width=960, height=540):

    #init
    pygame.init()
    self.clock=pygame.time.Clock()
    pygame.font.init()
    pygame.key.set_repeat(1, 50)

    #screen
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    #self.background.fill((250, 250, 250))  # set the background to white
    self.background.blit(pygame.image.load('assets/background.png'),(0,0))
    
    #objects
    self.player=player.Player(50,height/2,"assets/player2.png")

    self.enemies = pygame.sprite.Group()
    self.bullets=pygame.sprite.Group()
    self.bullet=bullet.Bullet(50,height/2,"assets/bullet.png")

    self.enemies_killed = 0
    self.number_of_enemies=5
    for i in range(self.number_of_enemies):
      self.enemies.add(enemy.Enemy(random.randrange(width/2, width*0.9),random.randrange(height/2, height*0.9),"assets/enemy.png"))
    
    
    #self.bullets.add(bullet.Bullet(-10,-10,"assets/Bullet_drawing.png"))
    self.all_sprites=pygame.sprite.Group((self.player),tuple(self.enemies), (self.bullet))
    self.gamestate="RUNNING"

  def mainloop(self):
    while True:
      if self.gamestate=="RUNNING":
        self.gameloop()
      if self.gamestate=="GAMEOVER":
        self.gameover()

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
      bullet_hit= pygame.sprite.spritecollide(self.bullet,self.enemies, True)
      
      if bullet_hit:
        for i in bullet_hit:
          i.kill()
          self.enemies_killed += 1

      print(self.enemies_killed)

      if self.enemies_killed == self.number_of_enemies:
        self.gamestate = "GAMEOVER"
          
      self.enemies.update()
      self.bullet.update()
      self.screen.blit(self.background, (0, 0))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()

  def gameover(self):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Game Over, play again? press SPACE ", False, (0, 0, 0))
    self.screen.blit(text, (200, 300))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
              if(event.key == pygame.K_SPACE):
                self.gamestate="RUNNING"
                break
                