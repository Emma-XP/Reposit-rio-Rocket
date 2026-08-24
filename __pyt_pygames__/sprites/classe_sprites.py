import pygame
class Frames(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[]
        self.image_a=pygame.image.load("carinha_sprites/sprite_0.png")
        self.image_b=pygame.image.load("carinha_sprites/sprite_1.png")
        self.sprites.append(self.image_a)
        self.sprites.append(self.image_b)
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
 
todas_as_sprites=pygame.sprite.Group()
carinha_deformado=Frames()
todas_as_sprites.add(carinha_deformado)



