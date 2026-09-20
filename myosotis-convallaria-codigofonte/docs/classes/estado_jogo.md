# EstadoJogo

## Descrição

Armazena somente dados em memória que sobrevivem às trocas de cena e aos
reinícios de tentativa.

## Localização

`src/estado_jogo.py`

## Propriedades

### `indice_fase_atual`

- Tipo: `int`
- Valor inicial: `0`.
- Descrição: índice da fase atual.

### `aberturas_vistas` e `fases_concluidas`

- Tipo: `set[str]`
- Valor inicial: conjuntos vazios.
- Descrição: progresso narrativo da execução atual.

### `jogo_concluido`

- Tipo: `bool`
- Valor inicial: `False`.
- Descrição: indica a chegada à conclusão.

Os dicionários `progresso` e `configuracoes` são mantidos por
compatibilidade com a infraestrutura inicial.

## Métodos

### `abertura_foi_vista(id_fase)` e `marcar_abertura_vista(id_fase)`

- Objetivo: consultar ou registrar uma abertura concluída.
- Parâmetros: identificador da fase.
- Retorno: consulta retorna `bool`; registro não retorna valor.
- Efeito no jogo: evita repetição da abertura após queda.

### `concluir_fase(id_fase, proximo_indice)`

- Objetivo: registrar avanço entre fases.
- Parâmetros: identificador concluído e próximo índice.
- Retorno: nenhum.
- Efeito no jogo: atualiza o progresso global em memória.

### `concluir_jogo()`

- Objetivo: marcar a chegada à conclusão.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: atualiza `jogo_concluido`.

### `reiniciar_execucao()`

- Objetivo: limpar todo o progresso narrativo.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: prepara uma nova trajetória desde a infância.

