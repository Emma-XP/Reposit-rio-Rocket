"""Caminhos centralizados para os recursos visuais e sonoros do jogo."""

from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_IMAGEM = RAIZ_PROJETO / "__pyt_pygames__" / "Imagens" / "telas"
PASTA_ASSETS = RAIZ_PROJETO / "assets"
PASTA_TELAS = PASTA_ASSETS / "imagens" / "telas" 
PASTA_SONS = PASTA_ASSETS / "sons"
PASTA_FONTES = PASTA_ASSETS / "fontes"
PASTA_SPRITES = PASTA_ASSETS / "imagens" / "movimentação"


# Quando estes arquivos forem adicionados, as entidades que os usam deixarão
# automaticamente de exibir suas formas geométricas temporárias.
IMAGEM_IDENTIDADE_VISUAL = PASTA_TELAS / "identidade_visual.png"
IMAGEM_PLATAFORMA = PASTA_TELAS / "plataforma.png"
IMAGEM_FLOR = PASTA_TELAS / "flor.png"
FONTE_PRINCIPAL = PASTA_FONTES / "fonte_principal.ttf"

IMAGENS_FUNDO = {
    "infancia": PASTA_TELAS / "Cenario 1.png",
    "adolescencia": PASTA_TELAS / "fundo_adolescencia.png",
    "vida_adulta": PASTA_TELAS / "fundo_vida_adulta.png",
}


def _quadros_jogadora(idade: str) -> dict[str, tuple[Path, ...]]:
    """Monta os caminhos previsíveis dos oito quadros de uma idade."""
    pasta = PASTA_SPRITES / idade
    return {
        "parada": tuple(pasta / f"parada_{indice}.png" for indice in range(1, 3)),
        
        "caminhada": tuple(
            pasta / "andar_lado" / f"Andar{indice}.jpeg" for indice in range(1, 3)
        ),
        "salto": tuple(
                    pasta / "pulo" / f"Pulo{indice}.jpeg" for indice in range(1, 3)
        ),
        "queda": tuple(
                    pasta / "queda" / f"Queda{indice}.jpeg" for indice in range(1, 2)
        )
    }


# A arte pode ser incluída depois sem alterar a lógica. Na ausência dos arquivos,
# a jogadora produz quadros geométricos distintos para cada idade e animação.
QUADROS_JOGADORA = {
    idade: _quadros_jogadora(idade)
    for idade in ("infancia", "adolescencia", "vida_adulta")
}
