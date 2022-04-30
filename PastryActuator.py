import pygame
from pygame.locals import*
import random
import time

totala = 0

def playGame():
  pygame.mixer.pre_init()
  pygame.mixer.music.load("Music/Erika.mp3")
  pygame.mixer.music.play(-1)
  imagevariable = pygame.image.load("Logo/edp455.jpg")
  screen.blit(imagevariable, (0,0))
  while True:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y=event.pos
        print("coords:")
        print("x:"+str(x))
        print("y:"+str(y))
        total += 1
        print(total, end = \n)