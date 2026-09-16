class Fundo:
    def __init__(self, imagem, velocidade):
        self.imagem = imagem
        self.velocidade = velocidade
        self.x = 0
        self.largura = imagem.get_width()

    def atualizar(self):
        self.x -= self.velocidade
        if self.x <= -self.largura:
            self.x = 0

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, 0))
        tela.blit(self.imagem, (self.x + self.largura, 0))
