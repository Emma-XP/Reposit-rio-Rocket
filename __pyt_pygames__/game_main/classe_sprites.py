import pygame
import sys

CAMINNHO_IMAGES = "__pyt_pygames__/MovimentaçãoDiana/"
class Frames(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[]
        self.image_a=pygame.image.load(CAMINNHO_IMAGES+"Andar 1.jpeg")
        self.image_b=pygame.image.load(CAMINNHO_IMAGES+"Andar 2.jpeg")
        self.image_c=pygame.image.load(CAMINNHO_IMAGES+"Andar 3.jpeg")

        self.sprites.append(self.image_a)
        self.sprites.append(self.image_b)
        self.sprites.append(self.image_c)
        self.indice_atual=0
        self.image=self.sprites[self.indice_atual]
        self.image=pygame.transform.scale(self.image,(300,360)) #Redimensionar
        self.rect=self.image.get_rect() #Torna a imagem retangular
        self.rect.topright=(400,100)

    def update(self):
        self.indice_atual=self.indice_atual + 0.05
        if self.indice_atual>=len(self.sprites):
            self.indice_atual=0
        self.image=self.sprites[int(self.indice_atual)]
        self.image=pygame.transform.scale(self.image,(300,360)) #Redimensionar
 
andar=pygame.sprite.Group()
Diana=Frames()
andar.add(Diana)

class Personagem:
    def __init__(self,imagem, x, y, velocidade=5):
        self.imagem= imagem
        self.x= x #Perambulam pelo plano cartesiano
        self.y= y
        self.velocidade=velocidade
    def mover (self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade
        if teclas[pygame.K_UP]:
            self.y -= self.velocidade
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidade
    def desenhar(self, tela):
        tela.blit(self.imagem,(self.x, self.y))


