import pygame

from Testes_gerais_Hills.movimentação.classe_personagem import Personagem

pygame.init()

CAMINNHO_IMAGES = "__pyt_pygames__/MovimentaçãoDiana/"

tela=pygame.display.set_mode((800,600)) #Define o formato e dimensões da tela 
clock= pygame.time.Clock()
diana=pygame.image.load(CAMINNHO_IMAGES+"leorio.png")
diana_redimensionado=pygame.transform.scale(diana,(100,185))
diana_m= Personagem (diana_redimensionado,375,275) #Instância (Objeto)
pygame.display.set_caption("Game maldito") #Parecido com o elemento label
rodando=True
while rodando: #Esse laço é importante visto que o game necessita de atualizações constantes 
    tela.fill((255,255,255)) #RGB
    obstaculo=pygame.draw.rect (tela,(210,105,30),(185,195,110,150))
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT: #No momento em que houver o clique sobre o botão fechar ("pygame.QUIT")
            rodando=False
    teclas=pygame.key.get_pressed()
    diana_m.mover(teclas)
    
    diana_m.desenhar(tela)
    
    pygame.display.flip() #Executa o código, por isso, dev ser posicionado em última instância
    clock.tick(45) #Frames por segundo. o elemnto "clock" foi definido na 7ª linha 
#Display=mostrar
pygame.quit()