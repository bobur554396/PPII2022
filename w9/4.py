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

clock = pygame.time.Clock()
# Frame per second
FPS = 60

image = pygame.image.load('img1.png')

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

    # Getting all pressed buttons
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    # Refresh the screen
    screen.fill(WHITE)

    # Drawing the objects
    # screen.blit(image, (x, y))
    pygame.draw.rect(screen, color, (x, y, 100, 100))

    # Screen updating
    pygame.display.flip()

    clock.tick(FPS)
