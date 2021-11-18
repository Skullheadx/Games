from setup import *

dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
window = pygame.display.set_mode(dimensions)

pygame.display.set_caption("TEST - EXPERIMENTAL GAME BY SKULLHEAD & LBC")

previous_time = pygame.time.get_ticks()

running = True

while running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time

    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
