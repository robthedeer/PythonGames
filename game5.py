
import pygame
import time
import random


pygame.init()

d_width=800
d_height=600

black=(0,0,0)
white =(255,255,255)
red=(255,0,0)
blue=(153,204,255)
grey =(128,128,128)

copter_width =73

showGame =pygame.display.set_mode((d_width,d_height))
pygame.display.set_caption('RACING SHIP')
clock =pygame.time.Clock()
back_image= pygame.image.load('Resources/main_image_star-forming_region_carina_nircam_final-5mb.jpeg')
copterImg=pygame.image.load('Resources/Enemies/enemyBlue5.png')
enemy1=pygame.image.load('Resources/Enemies/enemyBlack1.png')

#Function 1 -display copter image
def background_image(x2,y2):
    showGame.blit(back_image,(x2,y2))
def copter(x,y):
 showGame.blit(copterImg,(x,y))

def Enemy1(x1,y1):
    showGame.blit(enemy1,(x1,y1))
    
# end def

#Function 2 -display text and initialise font
def textShow(text,font):
 textSurface =font.render(text,True,red)
 return textSurface,textSurface.get_rect()

def textDisplay(text):
 largeText =pygame.font.Font('Resources/grand-hotel/GrandHotel-Regular.otf',80)
 TextSurf,TextRect =textShow(text,largeText)
 TextRect.center =((d_width/2),(d_height)/2)
 showGame.blit(TextSurf,TextRect)
 pygame.display.update()

def crash():
    textDisplay('You crashed')

def gameLoop():


     x = (d_width*0.42)
     y= (d_height*0.6)
     x1=random.randrange(0,d_width)
     y1=-600
     x2=0
     y2=0
     enemy1_speed=7
     enemy1_width=100
     enemy_height=100

     x_change =0

     gameOver= False

     while not gameOver:
         for event in pygame.event.get():
             if event.type ==pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type ==pygame.KEYDOWN:
                 if event.key ==pygame.K_LEFT or event.key ==pygame.K_a:
                     x_change =-3
                 if event.key ==pygame.K_RIGHT or event.key ==pygame.K_d:
                     x_change =3
             if event.type ==pygame.KEYUP:
                 if event.key ==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                     x_change=0
                 if event.key ==pygame.K_a or event.key ==pygame.K_d:
                     x_change =0
         x += x_change
        #load picture 1
         background_image(x2,y2)
         #load picture 2
         copter(x,y)
         #load picture 3
         Enemy1(x1,y1)
         y1+=enemy1_speed
         

         if x >d_width -copter_width or x<0:
             crash()
         
         if y1>d_height:
            y1=0-enemy_height
            x1=random.randrange(d_width)
            pygame.display.update()
            clock.tick(60)
gameLoop()
pygame.quit()
quit()

