import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()
WIDHT = 700
HIGHT = 700

a = randint(0, 255)
print(a)
FPS = 30
screen = pygame.display.set_mode((WIDHT, HIGHT))
screen.fill((randint(0, 255), 122, 244))
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    pygame.display.update()
