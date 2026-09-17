import pygame
import sys
from classe_sprites import Plataforma  # Movido para o topo por boa prática

pygame.init()

CAMINHO_IMAGEM = "__pyt_pygames__/MovimentaçãoDiana/"
CAMINHO_PLATAFORMAS = "__pyt_pygames__/game_main/"

LARGURA, ALTURA = 1200, 800
TAMANHO_JOGADOR = (50, 50)  # Definido como tupla para o transform.scale

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Movimentação com Animação")
relogio = pygame.time.Clock()

gravidade = 0.8          
velocidade_y = 0         
forca_pulo = -14  # Ajustado levemente para o pulo ficar fluido com as plataformas
no_chao = False           # Começa como False para ela cair na plataforma inicial

# --- CONFIGURAÇÃO DAS PLATAFORMAS ---
# Criamos um grupo do Pygame para gerenciar as colisões facilmente
grupo_plataformas = pygame.sprite.Group()

lista_plataformas = [
    Plataforma(0, 750, 1200, 50),       # Chão principal
    Plataforma(200, 600, 300, 30),     # Plataforma 1
    Plataforma(600, 450, 400, 30),     # Plataforma 2
    Plataforma(150, 300, 250, 30)      # Plataforma 3
]

# Adiciona todas as plataformas criadas para dentro do grupo
for plat in lista_plataformas:
    grupo_plataformas.add(plat)

# --- CARREGAMENTO E REDIMENSIONAMENTO DOS SPRITES ---
# Função interna rápida para carregar aplicando o TAMANHO_JOGADOR (50x50)
def carregar_e_escala(nome_arquivo):
    img = pygame.image.load(CAMINHO_IMAGEM + nome_arquivo).convert_alpha()
    return pygame.transform.scale(img, TAMANHO_JOGADOR)

animacao_esquerda = [
    carregar_e_escala("Andar 1.jpeg"),
    carregar_e_escala("Andar 2.jpeg"),
    carregar_e_escala("Andar 3.jpeg")
] 

animacao_direita = [pygame.transform.flip(f, True, False) for f in animacao_esquerda]

animacao_baixo = [
    carregar_e_escala("Andar frente.jpeg"),
    carregar_e_escala("Andar frente 2.jpeg"),
]

animacao_cima = [
    carregar_e_escala("Andar costas.jpeg"),
    carregar_e_escala("Andar costas-2.jpeg")
]

animacao_pulo = [
    carregar_e_escala("Pulo 1.jpeg"),
    carregar_e_escala("Pulo 2.jpeg"),
    carregar_e_escala("Pulo 3.jpeg"),
    carregar_e_escala("Pulo 4.jpeg"),
    carregar_e_escala("Pulo 5.jpeg")
]

velocidade = 5
frame_inicial = animacao_baixo[0]

# O rect agora assume perfeitamente o tamanho de 50x50 da imagem redimensionada
rect_jogador = frame_inicial.get_rect()
rect_jogador.center = (LARGURA // 2, 100)  # Começa no alto para cair na plataforma

# Controle de Animação
frames_atuais = animacao_baixo  
indice_frame = 0
ultimo_update = pygame.time.get_ticks()
tempo_por_frame = 200  
esta_movendo = False

# --- LOOP PRINCIPAL ---
while True:
    tela.fill((255, 255, 255))  
    esta_movendo = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    teclas = pygame.key.get_pressed()

    # --- MOVIMENTO HORIZONTAL ---
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        rect_jogador.x -= velocidade
        if no_chao: frames_atuais = animacao_esquerda
        esta_movendo = True
    elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        rect_jogador.x += velocidade
        if no_chao: frames_atuais = animacao_direita
        esta_movendo = True

    # --- MOVIMENTO VERTICAL (ANDAR / PULAR) ---
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        rect_jogador.y += velocidade
        if no_chao: frames_atuais = animacao_baixo
        esta_movendo = True
    elif teclas[pygame.K_UP] or teclas[pygame.K_w]:
        rect_jogador.y -= velocidade
        if no_chao: frames_atuais = animacao_cima
        esta_movendo = True

    # Comando do Pulo (Só se no_chao for True)
    if teclas[pygame.K_SPACE] and no_chao:
        velocidade_y = forca_pulo
        frames_atuais = animacao_pulo
        indice_frame = 0
        no_chao = False  

    # --- APLICAÇÃO DA FÍSICA E ANIMAÇÃO ---
    velocidade_y += gravidade
    rect_jogador.y += velocidade_y  

    # --- DETECÇÃO DE COLISÃO COM AS PLATAFORMAS ---
    # Criamos um rect temporário usando uma estrutura compatível para checar colisão contra o grupo
    colisoes = pygame.sprite.spritecollide(pygame.sprite.Sprite(), grupo_plataformas, False)
    
    # Como não transformamos a Diana em uma classe Sprite própria ainda, simulamos a colisão manualmente de forma simples:
    no_chao = False # Reseta o estado; se estiver tocando em algo, mudamos para True abaixo
    
    for plat in grupo_plataformas:
        if rect_jogador.colliderect(plat.rect):
            if velocidade_y > 0:  # Caindo em cima de uma plataforma
                rect_jogador.bottom = plat.rect.top
                velocidade_y = 0              
                no_chao = True                
            elif velocidade_y < 0:  # Batendo a cabeça por baixo de uma plataforma
                rect_jogador.top = plat.rect.bottom
                velocidade_y = 0

    # Lógica de controle de frames (Pulo vs Andar)
    if not no_chao:
        frames_atuais = animacao_pulo
        indice_frame += 0.15 
        if indice_frame >= len(frames_atuais):
            indice_frame = len(frames_atuais) - 1 
    else:
        if not esta_movendo:
            frames_atuais = animacao_baixo  
            indice_frame = 0

    # Troca de frames por tempo (Apenas quando estiver andando no chão)
    tempo_atual = pygame.time.get_ticks()
    if esta_movendo and no_chao:
        if tempo_atual - ultimo_update > tempo_por_frame:
            indice_frame = (indice_frame + 1) % len(frames_atuais)            
            ultimo_update = tempo_atual

    # --- RENDERIZAÇÃO (DESENHO) ---
    # Desenha todas as plataformas do grupo na tela
    grupo_plataformas.draw(tela)

    # Desenha o frame atual da Diana
    frame_para_desenhar = frames_atuais[int(indice_frame)]
    tela.blit(frame_para_desenhar, rect_jogador)

    pygame.display.update()
    relogio.tick(60)
