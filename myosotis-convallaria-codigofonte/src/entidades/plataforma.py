"""Plataforma sólida usada nas fases do jogo."""

import pygame

from src.configuracao.caminhos import IMAGEM_PLATAFORMA
from src.configuracao.configuracoes import COR_PLATAFORMA
from src.entidades.entidade_visual import EntidadeVisual


class Plataforma(EntidadeVisual):
    """Representa uma superfície imóvel sobre a qual a jogadora se apoia."""

    def __init__(self, retangulo: pygame.Rect) -> None:
        super().__init__(retangulo, COR_PLATAFORMA, IMAGEM_PLATAFORMA)
