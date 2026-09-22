# Fase

## Descrição

Especializa uma cena com campos genéricos de objetivo e progresso. A classe
`FasePlataforma` usa essa base para implementar as três fases técnicas.

## Localização

`src/cenas/fase.py`

## Propriedades

### `objetivo`

- Tipo: `str`
- Valor inicial: texto vazio.
- Descrição: espaço para o objetivo aprovado de uma fase futura.

### `progresso`

- Tipo: `int`
- Valor inicial: `0`.
- Descrição: valor genérico de progresso da fase.

## Métodos

### `definir_progresso(progresso)`

- Objetivo: atualizar o progresso sem aceitar valor negativo.
- Parâmetros: novo valor inteiro.
- Retorno: nenhum.
- Efeito no jogo: altera o progresso mantido pela fase.
