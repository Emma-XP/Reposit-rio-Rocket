# CenaInicial

## Descrição

Apresenta uma tela técnica e neutra enquanto o conteúdo definitivo é definido.

## Localização

`src/cenas/cena_inicial.py`

## Propriedades

### `estado`

- Tipo: `EstadoJogo`
- Valor inicial: instância recebida do jogo.
- Descrição: referência aos dados persistentes compartilhados.

## Métodos

### `entrar()`

- Objetivo: criar as entidades visuais da tela uma única vez.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: agenda marca temporária, título e texto informativo.
