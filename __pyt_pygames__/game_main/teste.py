import pygame
from classe_sprites import*
from pygame.locals import*

pygame.init()

clock=pygame.time.Clock()
tela=pygame.display.set_mode((800,600))
pygame.display.set_caption("Movimentação")
rodando=True
while rodando==True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando=False
    andar.draw(tela)
    andar.update()
    clock.tick(20)
    pygame.display.flip()
    
