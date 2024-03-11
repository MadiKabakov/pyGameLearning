import pygame
import random
from settings import screen_width, screen_height

class Food:
    def __init__(self):
        self.size = 20
        self.x = random.randint(0, screen_width - self.size)
        self.y = random.randint(0, screen_height - self.size)
        self.color = (255, 255, 0)  # Желтый цвет

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
