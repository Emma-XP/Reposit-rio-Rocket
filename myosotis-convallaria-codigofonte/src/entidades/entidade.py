"""Classe base para objetos existentes dentro de uma cena."""

from abc import ABC, abstractmethod

import pygame


class Entidade(ABC):
    """Define o contrato comum de atualização, desenho e entrada."""

    def __init__(self, ativa: bool = True, visivel: bool = True) -> None:
        self.ativa = ativa
        self.visivel = visivel

    def atualizar(self, delta_tempo: float) -> None:
        """Atualiza o estado próprio da entidade."""

    @abstractmethod
    def desenhar(self, superficie: pygame.Surface) -> None:
        """Desenha a entidade sem alterar seu estado."""

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        """Recebe um evento de entrada quando a entidade precisar dele."""
