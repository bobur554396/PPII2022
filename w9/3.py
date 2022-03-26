import pygame

# Initialize all configs
pygame.init()

# Creating main window
screen = pygame.display.set_mode((500, 500))
running = True

# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

color = BLUE

x = 10
y = 10

# Main loop
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = GREEN if color == BLUE else BLUE
            if event.key == pygame.K_RIGHT:
                x = x + 10
            if event.key == pygame.K_DOWN:
                y = y + 10
            if event.key == pygame.K_UP:
                y = y - 10

    # Refresh the screen
    screen.fill(WHITE)

    # Drawing the objects
    pygame.draw.rect(screen, color, (x, y, 100, 100))

    # Screen updating
    pygame.display.flip()
