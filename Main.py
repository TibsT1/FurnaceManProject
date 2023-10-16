import pygame

pygame.init() # initialaising pygame 
screen = pygame.display.set_mode((1000,500)) #creates the surface, 1000 = width, 500 = height
pygame.display.set_caption("Frunace Man") # Changes ther name of the window
running = True # Makes the 
while True: # makes the previous code continue to run
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # is equal to the "x" button on the window
            pygame.quit() # opposite of pygame.init
            exit() # cancels the "while True"

    pygame.display.update() 
