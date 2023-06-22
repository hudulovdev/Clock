import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 400, 300
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the window surface
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Clock")

# Set up the font
font = pygame.font.Font(None, 80)

# Main game loop
def run_clock():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        window.fill(WHITE)

        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Render the time text
        time_surface = font.render(current_time, True, BLACK)
        time_rect = time_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(time_surface, time_rect)

        pygame.display.update()
        clock.tick(FPS)

# Set up the clock
clock = pygame.time.Clock()

# Run the clock
run_clock()
