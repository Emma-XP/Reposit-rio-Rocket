import pygame
import sys

pygame.init()

CAMINHO_IMAGEM="__pyt_pygames__/MovimentaçãoDiana/"

#Variáveis
LARGURA, ALTURA = 800, 600
FUNDO= (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Movimentação com Animação")
relogio = pygame.time.Clock()

frame_inicial= [pygame.image.load(CAMINHO_IMAGEM + "Andar frente.jpeg").convert_alpha()]

animacao_esquerda = [
pygame.image.load(CAMINHO_IMAGEM + "Andar 1.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Andar 2.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Andar 3.jpeg").convert_alpha()
] 

# convert_alpha é o mesmo que remover o fundo de uma imagem, funcionado apenas com imagens de extensão PNG

# pygame.transform.flip(f,True,False) realiza a inversão da imagem

# O parâmetro "f" baseia-se no laço "for f in animação_esquerda
# O parâmetro "True" é referente a inversão horizontal, que é o que queremos
# O parâmetro "False" é refrente a inversão vertical, que não é o que queremos no momento

animacao_direita = [pygame.transform.flip(f, True, False) for f in animacao_esquerda]

animacao_baixo = [
    pygame.image.load(CAMINHO_IMAGEM + "Andar frente.jpeg").convert_alpha(),
    pygame.image.load(CAMINHO_IMAGEM+ "Andar frente 2.jpeg").convert_alpha()
]

animacao_cima = [
pygame.image.load(CAMINHO_IMAGEM + "Andar costas.jpeg"),
pygame.image.load(CAMINHO_IMAGEM + "Andar costas-2.jpeg")
]

# VARIÁVEIS DO JOGADOR 
velocidade = 5

frame_princ = pygame.image.load(CAMINHO_IMAGEM + "Andar frente.jpeg")
rect_jogador = frame_princ.get_rect()

rect_jogador.center = (LARGURA // 2, ALTURA // 2)# Controle de Animação
frames_atuais = animacao_esquerda  # Começa olhando para a direita
indice_frame = 0
ultimo_update = pygame.time.get_ticks()
tempo_por_frame = 200  # Tempo em milissegundos para mudar de quadro
esta_movendo = False

# Loop principal
while True:
    tela.fill((FUNDO))  
    esta_movendo = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimentação e troca de vetor de animação
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        rect_jogador.x -= velocidade
        frames_atuais = animacao_esquerda
        esta_movendo = True
    elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        rect_jogador.x += velocidade
        frames_atuais = animacao_direita
        esta_movendo = True
    elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        rect_jogador.y += velocidade
        frames_atuais = animacao_baixo
        esta_movendo=True
    elif teclas[pygame.K_UP] or teclas[pygame.K_w]:
        rect_jogador.y -= velocidade
        frames_atuais = animacao_cima
        esta_movendo = True

    # --- LÓGICA DA ANIMAÇÃO ---
    tempo_atual = pygame.time.get_ticks()
    
    if esta_movendo:
        # Se o tempo necessário passou, avança para o próximo frame
        if tempo_atual - ultimo_update > tempo_por_frame:
            indice_frame = (indice_frame + 1) % len(frames_atuais)
            ultimo_update = tempo_atual
    else:
        # Se parou de mover, reseta para o primeiro frame (em pé)
        indice_frame=0
    
    if indice_frame >= len(frames_atuais):
        indice_frame = 0

    # Desenha o frame atual do jogador na tela
    frame_para_desenhar = frames_atuais[indice_frame]
    tela.blit(frame_para_desenhar, (rect_jogador))


    pygame.display.update()
    relogio.tick(60)  # Mantém o jogo a 60 FPS
