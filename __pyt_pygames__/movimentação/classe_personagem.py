import pygame

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

    


