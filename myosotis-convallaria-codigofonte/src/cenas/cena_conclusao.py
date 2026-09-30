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
                "O primeiro passo para falar sempre será falar. ",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 - 70),
                40,
                COR_TEXTO,
                FONTE_PRINCIPAL,
            )
        )

        self.adicionar_entidade(
            Texto(
                "E mesmo após as mais sombrias das noites, o sol continuará nascendo brilhantemente no céu.",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 - 12),
                40,
                COR_TEXTO,
                FONTE_PRINCIPAL,
            )
        )

        self.adicionar_entidade(
    Texto(
        "As coisas podem parecer pesadas demais agora, e é nesses momentos",
        (LARGURA_TELA // 2, ALTURA_TELA // 2 + 40),
        40,
        COR_TEXTO_SECUNDARIO,
        FONTE_PRINCIPAL,
    )
)

        self.adicionar_entidade(
            Texto(
                "que você precisa se lembrar da efemeridade da vida. Tudo passa,",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 + 70),
                40,
                COR_TEXTO_SECUNDARIO,
                FONTE_PRINCIPAL,
            )
        )

        self.adicionar_entidade(
            Texto(
                "desde os momentos bons até os ruins. Se algum dia o peso em seus",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 + 100),
                40,
                COR_TEXTO_SECUNDARIO,
                FONTE_PRINCIPAL,
            )
        )

        self.adicionar_entidade(
            Texto(
                "ombros voltar, seus músculos já estarão fortalecidos contra aquele obstáculo.",
                (LARGURA_TELA // 2, ALTURA_TELA // 2 + 130),
                40,
                COR_TEXTO_SECUNDARIO,
                FONTE_PRINCIPAL,
            )
)
        self.adicionar_entidade(
                    Texto(
                        "Se lembrar desse fato é chave para sobreviver até a mais terrível das dificuldades..",
                        (LARGURA_TELA // 2, ALTURA_TELA // 2 + 160),
                        40,
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