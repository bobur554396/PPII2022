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


class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface([20, 20])
    self.x = random.randint(0, WINDOW_WIDTH)
    self.y = random.randint(0, WINDOW_HEIGHT)
    self.rect = self.image.get_rect(center=(self.x, self.y))
    self.generate_change()
    self.generate_color()
    self.image.fill(self.color)

  def generate_color(self):
    self.color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))  # RGB

  def generate_change(self):
    self.x_change = random.randint(-2, 2)
    self.y_change = random.randint(-2, 2)
    while self.x_change == 0:
      self.x_change = random.randint(-2, 2)

    while self.y_change == 0:
      self.y_change = random.randint(-2, 2)

  def draw(self):
    pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

  def update(self):
    self.rect.x += self.x_change
    self.rect.y += self.y_change
    
    if self.rect.x > WINDOW_WIDTH or self.rect.x < 0:
      self.x_change *= -1
      self.generate_color()
    if self.rect.y > WINDOW_HEIGHT or self.rect.y < 0:
      self.y_change *= -1
      self.generate_color()


balls = pygame.sprite.Group()
balls.add(Ball(), Ball())

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        balls.add(Ball())

  screen.fill(WHITE)
  balls.draw(screen)
  
  balls.update()  

  pygame.display.update()
  clock.tick(FPS)
