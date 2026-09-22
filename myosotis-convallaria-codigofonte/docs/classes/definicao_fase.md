# DefinicaoFase

## Descrição

Dataclass imutável que concentra conteúdo, layout e tema de uma fase. Valida
cinco flores, cinco mensagens e os limites de falas.

## Localização

`src/configuracao/fases.py`

## Propriedades

### `id`, `nome` e `idade`

- Tipo: `str`
- Valor inicial: informado na criação.
- Descrição: identificam progresso, apresentação e conjunto visual.

### `plataformas` e `posicoes_flores`

- Tipo: tuplas de coordenadas.
- Valor inicial: informado na criação.
- Descrição: definem o percurso e os cinco coletáveis.

### `dialogo_abertura`, `mensagens_flores` e `dialogo_encerramento`

- Tipo: `tuple[str, ...]`
- Valor inicial: informado na criação.
- Descrição: formam a sequência narrativa da fase.

## Métodos

### `__post_init__()`

- Objetivo: validar os limites fechados do conteúdo.
- Parâmetros: nenhum além da instância.
- Retorno: nenhum.
- Efeito no jogo: impede a criação de uma fase inconsistente.
