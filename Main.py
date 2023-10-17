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
player = Player(370, 130, pygame.image.load("Images/FurnaceMan.png"), 250, 400)

# Changes the name of the window
pygame.display.set_caption("Furnace Man")

fireballs = []

# Keeps the game running
running = True 
while running:

    for fireball in fireballs[::-1]:
        if fireball.x < 1000 and fireball.x > 0:
            fireball.x += fireball.vel
        else:
            fireballs.pop(fireballs.index(fireball))

    keys = pygame.key.get_pressed()


    # Key press creates fireball
    if keys[pygame.K_RIGHT]:
        if len(fireballs) < 1:
            fireballs.append(Projectile(470, 380, pygame.image.load("Images/Fireball.png"), 100, 70))
            for fireball in fireballs:
                fireball.draw(screen)
        else:
            continue

    # Sets the frame rate
    clock.tick(30)

    for event in pygame.event.get():

        # Draws the background
        screen.blit(background, (0, 0))

        # Draws the player
        screen.blit(player.img, (player.x, player.y))

        # Quits the game
        if event.type == pygame.QUIT:
            running = False   

    pygame.display.update() 