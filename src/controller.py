import pygame, sys, random
from src import bullet, enemy, player

class Controller:

  def __init__(self, width=960, height=540):

    #init
    pygame.init()
    self.clock = pygame.time.Clock()
    pygame.font.init()
    pygame.key.set_repeat(1, 50)

    #screen
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.background.blit(pygame.image.load('assets/background.png'),(0,0))
    
    #objects
    self.player = player.Player(250, self.height/2, "assets/player2.png")
    self.playergroup = pygame.sprite.Group()
    self.playergroup.add(self.player)
    self.enemies = pygame.sprite.Group()
    self.bullets = pygame.sprite.Group()
    self.bullet = bullet.Bullet(250, self.height/2, "assets/bullet.png")

    self.enemies_killed = 0
    self.number_of_enemies = 5
    for i in range(self.number_of_enemies):
      self.enemies.add(enemy.Enemy(random.randrange(self.width/2, self.width*0.9),random.randrange(self.height/5, self.height*0.9),"assets/enemy.png"))
    
    self.all_sprites = pygame.sprite.Group((self.player),tuple(self.enemies), (self.bullet))
    self.gamestate = "RUNNING"

  def mainloop(self):
    while True:
      if self.gamestate == "RUNNING":
        self.gameloop()
      if self.gamestate == "WIN":
        self.win()
      if self.gamestate == "LOSE":
        self.lose()

  def gameloop(self):
    
    while self.gamestate == "RUNNING":
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
        if event.type == pygame.KEYUP:
          if(event.key == pygame.K_SPACE):
            self.bullet.fired(self.player.rect.x,self.player.rect.y)
            
      bullet_hit = pygame.sprite.spritecollide(self.bullet, self.enemies, True)
      if bullet_hit:
        for i in bullet_hit:
          i.kill()
          self.enemies_killed += 1

      enemy_hit = pygame.sprite.groupcollide(self.enemies, self.playergroup, False, True)
      if enemy_hit:
        for i in enemy_hit:
          i.kill()
          self.gamestate = "LOSE"

      if self.enemies_killed == self.number_of_enemies:
        self.gamestate = "WIN"
          
      self.enemies.update()
      self.bullet.update()
      self.screen.blit(self.background, (0, 0))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()

  def win(self):
    font = pygame.font.SysFont(None, 50)
    text_1 = font.render("You won! Press R to play again.", False, (255, 255, 255))
    text_2 = font.render("Press Q to exit.", False, (255, 255, 255))
    
    self.screen.blit(text_1, (220, 250))
    self.screen.blit(text_2, (340,300))
    pygame.display.flip()
    
    while self.gamestate == "WIN":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
              if(event.key == pygame.K_r):
                self.player = player.Player(250, self.height/2, "assets/player2.png")
                self.playergroup = pygame.sprite.Group()
                self.playergroup.add(self.player)
                self.enemies = pygame.sprite.Group()
                self.bullets = pygame.sprite.Group()
                self.bullet = bullet.Bullet(250, self.height/2, "assets/bullet.png")
            
                self.enemies_killed = 0
                self.number_of_enemies = 5
                for i in range(self.number_of_enemies):
                  self.enemies.add(enemy.Enemy(random.randrange(self.width/2, self.width*0.9),random.randrange(self.height/5, self.height*0.9),"assets/enemy.png"))

                self.all_sprites = pygame.sprite.Group((self.player),tuple(self.enemies), (self.bullet))
                self.gamestate = "RUNNING"
              elif(event.key == pygame.K_q):
                sys.exit()

  def lose(self):
    font = pygame.font.SysFont(None, 50)
    text_1 = font.render("You lost! Press R to play again.", False, (255, 255, 255))
    text_2 = font.render("Press Q to exit.", False, (255, 255, 255))

    self.screen.blit(text_1, (220, 250))
    self.screen.blit(text_2, (340,300))
    pygame.display.flip()

    while self.gamestate == "LOSE":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
              if(event.key == pygame.K_r):
                self.player = player.Player(250, self.height/2, "assets/player2.png")
                self.playergroup = pygame.sprite.Group()
                self.playergroup.add(self.player)
                self.enemies = pygame.sprite.Group()
                self.bullets = pygame.sprite.Group()
                self.bullet = bullet.Bullet(250, self.height/2, "assets/bullet.png")
            
                self.enemies_killed = 0
                self.number_of_enemies = 5
                for i in range(self.number_of_enemies):
                  self.enemies.add(enemy.Enemy(random.randrange(self.width/2, self.width*0.9),random.randrange(self.height/5, self.height*0.9),"assets/enemy.png"))

                self.all_sprites = pygame.sprite.Group((self.player),tuple(self.enemies), (self.bullet))
                self.gamestate = "RUNNING"
              elif(event.key == pygame.K_q):
                sys.exit()
