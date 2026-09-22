"""Caixa de diálogo superior com revelação progressiva de texto."""

from pathlib import Path

import pygame

from src.configuracao.caminhos import FONTE_PRINCIPAL
from src.configuracao.configuracoes import (
    COR_BORDA_DIALOGO,
    COR_CAIXA_DIALOGO,
    COR_TEXTO,
    LARGURA_TELA,
    MARGEM_DIALOGO,
    VELOCIDADE_TEXTO,
)
from src.entidades.entidade import Entidade


class CaixaDialogo(Entidade):
    """Exibe uma fila de falas e controla avanço por Enter."""

    def __init__(
        self,
        falas: tuple[str, ...],
        velocidade_texto: float = VELOCIDADE_TEXTO,
        caminho_fonte: Path | None = FONTE_PRINCIPAL,
    ) -> None:
        if not falas:
            raise ValueError("Uma caixa de diálogo precisa de ao menos uma fala.")
        super().__init__()
        self.falas = falas
        self.velocidade_texto = velocidade_texto
        self.indice_fala = 0
        self.quantidade_caracteres = 0.0
        self.concluido = False
        caminho = str(caminho_fonte) if caminho_fonte and caminho_fonte.is_file() else None
        self._fonte = pygame.font.Font(caminho, 30)
        self._fonte_ajuda = pygame.font.Font(caminho, 20)
        self._area = pygame.Rect(MARGEM_DIALOGO, 42, LARGURA_TELA - MARGEM_DIALOGO * 2, 210)

    @property
    def fala_atual(self) -> str:
        """Retorna a fala atualmente selecionada."""
        return self.falas[self.indice_fala]

    @property
    def fala_completa(self) -> bool:
        """Informa se todos os caracteres da fala atual estão visíveis."""
        return int(self.quantidade_caracteres) >= len(self.fala_atual)

    def atualizar(self, delta_tempo: float) -> None:
        if self.concluido or self.fala_completa:
            return
        self.quantidade_caracteres = min(
            len(self.fala_atual),
            self.quantidade_caracteres + self.velocidade_texto * max(0.0, delta_tempo),
        )

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if self.concluido or evento.type != pygame.KEYDOWN or evento.key != pygame.K_RETURN:
            return
        if not self.fala_completa:
            self.quantidade_caracteres = float(len(self.fala_atual))
            return
        if self.indice_fala + 1 < len(self.falas):
            self.indice_fala += 1
            self.quantidade_caracteres = 0.0
            return
        self.concluido = True

    def desenhar(self, superficie: pygame.Surface) -> None:
        painel = pygame.Surface(self._area.size, pygame.SRCALPHA)
        painel.fill(COR_CAIXA_DIALOGO)
        superficie.blit(painel, self._area)
        pygame.draw.rect(superficie, COR_BORDA_DIALOGO, self._area, width=3, border_radius=14)

        texto_visivel = self.fala_atual[: int(self.quantidade_caracteres)]
        y = self._area.y + 34
        for linha in self._quebrar_linhas(texto_visivel, self._area.width - 70):
            imagem = self._fonte.render(linha, True, COR_TEXTO)
            superficie.blit(imagem, (self._area.x + 35, y))
            y += self._fonte.get_linesize() + 6

        ajuda = "ENTER: completar" if not self.fala_completa else "ENTER: continuar"
        imagem_ajuda = self._fonte_ajuda.render(ajuda, True, COR_BORDA_DIALOGO)
        superficie.blit(
            imagem_ajuda,
            (self._area.right - imagem_ajuda.get_width() - 28, self._area.bottom - 36),
        )

    def _quebrar_linhas(self, texto: str, largura_maxima: int) -> list[str]:
        palavras = texto.split(" ")
        linhas: list[str] = []
        linha = ""
        for palavra in palavras:
            candidata = palavra if not linha else f"{linha} {palavra}"
            if self._fonte.size(candidata)[0] <= largura_maxima:
                linha = candidata
                continue
            if linha:
                linhas.append(linha)
            linha = palavra
        if linha or not linhas:
            linhas.append(linha)
        return linhas
