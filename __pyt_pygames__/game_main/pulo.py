import pygame
import sys

pygame.init()

CAMINHO_IMAGEM = "__pyt_pygames__/MovimentaçãoDiana/"

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Movimentação com Animação")
relogio = pygame.time.Clock()

gravidade = 0.8          # Força que puxa o personagem para baixo a cada frame
velocidade_y = 0         # Velocidade vertical atual da Diana
forca_pulo = -16       # Altura do pulo (número negativo para subir)
no_chao = True           # Garante que ela só pule se estiver pisando no chão
altura_chao = 200        # A posição Y onde fica o seu chão

animacao_esquerda = [
pygame.image.load(CAMINHO_IMAGEM + "Andar 1.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Andar 2.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Andar 3.jpeg").convert_alpha()
] 

animacao_direita = [pygame.transform.flip(f, True, False) for f in animacao_esquerda]

animacao_baixo = [
    pygame.image.load(CAMINHO_IMAGEM + "Andar frente.jpeg").convert_alpha(),
    pygame.image.load(CAMINHO_IMAGEM+ "Andar frente 2.jpeg").convert_alpha(),
]

animacao_cima = [
pygame.image.load(CAMINHO_IMAGEM + "Andar costas.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Andar costas-2.jpeg").convert_alpha()
]

animacao_pulo=[
pygame.image.load(CAMINHO_IMAGEM + "Pulo 1.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Pulo 2.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Pulo 3.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Pulo 4.jpeg").convert_alpha(),
pygame.image.load(CAMINHO_IMAGEM + "Pulo 5.jpeg").convert_alpha()
]

velocidade = 5
frame_inicial= pygame.image.load(CAMINHO_IMAGEM + "Andar frente.jpeg").convert_alpha()

rect_jogador = frame_inicial.get_rect()

rect_jogador.center = (LARGURA // 2, ALTURA // 2)# Controle de Animação
frames_atuais = animacao_esquerda  # Começa olhando para a direita
indice_frame = 0
ultimo_update = pygame.time.get_ticks()
tempo_por_frame = 200  # Tempo em milissegundos para mudar de quadro
esta_movendo = False

while True:
    tela.fill((255, 255, 255))  
    esta_movendo = False

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()

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

    # Só funciona se estiver no chão
    if teclas[pygame.K_SPACE] and no_chao:
        velocidade_y = forca_pulo
        frames_atuais = animacao_pulo
        indice_frame = 0
        no_chao = False  

    if not no_chao:
        indice_frame += 0.15 
        if indice_frame >= len(frames_atuais):
            indice_frame = len(frames_atuais) - 1 
        

    else:
        if not esta_movendo:
            frames_atuais = animacao_baixo  
            indice_frame = 0
            
        velocidade_y += gravidade
    rect_jogador.y += velocidade_y  

    #Para não cair infinitamente...
    if rect_jogador.y >= altura_chao:
        rect_jogador.y = altura_chao  
        velocidade_y = 0              
        no_chao = True                

    tempo_atual = pygame.time.get_ticks()
    
    if esta_movendo:
        # Se o tempo necessário passou, avança para o próximo frame
        if tempo_atual - ultimo_update > tempo_por_frame:
            indice_frame = (indice_frame + 1) % len(frames_atuais)
            ultimo_update = tempo_atual
        
    else:
        # Se parou de mover, reseta para o primeiro frame (em pé)
        frames_atuais

    # Desenha o frame atual do jogador na tela
    frame_para_desenhar = frames_atuais[int(indice_frame)]
    tela.blit(frame_para_desenhar, (rect_jogador))

    pygame.display.update()
    relogio.tick(60)  # Mantém o jogo a 60 FPS
