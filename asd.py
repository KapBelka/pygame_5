import pygame
import os


SCREEN_SIZE = (600, 300)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def gameover():
    gameover_screen = pygame.sprite.Sprite(all_sprites)
    gameover_screen.image = gameover_image
    gameover_screen.rect = gameover_screen.image.get_rect()
    gameover_screen.rect.left = -600
    return gameover_screen


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
fps = 30
gameover_image = load_image('gameover.png')
all_sprites = pygame.sprite.Group()
GAMEOVER_EVENT = 30
gameover_speed = 200
pygame.time.set_timer(GAMEOVER_EVENT, 5000)
running = True
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
gameover_screen = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GAMEOVER_EVENT:
            gameover_screen = gameover()
    screen.fill(pygame.Color('blue'))
    if gameover_screen:
        gameover_screen.rect.x += gameover_speed / fps
        if gameover_screen.rect.right >= 600:
            gameover_screen = None
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.update()
