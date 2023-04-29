import pygame

#initialising pygame

#1.INITIALIZATION(init())
# -load window
#-size of the window
#Time 
#
#2.Game-controls
#Keys for  playing the game
#3. GAME LOOP
#while function 
#conditions 
#update()





pygame.init() #initialization

#defining size of game window
screen  = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Game1")
# clock to track time 
clock =pygame.time.Clock()


#Game-Loop
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            crashed:True
            print(event)
    pygame.display.update()
    clock.tick(190)
    
    
    