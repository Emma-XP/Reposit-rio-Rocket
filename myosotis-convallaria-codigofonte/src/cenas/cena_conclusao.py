"""Cena final da trajetória de Diana."""

from collections.abc import Callable

import pygame

from src.cenas.cena import Cena
from src.configuracao.caminhos import FONTE_PRINCIPAL
from src.configuracao.configuracoes import (
    ALTURA_TELA,
    COR_TEXTO,
    COR_TEXTO_SECUNDARIO,
    LARGURA_TELA,
)
from src.entidades.texto import Texto


class CenaConclusao(Cena):
    """Conclui a história de Diana e permite uma nova execução."""

    def __init__(self, ao_reiniciar: Callable[[], None]) -> None:
        super().__init__()
        self.ao_reiniciar = ao_reiniciar
        self._preparada = False
        self._reinicio_solicitado = False

    def entrar(self) -> None:
        if self._preparada:
            return
        self.adicionar_entidade(
            Texto(
                "Diana seguiu fazendo perguntas, ocupando espaços e reconhecendo o próprio valor.",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 - 70),
                30,
                COR_TEXTO,
                FONTE_PRINCIPAL,
            )
        )
        self.adicionar_entidade(
            Texto(
                "As pressões não escreveram o fim da história dela.",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 - 12),
                48,
                COR_TEXTO,
                FONTE_PRINCIPAL,
            )
        )
        self.adicionar_entidade(
            Texto(
                "Pressione ENTER para jogar novamente",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 + 40),
                25,
                COR_TEXTO_SECUNDARIO,
                FONTE_PRINCIPAL,
            )
        )
        self._preparada = True

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if (
            not self._reinicio_solicitado
            and evento.type == pygame.KEYDOWN
            and evento.key == pygame.K_RETURN
        ):
            self._reinicio_solicitado = True
            self.ao_reiniciar()
            return
        super().tratar_evento(evento)
