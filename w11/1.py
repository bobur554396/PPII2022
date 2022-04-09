import pygame
import random

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Surface
running = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

class Ball:
  def __init__(self):
    self.size = random.randint(5, 30)
    self.x = random.randint(0, WINDOW_WIDTH)
    self.y = random.randint(0, WINDOW_HEIGHT)
    self.generate_change()
    self.generate_color()

  def generate_color(self):
    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # RGB
  
  def generate_change(self):
    self.x_change = random.randint(-2, 2)
    self.y_change = random.randint(-2, 2)
    while self.x_change == 0:
      self.x_change = random.randint(-2, 2)
    
    while self.y_change == 0:
      self.y_change = random.randint(-2, 2)
    
  def draw(self):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)  

  def move(self):
    self.x += self.x_change
    self.y += self.y_change
    
    if self.x > WINDOW_WIDTH or self.x < 0:
      self.x_change *= -1
      self.generate_color()
    if self.y > WINDOW_HEIGHT or self.y < 0:
      self.y_change *= -1
      self.generate_color()


balls = [Ball(), Ball()]

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        balls.append(Ball())
  
  for ball in balls:
    ball.move()
  
  screen.fill(WHITE)
  for ball in balls:
    ball.draw()
  
  pygame.display.update()
  clock.tick(FPS)
