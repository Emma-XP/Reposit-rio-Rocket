import pygame
from random import randint
from sys import exit

# Tela principal
pygame.init()

x = 600
y = 400

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption("Pong")

relogio = pygame.time.Clock()

# VALORES DIANA
bX = 600
bY = 400
diametro = 10

# VARIÁVEL ITEM
v = 100

# VALORES ITEM
Xc = 200
Yc = 300

#VALORES ENEMY
Ec = 250
Ex = 350
ve=2
item_pego = False

#BARRAR O DESGRAÇADINHO
tempo_atual = pygame.time.get_ticks()

while True:

    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # TECLAS
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        bX -= 20

    if teclas[pygame.K_d]:
        bX += 20

    #if teclas[pygame.K_w]:
       # bY -= 20
       
    #corrigir pulo DIANA
    if teclas[pygame.K_s]:
        bY += 40
        bY -= 5
        bY -= 5
        bY -= 5
        bY -= 5
        bY -= 5
        bY -= 5
        bY -= 5
        bY -= 5

    #BARRAR A SONGAMONGA
    bX = max(diametro, min(x - diametro, bX))
    bY = max(diametro, min(y - diametro, bY))
    
    # TELA
    tela.fill((0, 0, 0))

    # DIANA
    Diana = pygame.draw.circle(
        tela,
        (255, 255, 255),
        (bX, bY),
        diametro
    )
    #ENEMY
    enemy = pygame.draw.rect(tela,(10, 178, 40), (Ec, Ex, 40, 50))
    
     # INIMIGO PERSEGUIDOR
  
    inimigo_pos = pygame.Vector2(Ec + 20, Ex + 25)
    diana_pos = pygame.Vector2(bX, bY)
    d = diana_pos - inimigo_pos
    if d.length() > 0:
        d = d.normalize()

        Ec += d.x * ve
        Ex += d.y * ve
            

    # ITEM
    if not item_pego:
        itemC = pygame.draw.rect( tela, (33, 138, 95), (Xc, Yc, 40, 50) )
        # COLISÕES ITEM 
        if Diana.colliderect(itemC):
                    v += 10
                    item_pego = True
                    print("v =", v)
    
    
     # COLISÕESs
    
    if Diana.colliderect(enemy):
        v-= 10
        print("v=", v)
        Ec = randint(40, 560)
        Ex = randint(40, 350)
        
    
    if v==0:
        print("GAME OVER")
        pygame.quit()
        exit()
    # ATUALIZA A TELA
    pygame.display.flip()

    # 60 FPS
    relogio.tick(60)


        
