import pygame
import random
from settings import screen_width, screen_height, ROOT_FOLDER


class Enemy:
    def __init__(self):
        self.size = 100
        self.x = random.randint(0, screen_width - self.size)  # Учитываем размер, чтобы не выходить за экран
        self.y = random.randint(0, screen_height - self.size)
        self.speed = 0.1
        self.image = pygame.image.load(ROOT_FOLDER + '/assets/images/enemy.png')  # Загрузка изображения врага
        self.image = pygame.transform.scale(self.image, (self.size, self.size))  # Масштабирование изображения

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Отрисовка изображения вместо прямоугольника

    def move_towards_player(self, player_x, player_y):
        # Движение в сторону игрока
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed

        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed
