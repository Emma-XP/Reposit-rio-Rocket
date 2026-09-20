"""Dados persistentes compartilhados entre as cenas."""


class EstadoJogo:
    """Armazena progresso e configurações sem usar variáveis globais."""

    def __init__(self) -> None:
        self.progresso: dict[str, object] = {}
        self.configuracoes: dict[str, object] = {}
        self.indice_fase_atual = 0
        self.aberturas_vistas: set[str] = set()
        self.fases_concluidas: set[str] = set()
        self.jogo_concluido = False

    def registrar_progresso(self, chave: str, valor: object) -> None:
        """Registra um valor persistente de progresso."""
        self.progresso[chave] = valor

    def definir_configuracao(self, chave: str, valor: object) -> None:
        """Registra uma preferência ou configuração do jogo."""
        self.configuracoes[chave] = valor

    def abertura_foi_vista(self, id_fase: str) -> bool:
        """Informa se a abertura já terminou na execução atual."""
        return id_fase in self.aberturas_vistas

    def marcar_abertura_vista(self, id_fase: str) -> None:
        """Preserva a conclusão da abertura entre tentativas da fase."""
        self.aberturas_vistas.add(id_fase)

    def concluir_fase(self, id_fase: str, proximo_indice: int) -> None:
        """Registra uma fase concluída e seleciona o próximo índice."""
        self.fases_concluidas.add(id_fase)
        self.indice_fase_atual = proximo_indice

    def concluir_jogo(self) -> None:
        """Marca que a trajetória chegou à cena de conclusão."""
        self.jogo_concluido = True

    def reiniciar_execucao(self) -> None:
        """Limpa todo o progresso narrativo mantido apenas em memória."""
        self.progresso.clear()
        self.indice_fase_atual = 0
        self.aberturas_vistas.clear()
        self.fases_concluidas.clear()
        self.jogo_concluido = False
