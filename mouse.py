# -*- coding: utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((600, 170), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('bg.jpg').convert()
plane = pygame.image.load('plane.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0,0))

    x, y = pygame.mouse.get_pos()

    x-= plane.get_width() / 2
    y-= plane.get_height() / 2

    screen.blit(plane, (x,y))

    pygame.display.update()