import pygame

cor = (0, 0, 0)

def Tela_inicio(tela, fundo):    
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
        tela.blit(fundo, (0,0))