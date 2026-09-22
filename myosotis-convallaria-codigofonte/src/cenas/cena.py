"""Classe base para telas e estados do jogo."""

import pygame

from src.configuracao.configuracoes import COR_FUNDO
from src.entidades.entidade import Entidade


class Cena:
    """Mantém e coordena as entidades pertencentes a uma tela."""

    def __init__(self, cor_fundo: tuple[int, int, int] = COR_FUNDO) -> None:
        self.cor_fundo = cor_fundo
        self.entidades: list[Entidade] = []
        self._entidades_para_adicionar: list[Entidade] = []
        self._entidades_para_remover: list[Entidade] = []

    def entrar(self) -> None:
        """Prepara os recursos necessários para a cena."""

    def sair(self) -> None:
        """Libera ou encerra os recursos próprios da cena."""

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        """Distribui um evento para as entidades ativas."""
        for entidade in tuple(self.entidades):
            if entidade.ativa:
                entidade.tratar_evento(evento)

    def atualizar(self, delta_tempo: float) -> None:
        """Atualiza entidades ativas e aplica alterações pendentes."""
        for entidade in tuple(self.entidades):
            if entidade.ativa:
                entidade.atualizar(delta_tempo)

        self._aplicar_alteracoes_pendentes()

    def desenhar(self, superficie: pygame.Surface) -> None:
        """Limpa o fundo e desenha as entidades visíveis."""
        superficie.fill(self.cor_fundo)
        for entidade in self.entidades:
            if entidade.visivel:
                entidade.desenhar(superficie)

    def adicionar_entidade(self, entidade: Entidade) -> None:
        """Agenda uma entidade para inclusão ao fim da atualização."""
        if entidade not in self._entidades_para_adicionar:
            self._entidades_para_adicionar.append(entidade)

    def remover_entidade(self, entidade: Entidade) -> None:
        """Agenda uma entidade para remoção ao fim da atualização."""
        if entidade not in self._entidades_para_remover:
            self._entidades_para_remover.append(entidade)

    def _aplicar_alteracoes_pendentes(self) -> None:
        for entidade in self._entidades_para_remover:
            if entidade in self.entidades:
                self.entidades.remove(entidade)

        for entidade in self._entidades_para_adicionar:
            if entidade not in self.entidades:
                self.entidades.append(entidade)

        self._entidades_para_remover.clear()
        self._entidades_para_adicionar.clear()
