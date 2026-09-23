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
<<<<<<< HEAD
IMAGEM_TELA_INICIO = PASTA_TELAS / "telainicio.png"
IMAGEM_BOTAO_JOGAR = PASTA_TELAS / "botaojogar.png"
IMAGEM_PLATAFORMA = PASTA_TELAS / "plataforma.png"
IMAGEM_FLOR = PASTA_TELAS / "flor.png"
=======
IMAGEM_PLATAFORMA = PASTA_ASSETS / "imagens" / "plataformas" / "plataforma.png"
IMAGEM_FLOR = PASTA_FLORES / "LirioDoVale.png"
>>>>>>> 43bd464ef41c69e0aa0afada65d210af2a68db14
FONTE_PRINCIPAL = PASTA_FONTES / "fonte_principal.ttf"

IMAGENS_FUNDO = {
    "infancia": PASTA_TELAS / "Cenario 1.png",
    "adolescencia": PASTA_TELAS / "fundo_adolescencia.png",
    "vida_adulta": PASTA_TELAS / "fundo_vida_adulta.png",
}

SPRITES_JOGADORA = { "parada": ( PASTA_SPRITES / "andar_frente" / "Andar frente.jpeg", ),
"caminhada": ( PASTA_SPRITES / "andar_lados" / "Andar 1.jpeg", PASTA_SPRITES / "andar_lados" / "Andar 2.jpeg", PASTA_SPRITES / "andar_lados" / "Andar 3.jpeg", ),
"frente": ( PASTA_SPRITES / "andar_frente" / "Andar frente.jpeg", PASTA_SPRITES / "andar_frente" / "Andar frente 2.jpeg", ),
"costas": ( PASTA_SPRITES / "costas" / "Costas.jpeg", PASTA_SPRITES / "costas" / "Andar costas.jpeg", PASTA_SPRITES / "costas" / "Andar costas-2.jpeg", ),
"salto": ( PASTA_SPRITES / "pulo" / "Pulo 1.jpeg", PASTA_SPRITES / "pulo" / "Pulo 2.jpeg", PASTA_SPRITES / "pulo" / "Pulo 3.jpeg", ),
"queda": ( PASTA_SPRITES / "queda" / "Queda 1.jpeg", PASTA_SPRITES / "queda" / "Queda 2.jpeg", ), }


def _quadros_jogadora(idade: str) -> dict[str, tuple[Path, ...]]:
    """Monta os caminhos previsíveis dos oito quadros de uma idade."""
    pasta = PASTA_SPRITES / idade
    return {
        "parada": tuple(pasta / f"parada_{indice}.png" for indice in range(1, 3)),
        
        "caminhada": tuple(
            pasta / "andar_lados" / f"Andar{indice}.jpeg" for indice in range(1, 4)
        ),
        "salto": tuple(
                    pasta / "pulo" / f"Pulo{indice}.jpeg" for indice in range(1, 4)
        ),
        "queda": tuple(
                    pasta / "queda" / f"Queda{indice}.jpeg" for indice in range(1, 3)
        )
    }


# A arte pode ser incluída depois sem alterar a lógica. Na ausência dos arquivos,
# a jogadora produz quadros geométricos distintos para cada idade e animação.

QUADROS_JOGADORA = { "infancia": SPRITES_JOGADORA, "adolescencia": SPRITES_JOGADORA, "vida_adulta": SPRITES_JOGADORA, }