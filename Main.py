import pygame
import sys
import random
import time
from Player import Player
from Projectile import Projectile
from Enemies import Enemies
from Items import Items

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

# Assigns the Menu Background Image
menu_background = pygame.image.load("Images/BrickBackground.jpg")

# Creates the player
player = Player(400, 180, pygame.image.load("Images/FurnaceMan.png"), 210, 340, 100)

# Changes the name of the window
pygame.display.set_caption("Furnace Man")

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

# Main Menu
main_menu_font = pygame.font.Font(None, 64)
main_menu_text = main_menu_font.render("Furnace Man", True, (255, 255, 255))
main_menu_text_rect = main_menu_text.get_rect(center=(SCREEN_WIDTH // 2, 100))

# Buttons
# Create the Play Button
play_button = pygame.Rect(400, 200, 200, 50)

# Create the Play Button Text
play_button_font = pygame.font.Font(None, 64)
play_button_text = play_button_font.render("Play", True, (255, 255, 255))
play_button_text_rect = play_button_text.get_rect(center=(500, 225))

# Create the Quit Button
quit_button = pygame.Rect(400, 400, 200, 50)

# Create the Quit Button Text
quit_button_font = pygame.font.Font(None, 64)
quit_button_text = quit_button_font.render("Quit", True, (255, 255, 255))
quit_button_text_rect = quit_button_text.get_rect(center=(500, 425))

def main_menu():

    while True:

        click = False

        for event in pygame.event.get():

            # Quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Blit the Menu Background and Menu Text
        screen.blit(menu_background, (0,0))
        screen.blit(main_menu_text, main_menu_text_rect)

        # Get X and Y positions of the mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if the Play Button is clicked
        if play_button.collidepoint((mouse_x, mouse_y)):
            if click: # If the Play Button is clicked, run the Main Game function
                game()

        # Check if the Quit Button is clicked 
        if quit_button.collidepoint((mouse_x, mouse_y)):
            if click: # If the Quit Button is clicked, closes the game
                pygame.quit()
                sys.exit()

        # Draws the Play Button Rect and Text
        pygame.draw.rect(screen, (0, 0, 0), play_button)
        screen.blit(play_button_text, play_button_text_rect)

        # Draws the Quit Button Rect and Text
        pygame.draw.rect(screen, (0, 0, 0), quit_button)
        screen.blit(quit_button_text, quit_button_text_rect)

        pygame.display.update()
                    
def game():
    fireballs_right = []
    fireballs_left = []
    shoot = False #Variable to make sure only one fireball can be created per key press
    consume = False
    font = pygame.font.Font(None, 64)
    start_time = time.time()
    elapsed_time = 0

    coal = Items(pygame.image.load("Images/Coal Frame.png"), 120, 120, 100)

    running = True
    game_over = False
    # Keeps the game running
    while running:

        coal_font = pygame.font.Font(None, 64)
        coal_text = coal_font.render("x{CoalAmount}".format(CoalAmount=coal.amount), True, (0, 0, 0))
        coal_text_rect = coal_text.get_rect(center=(135, 595))

        for event in pygame.event.get():

            # Quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checks if the game is over
            if not game_over:
                # Checks if the player's health is greater than 0 and smaller than 100
                if 100 >= player.health > 0:
                    # Right Arrow Key press creates fireball
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            if not shoot and len(fireballs_right) < 5: # Limits the number of fireballs on the screen to 5
                                fireballs_right.append(Projectile(500, 380, pygame.image.load("Images/Fireball_right.png"), 100, 70, 10))
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
                                fireballs_left.append(Projectile(400, 380, pygame.image.load("Images/Fireball_left.png"), 100, 70, 10))
                                shoot = True
                                player.health -= 5
                    else:
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT:
                                shoot = False

                if 100 > player.health > 0:
                    # Space Key press consumes coal
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if not consume and coal.amount > 0:
                                coal.amount -= 1
                                player.health += 20
                                consume = True
                    else:
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_SPACE:
                                consume = False
                
                # Checks if the player health is 0 or smaller
                elif player.health <= 0:
                    game_over = True
                
                elif player.health > 100:
                    player.health = 100

        # Draws the background
        screen.blit(background, (0, 0))

        elapsed_time += time.time() - start_time
        start_time = time.time()
        # Calculate minutes and seconds
        minutes, seconds = divmod(elapsed_time, 60)

        # Format the time as a string
        time_string = f"{minutes:02.0f}:{seconds:05.2f}"

        # Render the text with the formatted time
        text = font.render(time_string, True, (0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (418, 5, 200, 50))
        pygame.draw.rect(screen, (255, 255, 255), (423, 10, 190, 40))
        screen.blit(text, (430, 10))
        
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
            if fireball.x < -50 or fireball.x > SCREEN_WIDTH:
                fireballs_left.remove(fireball)

        # Draw health bar
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_length, health_bar_height)) # Draws the botton layer of the health bar
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, int(health_bar_length * (player.health / 100)), health_bar_height)) # Draws the top layer of the health bar which scales with player health
        screen.blit(health_bar_text, health_bar_text_rect)

        pygame.draw.rect(screen, (0, 0, 0), (31, 560, 160, 70))
        pygame.draw.rect(screen, (255, 255, 255), (36, 565, 150, 60))
        screen.blit(coal_text, coal_text_rect)
        screen.blit(coal.img, (10, 540))
        

        # Game over screen
        if game_over:
            screen.blit(game_over_background, (0, 0)) # Blits the game over background
            screen.blit(game_over_text, game_over_text_rect) # Blits the game over text

        

        # Sets the frame rate
        clock.tick(60)        

        pygame.display.update()


main_menu()