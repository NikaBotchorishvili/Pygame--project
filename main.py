import pygame
from pygame.locals import (
    K_w, K_a, K_s, K_d,
    K_UP, K_LEFT, K_DOWN, K_RIGHT,
    KEYDOWN, K_ESCAPE, QUIT
)

pygame.init()
pygame.display.set_caption('The most amazing game!')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True

while running:
    posX = 100
    posY = SCREEN_HEIGHT / 2
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill([255,255,255])

    surf = pygame.Surface([50, 50])

    surf.fill([0,0,0])

    rect = surf.get_rect()

    screen.blit(surf, [(SCREEN_WIDTH-surf.get_width()) / 2, (SCREEN_HEIGHT-surf.get_height()) / 2])
    pygame.display.flip()

pygame.quit()