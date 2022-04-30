import pygame
from pygame.locals import*
import random
import time
pink = (255,200,200)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
colors=[pink,blue,green]
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("window")

def show_text(msg,xp,yp,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(xp,yp))

def runPing():
  while True:
      if p1scorep==11:
          screen.fill(black)
          show_text("WINNER",40,10,white)
          pygame.display.update()
          time.sleep(2)
          quit()
      if p2scorep==11:
          screen.fill(black)
          show_text("WINNER",870,10,white)
          time.sleep(2)
          quit()
      pygame.display.update()
      screen.fill(black)
      show_text("Score:"+str(p1scorep),40,10,white)
      show_text("Score:"+str(p2scorep),870,10,white)
      pygame.draw.circle(screen,green,(xp,yp),10,0)
      pygame.draw.rect(screen,blue,(50,a,20,150))
      pygame.draw.rect(screen,pink,(950,b,20,150))
      pygame.draw.line(screen,white,(500,0),(500,600),5)
      for event in pygame.event.get():
          if event.type == KEYDOWN:
              if event.key == K_w:
                  acp=-2
              if event.key==K_DOWN:
                  bcp=2
              if event.key == K_s:
                  acp=2
              if event.key==K_UP:
                  bcp=-2
          if event.type == KEYUP:
              if event.key == K_w:
                  acp=0
              if event.key == K_DOWN:
                  bcp=0
              if event.key == K_s:
                  acp=0
              if event.key == K_UP:
                  bcp=0
  
      if xp < 80 and ap<yp<ap+150:
          xchangep=-xchangep
      if xp > 940 and bp<yp<bp+150:
          xchangep=-xchangep
     
          
      ap=ap+acp
      bp=bp+bcp
      if ap<=0:
          ap=0
      if ap>=450:
          ap=450
  
      if bp>=450:
          bp=450
      if bp<=0:
          bp=0
  
      if xp==990:
          xp=500
          yp=300
          p1score=p1score+1
      if xp==10:
          xp=500
          yp=300
          p2score=p2score+1
      if yp>590:
          ychangep=-2
      if yp<10:
          ychangep=2
  
      xp = xp + xchangep
      yp = yp + ychangep
