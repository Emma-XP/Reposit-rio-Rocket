"""Cena de plataforma orientada pelos dados de uma fase narrativa."""

from collections.abc import Callable
from enum import Enum, auto

import pygame

from src.cenas.fase import Fase
from src.configuracao.caminhos import FONTE_PRINCIPAL
from src.configuracao.configuracoes import ALTURA_TELA, COR_TEXTO, LARGURA_TELA
from src.configuracao.fases import DefinicaoFase
from src.entidades.flor import Flor
from src.entidades.jogadora import Jogadora
from src.entidades.plataforma import Plataforma
from src.entidades.texto import Texto
from src.estado_jogo import EstadoJogo
from src.interface.caixa_dialogo import CaixaDialogo

class EstadoFase(Enum):
    """Estados que controlam simulação, narrativa e transição da fase."""

    ABERTURA = auto()
    EXPLORACAO = auto()
    MENSAGEM_FLOR = auto()
    ENCERRAMENTO = auto()
    TRANSICAO = auto()


class FasePlataforma(Fase):
    """Executa uma fase completa sem duplicar lógica entre as três idades."""

    def __init__(
        self,
        definicao: DefinicaoFase,
        estado_jogo: EstadoJogo,
        ao_concluir: Callable[[], None],
    ) -> None:
        super().__init__(objetivo="Encontrar as cinco flores")
        self.definicao = definicao
        self.estado_jogo = estado_jogo
        self.ao_concluir = ao_concluir
        self.cor_fundo = definicao.cor_fundo
        self.plataformas: list[Plataforma] = []
        self.flores: list[Flor] = []
        self.jogadora: Jogadora | None = None
        self.caixa_dialogo: CaixaDialogo | None = None
        self.quantidade_coletada = 0
        self.estado_fase = EstadoFase.ABERTURA
        self._preparada = False
        self._transicao_solicitada = False
        self._imagem_fundo: pygame.Surface | None = None

    def entrar(self) -> None:
        if self._preparada:
            return
        self.plataformas = [
            Plataforma(pygame.Rect(area)) for area in self.definicao.plataformas
        ]
        self.jogadora = Jogadora(
            self.definicao.spawn_jogadora, self.plataformas, self.definicao.idade
        )
        for plataforma in self.plataformas:
            self.adicionar_entidade(plataforma)
        self.adicionar_entidade(self.jogadora)
        self.adicionar_entidade(
            Texto(
                self.definicao.nome,
                (LARGURA_TELA // 2, 300),
                28,
                COR_TEXTO,
                FONTE_PRINCIPAL,
            )
        )
        self._recriar_flores()
        self._carregar_fundo()
        if self.estado_jogo.abertura_foi_vista(self.definicao.id):
            self.estado_fase = EstadoFase.EXPLORACAO
        else:
            self._abrir_dialogo(self.definicao.dialogo_abertura, EstadoFase.ABERTURA)
        self._preparada = True

    def tratar_evento(self, evento: pygame.event.Event) -> None:
        if self.estado_fase in (
            EstadoFase.ABERTURA,
            EstadoFase.MENSAGEM_FLOR,
            EstadoFase.ENCERRAMENTO,
        ):
            if self.caixa_dialogo is not None:
                self.caixa_dialogo.tratar_evento(evento)
            return
        if self.estado_fase != EstadoFase.EXPLORACAO:
            return
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            self.reiniciar_tentativa()
            return
        if self.jogadora is not None:
            self.jogadora.tratar_evento(evento)

    def atualizar(self, delta_tempo: float) -> None:
        if self.estado_fase in (
            EstadoFase.ABERTURA,
            EstadoFase.MENSAGEM_FLOR,
            EstadoFase.ENCERRAMENTO,
        ):
            if self.caixa_dialogo is not None:
                self.caixa_dialogo.atualizar(delta_tempo)
            self._aplicar_alteracoes_pendentes()
            self._finalizar_dialogo_se_necessario()
            return
        if self.estado_fase != EstadoFase.EXPLORACAO:
            self._aplicar_alteracoes_pendentes()
            return

        super().atualizar(delta_tempo)
        if self.jogadora is None:
            return
        if self.jogadora.caiu_do_mapa():
            self.reiniciar_tentativa()
            return
        for flor in tuple(self.flores):
            if self.jogadora.retangulo.colliderect(flor.retangulo):
                self.registrar_coleta(flor)
                break
        self._aplicar_alteracoes_pendentes()

    def desenhar(self, superficie: pygame.Surface) -> None:
        superficie.fill(self.cor_fundo)
        if self._imagem_fundo is not None:
            superficie.blit(self._imagem_fundo, (0, 0))
        for entidade in self.entidades:
            if entidade.visivel:
                entidade.desenhar(superficie)

    def registrar_coleta(self, flor: Flor) -> str | None:
        """Registra uma flor inédita e abre a mensagem do índice de coleta."""
        if self.estado_fase != EstadoFase.EXPLORACAO or not flor.coletar():
            return None
        if flor in self.flores:
            self.flores.remove(flor)
        self.remover_entidade(flor)
        self.quantidade_coletada += 1
        self.definir_progresso(self.quantidade_coletada)
        mensagem = self.definicao.mensagens_flores[self.quantidade_coletada - 1]
        self._abrir_dialogo((mensagem,), EstadoFase.MENSAGEM_FLOR)
        return mensagem

    def reiniciar_tentativa(self) -> None:
        """Restaura física, flores e sequência, preservando a abertura vista."""
        if self.jogadora is not None:
            self.jogadora.reiniciar()
        if self.caixa_dialogo is not None:
            self.remover_entidade(self.caixa_dialogo)
            self.caixa_dialogo = None
        for flor in self.flores:
            self.remover_entidade(flor)
        self._entidades_para_adicionar = [
            entidade
            for entidade in self._entidades_para_adicionar
            if not isinstance(entidade, Flor)
        ]
        self.quantidade_coletada = 0
        self.definir_progresso(0)
        self.estado_fase = EstadoFase.EXPLORACAO
        self._recriar_flores()
        self._aplicar_alteracoes_pendentes()

    def _recriar_flores(self) -> None:
        self.flores = [Flor(posicao) for posicao in self.definicao.posicoes_flores]
        for flor in self.flores:
            self.adicionar_entidade(flor)

    def _abrir_dialogo(self, falas: tuple[str, ...], estado: EstadoFase) -> None:
        if self.caixa_dialogo is not None:
            self.remover_entidade(self.caixa_dialogo)
        self.caixa_dialogo = CaixaDialogo(falas)
        self.adicionar_entidade(self.caixa_dialogo)
        self.estado_fase = estado
        if self.jogadora is not None:
            self.jogadora.liberar_controles()

    def _finalizar_dialogo_se_necessario(self) -> None:
        if self.caixa_dialogo is None or not self.caixa_dialogo.concluido:
            return
        estado_anterior = self.estado_fase
        self.remover_entidade(self.caixa_dialogo)
        self.caixa_dialogo = None
        if estado_anterior == EstadoFase.ABERTURA:
            self.estado_jogo.marcar_abertura_vista(self.definicao.id)
            self.estado_fase = EstadoFase.EXPLORACAO
        elif estado_anterior == EstadoFase.MENSAGEM_FLOR:
            if self.quantidade_coletada == len(self.definicao.mensagens_flores):
                self._abrir_dialogo(
                    self.definicao.dialogo_encerramento, EstadoFase.ENCERRAMENTO
                )
            else:
                self.estado_fase = EstadoFase.EXPLORACAO
        elif estado_anterior == EstadoFase.ENCERRAMENTO:
            self.estado_fase = EstadoFase.TRANSICAO
            if not self._transicao_solicitada:
                self._transicao_solicitada = True
                self.ao_concluir()
        self._aplicar_alteracoes_pendentes()

    def _carregar_fundo(self) -> None:
        caminho = self.definicao.imagem_fundo
        if caminho is None or not caminho.is_file():
            return
        try:
            imagem = pygame.image.load(str(caminho))
            self._imagem_fundo = pygame.transform.smoothscale(
                imagem, (LARGURA_TELA, ALTURA_TELA)
            )
        except pygame.error:
            self._imagem_fundo = None
