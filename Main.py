import pygame
from Player import Player
from Projectile import Projectile

clock = pygame.time.Clock()

# Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640

# Initialising pygame
pygame.init() 

# Creates the surface using the variables assigned
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

# Assigns the Background Image
background = pygame.image.load("Images/bg_spaceship_1.png")

# Creates the player
player = Player(370, 100, pygame.image.load("Images/FurnaceMan.png"), 250, 500)

# Creates the projectile
projectile_left = Projectile(410, 410, pygame.image.load("Images/FB001_Left.png"), 150, 75)

# Changes the name of the window
pygame.display.set_caption("Furnace Man")

# Keeps the game running
running = True 
while running:

    # Sets the frame rate
    clock.tick(60)

    for event in pygame.event.get():

        # Draws the background
        screen.blit(background, (0, 0))

        # Draws the player
        screen.blit(player.img, (player.x, player.y))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                while projectile_left.x > 0:
                    screen.blit(projectile_left.img, (projectile_left.x, projectile_left.y))
                    projectile_left.x -= projectile_left.vel


        # Quits the game
        if event.type == pygame.QUIT:
            running = False   

    pygame.display.update() 