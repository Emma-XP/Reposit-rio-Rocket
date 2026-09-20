"""Entidade visual com sprite opcional e forma geométrica temporária."""

from pathlib import Path

import pygame

from src.entidades.entidade import Entidade


class EntidadeVisual(Entidade):
    """Exibe uma imagem ou, na ausência dela, uma forma simples."""

    def __init__(
        self,
        retangulo: pygame.Rect,
        cor: tuple[int, int, int],
        caminho_imagem: Path | None = None,
        forma: str = "retangulo",
    ) -> None:
        super().__init__()
        self.retangulo = retangulo
        self.cor = cor
        self.caminho_imagem = caminho_imagem
        self.forma = forma
        self._imagem = self._carregar_imagem()

    def desenhar(self, superficie: pygame.Surface) -> None:
        if self._imagem is not None:
            superficie.blit(self._imagem, self.retangulo)
            return

        if self.forma == "circulo":
            pygame.draw.ellipse(superficie, self.cor, self.retangulo)
            return

        pygame.draw.rect(superficie, self.cor, self.retangulo, border_radius=12)

    def _carregar_imagem(self) -> pygame.Surface | None:
        if self.caminho_imagem is None or not self.caminho_imagem.is_file():
            return None

        imagem = pygame.image.load(self.caminho_imagem).convert_alpha()
        return pygame.transform.smoothscale(imagem, self.retangulo.size)
