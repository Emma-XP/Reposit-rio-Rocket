import pygame

class Personagem(pygame.sprite.Sprite:
                 
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites=[]
            self.img_direita=pygame.image.load("testandopygame/cientista_alphys_right.png")
            self.img_esquerda=pygame.image.load("testandopygame/cientista_alphys_left.png")
            self.sprites.append(self.img_direita)
            self.sprites.append(self.img_esquerda)
            self.indice_atual=0
            self.image=self.sprites[self.indice_atual]
            self.image=pygame.transform.scale(self.image,(300,360)) #Redimensionar
            self.rect=self.image.get_rect() #Torna a imagem retangular
            self.rect.topright=(400,100)


    def Mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT]:
            self.x += self.vel
        if teclas[pygame.K_UP]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN]:
            self.y += self.vel