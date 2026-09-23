"""Ponto de entrada do jogo Myosotis convallaria."""

import pygame

from src.cenas.cena_conclusao import CenaConclusao
from src.cenas.fase_plataforma import FasePlataforma
from src.configuracao.configuracoes import (
    ALTURA_JANELA,
    ALTURA_TELA,
    FPS,
    LARGURA_JANELA,
    LARGURA_TELA,
    TITULO_JANELA,
)
from src.configuracao.fases import FASES
from src.controlador_cenas import ControladorCenas
from src.estado_jogo import EstadoJogo
from src.cenas.cena_inicial import CenaInicial


class Jogo:
    """Inicializa o Pygame e executa o fluxo principal do jogo."""

    def __init__(self) -> None:
        # Apenas os subsistemas usados são obrigatórios. Assim, a ausência de
        # dispositivo de áudio não impede a execução da versão sem trilha.
        pygame.display.init()
        pygame.font.init()
        self.janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
        self.superficie = pygame.Surface((LARGURA_TELA, ALTURA_TELA)).convert()
        pygame.display.set_caption(TITULO_JANELA)
        self.relogio = pygame.time.Clock()
        self.estado = EstadoJogo()
        self.controlador_cenas = ControladorCenas()
        self.em_execucao = True
        self.controlador_cenas.trocar_cena(
            CenaInicial(self.estado, self._iniciar_fase_inicial)
        )

    def _iniciar_fase_inicial(self) -> None:
        """Começa a primeira fase depois do clique em JOGAR."""
        self._iniciar_fase(0)

    def _iniciar_fase(self, indice: int) -> None:
        """Cria a fase pedida ou apresenta a conclusão da trajetória."""
        if indice >= len(FASES):
            self.estado.concluir_jogo()
            self.controlador_cenas.trocar_cena(
                CenaConclusao(self._reiniciar_jogo)
            )
            return
        self.estado.indice_fase_atual = indice
        definicao = FASES[indice]
        fase = FasePlataforma(
            definicao=definicao,
            estado_jogo=self.estado,
            ao_concluir=lambda: self._concluir_fase(indice),
        )
        self.controlador_cenas.trocar_cena(fase)

    def _concluir_fase(self, indice: int) -> None:
        """Registra o avanço e abre a fase seguinte."""
        proximo_indice = indice + 1
        self.estado.concluir_fase(FASES[indice].id, proximo_indice)
        self._iniciar_fase(proximo_indice)

    def _reiniciar_jogo(self) -> None:
        """Limpa o progresso em memória e retorna à infância."""
        self.estado.reiniciar_execucao()
        self._iniciar_fase(0)

    def executar(self, limite_quadros: int | None = None) -> None:
        """Executa o ciclo principal até o encerramento do jogo."""
        quadros_executados = 0

        try:
            while self.em_execucao:
                delta_tempo = self.relogio.tick(FPS) / 1000
                self._tratar_eventos()
                if not self.em_execucao:
                    break

                self.controlador_cenas.atualizar(delta_tempo)
                self.controlador_cenas.desenhar(self.superficie)
                self._exibir_quadro()
                pygame.display.flip()

                quadros_executados += 1
                if limite_quadros is not None and quadros_executados >= limite_quadros:
                    self.em_execucao = False
        finally:
            self.encerrar()

    def encerrar(self) -> None:
        """Finaliza a cena ativa e encerra os recursos do Pygame."""
        self.em_execucao = False
        self.controlador_cenas.encerrar()
        pygame.quit()

    def _exibir_quadro(self) -> None:
        """Ajusta a área lógica ao tamanho selecionado para a janela."""
        if self.janela.get_size() == self.superficie.get_size():
            self.janela.blit(self.superficie, (0, 0))
            return
        pygame.transform.smoothscale(
            self.superficie,
            self.janela.get_size(),
            self.janela,
        )

    def _tratar_eventos(self) -> None:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.em_execucao = False
                return

            self.controlador_cenas.tratar_evento(evento)


if __name__ == "__main__":
    Jogo().executar()
