import pygame


 
screen =pygame.display.set_mode((980,640))

running =True

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
            
    screen.fill((255,255,255))
   
    pygame.draw.circle(screen,(0,255,255),(20,20),20)
    pygame.draw.circle(screen,(238,130,238),(100,80),30)
    pygame.draw.circle(screen,(255,215,0),(185,150),41)
    pygame.draw.circle(screen,(255,165,0),(320,220),62)
    pygame.draw.circle(screen,(128,128,128),(645,150),71)
    pygame.draw.circle(screen,(139,0,0),(500,300),85)
    pygame.draw.circle(screen,(50,205,50),(750,440),175)
    
    pygame.display.flip()
    