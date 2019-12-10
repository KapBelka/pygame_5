import pygame
import random
import os


SCREEN_SIZE = (600, 95)


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


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, *args):
        super().__init__(args)
        self.image = car_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction
        if not 0 <= self.rect.center[0] + self.direction * self.rect.width // 2 <= SCREEN_SIZE[0]:
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction = -self.direction


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
all_sprites = pygame.sprite.Group()
car_image = load_image('car2.png')
# переменные
fps = 30
car_speed = 5
running = True
# Создаём машину
car = Car(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, car_speed, all_sprites)
# Функции pygame
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.update()
