import pygame

pygame.init()

lar, alt = 800, 600
tela = pygame.display.set_mode((lar, alt))
pygame.display.set_caption("Olá mundo")

rodando = True
while rodando:

    tela.fill((255, 0, 0))
    cX, cY = lar/2, alt/2
    pygame.draw.circle(tela, (255, 255, 255), (cX, cY), 50)
    pygame.display.flip()

    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

pygame.quit()