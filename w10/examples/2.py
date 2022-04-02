import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))  # Surface
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

color = BLUE

x = 150
y = 20
dx, dy = 3, 3
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        color = GREEN if color == BLUE else BLUE
      if event.key == pygame.K_RIGHT:
        dx = 3
      if event.key == pygame.K_LEFT:
        dx = -3
      if event.key == pygame.K_UP:
        dy = -3
      if event.key == pygame.K_DOWN:
        dy = 3
  
  x += dx
  y += dy
  
  if x + 100 >= 500 or x < 0:
    dx *= -1
  
  if y + 100 >= 500 or y < 0:
    dy *= -1


  screen.fill(WHITE)

  pygame.draw.rect(screen, color, (x, y, 100, 100))

  pygame.display.flip()

  clock.tick(FPS)
