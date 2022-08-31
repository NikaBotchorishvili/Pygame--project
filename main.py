import time

import pygame,pygame.freetype
import random
from pygame.locals import (
    K_w, K_a, K_s, K_d,
    K_UP, K_LEFT, K_DOWN, K_RIGHT,
    KEYDOWN, K_ESCAPE, QUIT,
    RLEACCEL
)

pygame.init()

pygame.font.init()
GAME_FONT = pygame.freetype.Font("AlfaSlabOne-Regular.ttf", 100)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.speed = 1
        self.surf = pygame.Surface([60, 20])
        self.surf.fill([0, 255, 0])
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        # PLAYER CONTROLLER
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            pygame.transform.rotate(self.surf, 90)

        if pressed_keys[K_s] or pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)


        #   MAKING SURE THAT PLAYER DOESN'T GO OUT OF BOUNDS
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface([50, 40])
        self.surf.fill([255, 0, 0])
        self.rect = self.surf.get_rect(
            center=[
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            ]
        )
        self.speed = random.uniform(0.7, 1.1)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.kill()

pygame.display.set_caption('The most amazing game!')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

running = True

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
while running:
    posX = 100
    posY = SCREEN_HEIGHT / 2
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemies)

    pressedKeys = pygame.key.get_pressed()

    player.update(pressedKeys)
    enemies.update()

    screen.fill([0, 0, 0])

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        text_surface, rect = GAME_FONT.render("Game Over!",[255, 255, 255])

        screen.blit(text_surface, [(SCREEN_WIDTH / 7) , (SCREEN_HEIGHT / 2.5)])
        pygame.display.flip()
        time.sleep(5)
        running = False
    pygame.display.flip()
pygame.quit()