"""Valores reutilizados pela janela e pelas cenas do jogo."""

# Altere somente esta variável para escolher o tamanho da janela.
RESOLUCAO_ATIVA = "1366x768"

RESOLUCOES_SUPORTADAS = {
    "1920x1080": (1920, 1080),
    "1366x768": (1366, 768),
}

if RESOLUCAO_ATIVA not in RESOLUCOES_SUPORTADAS:
    opcoes = ", ".join(RESOLUCOES_SUPORTADAS)
    raise ValueError(
        f"Resolução '{RESOLUCAO_ATIVA}' inválida. Use uma destas opções: {opcoes}."
    )

LARGURA_JANELA, ALTURA_JANELA = RESOLUCOES_SUPORTADAS[RESOLUCAO_ATIVA]

# As cenas usam uma área lógica fixa. O quadro pronto é ajustado à janela,
# preservando posições, colisões e dificuldade nas duas resoluções.
LARGURA_TELA = 1920
ALTURA_TELA = 1080
FPS = 60
TITULO_JANELA = "Myosotis convallaria"

COR_FUNDO = (24, 31, 42)
COR_PRIMARIA = (111, 168, 220)
COR_TEXTO = (238, 241, 245)
COR_TEXTO_SECUNDARIO = (184, 194, 207)

COR_JOGADORA = (236, 112, 99)
COR_PLATAFORMA = (83, 139, 100)
COR_SAIDA = (245, 196, 81)
COR_FLOR = (133, 191, 118)
COR_CAIXA_DIALOGO = (13, 20, 31, 235)
COR_BORDA_DIALOGO = (213, 221, 230)

LARGURA_JOGADORA = 58
ALTURA_JOGADORA = 82
VELOCIDADE_JOGADORA = 430
VELOCIDADE_PULO = 760
GRAVIDADE = 1900
VELOCIDADE_MAXIMA_QUEDA = 1100
TEMPO_BUFFER_PULO = 0.12
TEMPO_COYOTE = 0.10
FATOR_CORTE_PULO = 0.45

TAMANHO_FLOR = (64, 64)
VELOCIDADE_TEXTO = 42.0
MARGEM_DIALOGO = 54
