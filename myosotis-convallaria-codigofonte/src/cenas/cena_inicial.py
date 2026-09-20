"""Cena técnica exibida enquanto o conteúdo do jogo é definido."""

import pygame

from src.cenas.cena import Cena
from src.configuracao.caminhos import FONTE_PRINCIPAL, IMAGEM_IDENTIDADE_VISUAL
from src.configuracao.configuracoes import (
    ALTURA_TELA,
    COR_PRIMARIA,
    COR_TEXTO,
    COR_TEXTO_SECUNDARIO,
    LARGURA_TELA,
)
from src.entidades.entidade_visual import EntidadeVisual
from src.entidades.texto import Texto
from src.estado_jogo import EstadoJogo


class CenaInicial(Cena):
    """Apresenta uma tela neutra que confirma o funcionamento da base."""

    def __init__(self, estado: EstadoJogo) -> None:
        super().__init__()
        self.estado = estado
        self._preparada = False

    def entrar(self) -> None:
        if self._preparada:
            return

        largura_marca = 190
        altura_marca = 120
        area_marca = pygame.Rect(
            (LARGURA_TELA - largura_marca) // 2,
            95,
            largura_marca,
            altura_marca,
        )
        self.adicionar_entidade(
            EntidadeVisual(
                area_marca,
                COR_PRIMARIA,
                caminho_imagem=IMAGEM_IDENTIDADE_VISUAL,
            )
        )
        self.adicionar_entidade(
            Texto(
                "Myosotis convallaria",
                (LARGURA_TELA // 2, ALTURA_TELA // 2),
                46,
                COR_TEXTO,
                FONTE_PRINCIPAL,
            )
        )
        self.adicionar_entidade(
            Texto(
                "Estrutura inicial pronta para receber o conteúdo do jogo",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 + 62),
                23,
                COR_TEXTO_SECUNDARIO,
                FONTE_PRINCIPAL,
            )
        )
        self._preparada = True
