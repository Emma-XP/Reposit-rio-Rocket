import pygame
from __pyt_pygame__.sprites.classe_sprites import*
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
tela=pygame.display.set_mode((800,600))
pygame.display.set_caption("Teste de horrores")
rodando=True
while rodando==True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando=False
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    clock.tick(20)
    pygame.display.flip()
