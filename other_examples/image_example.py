import pygame
import sys

pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Display")

# Load the image
image = pygame.image.load("example_image.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the image at position (0, 0)
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
