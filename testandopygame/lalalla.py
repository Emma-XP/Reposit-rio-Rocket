import pygame
from classes import Personagem

pygame.init()
tela = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

cientista = Personagem("testandopygame/cientista_alphys.png", 375, 275)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    cientista.Mover(teclas)

    tela.fill((20, 20, 40))
    cientista.Desenhar(tela)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()