import pygame
import sys
from pygame.sprite import Sprite, Group

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвета
blue = (0, 0, 255)
red = (255, 0, 0)
background_color = (0, 0, 0)

# Скорость перемещения игрока
speed = 5


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf.fill(blue)
        self.rect = self.surf.get_rect(center=(screen_width // 4, screen_height // 2))

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_a]: self.rect.move_ip(-speed, 0)
        if pressed_keys[pygame.K_d]: self.rect.move_ip(speed, 0)
        if pressed_keys[pygame.K_w]: self.rect.move_ip(0, -speed)
        if pressed_keys[pygame.K_s]: self.rect.move_ip(0, speed)

        # Ограничение перемещения по экрану
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, screen_width)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, screen_height)


class Wall(Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 200))
        self.surf.fill(red)
        self.rect = self.surf.get_rect(center=(screen_width // 2, screen_height // 2))


# Создание игрока, стены и группы для стен
player = Player()
wall = Wall()

all_sprites = Group()
all_sprites.add(player)
all_sprites.add(wall)

walls = Group()
walls.add(wall)

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Проверка столкновений
    if pygame.sprite.spritecollideany(player, walls):
        # В случае столкновения, отменяем последнее движение
        if pressed_keys[pygame.K_a]: player.rect.move_ip(speed, 0)
        if pressed_keys[pygame.K_d]: player.rect.move_ip(-speed, 0)
        if pressed_keys[pygame.K_w]: player.rect.move_ip(0, speed)
        if pressed_keys[pygame.K_s]: player.rect.move_ip(0, -speed)

    # Отрисовка
    screen.fill(background_color)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
