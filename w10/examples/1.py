import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
surf = pygame.Surface((100, 100))

running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60


surf.fill(RED)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        color = GREEN if color == BLUE else BLUE
  
  screen.fill(WHITE)
  
  screen.blit(surf, (10, 10))
  
  pygame.display.flip()

  clock.tick(FPS)
