import pygame

# Initialize all configs
pygame.init()

# Creating main window (Surface)
screen = pygame.display.set_mode((500, 500))
running = True

# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Main loop
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Refresh the screen
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (10, 10, 50, 50))

    pygame.draw.line(screen, RED, (70, 10), (120, 10))
    pygame.draw.line(screen, RED, (70, 10), (120, 50))

    pygame.draw.circle(screen, GREEN, (100, 100), 50, 2)

    pygame.draw.ellipse(screen, RED, (100, 200, 100, 200), 3)

    # Screen updating
    pygame.display.flip()
