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



#Game loop
running =True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False

   #first
    gameDisplay.fill(pink)
   #second
    gameDisplay.blit(helicopter,((display_width*0.42),(display_height*0.6)))
   #third
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()