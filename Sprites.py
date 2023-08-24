import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the sprite sheet image
sprite_sheet = pygame.image.load('victorylosssprites.png')

# Create a list of rectangles that represent each frame in the sprite sheet
frames = [
    pygame.Rect(0, 0, 32, 32),
    pygame.Rect(32, 0, 32, 32),
    pygame.Rect(64, 0, 32, 32),
    pygame.Rect(96, 0, 32, 32),
    # ...add more frames here...
]

# Create a sprite that uses the first frame in the sprite sheet
my_sprite = pygame.sprite.Sprite()
my_sprite.image = sprite_sheet.subsurface(frames[0])
my_sprite.rect = my_sprite.image.get_rect()

# Set up the game loop
clock = pygame.time.Clock()
frame_index = 0
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the sprite's image to the next frame in the animation
    frame_index = (frame_index + 1) % len(frames)
    my_sprite.image = sprite_sheet.subsurface(frames[frame_index])

    # Draw the sprite
    screen.fill((255, 255, 255))
    screen.blit(my_sprite.image, my_sprite.rect)
    pygame.display.flip()

    # Wait for the next frame
    pygame.time.wait(100)

    # Limit the frame rate
    clock.tick(60)
