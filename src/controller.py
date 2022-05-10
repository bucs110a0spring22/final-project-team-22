import pygame
from src import bullet
class Controller:
  def __init__(self):
    pygame.init()
    self.display= pygame.display.set_mode((500,500))
    self.bullet=  bullet
    self.state="RUNNING"
  def mainloop(self):
    while True:
      if self.state== "RUNNING":
        self.gameloop()
      if self.state=="EXIT":
        self.exitloop()
  def gameloop(self):
    while self.state == "RUNNING":
      for event in pygame.event.get():
        if event.type== pygame.QUIT:
          self.state= "EXIT"
  def exitloop(self):
    pygame.quit()
    exit()
  mainloop(self)