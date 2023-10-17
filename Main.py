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

# Creates a black background for the game over screen
game_over_background = pygame.Surface(screen.get_size())
game_over_background.fill((0, 0, 0))

# Assigns the Background Image
background = pygame.image.load("Images/bg_spaceship_1.png")

# Creates the player
player = Player(370, 130, pygame.image.load("Images/FurnaceMan.png"), 250, 400, 100)

# Changes the name of the window
pygame.display.set_caption("Furnace Man")

fireballs_right = []
fireballs_left = []
shoot = False #Variable to make sure only one fireball can be created per key press

# Health bar
health_bar_length = 200
health_bar_height = 20
health_bar_x = 50
health_bar_y = 50
health_bar_font = pygame.font.Font(None, 24)
health_bar_text = health_bar_font.render("Fuel:", True, (255, 255, 255))
health_bar_text_rect = health_bar_text.get_rect(center=(70, 40))

# Game over
game_over_font = pygame.font.Font(None, 64)
game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Keeps the game running
running = True
game_over = False
while running:

    for event in pygame.event.get():

        # Quits the game
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if 100 >= player.health > 0:
                # Right Arrow Key press creates fireball
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if not shoot and len(fireballs_right) < 5: # Limits the number of fireballs on the screen to 5
                            fireballs_right.append(Projectile(500, 380, pygame.image.load("Images/Fireball_right.png"), 100, 70))
                            shoot = True
                            player.health -= 5
                else:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            shoot = False


                # Left Arrow Key press creates fireball
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not shoot and len(fireballs_left) < 5: # Limits the number of fireballs on the screen to 5
                            fireballs_left.append(Projectile(400, 380, pygame.image.load("Images/Fireball_left.png"), 100, 70))
                            shoot = True
                            player.health -= 5
                else:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            shoot = False
            
            elif player.health <= 0:
                game_over = True

    # Draws the background
    screen.blit(background, (0, 0))
    
    # Draws the player
    screen.blit(player.img, (player.x, player.y))

    # Update and draw fireballs
    for fireball in fireballs_right:
        fireball.draw(screen)
        fireball.x += fireball.vel

        # Check for fireball position
        if fireball.x < 0 or fireball.x > SCREEN_WIDTH:
            fireballs_right.remove(fireball)

    # Update and draw fireballs
    for fireball in fireballs_left:
        fireball.draw(screen)
        fireball.x -= fireball.vel

        # Check for fireball position
        if fireball.x < 0 or fireball.x > SCREEN_WIDTH:
            fireballs_left.remove(fireball)

    # Draw health bar
    pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_length, health_bar_height)) # Draws the botton layer of the health bar
    pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, int(health_bar_length * (player.health / 100)), health_bar_height)) # Draws the top layer of the health bar which scales with player health
    screen.blit(health_bar_text, health_bar_text_rect)

    # Game over screen
    if game_over:
        screen.blit(game_over_background, (0, 0)) # Blits the game over background
        screen.blit(game_over_text, game_over_text_rect) # Blits the game over text

    # Sets the frame rate
    clock.tick(60)        

    pygame.display.update()

pygame.quit()