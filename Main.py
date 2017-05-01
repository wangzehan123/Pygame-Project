import pygame
import random
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.active = False
    def move(self):
        if self.active:
            self.y -= 3
        if self.y < 0:
            self.active = False
    def restart(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        self.active = True

class Enemy:
    def restart(self):
        self.x = random.randint(50, 400)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png').convert_alpha()
    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()

pygame.init()
screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption("Attacking Jet!")
background = pygame.image.load('background2.jpg').convert()
plane = pygame.image.load('main character.png').convert()

bullets = []
for i in range(5):
    bullets.append(Bullet())
count_b = len(bullets)
index_b = 0
interval_b = 0
enemy = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    interval_b -= 1
    if interval_b < 0:
        bullets[index_b].restart()
        interval_b = 100
        index_b = (index_b + 1) % count_b
    for b in bullets:
        if b.active:
            b.move()
            screen.blit(b.image, (b.x, b.y))
            
    enemy.move()
    screen.blit(enemy.image, (enemy.x, enemy.y))
    x,y = pygame.mouse.get_pos()
    x-=plane.get_width()/2
    y-= plane.get_height()/2
    screen.blit(plane,(x,y))
    pygame.display.update()
