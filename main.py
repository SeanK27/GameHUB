import pygame
from pygame.locals import*
import random
import time
from Title import*

pink = (255,200,200)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
colors= [pink,blue,green]
pygame.init()
screen = pygame.display.set_mode((1000,600))

##########PING VARS#################
xp=300
yp=300
ap=300
bp=300
xchangep=2
ychangep=2
acp=0
bcp=0
p1scorep=0
p2scorep=0
###################################
#######PASTRY ACTUATOR VARS########
totala=0
displayscorea=""
###################################
pygame.mixer.pre_init()
pygame.mixer.music.load("Music/GloriousSound.mp3")
pygame.mixer.music.play(-1)
## 0: title screen; 1:game selection; 2: nft market; 3: ping; 4: pastryactuator; 5: skaavok; 6:worm
selection=0 

def show_text(msg,xp,yp,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(xp,yp))

while True:
  pygame.display.update()
  if selection == 0: ###################TITLE###########################
    drawTitle()
    pygame.display.update()
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          x,y=event.pos
          # print("coords:")
          # print("x:"+str(x))
          # print("y:"+str(y))
          if x>=333 and x<=666 and y>=266 and y<=366:
            screen.fill(black)
            pygame.display.update()
            x=0
            y=0
            selection = 1  #go to game selection
            print("going to game selection")
          if x>=333 and x<=666 and y>=450 and y<=550:
            screen.fill(black)
            pygame.display.update()
            x=0
            y=0
            selection = 2  #go to nft page
            print("going to NFTS")

  if selection == 1: #####################SELECT SCREEN###################
    drawSelect()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y=event.pos
        # print("coords:")
        # print("x:"+str(x))
        # print("y:"+str(y))
        if x>=143 and x<=429 and y>=200 and y<=300:
          screen.fill(black)
          pygame.display.update()
          x=0
          y=0
          selection = 3 #go to ping
          print("going to ping")
        if x>=143 and x<=429 and y>=400 and y<=500:
          screen.fill(black)
          pygame.display.update()
          x=0
          y=0
          selection = 5  #go to skaavok
          print("going to skaavok")
        if x>=572 and x<=858 and y>=200 and y<=300:
          screen.fill(black)
          pygame.display.update()
          x=0
          y=0
          selection = 4  #go to pastry actuator
          print("going to pastry actuator")
        if x>=572 and x<=858 and y>=400 and y<=500:
          screen.fill(black)
          pygame.display.update()
          x=0
          y=0
          selection = 6  #go to worm
          print("going to worm")
  
  if selection == 2:
    show_text("NFTS", 0, 0, white)
  if selection == 3: ############################PING######################
    while True:
        if p1scorep==5:
            screen.fill(black)
            show_text("WINNER",40,10,white)
            pygame.display.update()
            time.sleep(2)
            quit()
        if p2scorep==5:
            screen.fill(black)
            show_text("WINNER",870,10,white)
            pygame.display.update()
            time.sleep(2)
            quit()
        pygame.display.update()
        screen.fill(black)
        show_text("Score:"+str(p1scorep),40,10,white)
        show_text("Score:"+str(p2scorep),870,10,white)
        pygame.draw.circle(screen,green,(xp,yp),10,0)
        pygame.draw.rect(screen,blue,(50,ap,20,150))
        pygame.draw.rect(screen,pink,(950,bp,20,150))
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
            p1scorep=p1scorep+1
        if xp==10:
            xp=500
            yp=300
            p2scorep=p2scorep+1
        if yp>590:
            ychangep=-2
        if yp<10:
            ychangep=2
    
        xp = xp + xchangep
        yp = yp + ychangep

  if selection == 4:  ######################PASTRY ACTUATOR########################
    pygame.mixer.pre_init()
    pygame.mixer.music.load("Music/Erika.mp3")
    pygame.mixer.music.play(-1)
    edp445 = pygame.image.load("Logo/edp455.jpg")
    screen.blit(edp445, (350,150))
    show_text("Pastry Actuations: " + str(totala), 0, 0, white)
    pygame.display.update()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          xa,ya=event.pos
          # print("coords:")
          # print("x:"+str(xa))
          # print("y:"+str(ya))
          # print(totala)
          if xa>=350 and xa<=650 and ya>=150 and ya<=450:
            totala += 1
            screen.fill(black)
            screen.blit(edp445, (350,150))
            show_text("Pastry Actuations: " + str(totala), 0, 0, white)
            pygame.display.update()


      
  if selection == 5: ####################SKAAVOK###################
    show_text("skaavok", 0, 0, white)
  if selection == 6: #####################WORM#####################
    show_text("worm", 0, 0, white)