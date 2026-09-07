import pygame
import sys

pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Demonstração de Transparência (Alpha)")

# Criamos um fundo azul bem vivo para destacar o erro e o acerto
COR_FUNDO = (30, 144, 255) 

# --- MOEDA 1: SEM TRANSPARÊNCIA (Superfície Comum) ---
# O Pygame cria uma folha preta sólida de 50x50
moeda_com_canto_preto = pygame.Surface((50, 50))
# Desenhamos um círculo amarelo (RGB: 255, 215, 0) no centro dela
pygame.draw.circle(moeda_com_canto_preto, (255, 215, 0), (25, 25), 25)

# --- MOEDA 2: COM TRANSPARÊNCIA (Usando SRCALPHA) ---
# O Pygame cria uma folha invisível de 50x50
moeda_transparente = pygame.Surface((50, 50), pygame.SRCALPHA)
# Desenhamos o mesmo círculo amarelo no centro dela
pygame.draw.circle(moeda_transparente, (255, 215, 0), (25, 25), 25)

# Loop do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pinta a tela de azul
    tela.fill(COR_FUNDO)

    # 1. Desenha a moeda sem transparência na esquerda
    tela.blit(moeda_com_canto_preto, (150, 175))
    
    # 2. Desenha a moeda transparente na direita
    tela.blit(moeda_transparente, (400, 175))

    # Textos explicativos na tela
    fonte = pygame.font.SysFont(None, 24)
    txt1 = fonte.render("Sem SRCALPHA (Cantos Pretos)", True, (255, 255, 255))
    txt2 = fonte.render("Com SRCALPHA (Perfeita)", True, (255, 255, 255))
    tela.blit(txt1, (70, 140))
    tela.blit(txt2, (340, 140))

    pygame.display.flip()
