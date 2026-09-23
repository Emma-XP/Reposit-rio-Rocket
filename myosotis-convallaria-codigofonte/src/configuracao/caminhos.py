"""Caminhos centralizados para os recursos visuais e sonoros do jogo."""

from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_IMAGEM = RAIZ_PROJETO / "__pyt_pygames__" / "Imagens" / "telas"
PASTA_ASSETS = RAIZ_PROJETO / "assets"
PASTA_TELAS = PASTA_ASSETS / "imagens" / "telas" 
PASTA_SONS = PASTA_ASSETS / "sons"
PASTA_FONTES = PASTA_ASSETS / "fontes"
PASTA_SPRITES = PASTA_ASSETS / "imagens" / "movimentação"
PASTA_FLORES = PASTA_ASSETS / "imagens" / "flores"
# Quando estes arquivos forem adicionados, as entidades que os usam deixarão
# automaticamente de exibir suas formas geométricas temporárias.
IMAGEM_IDENTIDADE_VISUAL = PASTA_TELAS / "identidade_visual.png"
IMAGEM_TELA_INICIO = PASTA_TELAS / "telainicio.png"
IMAGEM_BOTAO_JOGAR = PASTA_TELAS / "botaojogar.png"
IMAGEM_PLATAFORMA = PASTA_TELAS / "plataforma.png"
IMAGEM_FLOR = PASTA_TELAS / "flor.png"
IMAGEM_PLATAFORMA = PASTA_ASSETS / "imagens" / "plataformas" / "plataforma.png"
IMAGEM_FLOR = PASTA_FLORES / "LirioDoVale.png"
FONTE_PRINCIPAL = PASTA_FONTES / "fonte_principal.ttf"

IMAGENS_FUNDO = {
    "infancia": PASTA_TELAS / "Cenario 1.png",
    "adolescencia": PASTA_TELAS / "fundo_adolescencia.png",
    "vida_adulta": PASTA_TELAS / "fundo_vida_adulta.png",
}

SPRITES_JOGADORA = {
    "parada": (PASTA_SPRITES / "andar_frente" / "Andar frente.png",),
    "caminhada": (
        PASTA_SPRITES / "andar_lados" / "Andar 1.png",
        PASTA_SPRITES / "andar_lados" / "Andar 2.png",
        PASTA_SPRITES / "andar_lados" / "Andar 3.png",
    ),
    "frente": (
        PASTA_SPRITES / "andar_frente" / "Andar frente.png",
        PASTA_SPRITES / "andar_frente" / "Andar frente 2.png",
    ),
    "costas": (
        PASTA_SPRITES / "costas" / "Costas.png",
        PASTA_SPRITES / "costas" / "Andar costas.png",
        PASTA_SPRITES / "costas" / "Andar costas-2.png",
    ),
    "salto": (
        PASTA_SPRITES / "pulo" / "Pulo 1.png",
        PASTA_SPRITES / "pulo" / "Pulo 2.png",
        PASTA_SPRITES / "pulo" / "Pulo 3.png",
    ),
    "queda": (
        PASTA_SPRITES / "queda" / "Queda 1.png",
        PASTA_SPRITES / "queda" / "Queda 2.png",
    ),
}


def _quadros_jogadora(idade: str) -> dict[str, tuple[Path, ...]]:
    """Monta os caminhos previsíveis dos oito quadros de uma idade."""
    pasta = PASTA_SPRITES / idade
    return {
        "parada": tuple(pasta / f"parada_{indice}.png" for indice in range(1, 3)),
        
        "caminhada": tuple(
            pasta / "andar_lados" / f"Andar{indice}.png" for indice in range(1, 4)
        ),
        "salto": tuple(
                    pasta / "pulo" / f"Pulo{indice}.png" for indice in range(1, 4)
        ),
        "queda": tuple(
                    pasta / "queda" / f"Queda{indice}.png" for indice in range(1, 3)
        )
    }


# A arte pode ser incluída depois sem alterar a lógica. Na ausência dos arquivos,
# a jogadora produz quadros geométricos distintos para cada idade e animação.

QUADROS_JOGADORA = { "infancia": SPRITES_JOGADORA, "adolescencia": SPRITES_JOGADORA, "vida_adulta": SPRITES_JOGADORA, }
