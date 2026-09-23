"""Tela inicial do jogo."""

import pygame

from src.cenas.cena import Cena
from src.configuracao.caminhos import IMAGEM_BOTAO_JOGAR, IMAGEM_TELA_INICIO
from src.configuracao.configuracoes import ALTURA_TELA, LARGURA_TELA
from src.estado_jogo import EstadoJogo


class CenaInicial(Cena):
    """Exibe a tela inicial e inicia o jogo ao clicar em JOGAR."""

    def __init__(self, estado: EstadoJogo, ao_jogar) -> None:
        super().__init__()
        self.estado = estado
        self.ao_jogar = ao_jogar

        self._fundo: pygame.Surface | None = None
        self._botao: pygame.Surface | None = None
        self._retangulo_botao = pygame.Rect(0, 0, LARGURA_TELA // 2.5, ALTURA_TELA // 1.5)

    def entrar(self) -> None:
        """Carrega as imagens da tela inicial."""
        if self._fundo is None:
            fundo = pygame.image.load(IMAGEM_TELA_INICIO).convert()
            self._fundo = pygame.transform.smoothscale(
                fundo, (LARGURA_TELA, ALTURA_TELA)
            )

        if self._botao is None:
            self._botao = pygame.image.load(IMAGEM_BOTAO_JOGAR).convert_alpha()
            self._botao = pygame.transform.smoothscale(self._botao, (500, 230))
            self._retangulo_botao = self._botao.get_rect(
                center=(LARGURA_TELA // 2.5, ALTURA_TELA // 1.5)
            )

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        """Inicia o jogo quando o botão JOGAR é clicado."""
        if evento.type == pygame.KEYDOWN and evento.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.ao_jogar()
            return
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self._retangulo_botao.collidepoint(evento.pos):
                self.ao_jogar()

    def desenhar(self, superficie: pygame.Surface) -> None:
        """Desenha somente o fundo e o botão JOGAR."""
        if self._fundo is not None:
            superficie.blit(self._fundo, (0, 0))

        if self._botao is not None:
            superficie.blit(self._botao, self._retangulo_botao)
