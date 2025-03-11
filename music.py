import pygame

# Initialize Pygame Mixer
pygame.init()
pygame.mixer.init()

# Load a single music file
music_file = "song1.mp3"  # Make sure this file is in the same folder as your script
pygame.mixer.music.load(music_file)

# Create Pygame window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Music Player")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play music
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:  # Stop music
                pygame.mixer.music.stop()

# Quit Pygame
pygame.quit()
