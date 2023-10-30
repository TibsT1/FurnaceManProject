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

enemy_interval = 1500 # 1000 milliseconds == 1 seconds
enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_event, enemy_interval)

clock = pygame.time.Clock()

# Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 640

# Creates the surface using the variables assigned
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

# Loads the sound effect for the fireball
fireball_sound_effect = pygame.mixer.Sound("Sounds/fireball_sound.wav")

# Creates a black background for the game over screen
game_over_background = pygame.Surface(screen.get_size())
game_over_background.fill((0, 0, 0))

# Loading images
background = pygame.image.load("Images/bg_spaceship_1.png").convert_alpha() # Assigns the Background Image
menu_background = pygame.image.load("Images/BrickBackground.jpg").convert_alpha() # Assigns the Menu Background Image
fireball_left_img = pygame.image.load("Images/Fireball_left.png").convert_alpha()
fireball_right_img = pygame.image.load("Images/Fireball_right.png").convert_alpha()
coal_img = pygame.image.load("Images/Coal Frame.png").convert_alpha()
ice_enemy_left_img = pygame.image.load("Images/IceEnemy_Left.png").convert_alpha()
ice_enemy_right_img = pygame.image.load("Images/IceEnemy_Right.png").convert_alpha()
log_enemy_right_img = pygame.image.load("Images/log_enemy_right.png").convert_alpha()
log_enemy_left_img = pygame.image.load("Images/log_enemy_left.png").convert_alpha()
left_arrow_key = pygame.image.load("Images/Left_Arrow.png")
left_arrow_key_big = pygame.transform.rotozoom(left_arrow_key, 0, 1.5)
right_arrow_key = pygame.image.load("Images/Right_Arrow.png")
right_arrow_key_big = pygame.transform.rotozoom(right_arrow_key, 0, 1.5)


# Creates the player
player = Player(400, 240, pygame.image.load("Images/FurnaceMan.png"), 176.2, 275, 100)

# Changes the name of the window
pygame.display.set_caption("Fornax Ignea")

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
main_menu_text = main_menu_font.render("Fornax Ignea", True, (255, 255, 255))
main_menu_text_rect = main_menu_text.get_rect(center=(SCREEN_WIDTH // 2, 100))

# Controls
controls_font = pygame.font.Font(None, 64)
controls_text = controls_font.render("Controls", True, (255, 255, 255))
controls_text_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, 100))

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

# Create the Controls Button
controls_button = pygame.Rect(400, 300, 200, 50)

# Create the Controls Button Text
controls_button_font = pygame.font.Font(None, 64)
controls_button_text = controls_button_font.render("Controls", True, (255, 255, 255))
controls_button_text_rect = controls_button_text.get_rect(center=(500, 325))

# Loads the background music and makes it loop forever
def background_music():
    pygame.mixer.music.load("Sounds/background_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

# Function for the main menu
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

        # Check if the Controls Button is clicked 
        if controls_button.collidepoint((mouse_x, mouse_y)):
            if click: # If the Controls Button is clicked, run the Controls function
                controls_menu()
                break


        # Draws the Play Button Rect and Text
        pygame.draw.rect(screen, (0, 0, 0), play_button)
        screen.blit(play_button_text, play_button_text_rect)

        # Draws the Controls Button Rect and Text
        pygame.draw.rect(screen, (0, 0, 0), controls_button)
        screen.blit(controls_button_text, controls_button_text_rect)

        # Draws the Quit Button Rect and Text
        pygame.draw.rect(screen, (0, 0, 0), quit_button)
        screen.blit(quit_button_text, quit_button_text_rect)

        pygame.display.update()
                    
def controls_menu():
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        screen.blit(menu_background, (0,0))
        screen.blit(controls_text, controls_text_rect)

        left_arrow_font = pygame.font.Font(None, 54)
        left_arrow_text = left_arrow_font.render("Shoot fireball to the left.", True, (255, 255, 255))
        left_arrow_text_rect = left_arrow_text.get_rect(center=(460, 207))

        right_arrow_font = pygame.font.Font(None, 54)
        right_arrow_text = right_arrow_font.render("Shoot fireball to the right.", True, (255, 255, 255))
        right_arrow_text_rect = right_arrow_text.get_rect(center=(475, 310))

        screen.blit(left_arrow_text, left_arrow_text_rect)
        screen.blit(left_arrow_key_big, (180, 182))

        screen.blit(right_arrow_text, right_arrow_text_rect)
        screen.blit(right_arrow_key_big, (180, 282))

        pygame.display.update()
                
# Function for the main game
def game():
    # Arrays to hold fireballs
    fireballs_right = []
    fireballs_left = []

    # Arrays to hold enemies
    ice_enemies_right_list = []
    ice_enemies_left_list = []
    log_enemies_left_list = []
    log_enemies_right_list = []

    shoot = False #Variable to make sure only one fireball can be created per key press

    consume = False #Variable to make sure only one coal can be consumed per key press

    spawn_left = False #Variable to check if the enemy has spawned on the left side
    spawn_right = False #Variable to check if the enemy has spawned on the right side

    # Timer font, start time and elapsed time
    font = pygame.font.Font(None, 64)
    start_time = time.time()
    elapsed_time = 0

    # Declaring the Coal item
    coal = Items(coal_img, 120, 120, 0)

    # Setting the score to 0 when the game starts
    score = 0

    # Starting the background music
    background_music()

    random_side = True
    random_enemy = True
    running = True
    game_over = False
    # Keeps the game running
    while running:
        log_enemy_left = Enemies(-110 , 380, log_enemy_left_img, 150, 150, 20, 5)
        log_enemy_right = Enemies(1020, 380, log_enemy_right_img, 150, 150, 20, 5)
        ice_enemy_left = Enemies(-110 , 400, ice_enemy_left_img, 120, 120, 10, 5)
        ice_enemy_right = Enemies(1020, 400, ice_enemy_right_img, 120, 120, 10, 5)
        fireball_right = Projectile(500, 380, fireball_right_img, 100, 70, 10)
        fireball_left = Projectile(400, 380, fireball_left_img, 100, 70, 10)

        while random_side == True:
            side = random.randint(1, 2)
            break

        while random_enemy == True:
            enemy_type = random.randint(1, 2)
            break

        coal_font = pygame.font.Font(None, 64)
        coal_text = coal_font.render("x{CoalAmount}".format(CoalAmount=coal.amount), True, (0, 0, 0))
        coal_text_rect = coal_text.get_rect(center=(135, 595))

        score_font = pygame.font.Font(None, 64)
        score_text = score_font.render("{Score}".format(Score=score), True, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(970, 30))

        for event in pygame.event.get():

            # Quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Checks if the game is over
            if not game_over and 100 >= player.health > 0:
                ice_enemy_left.health == 10
                log_enemy_left.health == 20
                ice_enemy_right.health == 10
                log_enemy_right.health == 20
                # Right Arrow Key press creates fireball
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not shoot and len(fireballs_right) < 5 and game_over == False:
                    fireballs_right.append(fireball_right)
                    shoot = True
                    player.health -= 5
                    pygame.mixer.Sound.play(fireball_sound_effect)
                elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    shoot = False


                # Left Arrow Key press creates fireball
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not shoot and len(fireballs_left) < 5 and game_over == False:
                    fireballs_left.append(fireball_left)
                    shoot = True
                    player.health -= 5
                    pygame.mixer.Sound.play(fireball_sound_effect)
                elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    shoot = False
                
            # enemies from the left
            if len(ice_enemies_left_list) < 3 and event.type == enemy_event and game_over == False and side == 1 and enemy_type == 1:
                ice_enemies_left_list.append(ice_enemy_left)
                spawn_left = True
                
            # enemies from the right
            if len(ice_enemies_right_list) < 3 and event.type == enemy_event and game_over == False and side == 2 and enemy_type == 1:
                ice_enemies_right_list.append(ice_enemy_right)
                spawn_right = True

            # enemies from the left
            if len(log_enemies_left_list) < 3 and event.type == enemy_event and game_over == False and side == 1 and enemy_type == 2:
                log_enemies_left_list.append(log_enemy_left)
                spawn_left = True
                
            # enemies from the right
            if len(log_enemies_right_list) < 3 and event.type == enemy_event and game_over == False and side == 2 and enemy_type == 2:
                log_enemies_right_list.append(log_enemy_right)
                spawn_right = True

            if 100 > player.health > 0:
                # Space Key press consumes coal
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not consume and coal.amount > 0 and game_over == False:
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
        for ice_enemy_left in ice_enemies_left_list:
            ice_enemy_left.draw(screen)
            ice_enemy_left.x += ice_enemy_left.vel
            
            # removes the enemy when it makes contact with player
            if ice_enemy_left.x == player.x and spawn_left == True and game_over == False:
                player.health -= 5
                ice_enemy_left.vel == 0
                ice_enemies_left_list.remove(ice_enemy_left)
                spawn_left = False
        
        # spawns the enemy from the right
        for ice_enemy_right in ice_enemies_right_list:
            ice_enemy_right.draw(screen)
            ice_enemy_right.x -= ice_enemy_right.vel
            
            # removes the enemy when it makes contact with player
            if ice_enemy_right.x == (player.x + 150) and spawn_right == True and game_over == False:
                player.health -= 5
                ice_enemy_right.vel == 0
                ice_enemies_right_list.remove(ice_enemy_right)
                spawn_right = False

        # spawns the enemy from the left
        for log_enemy_left in log_enemies_left_list:
            log_enemy_left.draw(screen)
            log_enemy_left.x += log_enemy_left.vel
            
            # removes the enemy when it makes contact with player
            if log_enemy_left.x == player.x and spawn_left == True and game_over == False:
                player.health -= 5
                log_enemy_left.vel == 0
                log_enemies_left_list.remove(log_enemy_left)
                spawn_left = False
        
        # spawns the enemy from the right
        for log_enemy_right in log_enemies_right_list:
            log_enemy_right.draw(screen)
            log_enemy_right.x -= log_enemy_right.vel
            
            # removes the enemy when it makes contact with player
            if log_enemy_right.x == (player.x + 150) and spawn_right == True and game_over == False:
                player.health -= 5
                log_enemy_right.vel == 0
                log_enemies_right_list.remove(log_enemy_right)
                spawn_right = False

        # Update and draw fireballs
        for fireball_right in fireballs_right:
            fireball_right.draw(screen)
            fireball_right.x += fireball_right.vel

            # Check for fireball position
            if fireball_right.x <= 0 or fireball_right.x >= SCREEN_WIDTH and game_over == False:
                fireballs_right.remove(fireball_right)

            if (ice_enemy_right.x - 60) <= fireball_right.x and spawn_right == True and game_over == False:
                ice_enemies_right_list.remove(ice_enemy_right)
                fireballs_right.remove(fireball_right)
                spawn_right = False
                score += 10

            if (log_enemy_right.x - 60) <= fireball_right.x and spawn_right == True and game_over == False:
                log_enemies_right_list.remove(log_enemy_right)
                log_enemy_right.health -= fireball_right.dmg
                fireballs_right.remove(fireball_right)
                score += 10
                coal.amount += 1
                spawn_right = False

        # Update and draw fireballs
        for fireball_left in fireballs_left:
            fireball_left.draw(screen)
            fireball_left.x -= fireball_left.vel

            # Check for fireball position
            if fireball_left.x <= -70 or fireball_left.x >= SCREEN_WIDTH and game_over == False:
                fireballs_left.remove(fireball_left)
                
            if (ice_enemy_left.x + 100) >= fireball_left.x and spawn_left == True and game_over == False:
                ice_enemies_left_list.remove(ice_enemy_left)
                fireballs_left.remove(fireball_left)
                spawn_left = False
                score += 10

            if (log_enemy_left.x + 100) >= fireball_left.x and spawn_left == True and game_over == False:
                log_enemies_left_list.remove(log_enemy_left)
                log_enemy_left.health -= fireball_left.dmg
                fireballs_left.remove(fireball_left)
                score += 10
                coal.amount += 1
                spawn_left = False

        if score >= 100:
            score_text_rect = score_text.get_rect(center=(960, 30))

        # Draw health bar
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_length, health_bar_height)) # Draws the botton layer of the health bar
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, int(health_bar_length * (player.health / 100)), health_bar_height)) # Draws the top layer of the health bar which scales with player health
        screen.blit(health_bar_text, health_bar_text_rect)

        pygame.draw.rect(screen, (0, 0, 0), (31, 560, 160, 70))
        pygame.draw.rect(screen, (255, 255, 255), (36, 565, 150, 60))
        screen.blit(coal_text, coal_text_rect)
        screen.blit(coal.img, (10, 540))

        screen.blit(score_text, score_text_rect)

        if elapsed_time >= 30:
            ice_enemy_left.vel = 10
            log_enemy_left.vel = 10
            ice_enemy_right.vel = 10
            log_enemy_right.vel = 10

        if elapsed_time >= 60:
            ice_enemy_left.vel = 15
            log_enemy_left.vel = 15
            ice_enemy_right.vel = 15
            log_enemy_right.vel = 15

        if elapsed_time >= 90:
            ice_enemy_left.vel = 20
            log_enemy_left.vel = 20
            ice_enemy_right.vel = 20
            log_enemy_right.vel = 20
        

        # Game over screen
        if game_over:
            screen.blit(game_over_background, (0, 0)) # Blits the game over background
            screen.blit(game_over_text, game_over_text_rect) # Blits the game over text
            screen.blit(score_text, (460, 400))
            pygame.mixer.music.stop()

        

        # Sets the frame rate
        clock.tick(30)        

        pygame.display.update()


main_menu()