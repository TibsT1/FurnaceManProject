import pygame

pygame.init() # initialaising pygame 
screen = pygame.display.set_mode((1000,500)) #creates the surface
running = True # Makes the 
while True: # makes the previous code continue to run
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # is equal to the "x" button on the window
            pygame.quit() # opposite of pygame.init
    pygame.display.update()
