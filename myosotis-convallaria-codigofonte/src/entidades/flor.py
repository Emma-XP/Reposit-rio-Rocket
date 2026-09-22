"""Entidade coletável usada para avançar as mensagens de uma fase."""

import pygame

from src.configuracao.caminhos import IMAGEM_FLOR
from src.configuracao.configuracoes import COR_FLOR, TAMANHO_FLOR
from src.entidades.entidade_visual import EntidadeVisual


class Flor(EntidadeVisual):
    """Mantém posição, colisão e estado local de uma flor."""

    def __init__(self, posicao: tuple[int, int]) -> None:
        super().__init__(
            pygame.Rect(posicao, TAMANHO_FLOR),
            COR_FLOR,
            IMAGEM_FLOR,
            forma="circulo",
        )
        self.coletada = False

    def coletar(self) -> bool:
        """Marca a coleta uma única vez e informa se ela foi inédita."""
        if self.coletada:
            return False
        self.coletada = True
        self.ativa = False
        self.visivel = False
        return True

    def desenhar(self, superficie: pygame.Surface) -> None:
        if self._imagem is not None:
            superficie.blit(self._imagem, self.retangulo)
            return

        centro_x = self.retangulo.centerx
        pygame.draw.rect(
            superficie,
            (70, 139, 82),
            (centro_x - 3, self.retangulo.centery, 6, self.retangulo.height // 2),
        )
        raio = self.retangulo.width // 5
        for deslocamento in ((-raio, 0), (raio, 0), (0, -raio), (0, raio)):
            pygame.draw.circle(
                superficie,
                self.cor,
                (centro_x + deslocamento[0], self.retangulo.y + 18 + deslocamento[1]),
                raio,
            )
        pygame.draw.circle(superficie, (245, 196, 81), (centro_x, self.retangulo.y + 18), 6)
