import pygame

ANCORA = 1000
ALTO = 600
BRANCO = (255,255,255)


class Disparo(pygame.sprite.Sprite):
    def __init__(self,x ,y) :
        super().__init__()
        self.image = pygame.image.load("projeto\\images\\bala.png").convert()
        self.image.set_colorkey(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y


    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.kill()