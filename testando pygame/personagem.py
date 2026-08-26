import pygame

class Personagem:
    def __init__(self, cam_img, x, y, vel=5):
        self.imagem = pygame.image.load(cam_img)
        self.x=x
        self.y=y
        self.vel=vel

    def Mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT]:
            self.x += self.vel
        if teclas[pygame.K_UP]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN]:
            self.y += self.vel
        
    def Desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))