"""Cena final da trajetória de Diana."""

from collections.abc import Callable

import pygame

from src.cenas.cena import Cena
from src.configuracao.caminhos import (
    FONTE_PRINCIPAL,
    CENA_CONCLUSAO,
)
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
        self._imagem_fundo = None

    def entrar(self) -> None:
        if self._preparada:
            return

        # Carrega a imagem de fundo
        if CENA_CONCLUSAO.is_file():
            imagem = pygame.image.load(CENA_CONCLUSAO).convert()

            self._imagem_fundo = pygame.transform.smoothscale(
                imagem,
                (LARGURA_TELA, ALTURA_TELA),
            )

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

    def desenhar(self, superficie) -> None:
        # Desenha a imagem de fundo
        if self._imagem_fundo is not None:
            superficie.blit(self._imagem_fundo, (0, 0))
        else:
            superficie.fill(self.cor_fundo)

        # Desenha os textos por cima do fundo
        for entidade in self.entidades:
            if entidade.visivel:
                entidade.desenhar(superficie)

    def tratar_evento(self, evento):
        if (
            not self._reinicio_solicitado
            and evento.type == pygame.KEYDOWN
            and evento.key == pygame.K_RETURN
        ):
            self._reinicio_solicitado = True
            self.ao_reiniciar()
            return

        super().tratar_evento(evento)