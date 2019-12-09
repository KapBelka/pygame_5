import pygame
import os


SCREEN_SIZE = (300, 300)


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


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, *groups):
        super().__init__(groups)
        self.image = hero_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed
        self.action = None

    def update(self):
        if self.action:
            if self.action == pygame.K_UP:
                self.rect.y -= self.speed
            if self.action == pygame.K_LEFT:
                self.rect.x -= self.speed
            if self.action == pygame.K_DOWN:
                self.rect.y += self.speed
            if self.action == pygame.K_RIGHT:
                self.rect.x += self.speed


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
fps = 30
hero_image = load_image('creature.png', -1)
all_sprites = pygame.sprite.Group()
hero = Hero(0, 0, 10, all_sprites)
running = True
pygame.mouse.set_visible(False)
pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            hero.action = event.key
        elif event.type == pygame.KEYUP:
            if event.key == hero.action:
                hero.action = None
    all_sprites.update()
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    pygame.time.delay(fps)
    pygame.display.update()
