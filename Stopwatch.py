#Library comands, no command works without this
import pygame
import sys
import time

#initialies pygame
pygame.init()

#variabels of the stopwatch
width, height = 75, 40
window = pygame.display.set_mode((width, height))

#colors/ fonts
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(None, 25)


start_time = (None)
elapsed_time = 0
running = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    start_time = time.time()
                    running = True

    # Clear the screen
    window.fill(black)

    # Display the elapsed time
    if running:
        elapsed_time += time.time() - start_time
        start_time = time.time()
    text = font.render(f" {elapsed_time:.2f}", True, white)
    window.blit(text, (10, 10))

    pygame.display.update()
