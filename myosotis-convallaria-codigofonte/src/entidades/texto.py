"""Entidade responsável por desenhar uma linha de texto."""

from pathlib import Path

import pygame

from src.entidades.entidade import Entidade


class Texto(Entidade):
    """Renderiza texto centralizado em uma posição da tela."""

    def __init__(
        self,
        conteudo: str,
        posicao: tuple[int, int],
        tamanho: int,
        cor: tuple[int, int, int],
        caminho_fonte: Path | None = None,
    ) -> None:
        super().__init__()
        self.conteudo = conteudo
        self.posicao = posicao
        self.tamanho = tamanho
        self.cor = cor
        self.caminho_fonte = caminho_fonte
        self._fonte = self._criar_fonte()

    def desenhar(self, superficie: pygame.Surface) -> None:
        imagem_texto = self._fonte.render(self.conteudo, True, self.cor)
        retangulo_texto = imagem_texto.get_rect(center=self.posicao)
        superficie.blit(imagem_texto, retangulo_texto)

    def _criar_fonte(self) -> pygame.font.Font:
        caminho = None
        if self.caminho_fonte is not None and self.caminho_fonte.is_file():
            caminho = str(self.caminho_fonte)
        return pygame.font.Font(caminho, self.tamanho)
