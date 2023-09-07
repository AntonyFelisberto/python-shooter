import pygame
import random

ANCORA = 1500
ALTURA = 700

class Zomby(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("projeto\\images\\zombi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (0,600)
        self.aparicao = 200
        self.radius = 22
        self.rect.y = 600
        self.rect.x = random.randrange(self.aparicao - self.rect.width)
        self.zomby_speed_x = 1

    def update(self):
        self.rect.x += self.zomby_speed_x
        if self.rect.right > ANCORA:
            self.kill()
