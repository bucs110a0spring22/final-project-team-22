import pygame
class Controller:
  def __init__(self):
    pygame.init()
  def mainloop(self):
    while self.state == "RUNNING":