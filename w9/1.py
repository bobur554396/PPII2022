import pygame

# Initialize all configs
pygame.init()

# Creating main window
screen = pygame.display.set_mode((500, 500))
running = True

# Main loop
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic

    # Screen updating
    pygame.display.flip()




