"""Controle central da cena ativa do jogo."""

import pygame

from src.cenas.cena import Cena


class ControladorCenas:
    """Mantém somente uma cena ativa e encaminha o fluxo principal."""

    def __init__(self) -> None:
        self.cena_ativa: Cena | None = None

    def trocar_cena(self, proxima_cena: Cena) -> None:
        """Encerra a cena atual e prepara a próxima cena."""
        if self.cena_ativa is not None:
            self.cena_ativa.sair()

        self.cena_ativa = proxima_cena
        self.cena_ativa.entrar()

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        """Encaminha um evento à cena ativa."""
        if self.cena_ativa is not None:
            self.cena_ativa.tratar_evento(evento)

    def atualizar(self, delta_tempo: float) -> None:
        """Atualiza a cena ativa."""
        if self.cena_ativa is not None:
            self.cena_ativa.atualizar(delta_tempo)

    def desenhar(self, superficie: pygame.Surface) -> None:
        """Solicita o desenho da cena ativa."""
        if self.cena_ativa is not None:
            self.cena_ativa.desenhar(superficie)

    def encerrar(self) -> None:
        """Encerra a cena ativa e remove sua referência."""
        if self.cena_ativa is not None:
            self.cena_ativa.sair()
            self.cena_ativa = None
