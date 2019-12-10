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
all_sprites = pygame.sprite.Group()
gameover_image = load_image('gameover.png')
# переменные
fps = 30
gameover_speed = 200
running = True
is_gameover = False
# Создаём событие gameover
GAMEOVER_EVENT_ID = pygame.USEREVENT + 1
gameover_event = pygame.event.Event(GAMEOVER_EVENT_ID, {})
pygame.event.post(gameover_event)  # Добавляем наше событие в очередь
# Функции pygame
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GAMEOVER_EVENT_ID:  # Обрабатывем наше собыите
            gameover_screen = gameover()  # Создаём спрайт с изображением gameover
            is_gameover = True  # Показываем что игра окончена
    screen.fill(pygame.Color('blue'))
    if is_gameover:
        gameover_screen.rect.x += gameover_speed / fps  # Двигаем спрайт gameover
        if gameover_screen.rect.right >= SCREEN_SIZE[0]:  # Как мы доходим до края экрана
            gameover_screen.rect.topleft = (0, 0)  # Поставить спрайт в начале координат
            is_gameover = False  # Отключаем этот блок кода
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.update()
