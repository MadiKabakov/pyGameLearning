import pygame
import sys

pygame.init()

# Load music and sound effects
pygame.mixer.music.load("background_music.mp3")
sound_effect = pygame.mixer.Sound("sound_effect.wav")

# Set up the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sound Demo")

# Play the background music
pygame.mixer.music.play(-1)  # -1 indicates looping indefinitely

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Play the sound effect when the space key is pressed
                sound_effect.play()

    pygame.display.flip()

pygame.quit()
sys.exit()
