import pygame
import random
import os


SCREEN_SIZE = (500, 500)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, *args):
        super().__init__(args)
        self.image = bomb_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.is_boom = False

    def boom(self):
        pos = self.rect.center
        self.image = boom_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.is_boom = True

    def get_click(self, mouse_x, mouse_y):
        if (self.rect.left <= mouse_x <= self.rect.right and
                self.rect.top <= mouse_y <= self.rect.bottom and not self.is_boom):
            self.boom()
            return True
        return False


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
all_sprites = pygame.sprite.Group()
bombs_sprites = pygame.sprite.Group()
bomb_image = load_image('bomb2.png')
boom_image = load_image('boom.png')
# переменные
fps = 30
count_bomb = 10  # 12 максимум)))
running = True
# Создание бомбочек
bombs = []
for i in range(count_bomb):
    width, height = bomb_size = bomb_image.get_rect().size
    x, y = random.randrange(SCREEN_SIZE[0] - width), random.randrange(SCREEN_SIZE[1] - height)
    bomb = Bomb(x, y)
    while pygame.sprite.spritecollide(bomb, bombs_sprites, False):
        x, y = random.randrange(SCREEN_SIZE[0] - width), random.randrange(SCREEN_SIZE[1] - height)
        bomb = Bomb(x, y)
    bombs_sprites.add(bomb)
    bombs.append(bomb)
# Функции pygame
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                for bomb in bombs:
                    bomb.get_click(*event.pos)
    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    bombs_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.update()
