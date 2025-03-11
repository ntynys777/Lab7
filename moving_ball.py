import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create window
pygame.display.set_caption("Moving Ball")  # Set window title

# Ball settings
ball_radius = 25  # Half of 50x50 size
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Start position (center of screen)
velocity = 20  # Move by 20 pixels per press

# Game loop
running = True
while running:
    pygame.time.delay(50)  # Small delay to control speed

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move ball but keep it within screen boundaries
    if keys[pygame.K_LEFT] and ball_x - velocity - ball_radius > 0:
        ball_x -= velocity
    if keys[pygame.K_RIGHT] and ball_x + velocity + ball_radius < WIDTH:
        ball_x += velocity
    if keys[pygame.K_UP] and ball_y - velocity - ball_radius > 0:
        ball_y -= velocity
    if keys[pygame.K_DOWN] and ball_y + velocity + ball_radius < HEIGHT:
        ball_y += velocity

    # Draw everything
    screen.fill((255, 255, 255))  # White background
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)  # Red ball
    pygame.display.update()  # Refresh display

# Quit Pygame properly
pygame.quit()
