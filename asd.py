import pygame
import os


SCREEN_SIZE = (600, 600)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image
    return image


pygame.init()
cursor_sprite = pygame.sprite.Group()
cursor_image = load_image('arrow.png')
cursor = pygame.sprite.Sprite(cursor_sprite)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
pygame.mouse.set_visible(False)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.topleft = event.pos
    screen.fill(pygame.Color('black'))
    if pygame.mouse.get_focused():
        cursor_sprite.draw(screen)
    pygame.display.update()
