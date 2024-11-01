import pygame
import os
from pygame.locals import *


pygame.init()
screen_width = 650
screen_height = 760
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = screen.get_rect()
pygame.display.set_caption("Flappy Bird")
FPS = 60



background = pygame.image.load(os.path.join('python','projects and problems', 'images', 'bg.png'))


class Bird():

    def __init__(self):
        self.bird = pygame.transform.scale(pygame.image.load(os.path.join('python','projects and problems', 'images', 'birdimage.png')),(180, 130))
        self.position = pygame.Rect(100, 200, 50, 5)
        self.velocity = 0
        self.gravity = 0.5

    def jump(self):
        self.velocity = -10

    def movement(self):
        if event.type == pygame.KEYDOWN:  
            if pygame.key == pygame.K_SPACE and self.position.y > 0:
                self.position.y -= self.velocity

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.position)







florinbird = Bird()

clock = pygame.time.Clock()

run = True
while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                florinbird.jump()
    
    florinbird.movement()

    screen.blit(background, (0, 0))
    screen.blit(florinbird.bird, florinbird.position)

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()