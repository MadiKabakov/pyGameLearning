import pygame
import sys

pygame.init()

# Set the window size
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Timer and Game Loop")

# Set colors
black = 0, 0, 0
red = 255, 0, 0

# Game loop setup
clock = pygame.time.Clock()
FPS = 60  # Frames per second

# Timer setup
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # Trigger event every second

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            print("Timer tick")  # Replace with your code for actions on each timer tick

    screen.fill(black)

    # Draw a red square at the center of the screen
    pygame.draw.rect(screen, red, pygame.Rect(width // 2 - 50, height // 2 - 50, 100, 100))

    pygame.display.flip()
    clock.tick(FPS)  # Control the frame rate

pygame.quit()
sys.exit()
