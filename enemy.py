import pygame
import random
from settings import screen_width, screen_height


class Enemy:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.size = 30
        self.speed = 0.3
        self.color = (0, 255, 0)  # Красный цвет

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

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
