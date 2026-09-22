"""Especialização de cena para futuras fases do jogo."""

from src.cenas.cena import Cena


class Fase(Cena):
    """Fornece estado básico de objetivo e progresso para uma fase."""

    def __init__(self, objetivo: str = "") -> None:
        super().__init__()
        self.objetivo = objetivo
        self.progresso = 0

    def definir_progresso(self, progresso: int) -> None:
        """Atualiza o progresso sem permitir valores negativos."""
        self.progresso = max(0, progresso)
