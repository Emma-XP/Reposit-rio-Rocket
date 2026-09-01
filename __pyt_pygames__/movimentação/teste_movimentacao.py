import pygame

from classe_personagem import Personagem

pygame.init()

CAMINNHO_IMAGES = "__pyt_pygames__/images/"

tela=pygame.display.set_mode((800,600)) #Define o formato e dimensões da tela 
clock= pygame.time.Clock()
leorio=pygame.image.load(CAMINNHO_IMAGES+"leorio.png")
leorio_redimensionado=pygame.transform.scale(leorio,(100,185))
cientista= Personagem (leorio_redimensionado,375,275) #Instância (Objeto)
pygame.display.set_caption("Game maldito") #Parecido com o elemento label
rodando=True
while rodando: #Esse laço é importante visto que o game necessita de atualizações constantes 
    tela.fill((255,255,255)) #RGB
    obstaculo=pygame.draw.rect (tela,(210,105,30),(185,195,110,150))
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT: #No momento em que houver o clique sobre o botão fechar ("pygame.QUIT")
            rodando=False
    teclas=pygame.key.get_pressed()
    cientista.mover(teclas)
    
    cientista.desenhar(tela)
    
    pygame.display.flip() #Executa o código, por isso, dev ser posicionado em última instância
    clock.tick(45) #Frames por segundo. o elemnto "clock" foi definido na 7ª linha 
#Display=mostrar
pygame.quit()