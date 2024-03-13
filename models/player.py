import pygame
from settings import ROOT_FOLDER


class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.size = 100  # Можно использовать для масштабирования, если нужно
        self.speed = 1
        self.score = 0  # Инициализация счёта игрока
        self.image = pygame.image.load(ROOT_FOLDER + '/assets/images/player.png')  # Загрузка изображения
        self.image = pygame.transform.scale(self.image, (self.size, self.size))  # Масштабирование изображения до нужного размера

    def update(self, screen_width, screen_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

        # Проверка границ и обновление позиции
        if self.x < 0 - self.size:
            self.x = screen_width
        elif self.x > screen_width:
            self.x = 0 - self.size
        if self.y < 0 - self.size:
            self.y = screen_height
        elif self.y > screen_height:
            self.y = 0 - self.size

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Отрисовка изображения вместо прямоугольника

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
