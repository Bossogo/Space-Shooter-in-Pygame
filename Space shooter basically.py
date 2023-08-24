import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
EMBROIDERY_GREEN = (30, 130, 76)

# Set up the player
player_width = 50
player_height = 50
player = pygame.Rect((WIDTH - player_width) // 2, HEIGHT - player_height - 10, player_width, player_height)
player_speed = 9.5

# Set up the bullet
bullet_width = 10
bullet_height = 20
bullet_color = YELLOW
bullet_speed = 5
bullet_list = []

# Set up the ground
ground_width = WIDTH
ground_height = 50
ground_color = GREEN
ground = pygame.Rect(0, HEIGHT - ground_height, ground_width, ground_height)

# Set up the score_rect
score = 0
score_font = pygame.font.Font(None, 36)
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
score_color = BROWN
score_bg_color = EMBROIDERY_GREEN
score_rect = pygame.Rect(WIDTH - 150, 10, 140, 40)
score_display = score_text.get_rect()

def draw_score(score, score_display):
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, score_display)
    
# Set up the enemies
enemy_width = 50
enemy_height = 50
enemy_color = RED
enemy_list = []
enemy_speed = 0.1
enemy_spawn_rate = 18
enemy_spawn_timer = 0.2

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_c:
                bullet = pygame.Rect(player.centerx - bullet_width // 2, player.top - bullet_height, bullet_width, bullet_height)
                bullet_list.append(bullet)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(player_speed, 0)

    # Move the bullets and remove them when they go off-screen
    for bullet in bullet_list:
        bullet.move_ip(0, -bullet_speed)
        if bullet.top <= 0:
            bullet_list.remove(bullet)

    # Spawn enemies at random
    if enemy_spawn_timer <= 0:
        if random.randint(0, 100) <= enemy_spawn_rate:
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_y = random.randint(0, HEIGHT // 2)
            enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
            enemy_list.append(enemy)
        enemy_spawn_timer = 5
    else:
        enemy_spawn_timer -= 1

    # Move the enemies and remove them when they collide with the ground
    for enemy in enemy_list:
        enemy.move_ip(0, enemy_speed)
        if enemy.colliderect(ground):
            enemy_list.remove(enemy)

    # Remove bullets that hit enemies and increase the score
        # Remove bullets that hit enemies and increase the score
    for bullet in bullet_list:
        for enemy in enemy_list:
            if bullet.colliderect(enemy):
                bullet_list.remove(bullet)
                enemy_list.remove(enemy)
                score += 1

    # Draw the objects onto the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), ground)
    pygame.draw.rect(screen, (0, 0, 255), player)
    for bullet in bullet_list:
        pygame.draw.rect(screen, (255, 255, 0), bullet)
    for enemy in enemy_list:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (139, 69, 19), score_rect)
    pygame.draw.rect(screen, (0, 255, 0), score_display)
    draw_score(score, score_display)
    # Update the score display
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    score_display.center = (score_rect.centerx, score_rect.centery)

    # Check for collisions with the screen edge and remove bullets
    for bullet in bullet_list:
        if bullet.top < 0:
            bullet_list.remove(bullet)
        elif bullet.bottom > HEIGHT:
            bullet_list.remove(bullet)

    # Check for collisions with the screen edge and remove enemies
    for enemy in enemy_list:
        if enemy.colliderect(score_rect):
            enemy_list.remove(enemy)
        elif enemy.top > HEIGHT:
            enemy_list.remove(enemy)

    # Move the bullets and enemies
    for bullet in bullet_list:
        bullet.move_ip(0, -10)
    for enemy in enemy_list:
        enemy.move_ip(0, 5)

    # Control the frame rate
    clock.tick(60)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
