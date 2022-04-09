import pygame
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Surface
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)

BLOCK_SIZE = 20

clock = pygame.time.Clock()
FPS = 3


def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)


class Wall:
  def __init__(self):
    self.body = []
    self.load_wall()
  
  def load_wall(self, level=1):
    with open(f'level{level}.txt', 'r') as f:
      wall_body = f.readlines()
    
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
  
  def draw(self):
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    
class Food:
  def __init__(self):
      self.generate_random_pos()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)
  
  def generate_random_pos(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))
  
  def draw(self):
    pygame.draw.rect(screen, BLUE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


class Snake:
  def __init__(self):
      self.body = [[10, 10], [11, 10],]
      self.dx = 1
      self.dy = 0
  
  def draw(self):
    for i, (x, y) in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy
    

snake = Snake()
food = Food()
wall = Wall()
score = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        snake.dx = 1
        snake.dy = 0
      if event.key == pygame.K_LEFT:
        snake.dx = -1
        snake.dy = 0
      if event.key == pygame.K_UP:
        snake.dx = 0
        snake.dy = -1
      if event.key == pygame.K_DOWN:
        snake.dx = 0
        snake.dy = 1
      if event.key == pygame.K_SPACE:
        pass        
  
  snake.move()    
    
  screen.fill(BLACK)
  
  draw_grid()
  snake.draw()
  food.draw()
  wall.draw()
  
  if snake.body[0][0] * BLOCK_SIZE == food.x and snake.body[0][1] * BLOCK_SIZE == food.y:
    snake.body.append([0, 0])
    food.generate_random_pos()
    score += 1
    if score == 4:
      wall.load_wall(level=2)

  
  font = pygame.font.Font(None, 30)
  text = font.render(f'Score: {score}', True, (255, 0, 0))
  
  screen.blit(text, (20, 20))
  
  pygame.display.update()
  clock.tick(FPS)
