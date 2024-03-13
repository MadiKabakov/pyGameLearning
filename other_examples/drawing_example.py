import pygame
import sys

pygame.init()

size = width, height = 800, 600  # Set window size
screen = pygame.display.set_mode(size)  # Create window
pygame.display.set_caption("Geometric Drawing")  # Set window title

black = 0, 0, 0  # Define black color
red = 255, 0, 0  # Define red color

running = True
while running:  # Main loop
    for event in pygame.event.get():  # Event handling
        if event.type == pygame.QUIT:  # Check for quit event
            running = False  # Exit loop if quit event is detected

    screen.fill(black)  # Fill window with black background

    # Draw a red rectangle at position (100, 100) with width 200 and height 150
    pygame.draw.rect(screen, red, pygame.Rect(100, 100, 200, 150))

    # Draw a red circle with center at (500, 300) and radius 50
    pygame.draw.circle(screen, red, (500, 300), 50)

    pygame.display.flip()  # Update display

pygame.quit()  # Quit Pygame
sys.exit()  # Exit script
