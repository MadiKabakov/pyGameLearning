import pygame
import sys

from settings import screen_width, screen_height, RED, BLACK


# Функция для отображения стартового экрана
def show_start_screen(screen, font):
    screen.fill(BLACK)  # Заливка экрана черным цветом
    start_text = font.render("Press Space to start", True, (255, 255, 255))  # Создание текста
    screen.blit(start_text, (screen_width / 2 - start_text.get_width() / 2, screen_height / 2))  # Отрисовка текста
    pygame.display.flip()  # Обновление экрана
    waiting = True  # Флаг для ожидания нажатия клавиши
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если нажата кнопка закрытия окна
                pygame.quit()  # Закрыть окно
                sys.exit()  # Завершить программу
            if event.type == pygame.KEYDOWN:  # Если нажата клавиша
                if event.key == pygame.K_SPACE:  # Если нажата клавиша пробел
                    waiting = False  # Завершить ожидание


# Функция для отображения экрана с сообщением о проигрыше
def show_game_over_screen(score, screen, font):
    screen.fill(BLACK)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    restart_text = font.render("Press R to restart", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2 - 30))
    screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, screen_height / 2))
    screen.blit(restart_text, (screen_width / 2 - restart_text.get_width() / 2, screen_height / 2 + restart_text.get_height() / 2 + 30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False