import pygame
from pygame.locals import*
import random
import time

pink = (255,200,200)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
x=0
y=0
colors=[pink,blue,green]
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("window")
titleLogo = pygame.image.load("Logo/titleLogo.png")


def drawTitle():
  screen.fill(black)
  pygame.display.set_caption("window")
  pygame.draw.rect(screen, white, (333, 266, 333, 100))
  pygame.draw.rect(screen, white, (333, 430, 333, 100))
  screen.blit(titleLogo, (250, 30))
  pygame.display.update()

def drawSelect():
  screen.fill(black)
  pygame.draw.rect(screen, white, (143, 200, 286, 100))
  pygame.draw.rect(screen, white, (143, 400, 286, 100))
  pygame.draw.rect(screen, white, (572, 200, 286, 100))
  pygame.draw.rect(screen, white, (572, 400, 286, 100))
  pygame.display.update()