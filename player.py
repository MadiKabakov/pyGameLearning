import pygame


class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.size = 50
        self.speed = 1
        self.score = 0  # Инициализация счёта игрока

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

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
