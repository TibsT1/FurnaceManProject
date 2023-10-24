import pygame
import sys
import random
import time
from Player import Player
from Projectile import Projectile
from Enemies import Enemies
from Items import Items

# Initialising pygame
pygame.init() 

enemy_interval = 3000 # 3000 milliseconds == 1 second
enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_event, enemy_interval)

clock = pygame.time.Clock()

def loadimg(imgname):
    return pygame.image.load(imgname).convert_alpha()

# Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640

# Creates the surface using the variables assigned
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

# Creates a black background for the game over screen
game_over_background = pygame.Surface(screen.get_size())
game_over_background.fill((0, 0, 0))

# Loading images
background = pygame.image.load("Images/bg_spaceship_1.png").convert_alpha() # Assigns the Background Image
menu_background = pygame.image.load("Images/BrickBackground.jpg").convert_alpha() # Assigns the Menu Background Image
fireball_left_img = pygame.image.load("Images/Fireball_left.png").convert_alpha()
fireball_right_img = pygame.image.load("Images/Fireball_right.png").convert_alpha()
coal_img = pygame.image.load("Images/Coal Frame.png").convert_alpha()
ice_enemy_left = pygame.image.load("Images/IceEnemy_Left.png").convert_alpha()
ice_enemy_right = pygame.image.load("Images/IceEnemy_Right.png").convert_alpha()

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
    enemies_right = []
    enemies_left = []
    shoot = False #Variable to make sure only one fireball can be created per key press
    consume = False
    spawn = False
    font = pygame.font.Font(None, 64)
    start_time = time.time()
    elapsed_time = 0
    coal = Items(coal_img, 120, 120, 100)

    running = True
    game_over = False
    # Keeps the game running
    while running:
        enemy_left = Enemies(-20 , 380, ice_enemy_left, 100, 100, 10, 2)
        enemy_right = Enemies(1020, 380, ice_enemy_right, 100, 100, 10, 2)
        fireball_right = Projectile(500, 380, fireball_right_img, 100, 70, 10)
        fireball_left = Projectile(400, 380, fireball_left_img, 100, 70, 10)

        coal_font = pygame.font.Font(None, 64)
        coal_text = coal_font.render("x{CoalAmount}".format(CoalAmount=coal.amount), True, (0, 0, 0))
        coal_text_rect = coal_text.get_rect(center=(135, 595))

        for event in pygame.event.get():

            # Quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checks if the game is over
            if not game_over and 100 >= player.health > 0:
                # Right Arrow Key press creates fireball
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not shoot and len(fireballs_right) < 5:
                    fireballs_right.append(fireball_right)
                    shoot = True
                    player.health -= 5
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    shoot = False


                # Left Arrow Key press creates fireball
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not shoot and len(fireballs_left) < 5:
                    fireballs_left.append(fireball_left)
                    shoot = True
                    player.health -= 5
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    shoot = False
                
            # enemies from the left
            if len(enemies_left) < 3 and event.type == enemy_event:
                enemies_left.append(enemy_left)
                spawn = True
                
            # enemies from the right
            if len(enemies_right) < 3 and event.type == enemy_event:
                enemies_right.append(enemy_right)
                spawn = True

            if 100 > player.health > 0:
                # Space Key press consumes coal
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not consume and coal.amount > 0:
                    coal.amount -= 1
                    player.health += 20
                    consume = True
                elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
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

        # spawns the enemy from the left
        for enemy_left in enemies_left:
            enemy_left.draw(screen)
            enemy_left.x += enemy_left.vel
            
            # removes the enemy when it makes contact with player
            if enemy_left.x == (player.x - 50):
                player.health -= 5
                enemies_left.remove(enemy_left)
        
        # spawns the enemy from the right
        for enemy_right in enemies_right:
            enemy_right.draw(screen)
            enemy_right.x -= enemy_right.vel
            
            # removes the enemy when it makes contact with player
            if enemy_right.x == (player.x + 150):
                player.health -= 5
                enemies_right.remove(enemy_right)

        # Update and draw fireballs
        for fireball_right in fireballs_right:
            fireball_right.draw(screen)
            fireball_right.x += fireball_right.vel

            # Check for fireball position
            if fireball_right.x <= 0 or fireball_right.x >= SCREEN_WIDTH:
                fireballs_right.remove(fireball_right)

            if enemy_right.x <= fireball_right.x and spawn == True:
                enemies_right.remove(enemy_right)
                fireballs_right.remove(fireball_right)
                spawn = False

        # Update and draw fireballs
        for fireball_left in fireballs_left:
            fireball_left.draw(screen)
            fireball_left.x -= fireball_left.vel

            # Check for fireball position
            if fireball_left.x <= -10 or fireball_left.x >= SCREEN_WIDTH:
                fireballs_left.remove(fireball_left)
                
            if enemy_left.x >= fireball_left.x and spawn == True:
                enemies_left.remove(enemy_left)
                fireballs_left.remove(fireball_left)
                spawn = False

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