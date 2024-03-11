import pygame
import sys
from player import Player
from food import Food
from enemy import Enemy
from settings import screen_width, screen_height, RED, BLACK

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простая игра на Pygame")
font = pygame.font.SysFont(None, 36)


def show_start_screen():
    screen.fill(BLACK)
    start_text = font.render("Press Space to start", True, (255, 255, 255))
    screen.blit(start_text, (screen_width / 2 - start_text.get_width() / 2, screen_height / 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def show_game_over_screen(score):
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


def run_game():
    player = Player()
    food = Food()
    enemy = Enemy()

    score = 0  # Начальный счёт
    running = True
    game_over = False

    while running:
        if game_over:
            show_game_over_screen(player.get_score())
            player = Player()  # Сброс игрока
            food = Food()  # Сброс еды
            enemy = Enemy()  # Сброс врага
            game_over = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(screen_width, screen_height)
        enemy.move_towards_player(player.x, player.y)

        if player.x < food.x + food.size and player.x + player.size > food.x and player.y < food.y + food.size and player.y + player.size > food.y:
            food = Food()
            player.increase_score()

        if player.x < enemy.x + enemy.size and player.x + player.size > enemy.x and player.y < enemy.y + enemy.size and player.y + player.size > enemy.y:
            game_over = True

        screen.fill(BLACK)
        player.draw(screen, RED)
        food.draw(screen)
        enemy.draw(screen)

        score_text = font.render(f"Score: {player.get_score()}", True, (255, 255, 255))
        screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

        pygame.display.flip()


if __name__ == '__main__':
    show_start_screen()  # Показать начальный экран
    while True:
        run_game()  # Запускать игру снова после завершения
