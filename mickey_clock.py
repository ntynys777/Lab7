import pygame
import sys
import time
import math

pygame.init()

# Load images
clock_image = pygame.image.load("mickey_clock.png")  # Replace with actual path
hand_image = pygame.image.load("hand.png")  # Replace with actual path

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Center coordinates
cx, cy = WIDTH // 2, HEIGHT // 2

def rotate_hand(image, angle):
    """ Rotates an image around its center """
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=(cx, cy))
    return rotated_image, rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_image, (0, 0))

    # Get time
    t = time.localtime()
    minutes_angle = (t.tm_min % 60) * 6
    seconds_angle = (t.tm_sec % 60) * 6

    # Rotate hands
    minute_hand, min_rect = rotate_hand(hand_image, minutes_angle)
    second_hand, sec_rect = rotate_hand(hand_image, seconds_angle)

    screen.blit(minute_hand, min_rect)
    screen.blit(second_hand, sec_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
