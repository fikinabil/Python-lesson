import pygame
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images and sounds
# Load player character
player_image = pygame.image.load("images/mario.png")
player_rect = player_image.get_rect()
player_rect.topleft = (100, SCREEN_HEIGHT - player_rect.height)

# Load background
background_image = pygame.image.load("images/background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario - DEV")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    # Draw everything
    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, player_rect.topleft)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
