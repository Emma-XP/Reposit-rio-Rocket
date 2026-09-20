"""Caminhos centralizados para os recursos visuais e sonoros do jogo."""

from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parents[2]
PASTA_ASSETS = RAIZ_PROJETO / "assets"
PASTA_IMAGENS = PASTA_ASSETS / "imagens"
PASTA_SONS = PASTA_ASSETS / "sons"
PASTA_FONTES = PASTA_ASSETS / "fontes"

# Quando estes arquivos forem adicionados, as entidades que os usam deixarão
# automaticamente de exibir suas formas geométricas temporárias.
IMAGEM_IDENTIDADE_VISUAL = PASTA_IMAGENS / "identidade_visual.png"
IMAGEM_PLATAFORMA = PASTA_IMAGENS / "plataforma.png"
IMAGEM_FLOR = PASTA_IMAGENS / "flor.png"
FONTE_PRINCIPAL = PASTA_FONTES / "fonte_principal.ttf"

IMAGENS_FUNDO = {
    "infancia": PASTA_IMAGENS / "fundo_infancia.png",
    "adolescencia": PASTA_IMAGENS / "fundo_adolescencia.png",
    "vida_adulta": PASTA_IMAGENS / "fundo_vida_adulta.png",
}


def _quadros_jogadora(idade: str) -> dict[str, tuple[Path, ...]]:
    """Monta os caminhos previsíveis dos oito quadros de uma idade."""
    pasta = PASTA_IMAGENS / "jogadora" / idade
    return {
        "parada": tuple(pasta / f"parada_{indice}.png" for indice in range(1, 3)),
        "caminhada": tuple(
            pasta / f"caminhada_{indice}.png" for indice in range(1, 5)
        ),
        "salto": (pasta / "salto_1.png",),
        "queda": (pasta / "queda_1.png",),
    }


# A arte pode ser incluída depois sem alterar a lógica. Na ausência dos arquivos,
# a jogadora produz quadros geométricos distintos para cada idade e animação.
QUADROS_JOGADORA = {
    idade: _quadros_jogadora(idade)
    for idade in ("infancia", "adolescencia", "vida_adulta")
}
