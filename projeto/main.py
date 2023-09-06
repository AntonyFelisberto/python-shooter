import pygame

ANCORA = 1500
ALTO = 700
FPS = 60

class Inicio():
    pygame.init()

tela = pygame.display.set_mode((ANCORA,ALTO))

fundo = pygame.transform.scale(pygame.image.load(""))

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

            pygame.display.flip()