"""Entidade controlável com física e animação independente da colisão."""

from collections.abc import Sequence
from pathlib import Path

import pygame

from src.configuracao.caminhos import QUADROS_JOGADORA
from src.configuracao.configuracoes import (
    ALTURA_JOGADORA,
    ALTURA_TELA,
    COR_JOGADORA,
    FATOR_CORTE_PULO,
    GRAVIDADE,
    LARGURA_JOGADORA,
    LARGURA_TELA,
    TEMPO_BUFFER_PULO,
    TEMPO_COYOTE,
    VELOCIDADE_JOGADORA,
    VELOCIDADE_MAXIMA_QUEDA,
    VELOCIDADE_PULO,
)
from src.entidades.entidade_visual import EntidadeVisual
from src.entidades.plataforma import Plataforma


class Jogadora(EntidadeVisual):
    """Controla a própria movimentação e resolve colisões com plataformas."""

    def __init__(
        self,
        posicao_inicial: tuple[int, int],
        plataformas: Sequence[Plataforma],
        idade: str = "infancia",
    ) -> None:
        retangulo = pygame.Rect(
            posicao_inicial,
            (LARGURA_JOGADORA, ALTURA_JOGADORA),
        )
        super().__init__(retangulo, COR_JOGADORA)
        self.posicao_inicial = posicao_inicial
        self.plataformas = plataformas
        self.idade = idade
        self.velocidade_vertical = 0.0
        self.velocidade_horizontal = 0.0
        self.no_chao = False
        self._posicao_x = float(retangulo.x)
        self._posicao_y = float(retangulo.y)
        self._movendo_esquerda = False
        self._movendo_direita = False
        self._pulo_pressionado = False
        self._tempo_buffer_pulo = 0.0
        self._tempo_coyote = 0.0
        self._direcao = "direita"
        self._estado_animacao = "queda"
        self._indice_quadro = 0
        self._tempo_animacao = 0.0
        self._quadros_direita = self._carregar_quadros()
        self._quadros_esquerda = {
            estado: tuple(
                pygame.transform.flip(quadro, True, False) for quadro in quadros
            )
            for estado, quadros in self._quadros_direita.items()
        }

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if evento.type not in (pygame.KEYDOWN, pygame.KEYUP):
            return

        pressionada = evento.type == pygame.KEYDOWN
        if evento.key in (pygame.K_LEFT, pygame.K_a):
            self._movendo_esquerda = pressionada
        elif evento.key in (pygame.K_RIGHT, pygame.K_d):
            self._movendo_direita = pressionada
        elif evento.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
            if pressionada and not self._pulo_pressionado:
                self._pulo_pressionado = True
                self._tempo_buffer_pulo = TEMPO_BUFFER_PULO
            elif not pressionada:
                self._pulo_pressionado = False
                self._interromper_pulo()

    def atualizar(self, delta_tempo: float) -> None:
        # Evita saltos grandes na física se a janela ficar temporariamente parada.
        delta_tempo = min(delta_tempo, 0.05)
        direcao = int(self._movendo_direita) - int(self._movendo_esquerda)
        self.velocidade_horizontal = direcao * VELOCIDADE_JOGADORA
        if direcao < 0:
            self._direcao = "esquerda"
        elif direcao > 0:
            self._direcao = "direita"

        self._atualizar_temporizadores(delta_tempo)
        self._tentar_pular()

        self._mover_horizontal(self.velocidade_horizontal * delta_tempo)
        self.velocidade_vertical = min(
            self.velocidade_vertical + GRAVIDADE * delta_tempo,
            VELOCIDADE_MAXIMA_QUEDA,
        )
        self._mover_vertical(self.velocidade_vertical * delta_tempo)
        # Consome um comando dado pouco antes da aterrissagem, sem cooldown.
        self._tentar_pular()

        self._atualizar_animacao(delta_tempo)

    def reiniciar(self) -> None:
        """Devolve a jogadora ao início da fase e zera sua velocidade."""
        self.retangulo.topleft = self.posicao_inicial
        self._posicao_x = float(self.retangulo.x)
        self._posicao_y = float(self.retangulo.y)
        self.velocidade_vertical = 0.0
        self.velocidade_horizontal = 0.0
        self.no_chao = False
        self._pulo_pressionado = False
        self._tempo_buffer_pulo = 0.0
        self._tempo_coyote = 0.0
        self._movendo_esquerda = False
        self._movendo_direita = False
        self._estado_animacao = "queda"
        self._indice_quadro = 0
        self._tempo_animacao = 0.0

    def liberar_controles(self) -> None:
        """Evita movimento retido quando uma caixa de diálogo pausa a fase."""
        self._movendo_esquerda = False
        self._movendo_direita = False
        self._pulo_pressionado = False
        self.velocidade_horizontal = 0.0

    def caiu_do_mapa(self) -> bool:
        """Informa à cena quando a tentativa deve ser reiniciada."""
        return self.retangulo.top > ALTURA_TELA + 150

    def desenhar(self, superficie: pygame.Surface) -> None:
        """Desenha o quadro atual centralizado na caixa de colisão estável."""
        colecao = (
            self._quadros_esquerda
            if self._direcao == "esquerda"
            else self._quadros_direita
        )
        quadros = colecao[self._estado_animacao]
        quadro = quadros[self._indice_quadro % len(quadros)]
        area = quadro.get_rect(midbottom=self.retangulo.midbottom)
        superficie.blit(quadro, area)

    def _carregar_quadros(self) -> dict[str, tuple[pygame.Surface, ...]]:
        caminhos = QUADROS_JOGADORA.get(self.idade, QUADROS_JOGADORA["infancia"])
        cores = {
            "infancia": (236, 137, 112),
            "adolescencia": (145, 126, 204),
            "vida_adulta": (76, 151, 166),
        }
        cor = cores.get(self.idade, COR_JOGADORA)
        quadros: dict[str, tuple[pygame.Surface, ...]] = {}
        for estado, caminhos_estado in caminhos.items():
            quadros[estado] = tuple(
                self._carregar_ou_criar_quadro(caminho, cor, indice, estado)
                for indice, caminho in enumerate(caminhos_estado)
            )
        return quadros

    def _carregar_ou_criar_quadro(
        self,
        caminho: Path,
        cor: tuple[int, int, int],
        indice: int,
        estado: str,
    ) -> pygame.Surface:
        if hasattr(caminho, "is_file") and caminho.is_file():
            try:
                imagem = pygame.image.load(str(caminho))
                return pygame.transform.smoothscale(imagem, self.retangulo.size)
            except pygame.error:
                pass

        quadro = pygame.Surface(self.retangulo.size, pygame.SRCALPHA)
        oscilacao = indice % 2
        pygame.draw.circle(quadro, (244, 208, 177), (29, 15), 13)
        pygame.draw.rect(quadro, cor, (13, 28, 32, 40), border_radius=10)
        if estado == "salto":
            pernas = ((18, 65, 7, 13), (36, 61, 7, 17))
        elif estado == "queda":
            pernas = ((15, 62, 7, 18), (38, 62, 7, 18))
        else:
            pernas = (
                (17 + oscilacao * 3, 65, 7, 17),
                (35 - oscilacao * 3, 65, 7, 17),
            )
        for perna in pernas:
            pygame.draw.rect(quadro, (44, 50, 62), perna, border_radius=3)
        return quadro

    def _atualizar_animacao(self, delta_tempo: float) -> None:
        if not self.no_chao:
            proximo_estado = "salto" if self.velocidade_vertical < 0 else "queda"
        elif self.velocidade_horizontal:
            proximo_estado = "caminhada"
        else:
            proximo_estado = "parada"

        if proximo_estado != self._estado_animacao:
            self._estado_animacao = proximo_estado
            self._indice_quadro = 0
            self._tempo_animacao = 0.0
            return

        quadros = self._quadros_direita[self._estado_animacao]
        if len(quadros) == 1:
            return
        intervalo = 0.16 if self._estado_animacao == "caminhada" else 0.42
        self._tempo_animacao += delta_tempo
        while self._tempo_animacao >= intervalo:
            self._tempo_animacao -= intervalo
            self._indice_quadro = (self._indice_quadro + 1) % len(quadros)

    def _atualizar_temporizadores(self, delta_tempo: float) -> None:
        if self.no_chao:
            self._tempo_coyote = TEMPO_COYOTE
        else:
            self._tempo_coyote = max(0.0, self._tempo_coyote - delta_tempo)

        self._tempo_buffer_pulo = max(
            0.0,
            self._tempo_buffer_pulo - delta_tempo,
        )

    def _tentar_pular(self) -> None:
        pode_pular = self.no_chao or self._tempo_coyote > 0
        if self._tempo_buffer_pulo <= 0 or not pode_pular:
            return

        self.velocidade_vertical = -VELOCIDADE_PULO
        self.no_chao = False
        self._tempo_buffer_pulo = 0.0
        self._tempo_coyote = 0.0

    def _interromper_pulo(self) -> None:
        if self.velocidade_vertical < 0:
            self.velocidade_vertical *= FATOR_CORTE_PULO

    def _mover_horizontal(self, deslocamento: float) -> None:
        self._posicao_x += deslocamento
        self.retangulo.x = round(self._posicao_x)
        self.retangulo.clamp_ip(
            pygame.Rect(0, -ALTURA_TELA, LARGURA_TELA, ALTURA_TELA * 3)
        )
        self._posicao_x = float(self.retangulo.x)

        for plataforma in self.plataformas:
            if not self.retangulo.colliderect(plataforma.retangulo):
                continue
            if deslocamento > 0:
                self.retangulo.right = plataforma.retangulo.left
            elif deslocamento < 0:
                self.retangulo.left = plataforma.retangulo.right
            self._posicao_x = float(self.retangulo.x)

    def _mover_vertical(self, deslocamento: float) -> None:
        topo_anterior = self.retangulo.top
        base_anterior = self.retangulo.bottom
        self.no_chao = False
        self._posicao_y += deslocamento
        self.retangulo.y = round(self._posicao_y)

        plataformas_cruzadas = [
            plataforma
            for plataforma in self.plataformas
            if self.retangulo.right > plataforma.retangulo.left
            and self.retangulo.left < plataforma.retangulo.right
            and (
                deslocamento >= 0
                and base_anterior <= plataforma.retangulo.top
                and self._posicao_y + self.retangulo.height
                >= plataforma.retangulo.top
                or deslocamento < 0
                and topo_anterior >= plataforma.retangulo.bottom
                and self._posicao_y <= plataforma.retangulo.bottom
            )
        ]

        if not plataformas_cruzadas:
            return

        if deslocamento >= 0:
            plataforma = min(
                plataformas_cruzadas,
                key=lambda item: item.retangulo.top,
            )
            self.retangulo.bottom = plataforma.retangulo.top
            self.no_chao = True
        else:
            plataforma = max(
                plataformas_cruzadas,
                key=lambda item: item.retangulo.bottom,
            )
            self.retangulo.top = plataforma.retangulo.bottom

        self.velocidade_vertical = 0.0
        self._posicao_y = float(self.retangulo.y)
