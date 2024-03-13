import pygame
import sys

pygame.init()  # Initialize Pygame

size = width, height = 640, 480  # Window size
screen = pygame.display.set_mode(size)  # Create window
pygame.display.set_caption("Basic Pygame Window")  # Window title

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit condition
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fill screen with black
    pygame.display.flip()  # Update display
