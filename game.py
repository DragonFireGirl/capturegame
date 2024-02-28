import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Capture the Flag")

# Load pirate ship background
background = pygame.image.load('pirate_ship_background.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define game parameters
player_size = 30
flag_size = 30
obstacle_size = 30
player_speed = 5

# Define player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Define flag position and movement direction
flag_x = random.randint(0, SCREEN_WIDTH - flag_size)
flag_y = random.randint(0, SCREEN_HEIGHT - flag_size)
flag_dx = random.choice([-1, 1]) * random.randint(2, 5)
flag_dy = random.choice([-1, 1]) * random.randint(2, 5)

# Define obstacle positions
num_obstacles = 20
obstacles = []
for _ in range(num_obstacles):
    obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_size)
    obstacle_y = random.randint(0, SCREEN_HEIGHT - obstacle_size)
    obstacles.append((obstacle_x, obstacle_y))

# Flag captured status
flag_captured = False

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += player_speed

    # Move the flag and bounce off screen edges
    flag_x += flag_dx
    flag_y += flag_dy
    if flag_x <= 0 or flag_x >= SCREEN_WIDTH - flag_size:
        flag_dx = -flag_dx
    if flag_y <= 0 or flag_y >= SCREEN_HEIGHT - flag_size:
        flag_dy = -flag_dy

    # Check for collision with flag
    if player_x < flag_x + flag_size and player_x + player_size > flag_x and player_y < flag_y + flag_size and player_y + player_size > flag_y:
        flag_captured = True

    # Clear the screen with background image
    screen.blit(background, (0, 0))

    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Draw the flag
    if not flag_captured:
        pygame.draw.rect(screen, GREEN, (flag_x, flag_y, flag_size, flag_size))
    else:
        # Flag text
        font = pygame.font.SysFont(None, 36)
        text = font.render('FLAG{C4TcH_M3_If_YoU_C4N}', True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        # Confetti
        for _ in range(100):
            confetti_x = random.randint(0, SCREEN_WIDTH)
            confetti_y = random.randint(0, SCREEN_HEIGHT)
            pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (confetti_x, confetti_y), 5)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
