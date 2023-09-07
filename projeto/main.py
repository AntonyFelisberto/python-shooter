import pygame
from zombi import Zomby
from disparo import Disparo

ANCORA = 1500
ALTO = 700
FPS = 60
BLACK = (0,0,0)
PURPLE = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

console = pygame.font.match_font("console")
time = pygame.font.match_font("time")
arial = pygame.font.match_font("arial")
contador = pygame.font.match_font("contador")

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("projeto\\images\\player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (ANCORA,650)
        self.rect.y = 600
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.cadencia = 300
        self.ultimate = pygame.time.get_ticks()

    def update(self):
        self.velocidade_x = 0

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:
            self.velocidade_x = -2
        if teclas[pygame.K_d]:
            self.velocidade_x = 2
        if teclas[pygame.K_SPACE]:
            tempo = pygame.time.get_ticks()
            if tempo - self.ultimate > self.cadencia:
                self.fire()
                self.ultimate = tempo

        self.rect.x += self.velocidade_x

        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.right > ANCORA:
            self.rect.right = ANCORA

    def fire(self):
        fires = Disparo(self.rect.centerx -20,self.rect.centery - 19)
        disparos.add(fires)

def Texto(tela,fonte,text,cor,dimensoes,x,y):
    tipo_letra = pygame.font.Font(fonte,dimensoes)
    superficie = tipo_letra.render(text,True,cor)
    retangulo = superficie.get_rect()
    retangulo.center = (x,y)
    tela.blit(superficie,retangulo)

class Inicio():
    pygame.init()

tela = pygame.display.set_mode((ANCORA,ALTO))

fundo = pygame.transform.scale(pygame.image.load("projeto\\images\\fondo.jpg").convert(),(1500,700))

pygame.display.set_caption("Shooter Fire")

time = pygame.time.Clock()

pontuacao = 5

zombies = pygame.sprite.Group()
jogador = pygame.sprite.Group()
disparos = pygame.sprite.Group()

jogadores = Jogador()
jogador.add(jogadores)

game_over = False

while game_over == False:

    time.tick(FPS)
    tela.blit(fundo,(0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

    colisao_bala = pygame.sprite.groupcollide(zombies,disparos,True,True)
    colisao_zumbi = pygame.sprite.groupcollide(zombies,jogador,False,False)

    Texto(tela,arial,str(pontuacao),GREEN,50,1450,67)

    if colisao_bala:
        pontuacao += 1
    if colisao_zumbi:
        pontuacao -= 1
    if pontuacao < 0:
        pontuacao = 0
        tela.fill(WHITE)
        while game_over == False:
            jogadores.kill()
            enemy.kill()
            Texto(tela,arial,"GAME OVER",PURPLE,200,700,400)
            pygame.display.update()


    enimigos = 5
    zombies.update()
    jogador.update()
    disparos.update()
    if pontuacao > 0:
        if not zombies:
            for x in range(enimigos):
                enemy = Zomby()
                zombies.add(enemy)
    zombies.draw(tela)
    jogador.draw(tela)
    disparos.draw(tela)
    pygame.display.flip()