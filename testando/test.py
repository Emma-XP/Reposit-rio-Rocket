import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo - Tela Inicial")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Fontes
fonte_titulo = pygame.font.SysFont(None, 64)
fonte_instrucao = pygame.font.SysFont(None, 32)

def tela_inicio():
    rodando = True
    while rodando:
        # Tratamento de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:  # Pressione ESPAÇO para começar
                    rodando = False

        # Preenche o fundo
        tela.fill(PRETO)

        # Renderiza os textos
        texto_titulo = fonte_titulo.render("MEU JOGO", True, VERDE)
        texto_instrucao = fonte_instrucao.render("Pressione ESPAÇO para Jogar", True, BRANCO)

        # Posiciona os textos na tela (centralizados)
        tela.blit(texto_titulo, (LARGURA // 2 - texto_titulo.get_width() // 2, ALTURA // 3))
        tela.blit(texto_instrucao, (LARGURA // 2 - texto_instrucao.get_width() // 2, ALTURA // 2))

        # Atualiza o display
        pygame.display.flip()

# Executa a tela de início
tela_inicio()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Aqui fica a lógica do seu jogo...
    tela.fill((50, 50, 50))  # Tela cinza representando o jogo rodando
    pygame.display.flip()
