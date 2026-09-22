# Jogadora

## Descrição

Entidade controlável responsável pela física, colisões e seleção visual de
animação, mantendo uma caixa de colisão estável.

## Localização

`src/entidades/jogadora.py`

## Propriedades

### `retangulo`

- Tipo: `pygame.Rect`
- Valor inicial: posição recebida e dimensões configuradas.
- Descrição: posição e área de colisão estável.

### `velocidade_vertical` e `velocidade_horizontal`

- Tipo: `float`
- Valor inicial: `0.0`.
- Descrição: velocidades usadas pela física e seleção visual.

### `no_chao`

- Tipo: `bool`
- Valor inicial: `False`.
- Descrição: informa se um novo pulo é permitido.

### `idade`

- Tipo: `str`
- Valor inicial: informado pela fase.
- Descrição: seleciona um dos três conjuntos de oito quadros.

O pulo possui buffer de 0,12 segundo, tempo coyote de 0,10 segundo e corte de
altura ao soltar o botão.

## Métodos

### `tratar_evento(evento)`

- Objetivo: receber movimento e pulo.
- Parâmetros: evento do Pygame.
- Retorno: nenhum.
- Efeito no jogo: altera o estado dos controles.

### `atualizar(delta_tempo)`

- Objetivo: aplicar movimento, gravidade, colisões e animação.
- Parâmetros: tempo decorrido em segundos.
- Retorno: nenhum.
- Efeito no jogo: muda posição e estado visual.

### `reiniciar()`

- Objetivo: restaurar spawn, velocidades e controles.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: prepara a jogadora para uma nova tentativa.

### `liberar_controles()`

- Objetivo: limpar entradas retidas ao abrir um diálogo.
- Parâmetros: nenhum.
- Retorno: nenhum.
- Efeito no jogo: mantém Diana imóvel ao retomar.

### `caiu_do_mapa()`

- Objetivo: informar a queda à cena.
- Parâmetros: nenhum.
- Retorno: `bool`.
- Efeito no jogo: nenhum diretamente.

### `desenhar(superficie)`

- Objetivo: desenhar o quadro do estado e direção atuais.
- Parâmetros: superfície do Pygame.
- Retorno: nenhum.
- Efeito no jogo: usa espelhamento em cache sem alterar a física.

