import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True

# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(0)

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
        if event.type == SONG_END:
            print("the song ended!")

    screen.fill(WHITE)

    pygame.display.flip()
