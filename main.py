import pygame
import sys
from models.player import Player
from models.food import Food
from models.enemy import Enemy
from settings import screen_width, screen_height, BLACK
from misc.utils import show_start_screen, show_game_over_screen

pygame.init()  # Инициализация Pygame
screen = pygame.display.set_mode((screen_width, screen_height))  # Создание экрана
pygame.display.set_caption("Простая игра на Pygame")  # Установка заголовка окна
font = pygame.font.SysFont(None, 36)  # Создание шрифта


def run_game():
    player = Player()  # Создание игрока
    food = Food()  # Создание еды
    enemy = Enemy()  # Создание врага

    score = 0  # Начальный счёт
    running = True  # Флаг для работы игры
    game_over = False  # Флаг для окончания игры

    while running:
        # Проверка на окончание игры
        if game_over:  # Если игра окончена, показать экран окончания игры
            show_game_over_screen(player.get_score(), screen, font)
            player = Player()  # Сброс игрока
            food = Food()  # Сброс еды
            enemy = Enemy()  # Сброс врага
            game_over = False
            continue

        # Обработка событий (нажатие клавиш, клики мыши и т.д.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False

        player.update(screen_width, screen_height)  # Обновление позиции игрока
        enemy.move_towards_player(player.x, player.y)  # Движение врага в сторону игрока

        # Проверка столкновения игрока с едой
        if player.x < food.x + food.size and player.x + player.size > food.x and player.y < food.y + food.size and player.y + player.size > food.y:
            food = Food()  # Создание новой еды
            player.increase_score()   # Увеличение счёта игрока

        # Проверка столкновения игрока с врагом (проигрыш)
        if player.x < enemy.x + enemy.size and player.x + player.size > enemy.x and player.y < enemy.y + enemy.size and player.y + player.size > enemy.y:
            game_over = True  # Игра окончена

        screen.fill(BLACK)  # Заливка экрана черным цветом
        player.draw(screen)  # Отрисовка игрока
        food.draw(screen)  # Отрисовка еды
        enemy.draw(screen)  # Отрисовка врага

        # Отрисовка счёта игрока
        score_text = font.render(f"Score: {player.get_score()}", True, (255, 255, 255))
        # Отрисовка счёта в правом верхнем углу
        screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

        # Обновление экрана
        pygame.display.flip()


if __name__ == '__main__':
    show_start_screen(screen, font)  # Показать начальный экран
    while True:
        run_game()  # Запускать игру снова после завершения
