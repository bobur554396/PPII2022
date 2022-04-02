import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))  # Surface
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 5

radius = 10
body = [[100, 100], [0, 0], [0, 0]]
'''
[[100, 100], [0, 0], [0, 0]]
[[115, 100], [100, 100], [0, 0]]
[[130, 100], [115, 100], [100, 100]]
[[145, 100], [130, 100], [115, 100]]
[[145, 115], [145, 100], [130, 100]]
'''

block = 15
dx, dy = 0, block
color = GREEN


def own_round(value, base=15):
  return base * round(value / 15)

# 15 * round(23/15)
def set_random_position():
  return own_round(random.randint(0, 500)), own_round(random.randint(0, 500))


food_x, food_y = set_random_position()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        dx = block
        dy = 0
      if event.key == pygame.K_LEFT:
        dx = -block
        dy = 0
      if event.key == pygame.K_UP:
        dx = 0
        dy = -block
      if event.key == pygame.K_DOWN:
        dx = 0
        dy = block
      if event.key == pygame.K_SPACE:
        body.append([0, 0])
        food_x, food_y = set_random_position()

  # Movement of the snake
  for i in range(len(body) - 1, 0, -1):
    body[i][0] = body[i - 1][0]
    body[i][1] = body[i - 1][1]
  
  # Change snake's head position
  body[0][0] += dx
  body[0][1] += dy
  
  if body[0][0] > 500:
    body[0][0] = 0


  screen.fill(BLACK)

  # Draw the food
  pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)

  # Draw snake
  for i, (x, y) in enumerate(body):
    color = RED if i == 0 else GREEN
    pygame.draw.circle(screen, color, (x, y), radius)


  
  pygame.display.flip()

  clock.tick(FPS)
