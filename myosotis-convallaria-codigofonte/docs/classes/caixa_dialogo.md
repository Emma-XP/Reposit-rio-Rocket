# CaixaDialogo

## Descrição

Componente superior que revela uma fila de falas com tempo, quebra linhas e
interpreta `Enter` sem encaminhá-lo à jogadora.

## Localização

`src/interface/caixa_dialogo.py`

## Propriedades

### `falas`

- Tipo: `tuple[str, ...]`
- Valor inicial: informado na criação.
- Descrição: fila imutável de textos.

### `indice_fala`, `quantidade_caracteres` e `concluido`

- Tipo: `int`, `float` e `bool`.
- Valor inicial: `0`, `0.0` e `False`.
- Descrição: representam o avanço atual do componente.

## Métodos

### `atualizar(delta_tempo)`

- Objetivo: revelar caracteres conforme o tempo decorrido.
- Parâmetros: segundos desde o quadro anterior.
- Retorno: nenhum.
- Efeito no jogo: avança somente a digitação.

### `tratar_evento(evento)`

- Objetivo: completar a fala ou avançar a fila com `Enter`.
- Parâmetros: evento do Pygame.
- Retorno: nenhum.
- Efeito no jogo: pode marcar o diálogo como concluído.

### `desenhar(superficie)`

- Objetivo: exibir painel, texto quebrado e ajuda contextual.
- Parâmetros: superfície do Pygame.
- Retorno: nenhum.
- Efeito no jogo: nenhum.
