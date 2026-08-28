import pygame
from random import randint
from sys import exit

pygame.init()


x = 600
y = 400


tela = pygame.display.set_mode((x, y))
relogio = pygame.time.Clock()

pygame.display.set_caption('Pong')
#1- base (se vc nn entedeu se demita)

bX = 300
bY = 200
diametro = 10


Xc = 200
Yc = 300
# bx/by= posição da bolinha Yc/Xc= posição do retangulo
while True:
    tela.fill((0, 0, 0))
    relogio.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Teclas(o minimo bosal)
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        bX -= 20

    if teclas[pygame.K_d]:
        bX += 20

    if teclas[pygame.K_w]:
        bY -= 20

    if teclas[pygame.K_s]:
        bY += 20

    # botar no papel
    bolinha = pygame.draw.circle(
        tela,
        (255, 255, 255),
        (bX, bY),
        diametro
    )

    coisa = pygame.draw.rect(
        tela,
        (33, 138, 95),
        (Xc, Yc, 40, 50)
    )

    # BOOM
    if bolinha.colliderect(coisa):
        Xc = randint(40, 560)
        Yc = randint(40, 350)

    pygame.display.update()