import pygame

pygame.init()

display_width =800
display_height =900

gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racing')

black = (0,0,0)
white =(255,255,255)
pink = (255,0,255)

clock =pygame.time.Clock()

helicopter=pygame.image.load('Resources/military-helicopter.png')
x =(display_width*0.42)
y=(display_height*0.6)
x_change =0
y_change=0
helicopterSpeed =0

#Game loop
running =True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False

        ###############################
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT :
                x_change =-5
            elif event.key ==pygame.K_RIGHT:
                x_change =5
        if event.type ==pygame.KEYUP:
            if event.key ==pygame.K_LEFT:
                x_change=0
            elif event.key==pygame.K_RIGHT:
                x_change=0

        #################################
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_UP :
                y_change =-5
            elif event.key ==pygame.K_DOWN :
                y_change =5
        if event.type ==pygame.KEYUP:
            if event.key ==pygame.K_UP :
                y_change=0
            elif event.key==pygame.K_DOWN :
                y_change=0
    ##
    x +=x_change
    y+=y_change
    #first

    gameDisplay.fill(pink)
    #second

    gameDisplay.blit(helicopter,(x,y))
    #third
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()