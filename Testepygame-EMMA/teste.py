import pygame
import math

pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Inimigo Perseguidor")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Posições iniciais
jogador_pos = pygame.Vector2(400, 300)
inimigo_pos = pygame.Vector2(100, 100)

velocidade_jogador = 5
velocidade_inimigo = 2

clock = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        jogador_pos.y -= velocidade_jogador
    if teclas[pygame.K_s]:
        jogador_pos.y += velocidade_jogador
    if teclas[pygame.K_a]:
        jogador_pos.x -= velocidade_jogador
    if teclas[pygame.K_d]:
        jogador_pos.x += velocidade_jogador

    # Movimento do inimigo em direção ao jogador
    direcao = jogador_pos - inimigo_pos
    if direcao.length() > 0:  # Evita divisão por zero
        direcao = direcao.normalize()
        inimigo_pos += direcao * velocidade_inimigo

    # Desenho
    tela.fill(BRANCO)
    pygame.draw.circle(tela, AZUL, (int(jogador_pos.x), int(jogador_pos.y)), 15)
    pygame.draw.circle(tela, VERMELHO, (int(inimigo_pos.x), int(inimigo_pos.y)), 15)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()